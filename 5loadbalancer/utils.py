import psutil

def check_python_script_running(script_name):
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['name'] == 'python' and script_name in process.info['cmdline']:
            return True
    return False

if check_python_script_running('health_check.py'):
    print('Your script is running.')
else:
    print('Your script is not running.')