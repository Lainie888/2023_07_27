# a=17
# if a > 18:
#     print("您的age:")
#     print("18")

# print("程式結束")

score = int(input("請輸入學生分數(最高分300分):"))
is_add = input("學生是否符合加分條件?(y,n)")

if (is_add == "y"):
    score *= 1.05

print(f"學生分數是{round(score)}")
