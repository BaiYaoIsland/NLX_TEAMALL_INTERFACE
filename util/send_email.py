# -*- coding: utf-8 -*-
# 发送邮件及启动邮件服务器
import smtplib
# 邮件格式及内容,邮件格式MIMEText
from email.mime.text import MIMEText
class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.sina.com"
    send_user = "wowaidananjing@sina.com"
    password = "*********"
    def send_mail(self,user_list,sub,content):
        user = "JHzhang" + "<" + send_user + ">"
        message = MIMEText(content, subtype='plain', charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 计算通过率的百分比
        pass_result = "%.1f%%" %(pass_num/count_num*100)
        # 计算失败率的百分比
        fail_result = "%.1f%%" %(fail_num/count_num*100)

        user_list = ['5zhishi20xb@sina.com']
        sub = '接口自动化测试报告'
        # 此处切记格式正确
        content = '此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s个。通过率为%s，失败率为%s。' %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)

if __name__ == '__main__':
    # sen = SendEmail()
    # sen.send_main([1,2,3,4],[2,3,4,5,6,7])
    sen = SendEmail()
    user_list = ['5zhishi20xb@sina.com']
    sub = '邮件'
    content = '收到的邮件'
