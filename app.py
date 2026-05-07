from flask import Flask, request, jsonify
from flask_cors import CORS
from stockfish import Stockfish
import os

app = Flask(__name__)
CORS(app)

STOCKFISH_PATH = "/opt/render/project/src/stockfish_bin"

print(f"Looking for Stockfish at: {STOCKFISH_PATH}")
print(f"File exists: {os.path.isfile(STOCKFISH_PATH)}")
print(f"Is executable: {os.access(STOCKFISH_PATH, os.X_OK) if os.path.isfile(STOCKFISH_PATH) else False}")

engine = Stockfish(path=STOCKFISH_PATH, parameters={"Skill Level": 10})
print("Stockfish loaded OK!")

@app.route("/bestmove", methods=["POST"])
def bestmove():
    data = request.json
    skill = int(data.get("skill", 10))
    engine.set_skill_level(skill)
    engine.set_fen_position(data["fen"])
    move = engine.get_best_move()
    return jsonify({"move": move})

if __name__ == "__main__":
    app.run()
