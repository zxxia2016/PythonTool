import os
import glob

decoder_path = "cwebp.exe"  # Windows10下其实也支持斜杠/路径
src_direct_name = 'png'  # 需要转换的图片的文件夹名称
tar_direct_name = 'webp'


def convert_jpg_to_png(fold_path):
    """
        将 fold_path(绝对路径)文件夹下的 jpg 图片修改成 png 图片
        偷懒的方式，直接通过修改文件后缀进行
    """
    # 获取 fold_path 路径下所有的以 png 结尾的图片
    files = glob.glob(fold_path + '/*.jpg')

    for f in files:
        print('当前处理图片：', os.path.basename(f))
        src = os.path.join(fold_path, f)
        r_name = f.split('.')[0] + '.png'
        dct = os.path.join(fold_path, r_name)
        os.rename(src, dct)


if __name__ == '__main__':
    current_path = os.path.abspath(__file__)  # 获取当前文件的绝对路径
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)  # 获取当前文件的父目录

    # 拼接成绝对路径
    src_path = os.path.join(father_path + os.path.sep + src_direct_name)
    tar_path = os.path.join(father_path + os.path.sep + tar_direct_name)
    exe_path = os.path.join(father_path + os.path.sep + decoder_path)

    convert_jpg_to_png(src_path)  # 将需要转换图片的文件夹下的 jpg 文件修改成 png 格式

    if not os.path.exists(tar_path):
        os.mkdir(tar_path)

    for f in os.listdir(src_path):
        res_f = str(f).replace(".png", ".webp") # 若webp文件命名有特殊,这里需要改改映射规则
        cmd = "{0} {1} -o {2}".format(exe_path, os.path.join(src_path, f),
                                      os.path.join(tar_path, res_f))
        os.system(cmd)
