'''AQAAAAAxhUvqAAV8Wn_FxaChMUjJgVtqGRQx12c
ID: f303b8380db54e49b15653a1209dab1f
Пароль: 7e2a45d0322a4784aca57c998ec24863'''


import yadisk

#y = yadisk.YaDisk(token="<токен>")
# или
y = yadisk.YaDisk("f303b8380db54e49b15653a1209dab1f", "7e2a45d0322a4784aca57c998ec24863", "AQAAAAAxhUvqAAV8Wn_FxaChMUjJgVtqGRQx12c")

# Проверяет, валиден ли токен
print(y.check_token())

# Получает общую информацию о диске
print(y.get_disk_info())

# Выводит содержимое "/some/path"
print(list(y.listdir("/temp")))

# Загружает "file_to_upload.txt" в "/destination.txt"
y.upload("data.txt", "/temp/data.txt")

'''# То же самое
with open("file_to_upload.txt", "rb") as f:
    y.upload(f, "/destination.txt")

# Скачивает "/some-file-to-download.txt" в "downloaded.txt"
y.download("/some-file-to-download.txt", "downloaded.txt")

# Безвозвратно удаляет "/file-to-remove"
y.remove("/file-to-remove", permanently=True)

# Создаёт новую папку "/test-dir"
print(y.mkdir("/test-dir"))'''