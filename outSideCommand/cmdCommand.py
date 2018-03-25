import sys
import subprocess
'''def getSid():
    proc = subprocess.Popen(['icacls.exe', 'C:\\'], shell=False, stdout=subprocess.PIPE)
    out = proc.communicate()
    print(out)
    proc.wait()

getSid()'''
#/grant[:r] *S-1-5-21-3787624965-3905448-1910963349-1119:(OI)(CI)(RX) /T /C
def a():
    input_dir = 'C:\\test'
    cmdline = ['/grant[:r] *S-1-5-21-3031917476-3821197223-2245162686-1001:(OI)(CI)(RX) /T /C']
    proc = subprocess.check_output(['icacls.exe', input_dir, cmdline], stderr=subprocess.STDOUT)
    print(proc.decode('cp866'))
a()