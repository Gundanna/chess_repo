#!/bin/bash
set -e

# Install Python deps
pip install -r requirements.txt

# Download Stockfish binary for Linux x86_64
wget -q https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64.tar
tar -xf stockfish-ubuntu-x86-64.tar
mv stockfish/stockfish-ubuntu-x86-64 stockfish_bin
chmod +x stockfish_bin
rm -rf stockfish stockfish-ubuntu-x86-64.tar

echo "Stockfish installed at: $(pwd)/stockfish_bin"