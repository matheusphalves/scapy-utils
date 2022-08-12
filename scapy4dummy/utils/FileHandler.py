import zipfile
import os, time

class FileHandler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def read_file(path, read_mode='w'):
        if path:
            with open(path, mode=read_mode) as f:
                content = f.read()
                f.close()
                return content
        return None

    @staticmethod
    def save_file(path, save_mode, file_object):
        with open(path, save_mode) as f:
            f.write(file_object)

    @staticmethod
    def save_dict_to_csv(dict_to_save, file_name, file_path=None):

        if file_path is None:
            file_path = os.getcwd() + '/tmp/'
            try:
                os.mkdir(file_path)
            except:
                pass

            file_path = os.path.join(file_path, f'{file_name}_{time.time_ns()}.csv')

        with open(file_path, 'w') as f:
            for key in dict_to_save.keys():
                f.write("%s, %s\n" % (key, dict_to_save[key]))

    @staticmethod
    def unzip_file(file_path, target_dir, read_mode='r'):
        with zipfile.ZipFile(file_path, read_mode) as zip_ref:
            zip_ref.extractall(target_dir)