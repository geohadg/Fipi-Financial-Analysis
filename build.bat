cd\
cd C:\Users\%USERNAME%\Downloads\Fipi-Financial-Analysis
python.exe -m pip install --upgrade pip
pip install --upgrade Pillow
pip install pyinstaller
pip install customtkinter
pip install pandas
pip install matplotlib
pyinstaller --noconfirm --onedir --windowed "Fipi-Financial-Analysis.py" --icon=fipiicon.ico
move fileexplorericon.png dist\Fipi-Financial-Analysis
pause