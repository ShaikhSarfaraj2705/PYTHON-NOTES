#shutil module:shutil is python module that provides a higher level interface for working 
#with file and directories.it provides a convinient  and efficient way  to automate tasks 
#that are commomnly performed on files and directories.
import shutil
#shutil.copy(src,dst):copies the file located at src to a new location specified by dst.
shutil.copy("100 days/52.shutil_module.py","100 days/52.shutil_module2.py") 

#shutil.copy2(src,dst):this function similar to shutil.copy but it also preserves more 
#meta data about original file,such as a timestamp

shutil.copytree("100 days/52.shutil_module_original_folder","100 days/52.shutil_module_copied_folder")