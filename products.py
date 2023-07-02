import os #operating system

def read_file(filename) :
    products = []
    with open (filename,'r',encoding = 'utf-8') as f :
        for line in f :
            if '商品,價格' in line :
                continue #繼續，沒有逃出迴圈，而是此循環接下來的動作不執行，進行下一循環，類似只有某一循環break
            name, price = line.strip().split(',')
            products.append([name,price])
        print(products)
    return products

#讓使用者輸入
def users_input(products) :
    while True :
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        products.append([name,price])

    return products

#印出所有購買紀錄
def print_products(products) :
    for p in products :
        print(p[0],'的價格為',p[1],'元')

#寫入檔案
def write_file(filename,products) :
    with open (filename,'w',encoding ='utf-8') as f :
        f.write('商品,價格\n')
        for p in products :
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename) :
        products = read_file(filename)
        print('找到檔案了！')
    else :
        print('找不到檔案...QQ')
    products = users_input(products)
    print_products(products)
    write_file('products.csv',products)

main()