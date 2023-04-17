import pytesseract,os,re,time
from PIL import Image

directory = "./images/"  # 將路徑替換成目標目錄的路徑
image_list = []

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".PNG") or filename.endswith(".JPG") or filename.endswith(".bmp") or filename.endswith(".BMP"):
        image_list.append(filename)
numberlist = []
for filename in image_list:
    print("辨識學號中...")
    # 打開圖片
    img = Image.open(directory+filename)

    threshold = 140
    img = img.point(lambda p: p > threshold and 255)
    
    #img.show()
    # 辨識圖片中的文本(英文和數字)
    text = pytesseract.image_to_string(img)
    #print(text)
    
    #只保留數字
    numbers = re.findall(r'\d+', text)
    #print(numbers)
    
    # 找出最前面的三碼數字
    first_three_numbers = ""
    for number in numbers:
        if len(number) == 3:
            if len(numberlist) == 0:
                first_three_numbers = number[:3]
                numberlist.append(int(first_three_numbers))
                break
            else :
                avg = sum(numberlist) / len(numberlist)
                if avg - 10 <= int(number[:3]) <= avg + 10:#濾掉奇怪的數字
                    first_three_numbers = int(number[:3])
                    numberlist.append(first_three_numbers)
                    break
    print("照片學號為:" + number)        
    # 將文件名改為對應數字
    new_file_name = str(int(first_three_numbers)) + '.png'
    os.rename(directory+filename, directory+new_file_name)
numberlist.sort()
print(numberlist)
# 設定目錄路徑及合成圖片大小
print("圖片合成中...")
img_size = (600, 900)

# 讀取目錄下所有圖片
img_list = []
for fileN in numberlist:
        img = Image.open(os.path.join(directory, str(fileN)+".png"))
        img = img.resize(img_size)
        img_list.append(img)
print(img_list)

while len(img_list) > 0:
    # 判斷要使用的宮格數
    if len(img_list) > 4:
        grid_size = (3, 3)
    else:
        grid_size = (2, 2)

    # 計算每張圖片應該放在哪個位置
    positions = [(i % grid_size[0], i // grid_size[1]) for i in range(len(img_list))]

    # 計算合成圖片的大小
    composite_size = (grid_size[0] * img_size[0], grid_size[1] * img_size[1])

    # 建立一張新的合成圖片
    composite_img = Image.new('RGB', composite_size)

    # 將所有圖片合成到新的合成圖片中
    for img, pos in zip(img_list, positions):
        x = pos[0] * img_size[0]
        y = pos[1] * img_size[1]
        composite_img.paste(img, (x, y))

    # 儲存合成圖片
    composite_img.save('composite_img'+str(len(img_list))+'.png')
    if len(img_list) >= 9:
        del img_list[0:9]
    else:
        del img_list[:]
print("圖片合成完畢!")
n = 30
while n > 0: 
    time.sleep(1)
    n = n - 1
    print("倒數"+str(n)+"s關閉程式")

