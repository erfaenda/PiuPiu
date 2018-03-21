import subprocess

user = str(input("Введите имя пользователя либо группы "))
def getSid():
    proc = subprocess.Popen(['powershell', '$objUser = New-Object System.Security.Principal.NTAccount(\"'+user+'\"); '
                         '$strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'], shell=True, stdout=subprocess.PIPE)
    out = proc.communicate()
    finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
    print(finalSid)
    proc.wait()

getSid()
