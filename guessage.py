import requests
import unittest
import random


class OrderTest(unittest.TestCase):
    # def setUp(self):
    #    url1 = "http://10.12.9.237:8089/sky-pay-cashier/order/initOrderTest"

    def Test_order_sucess(self):
        url1 = "http://10.12.9.237:8089/sky-pay-cashier/order/initOrderTest"
        data1 = {"account": "EHP1010000011770", "amount": "1111.1",
                 "amountCheck": "1", "bankCard": "6225730238200004",
                 "bankName": "收发二", "desc": "7", "extendPara": "6",
                 "lftAgreement": "5", "limitTimeCheck": "1",
                 "merchantProtocol": "201804230008", "notifyUrl": "3",
                 "orderType": "PROTOCOL", "partnerFlow": "20180424300422",
                 "partnerId": "11", "phone": "13421311144",
                 "subAccount": "11", "subOrderType": "NEW", "subject": "31"}
        data1["partnerFlow"] = random.randint(100000, 9999999)
        cc = data1["partnerFlow"]
        r = requests.post(url=url1, data=data1)
        result = r.json()
        print(result)
        #print(cc)
        print(data1["merchantProtocol"])
        bb = result["payCode"]

        url2 = "http://10.12.9.237:8089/sky-pay-cashier/order/payTest"
        data2 = {"brief":bb,"fcsSerialNum":"201804241005",
                 "otherAccBankName":"空中付","otherAccName":"收发二",
                 "otherAccNum":"6225730238200004","procTime":"2018042617:15:20",
                 "tradeAmount":"101.1"}
        data2["fcsSerialNum"] = random.randint(1000,10000)
        #aa = data2["fcsSerialNum"]
        re = requests.post(url=url2,data=data2)
        #result2 = r.json()
        print(re)
'''
if __name__  == "__main__":
    unittest.main()
        '''


OrderTest.Test_order_sucess(self=3)