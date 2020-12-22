import os
from time import *
def insert_img(driver,filename):
    driver.maximize_window()
    t = '登录成功' + strftime("%Y-%m-%d %H_%M_%S")
    dir = os.path.dirname(os.path.dirname(__file__)).replace('/','\\') + '\\Image\\'+filename+t+'.png'
    driver.get_screenshot_as_file(dir)   #跨类调用get_screenshot_as_file方法时，路径只能用绝对路径，不可以使用相对路径
