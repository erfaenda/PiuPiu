import yadisk

y = yadisk.YaDisk("f303b8380db54e49b15653a1209dab1f", "7e2a45d0322a4784aca57c998ec24863",
                  "AQAAAAAxhUvqAAV8Wn_FxaChMUjJgVtqGRQx12c")

# Проверяет, валиден ли токен
print(y.check_token())

# Скачивает "/some-file-to-download.txt" в "downloaded.txt"
y.download("/temp/data.txt", "downloaded_data.txt")
