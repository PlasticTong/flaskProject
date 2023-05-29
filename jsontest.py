import json

# with open("E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//tablemes.json", "r", encoding="utf-8") as f:
#     content = json.load(f)
# for a in content["list"]:
#     if a["id"]%2 == 0:
#         a["content"] = "学习"
#     if a["id"]%2 == 1:
#         a["content"] = "下班"
#     # print(a)
#
# with open('E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//tablemes3.json','w',encoding='utf8') as f2:
#     # ensure_ascii=False才能输入中文，否则是Unicode字符
#     # indent=2 JSON数据的缩进，美观
#     json.dump(content,f2,ensure_ascii=False,indent=2)
# print(content["list"])

import random
import json

cotent = {
    "list":[],
    "pageTotal":10000
}
for i in range(0,10000):
    # print(i)
    data = {
        "id": i + 1,
        "source": "192.168.1." + str(random.randint(1, 200)),
        "target": "192.168.1." + str(random.randint(1, 200)),
        "time": random.randint(1, 1800),
        "content": random.choice(["work", "study", "play"])
    }
    cotent["list"].append(data)


json_data = json.dumps(cotent)
print(json_data)
with open('E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//tablemes3.json','w',encoding='utf8') as f2:
    # ensure_ascii=False才能输入中文，否则是Unicode字符
    # indent=2 JSON数据的缩进，美观
    json.dump(cotent,f2,ensure_ascii=False,indent=2)

import pandas as pd
