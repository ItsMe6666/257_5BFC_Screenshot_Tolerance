
使用到的OCR庫:pytesseract

pip install pytesseract

先辨識出圖片中的學號，在將依序由小到大、由左至右、由上而下拼成九宮格或四宮格。

1.使用方法:將截圖放在images資料夾後點選[Screenshot_Tolerance_V1.exe]後生成圖片，生成位置在目錄下。

![image](https://github.com/ItsMe6666/257_5BFC_Screenshot_Tolerance/blob/main/stepimg/Step%20(1).png)

![image](https://github.com/ItsMe6666/257_5BFC_Screenshot_Tolerance/blob/main/stepimg/Step%20(2).PNG)

![image](https://github.com/ItsMe6666/257_5BFC_Screenshot_Tolerance/blob/main/stepimg/Step%20(3).PNG)

程式流程圖

![image](https://github.com/ItsMe6666/257_5BFC_Screenshot_Tolerance/blob/publish/stepimg/%E6%B5%81%E7%A8%8B%E5%9C%96.png)

2.編譯指令pyinstaller Screenshot_Tolerance.py --onefile -i ./icon/icon.png

3.已知BUG:未知


