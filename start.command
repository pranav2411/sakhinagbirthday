#!/bin/bash
cd "$(dirname "$0")"
echo "=================================================="
echo "      💖 LAUNCHING BIRTHDAY SITE FOR SAKHI 💖     "
echo "=================================================="
echo "Opening website in your browser..."
# Wait 1 second and open the browser
(sleep 1 && open http://localhost:8000) &
# Start the Python HTTP server
python3 serve.py
