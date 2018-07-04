from ftplib import FTP

#создал экземпляр фтп
ftp = FTP('ftp.cse.buffalo.edu')
ftp.login() # вошел

ftp.cwd('bin')

data = ftp.retrlines('LIST')

print(data)