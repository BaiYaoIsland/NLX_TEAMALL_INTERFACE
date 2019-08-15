# coding:utf-8
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from data import data_config
from util.connect_db import OperationMysql

class GetData:
    # 构造函数，类初始化
    def __init__(self,file_name=None,sheet_id=None):
        self.opera_excel = OperationExcel(file_name,sheet_id)
    # 获取excel行数，即用例个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()
    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.GLOBAL_VAR.RUN.value)
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = int(data_config.GLOBAL_VAR.HEADER.value)
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            return data_config.get_header_value()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.GLOBAL_VAR.REQUEST_WAY.value)
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = int(data_config.GLOBAL_VAR.URL.value)
        url = self.opera_excel.get_cell_value(row, col)
        # print("Running URL=",url)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.GLOBAL_VAR.DATA.value)
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 通过获取关键字请求数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        res = self.get_request_data(row)
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = int(data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 通过SQL获取预期结果
    def get_expcet_data_for_mysql(self,row):
        op_mysql = OperationMysql()
        sql = self.get_expcet_data(row)
        res = op_mysql.search_one(sql)
        return res

    # 写入实际结果
    def write_result(self,row,value):
        col = int(data_config.GLOBAL_VAR.RESULT.value)
        self.opera_excel.write_value(row,col,value)

    # 获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.GLOBAL_VAR.DATA_DEPEND.value)
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.GLOBAL_VAR.CASE_DEPEND.value)
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_fileld(self,row):
        col = int(data_config.GLOBAL_VAR.FIELD_DEPEND.value)
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data

if __name__ == '__main__':
    file_name = '../dataconfig/interfaceTest.xlsx'
    sheet_id = 0
    data = GetData(file_name,sheet_id)
    print('This is json data :',data.get_data_for_json(2))
    print('This is request data :',data.get_request_data(8))
    print('This is header data :',data.is_header(2))
    print('This is method :',data.get_request_method(4))
    print('This is depend fileld :',data.get_depend_fileld(8))