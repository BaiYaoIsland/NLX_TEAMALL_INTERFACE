# -*- coding: utf-8 -*-
import pymysql
import json

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.2.92',
            port=3306,
            user='testClient',
            password='clientAdmin',
            db='node_v2',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    # 查询一条数据
    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        return result

if __name__ == '__main__':
    op_mysql = OperationMysql()
    print(op_mysql.search_one("SELECT * from t_node_user WHERE `TRADE_ACCOUNT`='100000000598'"))