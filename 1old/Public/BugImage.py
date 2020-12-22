import os

def insert_img(drvier,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__)) #获取父级文件路径
                                                        #os.path.dirname(__file__)表示获取当前文件的绝对路径
    base_dir=base_dir+'/Image/'
    file_name=base_dir+file_name
    drvier.get_screenshot_as_file(file_name) #截图并存放在Report文件夹中