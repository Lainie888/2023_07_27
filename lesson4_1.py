
score = int(input("請輸入學生分數(最高分300分):"))
is_add = input("學生是否符合加分條件?(y,n)")

if (is_add == "y"):
    score *= 1.05
    if score > 300:
     score = 300


print(f"學生分數是{round(score)}") #round 可四捨五入
