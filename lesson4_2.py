
# 90(含)~100分為「優」
# 80(含)~89分為「甲」
# 70(含)~79分為「乙」
# 60(含)~69分為「丙」
# 0(含)~59分為「丁」

#if條件判斷式 有()跟沒括號沒差，但沒括號時要空一格

# score = int(input("請輸入學生分數:"))

# #多項選擇

# if score >= 90:
#     grade = "優"
# elif score >= 80:
#     grade = "甲"
# elif score >= 70:
#     grade = "乙"
# elif score >= 60:
#     grade = "丙"
# else:
#     grade = "丁"

# print(f"學生等級:{grade}")

# money = int(input("請輸入購買金額:"))
# payMoney = 0
# if(money >= 100000):
#     payMoney = money * 0.8
# elif(money >= 50000):
#     payMoney = money * 0.85
# elif(money >= 30000):
#     payMoney = money * 0.9
# elif(money <= 10000):
#     payMoney = money * 0.95
# else:
#     payMoney = money 
# print(f"實付金額:{int(payMoney)}") #int 是轉成整數

money = int(input("請輸入購買金額:"))
payMoney = 0
if(money < 10000):
    payMoney = money 
elif(money < 30000):
    payMoney = money * 0.95
elif(money < 50000):
    payMoney = money * 0.9
elif(money < 100000):
    payMoney = money * 0.85
else:
    payMoney = money * 0.8
     
print(f"實付金額:{int(payMoney)}") 