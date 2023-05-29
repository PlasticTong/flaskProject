from flask import Flask, request
import random
from flask_cors import CORS
import multinet as mn
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


@app.route('/mesfilter/mesDraw', methods=['POST'])
def mesDraw():
    params = request.get_json()
    node = params["node"]
    link = params["link"]
    g2 = mn.generate_simulation_network(1, 5, 1.1, 0)
    layout2 = mn.kamada_kawai_layout(g2)
    print(layout2)
    # print("node:", node)
    # print("link:", link)
    return layout2

@app.route('/mesfilter/mesCross', methods=['POST'])
def mesCross():
    params = request.get_json()
    node = params["node"]
    link = params["link"]
    g2 = mn.generate_simulation_network(1, 5, 1.1, 0)
    layout2 = mn.kamada_kawai_layout(g2)
    print(layout2)
    # print("node:", node)
    # print("link:", link)
    return layout2


if __name__ == '__main__':
    app.run()
