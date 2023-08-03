
# 90(含)~100分為「優」
# 80(含)~89分為「甲」
# 70(含)~79分為「乙」
# 60(含)~69分為「丙」
# 0(含)~59分為「丁」

#if條件判斷式 有()跟沒括號沒差，但沒括號時要空一格

score = int(input("請輸入學生分數:"))

if score >= 90:
    grade = "優"
elif score >= 80:
    grade = "甲"
elif score >= 70:
    grade = "乙"
elif score >= 60:
    grade = "丙"
else:
    grade = "丁"

print(f"學生等級:{grade}")