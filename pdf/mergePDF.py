import os
import argparse

from PyPDF2 import PdfFileWriter, PdfFileReader


def merge_pdf(filename, read_dirpath, save_dirpath):
    """
    合并多个 PDF 文件
    :param filename: pdf文件名称的前缀
    :param read_dirpath: 要合并的 PDF 目录
    :param save_dirpath: 合并后的 PDF 文件路径
    :return:
    """

    pdf_writer = PdfFileWriter()
    # 对文件名进行排序
    list_filename = os.listdir(read_dirpath)
    list_filename.sort(key=lambda x: int(x[:-4].replace(filename, "")))

    for fn in list_filename:
        print(fn)
        filepath = os.path.join(read_dirpath, fn)

        # 读取文件并获取文件的页数
        pdf_reader = PdfFileReader(filepath)
        pages = pdf_reader.getNumPages()

        # 逐页添加
        for page in range(pages):
            pdf_writer.addPage(pdf_reader.getPage(page))

    save_dirpath = os.path.join(save_dirpath, filename + '.pdf')
    # 保存合并后的文件
    with open(save_dirpath, "wb") as out:
        pdf_writer.write(out)
    print("文件已成功合并，保存路径为：", save_dirpath)


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Use for merge pdf")
    parser.add_argument('--filename', type=str, help='The premix name of mini pdf.')
    parser.add_argument('--read_dirpath', type=str, help='The directory path which store mini pdfs.')
    parser.add_argument('--save_dirpath', type=str, help="Result pdf's path")

    opt = parser.parse_args()

    merge_pdf(opt.filename, opt.read_dirpath, opt.save_dirpath)
