# encoding = utf-8
import os

end_with = ".txt"
convert_result_dir = "转换结果"


def resolve_dir(path, source_path, target_path):
    path = str(path)
    if not os.path.isdir(path):
        pass
    else:
        files = os.listdir(path)
        for file in files:
            new_path = path + os.sep + file
            if os.path.isdir(new_path):
                target_path_file = target_path + os.sep + file
                if os.path.basename(target_path_file) != convert_result_dir:
                    if not os.path.exists(target_path_file):
                        os.makedirs(target_path_file)
                    resolve_dir(new_path, source_path, target_path_file)
            else:
                resolve_file(new_path, source_path, target_path)


def resolve_file(path, source_path, target_path):
    path = str(path)
    new_path = path.split(os.sep)[-1]
    if path.endswith(end_with):
        if not os.path.exists(target_path) and target_path != "":
            os.makedirs(target_path)
        try:
            txt_file = open(path, "r")
            new_file = open(target_path + os.sep +
                            new_path, "w", encoding="utf-8")
            for line in txt_file:
                new_file.write(line)
        except UnicodeDecodeError:
            txt_file = open(path, "r", encoding="utf-8")
            new_file = open(target_path + os.sep +
                            new_path, "w", encoding="utf-8")
            for line in txt_file:
                new_file.write(line)
        txt_file.close()
        new_file.close()
        print("转换文件: " + target_path + os.sep + new_path + " 完成")


if __name__ == '__main__':
    source_path = os.path.abspath('.')
    target_path = source_path + os.sep + convert_result_dir
    print("转换目录: " + source_path)
    resolve_dir(source_path, source_path, target_path)
    print("转换完成")
