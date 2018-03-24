import sys
import subprocess
'''def getSid():
    proc = subprocess.Popen(['icacls.exe', 'C:\\'], shell=False, stdout=subprocess.PIPE)
    out = proc.communicate()
    print(out)
    proc.wait()

getSid()'''


def check_accsess():
    proc = subprocess.check_output(['icacls.exe', r'C:\\'], stderr=subprocess.STDOUT)
    print(proc)

check_accsess()