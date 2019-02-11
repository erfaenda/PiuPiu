import posixpath, os, yadisk
from time import sleep


class YandexDisk():
    # Загружает "file_to_upload.txt" в "/destination.txt"
    def uploadOneFile(self):
        path = "/temp/data.txt"
        if y.exists(path):
            # Безвозвратно удаляет "/file-to-remove"
            y.remove(path, permanently=True)
            sleep(1)
            y.upload("data.txt", "/temp/data.txt")
        else:
            y.upload("data.txt", "/temp/data.txt")

    def downLoadOneFile(self):
        y.download("/temp/data.txt", "downloaded_data.txt")


if __name__ == "__main__":
    app = YandexDisk()
    y = yadisk.YaDisk("f303b8380db54e49b15653a1209dab1f", "7e2a45d0322a4784aca57c998ec24863",
                      "AQAAAAAxhUvqAAV8Wn_FxaChMUjJgVtqGRQx12c")
    app.uploadOneFile()
    sleep(5)
    #app.downLoadOneFile()

