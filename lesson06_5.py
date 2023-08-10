import random

def play_game(): #自訂function
    min = 1
    max = 100
    target = random.randint(min,max) #宣告亂數的範圍是在1~10
    #random.randint(a, b)
    #回傳一個隨機整數 N，使得 a <= N <= b。為 randrange(a, b+1) 的別名。
    print(target)
    count = 0
    print("=============猜數字遊戲============\n\n")
    while True:
        keyin = int(input(f"猜數字的範圍{min}~{max}："))
        count += 1
        if keyin >= min and keyin <= max:
            if(keyin == target):
                print(f"bingo.猜對了，答案是:{keyin}")
                print(f"你總共猜了{count}次")
                break
            elif(keyin > target):
                    print("再小一點")
                    max = keyin - 1
            elif(keyin < target):
                print("再大一點")
                min = keyin + 1

            print(f"你總共猜了{count}次")
        else:
            print("超出範圍")

while True:
    play_game() #呼叫執行這個函式
    play_again = input("你還要繼續嗎?(y or n)")
    if play_again == "n":
        break
    else:
        continue

print("遊戲結束")