# ! https://ob6nfbpu76.apifox.cn/api-124951880

import http.client
import json


def obtain_text(messages):

    conn = http.client.HTTPSConnection("api2.aigcbest.top")
    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": messages
    })
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer sk-ZXlWBlusVzO3UDGN71238cE8B6574fE09a5e3c1eBeFf610c',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    dict = json.loads(data)
    print(f'{dict}')
    answer = dict['choices'][0]['message']['content']
    return answer
