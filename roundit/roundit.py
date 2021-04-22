from PIL import Image, ImageDraw
import os

src_direct_name = 'photo'
tar_direct_name = 'save'


def circle_corner(img, radii):
    # 画圆（用于分离4个角）
    circle = Image.new('L', (radii * 2, radii * 2), 0)  # 创建黑色方形
    # circle.save('1.jpg','JPEG',qulity=100)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radii * 2, radii * 2), fill=255)  # 黑色方形内切白色圆形
    # circle.save('2.jpg','JPEG',qulity=100)

    img = img.convert("RGBA")
    w, h = img.size

    alpha = Image.new('L', img.size, 255)
    alpha.paste(circle.crop((0, 0, radii, radii)), (0, 0))  # 左上角
    alpha.paste(circle.crop((radii, 0, radii * 2, radii)),
                (w - radii, 0))  # 右上角
    alpha.paste(circle.crop((radii, radii, radii * 2, radii * 2)),
                (w - radii, h - radii))  # 右下角
    alpha.paste(circle.crop((0, radii, radii, radii * 2)),
                (0, h - radii))  # 左下角

    img.putalpha(alpha)  # 白色区域透明可见，黑色区域不可见

    return img


if __name__ == '__main__':

    radii = 20  # 圆角大小
    tar_width = 300  # 放缩的宽
    tar_height = 300  # 放缩的高

    current_path = os.path.abspath(__file__)  # 获取当前文件的绝对路径
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep)  # 获取当前文件的父目录

    # 拼接成绝对路径
    src_path = os.path.join(father_path + os.path.sep + src_direct_name)
    tar_path = os.path.join(father_path + os.path.sep + tar_direct_name)

    for f in os.listdir(src_path):
        img_name = os.path.basename(f)
        print('当前处理：', img_name)
        img = Image.open(os.path.join(src_path + os.path.sep, img_name))
        img = img.resize((tar_width, tar_height), Image.ANTIALIAS)
        img = circle_corner(img, radii)
        img.save(tar_path + os.path.sep + img_name, 'png', quality=100)
