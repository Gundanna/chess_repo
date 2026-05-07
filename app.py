from flask import Flask, request, jsonify
from flask_cors import CORS
from stockfish import Stockfish
import os

app = Flask(__name__)
CORS(app)

# Binary is downloaded by build.sh into the project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STOCKFISH_PATH = os.path.join(BASE_DIR, "stockfish_bin")

if not os.path.isfile(STOCKFISH_PATH):
    raise RuntimeError(f"Stockfish binary not found at {STOCKFISH_PATH}")

engine = Stockfish(path=STOCKFISH_PATH, parameters={"Skill Level": 10})

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