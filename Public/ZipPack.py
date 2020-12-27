import zipfile
import os


def dfs_get_zip_file(input_path, filelists):
    files = os.listdir(input_path)  # 获取文件目录列表
    for file in files:  # 循环列表
        if os.path.isdir(input_path + '/' + file):  # 判断是文件还是目录
            dfs_get_zip_file(input_path + '/' + file, filelists)  # 如果是文件夹则继续调用自身方法，获取该文件夹下的文件。以此类推
        else:
            filelists.append(input_path + '/' + file)  # 将文件路径存放在列表中


def zip_path(input_path, output_path, output_name):  # input_path:获取文件路径  output_path：打包文件输出路径  output_name：打包文件名称

    zip = zipfile.ZipFile(output_path + r"/" + output_name, 'w',
                          zipfile.ZIP_DEFLATED)  # 创建一个新zip包  w：写入模式  ZIP_DEFLATED：压缩文件
    filelists = []
    dfs_get_zip_file(input_path, filelists)  # 获取全部文件的方法，传进去一个初始路径和一个列表。列表用于存储文件路径
    for file in filelists:  # 遍历文件路径
        zip.write(file)  # 将文件写入zip包中
    zip.close()  # 关闭zip包
    return output_path + r"/" + output_name  # 返回一个zip包路径
# if __name__=='__main__':
#     zip_path('./Report/Html/','./Report/Zip','test.zip')
