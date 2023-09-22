import csv

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import random
from flask_cors import CORS
from matplotlib import pyplot as plt

import multinet as mn
import json
import numpy
import Simulated2 as sim
import path
import test

app = Flask(__name__)
CORS(app, resources=r'/*')

resultformark = []


@app.route('/mesfilter/test', methods=['POST'])
def mesfilter_test():  # put application's code here
    print(request.args)
    username = request.args.get('username')
    password = request.args.get('password')
    return [username, password, "qwerqweqweqwe"]


@app.route('/mesfilter/mesSelectBytime', methods=['POST'])
def mesSelectBytime():  # put application's code here
    params = request.get_json()
    order = params["param"]["order"]
    print(order)
    # print(request.get_data())
    cotent = []
    if order == "1":
        for i in range(0, 100):
            data = {
                "source": "192.168.1." + str(random.randint(1, 200)),
                "target": "192.168.1." + str(random.randint(1, 200)),
                "weight": random.randint(1, 12),
            }
            cotent.append(data)
    elif order == "2":
        for i in range(0, 100):
            data = {
                "source": "192.168.1." + str(random.randint(1, 200)) + '-' + "192.168.1." + str(random.randint(1, 200)),
                "target": "192.168.1." + str(random.randint(1, 200)) + '-' + "192.168.1." + str(random.randint(1, 200)),
                "weight": random.randint(1, 12),
            }
            cotent.append(data)
    elif order == "3":
        for i in range(0, 100):
            data = {
                "source": "192.168.1." + str(random.randint(1, 200)) + '-' + "192.168.1." + str(
                    random.randint(1, 200)) + '-' + "192.168.1." + str(random.randint(1, 200)),
                "target": "192.168.1." + str(random.randint(1, 200)) + '-' + "192.168.1." + str(
                    random.randint(1, 200)) + '-' + "192.168.1." + str(random.randint(1, 200)),
                "weight": random.randint(1, 12),
            }
            cotent.append(data)
    elif order == "4":
        for i in range(0, 100):
            data = {
                "source": "192.168.1." + str(random.randint(1, 200)) + '-' + "192.168.1." + str(
                    random.randint(1, 200)) + '-' + "192.168.1." + str(
                    random.randint(1, 200)) + '-' + "192.168.1." + str(random.randint(1, 200)),
                "target": "192.168.1." + str(random.randint(1, 200)) + '-' + "192.168.1." + str(
                    random.randint(1, 200)) + '-' + "192.168.1." + str(
                    random.randint(1, 200)) + '-' + "192.168.1." + str(random.randint(1, 200)),
                "weight": random.randint(1, 12),
            }
            cotent.append(data)
    return cotent


def default(self, obj):
    if isinstance(obj, (numpy.int_, numpy.intc, numpy.intp, numpy.int8,
                        numpy.int16, numpy.int32, numpy.int64, numpy.uint8,
                        numpy.uint16, numpy.uint32, numpy.uint64)):
        return int(obj)
    elif isinstance(obj, (numpy.float_, numpy.float16, numpy.float32,
                          numpy.float64)):
        return float(obj)
    elif isinstance(obj, (numpy.ndarray,)):  # add this line
        return obj.tolist()  # add this line
    return json.JSONEncoder.default(self, obj)


@app.route('/mesfilter/mesDraw', methods=['POST'])
def mesDraw():
    params = request.get_json()
    node = params["node"]
    link = params["link"]
    lay = ['layerID layerLabel', '1 advice']
    g1 = mn.build_network2(lay, link, node)
    layout1 = mn.independent_layout(g1)
    res = []
    print(layout1)
    for key, value in layout1[0].items():
        data = {
            "x": value[0],
            'y': value[1]
        }
        res.append(data)
    print(res)
    return res


@app.route('/mesfilter/mesCross', methods=['POST'])
def mesCross():
    params = request.get_json()
    # print(params[1])
    length_mat = params[0]
    all_path, all_ex = sim.sa(3000, pow(10, -1), 0.1, 200, length_mat, params[1])
    print(sim.search(all_path, length_mat), round(sim.e(sim.search(all_path, length_mat), length_mat)))
    iteration = len(all_path)
    res = sim.search(all_path, length_mat)
    # print(sim.e2(res,length_mat))
    all_path = np.array(all_path)
    all_ex = np.array(all_ex)
    # plt.xlabel("Iteration")
    # plt.ylabel("cross")
    # plt.plot(range(iteration), all_ex)
    # plt.show()

    return res


@app.route('/mesfilter/markov', methods=['POST'])
def mesMarkov():
    print("kaishi")
    data_dict = request.get_json()
    data = data_dict['data']
    parameter = data_dict['parameter']
    metrix = path.Tn_paths(data, parameter['k'], parameter['delta'])

    return metrix


@app.route('/mesfilter/selectGra', methods=['POST'])
def selectGra():
    data_dict = request.get_json()
    # test.find_connected_data(data_dict['data'],data_dict['name'])
    result = test.find_connected_data(data_dict['data'], data_dict['name'])
    # print(data_dict)
    # print(list(set(result)))

    return list(set(result))


@app.route('/mesfilter/senddata', methods=['POST'])
def senddata():
    import json
    data_dict = request.get_json()
    name = data_dict['name']
    # 打开 JSON 文件
    with open('E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//' + name) as f:
        data = json.load(f)

    # 打印读取的数据,可以看到读取的JSON数据被转换为Python字典对象
    # print(data)

    return data


@app.route('/mesfilter/readdata', methods=['POST'])
def readdata():
    data = []
    data_dict = request.get_json()
    name = data_dict['name']
    # 打开 JSON 文件
    with open('E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//' + name) as f:
        data = json.load(f)

    # 打印读取的数据,可以看到读取的JSON数据被转换为Python字典对象
    # print(data)

    return data


@app.route('/mesfilter/uploadfile', methods=['POST'])
def upload():
    # print(111)
    data_dict = request.get_data()
    file = request.files['file']
    name = file.filename
    file.save('E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//' + name)
    # with open('E://vueworkspace//vue-manage-system-master//vue-manage-system-master//public//tablemestest.json', 'w',
    #           encoding='utf8') as f2:
    #     # ensure_ascii=False才能输入中文，否则是Unicode字符
    #     # indent=2 JSON数据的缩进，美观
    #     json.dump(file, f2, ensure_ascii=False, indent=2)

    # print(file)
    return name


# @app.route('/mesfilter/path_generation', methods=['POST'])
# def path_generation():
#     from path import Tn_paths
#     data_dict = request.get_json()
#     data = data_dict['data']
#     parameter = data_dict['parameter']
#     metrix =Tn_paths(data,parameter['k'],parameter['delta'])
#     return '123123'

@app.route('/mesfilter/uploadForCsv', methods=['POST'])
def uploadForCsv():
    data_dict = request.get_data()
    file = request.files['file']
    name = file.filename
    file.save("../data/" + name)
    return name


@app.route('/mesfilter/readForCsv', methods=['POST'])
def readForCsv():
    data = request.get_json()
    name = data['name']
    data_res = []
    index = 1
    with open("../data/" + name, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # 读取第一行作为表头
        for row in csv_reader:
            data_res.append({
                'id': index,
                'source': row[0],
                'target': row[1],
                'time': row[2],
            })
            index = index + 1
    return data_res


@app.route('/mesfilter/searchData', methods=['POST'])
def searchData():
    data = request.get_json()
    # print(data)
    data_ip = searchFromIPS(data['data'], data['form']['user'])
    data_time = searchFromTime(data_ip, data['form']['timestart'], data['form']['timeend'])
    data_hop = searchHopOnce(data['data'], data_time, data['form']['hop'], data['form']['timestart'],
                             data['form']['timeend'])
    return data_hop


# 检索Ip段，多个ip
def searchFromIPS(data, user):
    Ips = user.split(";")
    res = []
    for data_mes in data:
        for ip in Ips:
            parts = ip.split(".")
            ip_result = ".".join(parts[:3])+'.'
            if ip_result in data_mes['source']['name'] or ip_result in data_mes['target']['name']:
                res.append(data_mes)
    return res


# 检索时间
def searchFromTime(data, timestart, timeend):
    res = []
    for data_time in data:
        if timestart <= data_time['timesecond'] <= timeend:
            res.append(data_time)
    return res


# 检索一条信息的前后n跳数
def searchHopOnce(data, mes_hop, n, start, end):
    res = []
    mes = mes_hop
    n = int(n)
    while n > 0:
        temp = []
        for index in mes:
            if isinstance(index, int):
                mes_index = data[index - 1]
            else:
                mes_index = index
                res.append(index['id'])
            for data_index in data:
                if start <= data_index['timesecond'] <= end:
                    if data_index['timesecond'] < mes_index['timesecond'] and mes_index['source'] == data_index['target']:
                        res.append(data_index['id'])
                        temp.append(data_index['id'])
                    if data_index['timesecond'] > mes_index['timesecond'] and mes_index['target'] == data_index['source']:
                        res.append(data_index['id'])
                        temp.append(data_index['id'])
        mes = list(set(temp))
        n -= 1
    res_final = []
    for index in list(set(res)):
        res_final.append(data[index - 1])
    return res_final

@app.route('/mesBE/check_ip', methods=['POST'])
def check_ip():
    data_json = request.get_json()
    data = data_json["data"]
    form = data_json["form"]
    ips = form['user'].split(";")
    hop = int(form['hop'])
    start_time = form["timestart"]
    end_time = form["timeend"]
    df = pd.DataFrame(data, index=None)
    df = df[(df.timesecond >= start_time) & (df.timesecond <= end_time)]
    new_df = pd.DataFrame()
    print(df)
    for ip_ in ips:
        up, down = [ip_], [ip_]
        for i in range(1, hop + 1):
            if len(up) != 0:
                for ip in up:
                    if i == 1:
                        df_1 = df[df.target == ip]
                        if len(df_1) != 0:
                            up = df_1.loc[:, ['source', 'timesecond']].values
                            new_df = pd.concat([new_df, df_1], axis=0)
                        else:
                            up = []
                    else:
                        df_1 = df[(df.target == ip[0]) & (df.timesecond < ip[1])]
                        if len(df_1) != 0:
                            up = df_1.loc[:, ['source', 'timesecond']].values
                            new_df = pd.concat([new_df, df_1], axis=0)
                        else:
                            up = []
            if len(down) != 0:
                for ip in down:
                    if i == 1:
                        df_2 = df[df.source == ip]
                        if len(df_2) != 0:
                            down = df_2.loc[:, ['source', 'timesecond']].values
                            new_df = pd.concat([new_df, df_2], axis=0)
                        else:
                            down = []
                    else:
                        df_2 = df[(df.target == ip[0]) & (df.timesecond < ip[1])]
                        if len(df_2) != 0:
                            up = df_1.loc[:, ['source', 'timesecond']].values
                            new_df = pd.concat([new_df, df_2], axis=0)
                        else:
                            down = []
            # for ip in up:
            #     df_1 = df[df.target == ip]
            #     up = df_1.source.tolist()
            #     print(up)
            #     new_df = pd.concat([new_df, df_1], axis=0)
            # for ip in down:
            #     df_2 = df[df.source == ip]
            #     down = df_2.target.tolist()
            #     new_df = pd.concat([new_df, df_2], axis=0)
    new_df = new_df.drop_duplicates(keep='first')
    dd = new_df.sort_values('id').to_dict("records")
    print(dd)
    return dd


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5001')
