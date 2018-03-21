import subprocess

ip = str(input('Ведите ip адресс: '))
proc = subprocess.Popen("ping -c2 %s" % ip, shell=True, stdout=subprocess.PIPE)
out = proc.communicate()
print(out)