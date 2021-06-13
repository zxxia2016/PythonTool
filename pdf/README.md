# PDF分割：splitPDF.py

使用方法：在cmd中输入：

> python splitPDF.py --pdf_path F:\pythonProject\data\GNN.pdf --save_directory F:\pythonProject\data --step 4

- --pdf_path：是pdf文件的绝对路径
- --save_directory：是pdf文件分割后的文件存储绝对路径
- --step：是按多少页分割成一个文件



# PDF合并：mergePDF.py

使用方法：在cmd中输入：

> python mergePDF.py --filename GNN --read_dirpath F:\pythonProject\data --save_dirpath F:\pythonProject\result

- --filename：文件名
- --read_dirpath：要合并的 PDF 目录
- --save_dirpath：合并后的 PDF 文件路径