import json

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json","w",encoding="utf-8")as f:
        json.dump(tasks,f,ensure_ascii=False,indent=4)

tasks=load_tasks()
while True:
    menu=("1.append","2.show","3.delete","4.exit")
    print(menu)
    choice=input("choose:")
    if choice=="1":
        tasks.append({"task":input("task:")})
        save_tasks(tasks)
    elif choice=="2":
        for i,t in enumerate(tasks,start=1):
            print(i,t["task"])
    elif choice=="3":
        try:
            number=int(input("task number:"))
            tasks.pop(number-1)
            save_tasks(tasks)
        except (ValueError,IndexError):
            print("invalid number")
    elif choice=="4":
        break
    else:
        print("invalid choice")


