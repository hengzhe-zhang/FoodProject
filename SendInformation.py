#向移动云端发送数据
import requests,json
url="http://api.heclouds.com/devices/"
headers={"api-key":""}
def senddata(value):
    data={
        "datastreams":[
            {
                "id":"uid",
                "datapoints":[
                    {"value":value},
                ]
            }

        ]
    }
    wb_data=requests.post(url,headers=headers,data=json.dumps(data))
    print(wb_data.text)