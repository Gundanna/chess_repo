from flask import Flask, request, jsonify
from flask_cors import CORS
from stockfish import Stockfish
import os, shutil, glob

app = Flask(__name__)
CORS(app)

def find_stockfish():
    # All places to check
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "stockfish_bin"),
        "/opt/render/project/src/stockfish_bin",
        shutil.which("stockfish"),
        "/usr/bin/stockfish",
        "/usr/games/stockfish",
    ]
    # Also search the whole project dir for any stockfish binary
    project_dir = os.environ.get("RENDER_PROJECT_DIR", "/opt/render/project/src")
    candidates += glob.glob(f"{project_dir}/**/stockfish*", recursive=True)

    for path in candidates:
        if path and os.path.isfile(path) and os.access(path, os.X_OK):
            print(f"Found Stockfish at: {path}")
            return path

    # Print everything in project dir to help debug
    print("=== Could not find Stockfish. Listing project files: ===")
    for root, dirs, files in os.walk(project_dir):
        for f in files:
            print(os.path.join(root, f))
    raise RuntimeError("Stockfish binary not found anywhere!")

engine = Stockfish(path=find_stockfish(), parameters={"Skill Level": 10})

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
