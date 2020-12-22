from time import *


class Log():
    # 登录
    def Login(self, driver, username, password):
        # 点击登录框右上角，将登录框从扫描二维码切换至输入用户名和密码
        # driver.find_element_by_id('lbNormal').click()
        sleep(2)
        # 定位iframe   通过xpath路径获取iframe控件
        # contains(@id,'value')方法用于标签属性值包含特定字符定位，其中@id表示需要匹配属性，value表示被包含的属性值
        iframe = driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]')
        driver.switch_to.frame(iframe)  # 切换到iframe页签
        sleep(1)

        # 定位用户名框
        driver.find_element_by_xpath("//input[@name='email']").clear()  # 清空用户名框
        driver.find_element_by_xpath("//input[@name='email']").send_keys(username)  # 填写用户名
        sleep(1)
        # 定位密码框
        driver.find_element_by_xpath("//input[@name='password']").clear()  # 清空用户名框
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)  # 填写用户名
        sleep(2)
        # 点击登录按钮
        driver.find_element_by_link_text('登  录').click()

    # 退出
    def Logout(self, driver):
        driver.find_element_by_link_text('退出').click()

    # 写邮件
    def Body(self, driver, mailaddres, mailtitle, mailtext):
        # 点击写信按钮，进入写信页面
        # text是标签的一个方法，在xpath中标签方法的调用写作name(),属性的调用写作@name
        driver.find_element_by_xpath('//span[(text()="写 信")]').click()
        sleep(2)

        # 输入收件人地址
        driver.find_element_by_xpath('//input[contains(@class,"nui-editableAddr-ipt")]').send_keys(mailaddres)
        sleep(1)

        # 输入邮件标题
        driver.find_element_by_xpath('//input[contains(@id,"subjectInput")]').send_keys(mailtitle)
        sleep(1)

        # 定位iframe   通过xpath路径获取iframe控件
        driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="APP-editor-iframe"]'))

        # 通过JavaScript脚本写入邮件正文
        '''text = "document.getElementsByTagName('body')[0].innerHTML='<b>" + mailtext + "</b>'"
        driver.execute_script(text)
        sleep(2)'''
        # 126邮箱发送邮件页面，将邮件正文输入框放在了iframe框架下，所以在获取正文框时需先切换到iframe框中

        # 通过xpath定位到body元素，写入邮件正文。find_element_by_xpath方法只能获取一个标签元素。
        driver.find_element_by_xpath('//body[contains(@class,"nui-scroll")]').send_keys(mailtext)

        '''# 通过xpath定位到全部的body标签集合，并指定在第一个body标签（即('//body')[0]）中写入邮件正文
        driver.find_elements_by_xpath('//body')[0].send_keys(mailtext)'''

        # 返回上一个iframe表单中
        driver.switch_to.parent_frame()

        # 点击上边的发送按钮
        # driver.find_element_by_xpath('//div[contains(@id,"mail_button")]//span[text()="发送"]').click()

        # 点击下边的发送按钮
        # driver.find_element_by_xpath('//footer//span[text()="发送"]').click()

        # 点击发送按钮
        driver.find_element_by_xpath('//span[text()="发送"]').click()
        sleep(5)
