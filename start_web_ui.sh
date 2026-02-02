#!/bin/bash

echo "🚀 Starting AWS Knowledge Query Web UI..."
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run: python3 -m venv venv"
    exit 1
fi

# Check if dependencies are installed
if ! venv/bin/python -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    venv/bin/pip install flask mcp httpx -q
fi

echo "✅ Dependencies ready"
echo ""
echo "🌐 Starting web server..."
echo "📱 Open your browser to: http://localhost:8080"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Start the web UI
venv/bin/python web_ui.py
