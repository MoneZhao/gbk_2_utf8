# encoding = utf-8
import os
import sys

end_with = ".txt"
convert_source_dir = "source"
convert_result_dir = "result"


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

        with open(path, "r", encoding="gbk") as txt_file, open(target_path + os.sep + new_path, "w", encoding="utf-8") as new_file:
            try:
                new_file.write(txt_file.read())
                print("转换文件: " + target_path + os.sep + new_path + " 完成")
            except UnicodeDecodeError as e:
                print('转换', new_path, '失败：', e)


if __name__ == '__main__':
    source_path = os.path.abspath('.') + os.sep + convert_source_dir
    if os.path.exists(source_path):
        target_path = os.path.abspath('.') + os.sep + convert_result_dir
        resolve_dir(source_path, source_path, target_path)
        print("转换结束")
    else:
        os.makedirs(source_path)
        print("转换结束")
