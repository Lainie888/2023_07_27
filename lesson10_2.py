import random
def allNames():
    names_list = []
    with open("names.txt", encoding="utf-8") as file:
        for i in file:
            names_list.append(i[:3])
    return names_list

print("===========取名字系統=========\n\n")

while True:
    names_list = allNames()
    first_name = input("請輸入你的姓:")
    count = int(input("請輸入你要的筆數:"))
    random_names = random.choices(names_list, k= count) #隨機抓5個
    for i in random_names:
        print(first_name + i[-2:])

    again = input("你還要繼續嗎? (y , n)")
    if again.lower() == "n":
        break

print("系統結束")
