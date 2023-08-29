import random
def get_score() -> list:  #隨機跑5個分數
    score = []
    for i in range(5):
        score.append(random.randint(50,100))
    return score

def get_names(nums:int) -> list:
    with open("names.txt",encoding="utf-8",newline="") as file:
        names_str = file.read()
        all_names_list = names_str.split(sep="\n")
        names_list = random.choices(all_names_list,k=nums_int) #取出一定數量的姓名
    return names_list


nums_int = int(input("請輸入學生數:"))
#取得nums_int個姓名
names_list = get_names(nums_int)

students = []
for i in range(nums_int): #變數【 _ 】為省略運算子
    scores = get_score() #宣告一個新的變數 = 上面的函式
    new_list = [names_list[i]] + scores
    students.append(new_list)

print(students)