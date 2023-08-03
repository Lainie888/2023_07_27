
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

# score = int(input("請輸入學生分數(0~100):"))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")
