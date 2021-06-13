import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse


def split_pdf(filepath, save_dirpath, step=5):
    """
    拆分PDF为多个小的PDF文件
    :param filepath: 文件路径
    :param save_dirpath: 保存小的PDF的文件路径
    :param step: 每step间隔的页面生成一个文件，例如step=5，表示0-4页为一个文件
    :return:
    """

    if not os.path.exists(save_dirpath):  # 保存小文件的路径不存在
        os.mkdir(save_dirpath)

    pdf_reader = PdfFileReader(filepath)

    filename = os.path.basename(filepath).replace('.pdf', '')

    # 读取每一页的数据
    pages = pdf_reader.getNumPages()
    for page in range(0, pages, step):
        pdf_writer = PdfFileWriter()
        # 拆分pdf，每 step 页的拆分为一个文件
        for index in range(page, page+step):
            if index < pages:
                pdf_writer.addPage(pdf_reader.getPage(index))

        # 保存拆分后的小文件
        save_path = os.path.join(save_dirpath, filename+str(int(page/step)+1) + '.pdf')
        print(save_path)
        with open(save_path, 'wb') as out:
            pdf_writer.write(out)

    print("文件已成功拆分，保存路径为：" + save_dirpath)


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Use for split pdf")
    parser.add_argument('--pdf_path', type=str, help='Path to the pdf.')
    parser.add_argument('--save_directory', type=str, help='Path use to store mini pdf.')
    parser.add_argument('--step', type=int, default=5, help="Each mini pdf's total pages.")

    opt = parser.parse_args()

    split_pdf(opt.pdf_path, opt.save_directory, opt.step)
