from selenium import webdriver
from time import *
from selenium.webdriver import ActionChains  # 引入鼠标事件
from selenium.webdriver.common.keys import Keys

# 浏览器启动
# d = webdriver.Chrome()    #调用谷歌浏览器
# d = webdriver.Ie()      #调用IE浏览器
d = webdriver.Firefox()  # 调用火狐浏览器
d.maximize_window()  # 全屏显示浏览器
d.get('https://www.baidu.com/')  # 输入网址
sleep(2)

# 模拟鼠标操作
# set = d.find_element_by_link_text('设置')  #获取“设置”按钮元素，当页签元素<a>出现时用link定位法。其他定位法无效
set = d.find_element_by_id('s-usersetting-top')  # 2020-7-8 百度首页变化，设置按钮从<a>标签变为<span>标签，并设有id，所以直接获取id即可
ActionChains(d).move_to_element(set).perform()  # 鼠标悬停在“设置”按钮
sleep(2)
g = d.find_element_by_link_text('关闭预测')
sleep(2)
ActionChains(d).move_to_element(g).click().perform()

"""
'''
ActionChains(d)
调用ActionChains()类，将浏览器驱动d作为参数
move_to_element(set)
调用move_to_element()方法用于模拟鼠标悬停操作，在调用时需要指定元素定位
perform()
执行所有ActionChains中存储的行为，可以理解为对整个操作的提交动作
'''
sleep(2)
gb  = d.find_element_by_link_text('关闭预测') #获取“关闭预测”按钮元素
ActionChains(d).click(gb).perform()          #鼠标点击“关闭预测”按钮
sleep(2)

#页面基础操作
d.find_element_by_id("kw").send_keys('Selenium') #输入框中输入“Selenium”
sleep(2)
d.find_element_by_id("su").click()  #点击“百度一下”按钮
sleep(2)

d.back()  #控制浏览器后退
sleep(2)
d.forward() #控制浏览器前进
sleep(2)
d.refresh() #控制浏览器刷新页面
sleep(2)
d.find_element_by_id('kw').clear() #清空输入框内容
sleep(2)
d.find_element_by_id('kw').send_keys('C#') #输入框中输入“C#”
sleep(2)
d.find_element_by_id('kw').submit()  #点击“百度一下”按钮
sleep(2)
#键盘操作
'''
Keys.BACK_SPACE：回退键（BackSpace）
Keys.TAB：制表键（Tab）
Keys.ENTER：回车键（Enter）
Keys.SHIFT：大小写转换键（Shift）
Keys.CONTROL：Control键（Ctrl）
Keys.ALT：ALT键（Alt）
Keys.ESCAPE：返回键（Esc）
Keys.SPACE：空格键（Space）
Keys.PAGE_UP：翻页键上（Page Up）
Keys.PAGE_DOWN：翻页键下（Page Down）
Keys.END：行尾键（End）
Keys.HOME：行首键（Home）
Keys.LEFT：方向键左（Left）
Keys.UP：方向键上（Up）
Keys.RIGHT：方向键右（Right）
Keys.DOWN：方向键下（Down）
Keys.INSERT：插入键（Insert）
DELETE：删除键（Delete）
NUMPAD0 ~ NUMPAD9：数字键1-9
F1 ~ F12：F1 - F12键
(Keys.CONTROL, ‘a’)：组合键Control+a，全选
(Keys.CONTROL, ‘c’)：组合键Control+c，复制
(Keys.CONTROL, ‘x’)：组合键Control+x，剪切
(Keys.CONTROL, ‘v’)：组合键Control+v，粘贴
'''
d.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
sleep(2)
d.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
sleep(2)
d.find_element_by_id('kw').send_keys('JVAV和')
sleep(2)
d.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
sleep(2)
d.find_element_by_id('kw').send_keys(Keys.ENTER)
sleep(2)

#自动化判定结果的一个小尝试
print(ctime())
for i in range(5): #循环5次
    try:
      el=d.find_element_by_id('kw')
      if el.is_displayed(): #判断元素是否显示
          print('找到ID为‘kw’的控件')
    except Exception as a:
        i=i+1
        print('第%r次没找到控件'%i)
        i=i-1
    else: #当判定成功后，执行else语句
        print('判定成功')
        break #跳出当前循环
    sleep(1)
    print(ctime())
else: #当for语句循环完成后，执行else语句
    print('time out')
d.close() #关闭当前窗口
print(ctime())

#定位一组元素（本内容无法执行，仅供参考之用，详见书中第4.8章节）
checkboxes=d.find_elements_by_xpath("//input[@type='checkboxe']") #通过xpath找到所有type=checkbox的元素（复选框）
for checkbox in checkboxes: #遍历checkboxes元素
    checkbox.click() #勾选复选框
    sleep(1)

print(len(checkboxes)) #打印当前页面type为checkbox的个数
d.find_elements_by_xpath("//input[@type='checkboxe']").pop().click() #把页面上最后一个checkbox的勾选去掉
                                                                    #pop()方法用于获取列表中的一个元素（默
                                                                    #认为最后一个），pop(0)为第一个

#多表单切换（本内容无法执行，仅供参考之用，详见书中第4.9章节）
d.switch_to.frame('if')  #切换到iframe(id=if)
d.find_element_by_id('kw').send_keys('Selenium')

#多窗口切换（因现行浏览器默认以多页签形式展现，本段代码暂无法正常运行，仅供参考）
baidu=d.current_window_handle #获取当前窗口句柄(百度首页）
print('首页句柄：',baidu)
d.find_element_by_link_text('登录').click()
sleep(2)
d.find_element_by_link_text('立即注册').click()
sleep(2)
reg1=d.current_window_handle #获取当前窗口句柄（注册页面1）
print('注一句柄：',baidu)
span=d.find_elements_by_tag_name('span') #通过标签名称获取页面元素集，实在无法找到元素的终极手段。
for s in span:                           #遍历元素集，并通过唯一性找到需要的元素
    if s.id=='login_btn':
        s.click()
sleep(2)
d.find_element_by_link_text('立即注册').click()
sleep(2)
reg2=d.current_window_handle #获取当前窗口句柄（注册页面2）
print('注二句柄：',baidu)
all_handles=d.window_handles #获取全部窗口句柄

for handles in all_handles:
    print('全部句柄：', baidu)
    if handles==reg2:
        print(handles)
        d.switch_to.window(handles)  #跳转到注2窗口
        d.close()                    #关闭注2窗口
sleep(2)
d.switch_to.window(baidu)
d.find_element_by_id('kw').send_keys('Selenium')

#警告框处理
#set = d.find_element_by_link_text('设置')  #获取“设置”按钮元素，当页签元素<a>出现时用link定位法。其他定位法无效
ActionChains(d).move_to_element(set).perform() #鼠标悬停在“设置”按钮

sleep(2)
gb  = d.find_element_by_link_text('搜索设置') #获取“关闭预测”按钮元素
ActionChains(d).click(gb).perform()          #鼠标点击“关闭预测”按钮
sleep(2)

d.find_element_by_link_text('保存设置').click()
sleep(2)
print(d.switch_to.alert.text) 
sleep(2)
d.switch_to.alert.accept() 

'''
# 警告框备注
switch_to.alert 	切换到Alert
accept 	点击Alert的【确认】按钮
authenticate(username,password) 	给需要验证的Alert发送账号和密码，默认点击OK
dismiss()  	点击Alert的【取消】按钮
send_keys(keysToSend) 	在Alert的输入框输入信息
text 	获取Alert上的文言信息  '''

#上传文件
#上传文件的整体思路是在上传文件框中输入文件地址，当无法输入地址时用Autolt软件先录制一个获取文件的exe脚本后，在Python中执行
d.find_element_by_id('file').send_keys('D:\\up.txt') #推荐第一种方法，第二种方法详见书中第4.12章节

#下载文件的相关内容详见书中4.13章节，本章节仅介绍了Firefox浏览器下载文件的相关设置

#操作Cookie
d.add_cookie({'name':'aa','value':'001'}) #添加一个Cookie
cookie=d.get_cookies() #获取全部Cookie
for c in cookie:
    if c['name']=='aa': #判断Cookie中‘name’值等于‘aa’，并打印该Cookie的name和value值
          print('%r->%r'%(c['name'],c['value']))
          print('第一次',c)
d.delete_cookie('aa')  #删除Cookie时，不支持中文。所以在添加Cookie时不要添加中文
cookie2=d.get_cookies()
for c2 in cookie2:
    if c2['name'] == 'aa':
        print('第二次：%r->%r'%(c2['name'],c2['value']))
        print('第二次',c2)

#调用JavaScript
#此处仅说明Selenium可以执行JavaScript脚本，实际应用中所涉及的具体操作需参考JavaScript语言编写，同时JavaScript也可以操作HTML5页面
d.set_window_size(600,600) #将窗口大小控制在600*600
sleep(2)
js='window.scrollTo(50,150)' #编辑JavaScript脚本，控制滚动条位置
d.execute_script(js) #执行JavaScript脚本
"""
# 窗口截图（可用于Bug截图操作）
# d.get_screenshot_as_file('C:\\Users\\Yuxiao\\Desktop\\baidu.png')
# d.quit()  #退出驱动关闭所有窗口
