
import subprocess

count = 0
def start():
    proc = subprocess.Popen('icacls C:\\test /grant[:r] *S-1-5-21-3031917476-3821197223-2245162686-1001:(OI)(CI)(F) /T /C', shell=False, stdout=subprocess.PIPE)
    for line in proc.stdout:
        line = line.strip()
        print(line.decode('cp866'))
    proc.stdout.close()


'''def getLocalSid():
    cmdline = ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount("{}"); $strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'.format('alex')]
    proc = subprocess.Popen(cmdline, shell=False, stdout=subprocess.PIPE)
    for line in proc.stdout:
        line = line.strip()
        print(line.decode('cp866'))
        proc.terminate()'''


start()
