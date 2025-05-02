@echo off
py -3.8 -m PyInstaller --noconfirm --onefile --windowed --icon "./icon.ico" --name "Answers Time" --add-data "./src;src/" --add-data "./content;content/"  "./main.py"
md "./Answers Time Composed"
copy "./dist" "./Answers Time Composed"
rd "./dist" /s /Q
rd "./build" /s /Q
del "./Answers Time.spec" /Q