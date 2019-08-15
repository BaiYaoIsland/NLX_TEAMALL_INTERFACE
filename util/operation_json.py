# coding:utf-8
import json
# fp = open('./dataconfig/login.json')
# data = json.load(fp)
# print(data['login'])

class OperationJson:
    def read_data(self):
        with open('../dataconfig/login.json') as fp:
            data = json.load(fp)
            return data

    def __init__(self):
        self.data = self.read_data()

    def get_data(self, id):
        if id != None:
            return self.data[id]

if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('addcart'))
    print(opjson.get_data('pageParam'))