# 檢查檔案是否存在與讀取檔案
import os 

products = []
if os.path.isfile('products.csv'):
    print('找到檔案了！')
    with open('products.csv','r',encoding= 'utf-8') as f :
        for line in f :
            if '商品,價格' in line :
                continue
            name , price = line.strip().split(',')
            products.append([name,price])
else :
    print('找不到檔案......')


# 讓使用者輸入
while True :
    name = input('請輸入商品名稱：')
    if name == 'q' :
        break
    price = input('請輸入商品價格：')
    products.append([name,price])

# 印出購買紀錄
for p in products :
    print(p[0],'的價格為',p[1],'元')

# 寫入檔案
with open('products.csv','w',encoding= 'utf-8') as f :
    f.write('商品,價格\n')
    for p in products :
        f.write(p[0] + ',' + p[1] + '\n' ) 