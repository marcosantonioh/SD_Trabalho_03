from flask import Flask, request, jsonify
from datetime import datetime
from database import criar_tabela, inserir_leitura, check_uuid

app = Flask(__name__)

criar_tabela()

def process_temperature(temp):

    if temp > 15:
        return "Crítico"
    elif temp > 10:
        return "Alerta"
    else:
        return "Normal"


@app.route('/sensor', methods=['POST'])
def receber_dados():

    dados = request.json

    uuid = dados.get("uuid")
    sensor_id = dados.get("sensor_id")
    temperatura = dados.get("temperatura")

    if check_uuid(uuid):
        return jsonify({
            "status": "duplicado"
        })

    status_logico = process_temperature(temperatura)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    inserir_leitura(uuid, sensor_id, temperatura, status_logico, timestamp)

    return jsonify({
        "status": status_logico
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)