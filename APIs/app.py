from flask import Flask, request, jsonify
from secrets import token_hex
from utils import yaml_function

app = Flask(__name__)

@app.route("/api/v1/devices/", methods=["GET", "POST"])
def get_devices():
    if request.method == "GET":
        devices = yaml_function("./data/devices.yml", "read")
        return jsonify({"data": devices}), 200
    elif request.method == "POST":
        if len(request.json) != 6:
            return jsonify({"error": "The number of params you specific is invalid!"}), 400
        data = yaml_function("./data/devices.yml", "read")
        for entry in data:
            if entry.get("name").lower() == request.json.get("name").lower():
                return jsonify({"data": "Device already exists!"}), 200
        new_data = request.json
        data.append(new_data)
        yaml_function("./data/devices.yml", "write", data=data)
        return jsonify({"data": request.json}), 201

@app.route("/api/v1/devices/<string:device>/")
def get_device(device: str):
    devices = yaml_function("./data/devices.yml", "read")
    for a_device in devices:
        if a_device.get("name") == device:
            return jsonify({"data": a_device}), 200
    return jsonify({"error": f"Device {device} not found!"}), 404

@app.route("/api/v1/config/compliance/", methods=["GET", "POST"])
def get_policies():
    schema = {
        "name": "Telnet Disable Cisco",
        "description": "Disables telnet on Cisco devices",
        "platform": "cisco_ios",
        "device_types": ["router", "switch"],
        "config": "no transport input telnet",
        "parent": "line vty 0 4"
    }
    if request.method == "GET":
        policies = yaml_function("./data/policies.yml", "read")
        return jsonify({"data": policies}), 200

    elif request.method == "POST":
        if len(request.json) != 6:
            return jsonify({"error": f"The number of parameters you specified is invalid! Valid fields example: {schema}"}), 400
        data = yaml_function("./data/policies.yml", "read")
        for entry in data:
            if entry.get("name").lower() == request.json.get("name").lower() and entry.get("platform").lower() == request.json.get("platform").lower():
                return jsonify({"error": "Configuration policy already exists"}), 200
        new_data = request.json
        new_data["id"] = token_hex(16)
        data.append(new_data)
        yaml_function("./data/policies.yml", "write", data=data)
        return jsonify({"data": request.json}), 201

@app.route("/api/v1/config/compliance/<string:id>/", methods=["DELETE"])
def delete_policy(id: str):
    policies = yaml_function("./data/policies.yml", "read")
    for policy in policies:
        if policy.get("id") == id:
            policies.remove(policy)
            yaml_function("./data/policies.yml", "write", data=policies)
            return jsonify({}), 204
    return jsonify({"error": f"Config policy {id} not found!"}), 404
