import paramiko
import time
import sys

def get_file_last_modified(file_path, ssh):
    try:
        sftp = ssh.open_sftp()
        stat = sftp.stat(file_path)
        return stat.st_mtime
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def check_file_last_modified():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('8.210.146.64', username='root', password='Sifc@1234')

        file_path = '/usr/local/pkg/server/ai/D:\\logs/tchability/error.log'

        # 获取文件的修改时间
        file_time = get_file_last_modified(file_path, ssh)
        if file_time is None:
            print("File not found or error occurred.")
            return 0  # 文件不存在或发生错误，返回0
        else:
            current_time = time.time()
            half_hour_ago = current_time - (30 * 60)  # 半小时前的时间戳

            print(f"File Time: {file_time}")
            print(f"Current Time: {current_time}")

            # 检查文件修改时间是否在半小时内
            if file_time >= half_hour_ago:
                print("File was modified in the last half hour.")
                return 1  # 文件在半小时内被修改过，返回1
            else:
                print("File was not modified in the last half hour.")
                return 0  # 文件在半小时内未被修改过，返回0

        ssh.close()
    except Exception as e:
        print(f"Error: {e}")
        return 0  # 发生异常，返回0

return_code = check_file_last_modified()
sys.exit(return_code)
print(f"Result: {result}")
