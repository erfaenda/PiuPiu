import subprocess

count = 0
def start():
    proc = subprocess.Popen('icacls C:\\test /grant[:r] *S-1-5-21-1017654698-597425923-2411056522-1000:(OI)(CI)(F) /T /C', shell=False, stdout=subprocess.PIPE)
    i = 0
    count = 0
    for line in proc.stdout:
        line = line.strip()
        print(line.decode('cp866'))
        i = i + 1
        count = i
    proc.stdout.close()
    print(count)

def getLocalSid():
    cmdline = ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount("{}"); $strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'.format('virtualbox')]
    proc = subprocess.Popen(cmdline, shell=False, stdout=subprocess.PIPE)
    for line in proc.stdout:
        line = line.strip()
        print(line.decode('cp866'))
        proc.terminate()


getLocalSid()
start()