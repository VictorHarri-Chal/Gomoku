rm pbrain-gomuku-ai.exe
rm pbrain-gomoku-ai.spec
pyinstaller .\pbrain-gomoku-ai.py --onefile -n pbrain-gomoku-ai
mv ./dist/pbrain-gomoku-ai.exe ./