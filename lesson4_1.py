try: #有可能raise 的程式碼出錯
    score = int(input("請輸入學生分數(最高分300分):"))
    if score <=300:
        is_add = input("學生是否符合加分條件?(y,n)")

        if (is_add == "y"):
            score *= 1.05
            if score > 300:
                score = 300

        print(f"學生分數是{round(score)}") #round 可四捨五入

    else:
        print("學生分數不可大於300分")
except: #出錯後的程式碼執行
    print("格式錯誤")




# score = int(input("請輸入學生分數(0~100):"))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")



#專門在檢查輸入格式錯誤
# try:
#     money=int(input("請輸入金額:"))
#     print(money)
# except:
#     print("輸入金額錯誤")