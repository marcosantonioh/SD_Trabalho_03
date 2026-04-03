from flask import Flask, request, jsonify
from datetime import datetime
from database import create_table, insert_reading, check_uuid

app = Flask(__name__)

create_table()

def process_temperature(temp):

    if temp > 15:
        return "Crítico"
    elif temp > 10:
        return "Alerta"
    else:
        return "Normal"


@app.route('/sensor', methods=['POST'])
def receive_data():

    data = request.json

    uuid = data.get("uuid")
    sensor_id = data.get("sensor_id")
    temperatura = data.get("temperatura")

    if check_uuid(uuid):
        return jsonify({
            "status": "duplicado"
        })

    status_logico = process_temperature(temperatura)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    insert_reading(uuid, sensor_id, temperatura, status_logico, timestamp)

    return jsonify({
        "status": status_logico
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)