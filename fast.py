"""
力引导图布局
"""
import json
import random
import math
from matplotlib import pyplot as plt
import networkx as nx
import time
import numpy as np

# 模型参数
K_r = 6
K_s = 0.3
L = 5
delta_t = 50
MaxLength = 30
iterations = 200
color = ['red', 'green', 'blue', 'orange']
Node_num = 200
original_max_posx = 40
original_max_posy = 40
# 图形容器
Edge = []
Node_force = {}
Node_position = {}
# 节点大小用来反映节点的度
Node_degree = []

# 与采样退火有关的参数
Displacement_list = []  # 用于采样的列表
scale = 3  # 采样的范围；


def init():
    for i in range(0, Node_num):  # 随机生成点坐标,初始化力
        posx = random.uniform(0, original_max_posx)
        posy = random.uniform(0, original_max_posy)  # 初始化点坐标和受力
        Node_position[i] = (posx, posy)
        Node_force[i] = (0, 0)
    for i in range(0, int(Node_num / 2) - 1):  # 随机生成边
        index = random.randint(0, i)
        Edge.append((i, index))
        index = random.randint(0, i)
        Edge.append((i, index))
    for i in range(int(Node_num / 2), Node_num):  # 随机生成边
        index = random.randint(int(Node_num / 2), Node_num - 1)
        Edge.append((i, index))


def compute_repulsion():  # 计算每两个点之间的斥力
    for i in range(0, Node_num):
        for j in range(i + 1, Node_num):
            dx = Node_position[j][0] - Node_position[i][0]
            dy = Node_position[j][1] - Node_position[i][1]
            if dx != 0 or dy != 0:
                distanceSquared = dx * dx + dy * dy
                distance = math.sqrt(distanceSquared)
                R_force = K_r / distanceSquared
                fx = R_force * dx / distance
                fy = R_force * dy / distance  # 更新受力
                fi_x = Node_force[i][0]
                fi_y = Node_force[i][1]
                Node_force[i] = (fi_x - fx, fi_y - fy)
                fj_x = Node_force[j][0]
                fj_y = Node_force[j][1]
                Node_force[j] = (fj_x + fx, fj_y + fy)


def compute_string():
    for i in range(0, Node_num):  # 取出其邻居
        neighbors = [n for n in G[i]]  # 对每一个邻居，计算斥力；j
        for j in neighbors:
            if i < j:
                dx = Node_position[j][0] - Node_position[i][0]
                dy = Node_position[j][1] - Node_position[i][1]
                if dx != 0 or dy != 0:
                    distance = math.sqrt(dx * dx + dy * dy)
                    S_force = K_s * (distance - L)
                    fx = S_force * dx / distance
                    fy = S_force * dy / distance  # 更新受力
                    fi_x = Node_force[i][0]
                    fi_y = Node_force[i][1]
                    Node_force[i] = (fi_x + fx, fi_y + fy)
                    fj_x = Node_force[j][0]
                    fj_y = Node_force[j][1]
                    Node_force[j] = (fj_x - fx, fj_y - fy)


def update_position(times):  # 更新坐标
    Displacement_sum = 0
    for i in range(0, Node_num):
        dx = delta_t * Node_force[i][0]
        dy = delta_t * Node_force[i][1]
        displacementSquard = dx * dx + dy * dy
        # 随迭代次数增加，MaxLength逐渐减小；

        current_MaxLength = MaxLength / (times + 0.1)

        if (displacementSquard > current_MaxLength):
            s = math.sqrt(current_MaxLength / displacementSquard)
            dx = dx * s
            dy = dy * s
        (newx, newy) = (Node_position[i][0] + dx, Node_position[i][1] + dy)
        Displacement_sum += math.sqrt(dx * dx + dy * dy)
        Node_position[i] = (newx, newy)
    return Displacement_sum


if __name__ == '__main__':

    # print(content)
    G = nx.Graph()
    G.add_nodes_from(list(range(0, Node_num)))
    # init()  # 初始化节点得坐标和图中的边
    # G.add_edges_from(Edge)

    # 获得节点的度
    for i in range(0, Node_num):
        Node_degree.append(pow(G.degree(i), 2))
    # 获得联通子图
    connected_num = 0
    connected_subgraph = []
    for c in nx.connected_components(G):
        connected_num += 1
        nodeSet = G.subgraph(c)
        connected_subgraph.append(nodeSet)

    # 原图
    nx.draw_networkx_nodes(G, pos=Node_position, node_size=20, node_color='red', alpha=0.8)
    nx.draw_networkx_edges(G, pos=Node_position, edge_color='lightblue', width=0.5)
    plt.show()

    fig = plt.figure('不同迭代次数force-direction_layout')
    start = time.perf_counter()
    iteration_time = 0
    for times in range(0, 1 + iterations):
        for i in range(0, Node_num):
            Node_force[i] = (0, 0)
        compute_repulsion()
        compute_string()
        # 记录本次迭代移动距离：
        Displacement_sum = update_position(times)
        Displacement_list.append(Displacement_sum)
        # print(Displacement_sum)
        if len(Displacement_list) > scale:
            last = np.mean(Displacement_list[times - 4:times - 1])
            now = np.mean(Displacement_list[times - 3:times])
            if (last - now) / last < 0.01:
                break
        iteration_time = times
    end = time.perf_counter()

    print('Running time: %s Seconds' % (end - start))
    print('最终迭代次数:', iteration_time)
    index = 0
    for subgrap in connected_subgraph:
        sub_position = dict({i for i in Node_position.items() if i[0] in list(subgrap)})
        sub_degree = [degree + 5 for (point, degree) in enumerate(Node_degree) if point in list(subgrap)]
        print(sub_position)
        nx.draw_networkx_nodes(subgrap, pos=sub_position, node_size=sub_degree, node_color=color[index % 4], alpha=0.8)
        nx.draw_networkx_edges(subgrap, pos=sub_position, edge_color='lightblue', width=0.5)
        index += 1
    # 受力得初始化：
    plt.show()
