import os
import shutil


address = os.getcwd()
address = r"/".join(address.split("\\"))
report_path_del = address+'/report'
print(report_path_del)
# os.remove(report_path_del)
shutil.rmtree(report_path_del)
