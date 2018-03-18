import subprocess
with open('sh$18mc.txt', 'w', encoding='utf-8') as file:
    ip = str(input('Ведите ip адресс: '))
    #subprocess.run(r'c:\windows\system32\cmd.exe /C arp -a', stdout=file, check=True)
    print('Щаа все запишем')
    print(subprocess.run(r'c:\windows\system32\cmd.exe /C ping {}'.format(ip), stdout=file, check=True))
    subprocess.run(r'c:\windows\system32\cmd.exe /C ping {}'.format(ip), stdout=file, check=True)