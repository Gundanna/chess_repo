from flask import Flask, request, jsonify
from flask_cors import CORS
from stockfish import Stockfish
import shutil

app = Flask(__name__)
CORS(app)

# Find stockfish binary wherever it's installed
stockfish_path = shutil.which("stockfish") or "/usr/games/stockfish"
engine = Stockfish(path=stockfish_path)

@app.route("/bestmove", methods=["POST"])
def bestmove():
    data = request.json
    fen = data["fen"]

    engine.set_fen_position(fen)
    move = engine.get_best_move()

    return jsonify({"move": move})

if __name__ == "__main__":
    app.run()
