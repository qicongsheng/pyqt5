pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple Nuitka PyQt5 PyQt5-tools qdarkstyle eric-ide pyinstaller  
python3.9

pyinstaller --noconsole main.py

nuitka --standalone --show-memory --show-progress --show-scons --nofollow-imports -follow-import-to=need --plugin-enable=pyqt5 --include-qt-plugins=all --include-qt-plugins=sensible,styles  --output-dir=out  main.py
