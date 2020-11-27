import os
import zipfile


def get_zip_file(input_path, result):
    files = os.listdir(input_path)

    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result)
        else:
            result.append(input_path + '/' + file)


def zip_file(input_path, output_path, output_name,repotrname):
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        if 'html' in file:
            repotrname = repotrname + '.html'
            f.write(input_path +'/' +  repotrname, arcname=repotrname)
        else:
            f.write(input_path + 'assets/style.css', arcname='assets/style.css')
    f.close()
