# coding:utf-8
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail
import HTMLTestRunner
from log.user_log import UserLog

logger = UserLog().get_log()

class RunTest:
    def __init__(self):
        self.run = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_mail = SendEmail()
        self.log = UserLog()
        self.logger = UserLog.get_log()

    # 程序执行的主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                # if i == 7:
                #     print("已经成年")
                # url = 'http://192.168.2.81:10003/shop/goods/new-list'
                method = self.data.get_request_method(i)
                is_run = self.data.get_is_run(i)
                data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data(i)
                # expect = self.data.get_expcet_data_for_mysql(i)
                # data = {'pageNum': 1, 'pageSize': 10}
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                # header = {'Content-Type': 'application/json'}
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    print("this is dependResponseData = ",depend_response_data)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_fileld(i)
                    print("*************this is depend_key = ",depend_key)
                    # 根据获取的依赖key,将depend_kay更新成depend_response_data
                    data[depend_key] = depend_response_data
                    print("*************this is data[depend_key]",data[depend_key])

                res = self.run.run_main(method, url, data, header)
                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,'Pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,res)
                    fail_count.append(i)
            else:
                self.data.write_result(i, 'N/A')
                continue
            # print(res)
            #     print(len(pass_count))
            #     print(len(fail_count))
        self.send_mail.send_main(pass_count,fail_count)
                # return res

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
    filepath = '../report/htmlreport1.html'
    fp = open(filepath, 'wb')
    runer = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    runer.run(run)