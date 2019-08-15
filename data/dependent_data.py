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


    '''
    所有与其他case有依赖关系的处理方法
    通过case_id获取该case_id的整行数据，此处为独立的逻辑，与之前无关
    '''
    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self):
        # 因为执行case所以用到runmethod方法
        self.run_method = RunMethod()
        # 因为get_data各数据通过行号获取，故依然需要定义行号
        # row_num = 6
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = self.run_method.run_main(method,url,request_data,header)
        # print("there are res's data",res)
        # 只能从dict中获取数据,故需将str转义成dict
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        # 根据行和列定位到“依赖的返回数据”该条case所需依赖数据的位置，获取诸如data:[0]item:num这样的层级解析公式
        depend_data = self.data.get_depend_key(row)
        print("this is dependData =",depend_data)
        # 获取执行依赖case执行的返回结果并赋值给response_data
        response_data = self.run_dependent()
        print("this is responsedata = ",response_data)
        # parse是jsonpath里规则，类似正则表达式，将该路径规则转义正正则表达式然后赋值给json_exe
        jsonpath_exe = parse(depend_data)
        # print("this json_exe=",jsonpath_exe)
        # find也是jsonpath里的规则，即通过转义后的规则中的find方法在response中按此规则查找相应的值并赋给madle
        print(parse("data.shopGoodsList[*].rderNum").find(response_data))
        madle = jsonpath_exe.find(response_data)
        print("this is madle = ",madle)
        # for i in madle:
        #     i.value
        # 增加的for循环，类似于for i in madle，官方写法如此。因为返回的字段为列表，故以[0]写法
        print( [match.value for match in madle][0])
        return [match.value for match in madle][0]

if __name__ == '__main__':
    pass