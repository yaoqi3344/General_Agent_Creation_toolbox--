from flask import Flask, render_template, request, jsonify,redirect,url_for
from apscheduler.schedulers.background import BackgroundScheduler
import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

app = Flask(__name__)
scheduler = BackgroundScheduler()
tasks = []
next_task_id = 1  # 初始化任务ID

# 邮件服务器配置
SMTP_HOST = "smtp.126.com"
SMTP_PORT = 465
SMTP_USERNAME = "yaoqi100@126.com"
SMTP_PASSWORD = "RJFGUBFZAKLELMBD"
SENDER_EMAIL = "yaoqi100@126.com"

def send_email(subject, message, recipient_email):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    try:
        smtpObj = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        smtpObj.login(SMTP_USERNAME, SMTP_PASSWORD)
        smtpObj.sendmail(SENDER_EMAIL, [recipient_email], msg.as_string())
        smtpObj.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print("Error sending email:", str(e))

def execute_python_script(script_path, recipient_email):
    try:
        process = subprocess.Popen(["/usr/bin/python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return_code = process.returncode
        if return_code == 0:
            success_message = f"Script {script_path} executed successfully.\n{stdout.decode('utf-8')}"
            print(success_message)
        else:
            error_message = f"Error executing script {script_path}:\n{stderr.decode('utf-8')}"
            print(error_message)
            send_email("Script Execution Error", error_message, recipient_email)
    except Exception as e:
        error_message = f"Error executing script {script_path}: {str(e)}"
        print(error_message)
        send_email("Script Execution Error", error_message, recipient_email)

@app.route('/om/upload', methods=['POST'])
def upload_and_schedule():
    global next_task_id
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        execution_interval = request.form['execution_interval']
        recipient_email = request.form['recipient_email']

        task_id = next_task_id
        next_task_id += 1
        tasks.append({'id': task_id, 'script_path': file_path, 'execution_interval': execution_interval, 'recipient_email': recipient_email})
        scheduler.add_job(execute_python_script, 'interval', args=[file_path, recipient_email], id=str(task_id), seconds=int(execution_interval))

    return redirect(url_for('om'))

@app.route('/om', methods=['GET'])
def om():
    return render_template('om_front.html', tasks=tasks)

@app.route('/om/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    # 从任务列表中移除任务
    global tasks
    print(f"Attempting to delete task with ID {task_id}")
    task_to_remove = next((task for task in tasks if task['id'] == task_id), None)
    if not task_to_remove:
        return jsonify({"error": "Task not found"}), 404

    try:
        # 移除任务调度
        scheduler.remove_job(str(task_id))

        # 检查文件是否存在并尝试删除
        script_path = task_to_remove['script_path']
        if os.path.exists(script_path):
            try:
                os.remove(script_path)
                print(f"File {script_path} deleted successfully.")
            except Exception as e:
                print(f"Error deleting file {script_path}: {e}")
        else:
            print(f"File {script_path} not found.")

        
        tasks = [task for task in tasks if task['id'] != task_id]

        return jsonify({"message": "Task and file deleted successfully"}), 200
    except Exception as e:
        print(f"Error deleting task: {str(e)}")
        return jsonify({"error": "Error deleting task"}), 500




if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    scheduler.start()
    app.run(debug=False, host='0.0.0.0', port=5000)
