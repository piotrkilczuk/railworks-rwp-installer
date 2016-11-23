mkdir build

REM Make the icon
convert media\icon256.png media\icon128.png media\icon64.png media\icon32.png build\icon.ico

REM Build EXE
.\venv\Scripts\pyinstaller.exe rwp.py --onefile --console --name rwpinstaller --icon build\icon.ico

REM Sign digitally
signtool sign /a dist/rwpinstaller.exe
