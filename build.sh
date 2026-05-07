#!/bin/bash
set -e

echo "=== Working directory: $(pwd)"
echo "=== Installing Python deps..."
pip install -r requirements.txt

echo "=== Downloading Stockfish..."
wget -q https://github.com/official-stockfish/Stockfish/releases/download/sf_16/stockfish-ubuntu-x86-64.tar
tar -xf stockfish-ubuntu-x86-64.tar

echo "=== Listing extracted files..."
find . -name "stockfish*" -type f

echo "=== Moving binary..."
# Find and move whatever binary was extracted
BINARY=$(find . -name "stockfish*" -type f ! -name "*.tar" | head -1)
echo "Found binary at: $BINARY"
cp "$BINARY" ./stockfish_bin
chmod +x ./stockfish_bin

echo "=== Verifying..."
ls -la ./stockfish_bin
./stockfish_bin --version || echo "version check done"

echo "=== Build complete. Binary at: $(pwd)/stockfish_bin"
