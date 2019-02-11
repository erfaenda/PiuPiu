import posixpath, os, yadisk
from time import sleep

class YandexDisk():
    # функция для рекурсивной закачки файлов
    def recursive_upload(self, y, from_dir, to_dir):
         for root, dirs, files in os.walk(from_dir):
             p = root.split(from_dir)[1].strip(os.path.sep)
             dir_path = posixpath.join(to_dir, p)

             try:
                 y.mkdir(dir_path)
             except yadisk.exceptions.PathExistsError:
                 pass

             for file in files:
                 file_path = posixpath.join(dir_path, file)
                 p_sys = p.replace("/", os.path.sep)
                 in_path = os.path.join(from_dir, p_sys, file)
                 try:
                     y.upload(in_path, file_path)
                 except yadisk.exceptions.PathExistsError:
                     pass
    def downLoadOneFile(self):
        y.download("/temp/data.txt", "downloaded_data.txt")

if __name__ == "__main__":
    app = YandexDisk()
    y = yadisk.YaDisk("f303b8380db54e49b15653a1209dab1f", "7e2a45d0322a4784aca57c998ec24863",
                      "AQAAAAAxhUvqAAV8Wn_FxaChMUjJgVtqGRQx12c")
    to_dir = "/temp"
    from_dir = "C:\\Users\\Alex\\PycharmProjects\\PiuPiu\\yandexDisk\\upload"
    app.recursive_upload(y, from_dir, to_dir)
    sleep(5)
    app.downLoadOneFile()

