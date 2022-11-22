rm pbrain
rm pbrain.spec
pyinstaller .\pbrain-gomoku-ai.py --onefile -n pbrain
mv ./dist/pbrain.exe ./