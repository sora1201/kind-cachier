import random

price = random.randrange(15000) # 一万五千円までのランダムな値段

#財布の中身
pocket_money = [random.randrange(10), # 0:一円玉
                random.randrange(10), # 1:五円玉
                random.randrange(10), # 2:十円玉
                random.randrange(10), # 3:五十円玉
                random.randrange(10), # 4:百円玉
                random.randrange(10), # 5:五百円玉
                random.randrange(10), # 6:千円札
                random.randrange(10), # 7:五千円札
                random.randrange(10)] # 8:一万円札

# 各金を何枚ずつ出すか入力する関数
def pay(money: str):
    num = 0
    if money == '一円玉':
        if pocket_money[0] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[0]) + '枚中: '))
            if num > pocket_money[0]:
                print('ありません')
                num = pay('一円玉')

    elif money == '五円玉':
        if pocket_money[1] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[1]) + '枚中: '))
            if num > pocket_money[1]:
                print('ありません')
                num = pay('五円玉')

    elif money == '十円玉':
        if pocket_money[2] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[2]) + '枚中: '))
            if num > pocket_money[2]:
                print('ありません')
                num = pay('十円玉')

    elif money == '五十円玉':
        if pocket_money[3] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[3]) + '枚中: '))
            if num > pocket_money[3]:
                print('ありません')
                num = pay('五十円玉')

    elif money == '百円玉':
        if pocket_money[4] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[4]) + '枚中: '))
            if num > pocket_money[4]:
                print('ありません')
                num = pay('百円玉')

    elif money == '五百円玉':
        if pocket_money[5] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[5]) + '枚中: '))
            if num > pocket_money[5]:
                print('ありません')
                num = pay('五百円玉')

    elif money == '千円札':
        if pocket_money[6] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[6]) + '枚中: '))
            if num > pocket_money[6]:
                print('ありません')
                num = pay('千円札')

    elif money == '五千円札':
        if pocket_money[7] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[7]) + '枚中: '))
            if num > pocket_money[7]:
                print('ありません')
                num = pay('五千円札')

    elif money == '一万円札':
        if pocket_money[8] == 0:
            num = 0
            print(money+'を何枚出しますか / 0枚中', 0)
        else:
            num = int(input(money+'を何枚出しますか / ' + str(pocket_money[8]) + '枚中: '))
            if num > pocket_money[8]:
                print('ありません')
                num = pay('一万円札')

    return num

while True:
    recieved_money = 0
    remain_money = price
    print('---支払い---')
    print('代金は', price, '円です．',
      '財布の中には 一円玉:', pocket_money[0], 
               '枚, 五円玉:', pocket_money[1], 
               '枚, 十円玉',    pocket_money[2], 
               '枚, 五十円玉',  pocket_money[3], 
               '枚, 百円玉',    pocket_money[4], 
               '枚, 五百円玉',  pocket_money[5], 
               '枚, 千円札',    pocket_money[6], 
               '枚, 五千円札',    pocket_money[7], 
               '枚, 一万円札',    pocket_money[8], '枚あります．', sep='')

    money1     =     1 * pay('一円玉')
    recieved_money += money1
    remain_money -= money1
    print('  残り', remain_money, '円', sep='')
    
    if remain_money >= 0:
        money5     =     5 * pay('五円玉')
        recieved_money += money5
        remain_money -= money5
        print('  残り', remain_money, '円', sep='')

    if remain_money >= 0:
        money10    =    10 * pay('十円玉')
        recieved_money += money10
        remain_money -= money10
        print('  残り', remain_money, '円', sep='')
            
    if remain_money >= 0:
        money50    =    50 * pay('五十円玉')
        recieved_money += money50
        remain_money -= money50
        print('  残り', remain_money, '円', sep='')

    if remain_money >= 0:
        money100   =   100 * pay('百円玉')
        recieved_money += money100
        remain_money -= money100
        print('  残り', remain_money, '円', sep='')

    if remain_money >= 0:
        money500   =   500 * pay('五百円玉')
        recieved_money += money500
        remain_money -= money500
        print('  残り', remain_money, '円', sep='')
    
    if remain_money >= 0:
        money1000  =  1000 * pay('千円札')
        recieved_money += money1000
        remain_money -= money1000
        print('  残り', remain_money, '円', sep='')
    
    if remain_money >= 0:
        money5000  =  5000 * pay('五千円札')
        recieved_money += money5000
        remain_money -= money5000
        print('  残り', remain_money, '円', sep='')

    if remain_money >= 0:
        money10000 = 10000 * pay('一万円札')
        recieved_money += money10000
        remain_money -= money10000
        print('  残り', remain_money, '円', sep='')

    if input('これで良いですか？ yes/no: ') == 'yes':
        break
    print('やり直します．\n-----------\n')

# お釣り（枚数）
change = price - recieved_money
change10000 = change//10000
change5000  = (change - 10000*change10000)//5000
change1000  = (change - 10000*change10000 - 5000*change5000)//1000
change500   = (change - 10000*change10000 - 5000*change5000 - 1000*change1000)//500
change100   = (change - 10000*change10000 - 5000*change5000 - 1000*change1000 - 500*change500)//100
change50    = (change - 10000*change10000 - 5000*change5000 - 1000*change1000 - 500*change500 - 100*change100)//50
change10    = (change - 10000*change10000 - 5000*change5000 - 1000*change1000 - 500*change500 - 100*change100 - 50*change50)//10
change5     = (change - 10000*change10000 - 5000*change5000 - 1000*change1000 - 500*change500 - 100*change100 - 50*change50 - 10*change10)//5
change1     = (change - 10000*change10000 - 5000*change5000 - 1000*change1000 - 500*change500 - 100*change100 - 50*change50 - 10*change10 - 5*change5)//1

print('\n---レシート---')
print('  　合計　: ', price, '円', sep='')
print('  お預かり: ', recieved_money, '円', sep='')
print('  お釣り　: ',  change,      '円', sep='')
print('\n---各お金の枚数---')
print('  一万円札:', change10000, '枚', sep='')
print('  五千円札:', change5000,  '枚', sep='')
print('  千円札  :',   change1000,  '枚', sep='')
print('  五百円玉:', change500,   '枚', sep='')
print('  百円玉  :',   change100,   '枚', sep='')
print('  五十円玉:', change50,    '枚', sep='')
print('  十円玉  :',   change10,    '枚', sep='')
print('  五円玉  :',   change5,     '枚', sep='')
print('  一円玉  :',   change1,     '枚', sep='')