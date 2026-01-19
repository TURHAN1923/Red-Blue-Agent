from flask import Flask, request, jsonify
from redAgent import red_team_attack
from blue_agent import blue_team_defense

app = Flask(__name__)

@app.route("/")
def home():
    return "Red & Blue Agent Server aktif."

@app.route("/red", methods=["POST"])
def red_agent():
    data = request.json
    system_info = data.get("system_info")

    if not system_info:
        return jsonify({"error": "system_info gerekli"}), 400

    red_response = red_team_attack(system_info)
    return jsonify({"red_team_plan": red_response})

@app.route("/blue", methods=["POST"])
def blue_agent():
    data = request.json
    system_info = data.get("system_info")
    red_plan = data.get("red_team_plan")

    if not system_info or not red_plan:
        return jsonify({"error": "system_info ve red_team_plan gerekli"}), 400

    blue_response = blue_team_defense(system_info, red_plan)
    return jsonify({"blue_team_response": blue_response})

if __name__ == "__main__":
    app.run(debug=True)
