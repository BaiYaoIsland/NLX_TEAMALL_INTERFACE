# -*- coding: utf-8 -*-
'''
处理数据依赖的相关问题
'''
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json
class DependentData:
    # 构造函数,引用定义的类的方法时需要实例化后方可进行
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        self.run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = self.run_method.run_main(method,url,request_data,header)
        # print("there are res's data",res)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        print("this is dependData =",depend_data)
        # 获取执行依赖case执行的返回结果并赋值给response_data
        response_data = self.run_dependent()
        print("this is responsedata = ",response_data)
        jsonpath_exe = parse(depend_data)
        # print("this json_exe=",jsonpath_exe)
        print(parse("data.shopGoodsList[*].rderNum").find(response_data))
        madle = jsonpath_exe.find(response_data)
        print("this is madle = ",madle)
        print( [match.value for match in madle][0])
        return [match.value for match in madle][0]

if __name__ == '__main__':
    pass