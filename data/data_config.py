# coding:utf-8
from enum import Enum

class global_var(Enum):
    Id = '1'
    module = '2'
    url = '3'
    run = '4'
    request_way = '5'
    header = '6'
    case_depend = '7'
    data_depend = '8'
    field_depend = '9'
    data = '10'
    expect = '11'
    result = '12'
    # header = '12'

def get_header_value():
    header ={'Content-Type': 'application/json','token':'c56c9f5e-9b49-4b87-94c0-f1c5b58b1b1c'}
    return header

if __name__ == '__main__':
    print(global_var.Id.value)