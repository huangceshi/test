import os
import zipfile


def get_zip_file(input_path, result):
    files = os.listdir(input_path)

    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result)
        else:
            result.append(file)

def zip_file(input_path, output_path, output_name):

    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        if 'html' in file:
            f.write(input_path + '2020-11-26-19-44-38.html', arcname='2020-11-26-19-44-38.html')
        else:
            f.write(input_path + 'assets/style.css', arcname='assets/style.css')
    f.close()

if __name__ == '__main__':
#     address = os.getcwd()
#     address = r"/".join(address.split("\\"))
#     print(address)
    report_path1 = 'E:/test/testPT/api/report/'
    report_path2 = 'E:/test/testPT/api'
    zip_file(report_path1, report_path2, 'report.zip')

# currpath =os.getcwd()
# print(currpath)
# zipname =currpath+"\\"+"report.zip"
#
# f =zipfile.ZipFile(zipname,'w',zipfile.ZIP_DEFLATED)
# f.write(currpath+'\\'+"report",arcname="report")
# f.close()








