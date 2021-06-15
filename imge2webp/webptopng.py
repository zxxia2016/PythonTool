import os

decoder_path = "dwebp.exe" # Windows10下其实也支持斜杠/路径
src_direct_name = 'webp'
tar_direct_name = 'png'


if __name__ == '__main__':
    current_path = os.path.abspath(__file__)  # 获取当前文件的绝对路径
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)  # 获取当前文件的父目录

    # 拼接成绝对路径
    src_path = os.path.join(father_path + os.path.sep + src_direct_name)
    tar_path = os.path.join(father_path + os.path.sep + tar_direct_name)
    exe_path = os.path.join(father_path + os.path.sep + decoder_path)

    if not os.path.exists(tar_path):
        os.mkdir(tar_path)
  
    for f in os.listdir(src_path):
        res_f = str(f).replace(".webp", ".png")
        cmd = "{0} {1} -o {2}".format(exe_path, os.path.join(src_path, f),
                                      os.path.join(tar_path, res_f))
        os.system(cmd)
