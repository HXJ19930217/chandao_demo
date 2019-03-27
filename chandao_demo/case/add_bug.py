#coding ：utf-8
from selenium import webdriver
from chandao_demo.common.Base import  Base

"'封装添加BUG的方法  " \
"1.登录  " \
" 2.添加BUG   " \
"3.判断是否添加成功 '"

class ZenTaoBug(Base):  #继承Base的所有方法

    url='http://pro.demo.zentao.net/bug-browse-20.html'
    #定位登录
    admin_name=('id','account')
    admin_pwd=('name','password')
    login_button=('id','submit')

    #添加BUG
    test_name=('xpath',".//*[@id='navbar']/ul/li[4]/a")  #导航
    test_modle = ('xpath', ".//*[@id='subNavbar']/ul/li[1]/a")  # bug模块
    button_bug=('xpath',".//*[@id='mainMenu']/div[3]/a[3]") #添加Bug
    version1=('xpath',".//*[@id='openedBuild_chosen']/ul") #点击版本输入框
    version2=('xpath',".//*[@id='openedBuild_chosen']/div/ul/li")  #点击版本号
    bug_title=('id','title')   #标题
    frmae=('id','ke-edit-iframe')
    bug_step=('xpath','html/body')  #内容
    bug_sumit=('id','submit')   #提交bug


    def login(self,user="demo",pwd='123456'):
        driver.get('http://pro.demo.zentao.net/user-login.html')
        self.clear(self.admin_name)
        self.input_text(self.admin_name,user)
        self.clear(self.admin_pwd)
        self.input_text(self.admin_pwd,pwd)
        self.click(self.login_button)
        self.sleep_time(3)

    def add_bug(self):
        self.click(self.test_name)
        self.click(self.test_modle)
        self.click(self.button_bug)
        self.click(self.version1)
        self.click(self.version2)
        self.input_text(self.bug_title,'标题325')
        #输入框body
        frame=self.find_element('class name','ke-edit-iframe')
        self.driver.switch_to_frame(frame)  #切换进入frame输入框

        #富文本不能clear
        self.input_text(self.bug_step,"bug内容")
        self.driver.switch_to_default_content()   #退出frame
        self.click(self.bug_sumit)  #点击提交按钮


if __name__ == '__main__':      #调试
    driver=webdriver.Firefox()
    bug=ZenTaoBug(driver)
    bug.login()
    bug.add_bug()

