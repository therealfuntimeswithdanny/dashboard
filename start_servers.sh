#!/bin/zsh
# Start Flask backend on port 5050
source /Users/danny/Desktop/simpleserver/.venv/bin/activate
nohup /Users/danny/Desktop/simpleserver/.venv/bin/python /Users/danny/Desktop/simpleserver/app.py > flask.log 2>&1 &
FLASK_PID=$!
echo "Flask backend started on port 5050 (PID: $FLASK_PID)"

# Start static server on port 8000
nohup python3 /Users/danny/Desktop/simpleserver/server.py > static.log 2>&1 &
STATIC_PID=$!
echo "Static server started on port 8000 (PID: $STATIC_PID)"

echo "To stop servers: kill $FLASK_PID $STATIC_PID"
