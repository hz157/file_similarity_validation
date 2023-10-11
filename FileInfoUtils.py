import os
import stat
import platform
import datetime

class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)

    def get_size(self):
        return os.path.getsize(self.file_path)

    def get_create_time(self):
        if platform.system() == 'Windows':
            return datetime.datetime.fromtimestamp(os.path.getctime(self.file_path))
        else:
            return datetime.datetime.fromtimestamp(os.stat(self.file_path).st_birthtime)

    def get_modify_time(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path))

    def get_owner(self):
        if platform.system() == 'Windows':
            import getpass
            return getpass.getuser()
        else:
            import pwd
            return pwd.getpwuid(os.stat(self.file_path).st_uid).pw_name

    def get_computer_name(self):
        return platform.node()

    def get_file_type(self):
        file_type = ""
        if os.path.isdir(self.file_path):
            file_type = "Directory"
        elif os.path.islink(self.file_path):
            file_type = "Symbolic Link"
        elif os.path.isfile(self.file_path):
            file_type = "File"
        return file_type

    def get_file_location(self):
        return os.path.dirname(os.path.abspath(self.file_path))


