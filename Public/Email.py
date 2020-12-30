import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


# 发送带附件的Email
def EmailEnclosure(subject, file_name, Emailtext):

    # --------------------------------------------
    sender = '发送邮件地址'  # 发送邮件地址
    receivers = '接收邮件地址'  # 接收邮件地址
    # --------------------------------------------

    mailhost = 'smtp.qq.com'  # 发送邮件的服务器

    message = MIMEMultipart()  # MIMEMultipart用于定义带附件的邮件
    message['From'] = Header(sender, 'utf-8')  # 在邮件的头部信息中加入发送人地址
    message['To'] = Header(receivers, 'utf-8')  # 在邮件的头部信息中加入收件人地址
    message['Subject'] = Header(subject, 'utf-8')  # 在邮件的头部信息中加入标题

    path = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\')  # 获取相对路径并将路径中'\'转换为'//'
    result_dir = path + '\\Report\\Zip\\'  # 定义测试报告目录
    report = os.listdir(result_dir)  # os.listdir()方法可以获取目录下的全部文件和文件
    report.sort(key=lambda fn: os.path.getmtime(result_dir + '\\' + fn))  # 对目录下的文件和文件夹按照时间重新排序

    # 构造附件，传送当前目录下的最新报告
    att1 = MIMEText(open(result_dir + report[-1], 'rb').read(), 'base64', 'utf-8')  # 加载最新的报告
    att1.add_header('Content-Type', 'application/octet-stream')
    att1.add_header('Content-Disposition', 'attachment', filename=file_name)  # filename为附件名称
    message.attach(att1)  # 加载附件

    # 构造文本信息
    text = MIMEText(Emailtext, 'plain', 'utf-8')
    message.attach(text)  # 加载文本信息

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mailhost)  # 加载发送邮件的服务器
    '''
    邮箱第三方登录授权码说明：
    QQ邮箱在第三方登录时需要一个授权码，授权码位置：设置—>账户-
    ->POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务->开启服务（选第一个）->点击生成授权码
    '''
    # ----------------------------------------------------------------
    smtpObj.login('账号', '邮箱第三方登录授权码')  # 登录发送邮件的邮箱
    # ----------------------------------------------------------------

    smtpObj.sendmail(sender, receivers,
                     message.as_string())  # 发送邮件 sender发送人, receivers收件人, message.as_string()邮件信息并强制转换为字符串格式
    smtpObj.close()

