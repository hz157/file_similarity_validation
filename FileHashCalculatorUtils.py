import hashlib

class FileHashCalculator:
    @staticmethod
    def calculate_hash(file_path, algorithm="sha256"):
        """
        计算文件的哈希值

        :param file_path: 文件路径
        :param algorithm: 哈希算法，可选值为 "md5", "sha256", "sha512"，默认为 "sha256"
        :return: 哈希值的十六进制表示
        """
        if algorithm not in ["md5", "sha256", "sha512"]:
            raise ValueError("不支持的哈希算法")

        hash_algorithm = getattr(hashlib, algorithm)()
        with open(file_path, "rb") as file:
            while True:
                data = file.read(65536)  # 每次读取 64KB
                if not data:
                    break
                hash_algorithm.update(data)

        return hash_algorithm.hexdigest()


