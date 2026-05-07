from flask import Flask, request, jsonify
from flask_cors import CORS
from stockfish import Stockfish
import shutil, os

app = Flask(__name__)
CORS(app)

stockfish_path = shutil.which("stockfish") or "/usr/bin/stockfish"
if not os.path.isfile(stockfish_path):
    raise RuntimeError("Stockfish binary not found!")

engine = Stockfish(path=stockfish_path, parameters={"Skill Level": 10})

@app.route("/bestmove", methods=["POST"])
def bestmove():
    data = request.json
    engine.set_fen_position(data["fen"])
    move = engine.get_best_move()
    return jsonify({"move": move})

if __name__ == "__main__":
    app.run()