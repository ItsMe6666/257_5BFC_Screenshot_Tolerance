使用到的OCR庫:pytesseract

pip install pytesseract

先辨識出圖片中的學號，在將依序由小到大、由左至右、由上而下拼成九宮格或四宮格。

1.使用方法:將截圖放在images資料夾後點選[截圖公差腳本.exe]後生成圖片，生成位置在目錄下。

2.編譯指令pyinstaller main.py --onefile -i icon.png

3.已知BUG:未知
