# coding:utf-8
import requests
import json
class RunMethod:
    def post_main(self, url, data=None, header=None):
        res = None
        if data != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url)
        # print("Request status code =",res.status_code)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if data != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        # print("Request status code =", res.status_code)
        return res.text

    def run_main(self, method, url, data=None, header=None):
        data = json.dumps(data)
        res = None
        if method == "POST":
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == '__main__':
    run = RunMethod()
    url = 'http://192.168.2.81:10003/shop/goods/new-list'
    data = {'pageNum': 1,'pageSize': 10}
    header = {'Content-Type':'application/json'}
    # r = requests.post(url,data)

    print(run.run_main("POST",url,data,header))




# # r = requests.post(url='http://192.168.2.81:10003/shop/goods/new-list',data=json.dumps({'pageNum': 1,'pageSize': 10}),headers={'Content-Type':'application/json'})
# r = requests.post(url='http://192.168.2.81:10003/shop/goods/new-list',data=('{"pageNum": 1,"pageSize": 10}').json(),headers={'Content-Type':'application/json'})
# print(r.text)