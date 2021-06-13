import os
import argparse
from pdf2image import convert_from_bytes


def pdf2image(pdf_path, pic_dirpath):
    if not os.path.exists(pic_dirpath):
        os.mkdir(pic_dirpath)

    images = convert_from_bytes(open(pdf_path, 'rb').read())
    for image in images:
        # 保存图片
        pdf_name = os.path.basename(pdf_path)[:-4]  # 获取文件名称
        pic_filepath = os.path.join(pic_dirpath, pdf_name + "_" + str(images.index(image)) + '.png')
        image.save(pic_filepath, 'PNG')


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Use for merge pdf")
    parser.add_argument('--pdf_path', type=str, help='The pdf file path.')
    parser.add_argument('--pic_dirpath', type=str, help='The directory path which use to store images.')

    opt = parser.parse_args()

    pdf2image(opt.pdf_path, opt.pic_dirpath)

