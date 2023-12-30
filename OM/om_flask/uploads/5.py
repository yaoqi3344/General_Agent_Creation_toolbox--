# test_script.py

import sys

def main():
    try:
        # 这里可以添加一些需要执行的代码
        # ...

        # 模拟成功，返回0
        return 1

    except Exception as e:
        # 模拟出现错误，返回1
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    return_code = main()
    sys.exit(return_code)
