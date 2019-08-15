# coding:utf-8
from enum import Enum

class GLOBAL_VAR(Enum):
    ID = '1'
    MODULE = '2'
    URL = '3'
    RUN = '4'
    REQUEST_WAY = '5'
    HEADER = '6'
    CASE_DEPEND = '7'
    DATA_DEPEND = '8'
    FIELD_DEPEND = '9'
    DATA = '10'
    ECPECT = '11'
    RESULT = '12'
    # header = '12'

def get_header_value():
    header ={'Content-Type': 'application/json','token':'c56c9f5e-9b49-4b87-94c0-f1c5b58b1b1c'}
    return header

if __name__ == '__main__':
    print(GLOBAL_VAR.ID.value)