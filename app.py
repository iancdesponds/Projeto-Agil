from flask import Flask, request

sabores_list = ['pistache', 'vanila', 'chocolate', 'passas ao rum']


app = Flask("Minha Gelateria")

@app.route("/")
def hello_world():
    return '<p>Hello, World!</p>'

@app.route("/sabores", methods=["GET"])
def sabores():
    
    dict_resp = {'sabores': sabores_list}




    return dict_resp

@app.route("/sabor/<int:id>", methods=["GET"])
def sabor(id):
    if id < len(sabores_list):
        return f'O sabor {id} é {sabores_list[id]}'
    else:
        return f"Sabor {id} não existe", 400

@app.route("/adicionar_sabor", methods=["POST"])
def adicionar_sabor():

    request_data = request.json

    if 'sabor' not in request_data:
        return "Sabor não informado", 400
    else:
        sabor = request_data['sabor']
        if sabor in sabores_list:
            return f"Sabor {sabor} já existe", 400
        else:
            sabores_list.append(sabor)
    return f"Sabor {sabor} adicionado com sucesso!"

@app.route("/apagar_sabor", methods=["GET"])
def apagar_sabor():
    sabor=request.args.get('sabor')
    if sabor in sabores_list:
        sabores_list.remove(sabor)
        return f"Sabor {sabor} apagado com sucesso!"
    else:
        return f"Sabor {sabor} não existe", 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
