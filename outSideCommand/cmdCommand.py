import sys
import subprocess
def getSid(self):
    proc = subprocess.Popen(
        ['icacls', '$objUser = New-Object System.Security.Principal.NTAccount(\"' + user + '\"); '
                                                                                               '$strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'],
        shell=True, stdout=subprocess.PIPE)
    out = proc.communicate()
    proc.wait()
