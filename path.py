import pathpy as pp
import pandas as pd
import json
import numpy as np


def Tn_paths(data, k, delta=np.inf):
    tn = pp.TemporalNetwork()
    for d in data:
        tn.addEdge(d.get('source').get('name'), d.get('target').get('name'), ts=d.get('time'))
    trp = pp.Paths.fromTemporalNetwork(tn, delta=delta)
    h_network = pp.HigherOrderNetwork(trp, k)
    g = []
    nums = []
    for e in h_network.edges:
        one_ed = [e[0], e[1]]
        g.append(one_ed)
        nums.append(h_network.edges[e].sum())
    new_data = json.dumps(tp(g,nums))

    return new_data


def tp(data, nums):
    nodes = []
    juzheng = []
    for i in data:
        if i[0] not in nodes:
            nodes.append(i[0])
        if i[1] not in nodes:
            nodes.append(i[1])
    all_s=[]

    for n in nodes:
        num = 0
        for m in nodes:
            if [n,m] in data:
                index = data.index([n,m])
                num+=nums[index]
        all_s.append(num)
    for key,n in enumerate(nodes):
        sss = []
        for m in nodes:
            if [n,m] in data:
                pro = nums[data.index([n,m])]/all_s[key]
                sss.append(pro)
            else:
                sss.append(0)
        juzheng.append(sss)

    df = pd.DataFrame(juzheng,index=nodes,columns=nodes)
    new_data = []
    for mm in data:
        source = mm[0]
        target = mm[1]
        one_data = {
            'source':source,
            'target':target,
            'weight':df.loc[source,target]
        }
        new_data.append(one_data)

    return new_data
