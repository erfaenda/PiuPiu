'''import subprocess

p = subprocess.Popen(['ping', '10.9.155.2'], stdout=subprocess.PIPE, bufsize=1)
for line in iter(p.stdout.readline, b''):
    print(line)
p.stdout.close()
p.wait()'''

import subprocess

def ping1():
    p = subprocess.Popen(['ping', '10.9.155.2'], shell=False, stdout=subprocess.PIPE)
    i = 0
    for line in iter(p.stdout.readline, ''):
        print(line)
        i = i + 1
        print(i)
    p.stdout.close()

ping1()