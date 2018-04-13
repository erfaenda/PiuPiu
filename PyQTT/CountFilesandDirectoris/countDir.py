import os

src = 'C:\\test'
z = 0
for dir_name, dirs, files in os.walk(src):
    i = 0
    a = i + len(dirs) + len(files)
    z = z + a
    #print(dir_name, len(dirs))
    print(z)