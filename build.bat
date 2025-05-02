@echo off
py -3.8 -m PyInstaller --noconfirm --onedir --windowed --icon "./icon.ico" --name "Answers Time Editor" --add-data "./src;src/"  "./main.py"
xcopy "./content" "./Answers Time Editor/content" /E /I /Y
xcopy "./dist/Answers Time Editor" "./Answers Time Editor" /E /I /Y
rd "./dist" /s /Q
rd "./build" /s /Q
del "./Answers Time Editor.spec" /Q