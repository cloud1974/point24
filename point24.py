def point24(numbers):
    global solutions
    if len(numbers) == 1:
        if abs(eval(numbers[0]) - 24) < 0.00001:
            solutions.add(numbers[0])
    else:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                rest_numbers = [x for p, x in enumerate(numbers) if p != i and p != j]
                for op in "+-*/":
                    if op in "+-*" or eval(str(numbers[j])) != 0:
                        point24(["("+ str(numbers[i]) + op + str(numbers[j]) + ")"] + rest_numbers)
                    if op == "-" or (op == "/" and eval(str(numbers[i])) != 0):
                        point24(["("+ str(numbers[j]) + op + str(numbers[i]) + ")"] + rest_numbers)


while True:
    line = input("\n24点游戏开始，请输入四张牌的点数，用空格或逗号分隔。输入q退出：")
    if line == "q":
        break
    for x in line:
        if not x in "0123456789 ,":
            print("你刚才的输入中包含非法字符，请重新输入。")
            continue
    data = line.replace(",", " ").split(" ")
    solutions = set()
    if len(data) != 4:
        print("只能输入四张牌的点数哦，您刚才输入了%d个数字，请重新输入。" %len(data))
        continue
    point24(data)
    if len(solutions) == 0:
        print("这道题无解，再试试别的数字吧。")
        continue
    print("找到%d种解法：" %len(solutions))
    for i, s in enumerate(solutions):
        print("%d: %s = 24" %(i+1, s[1:-1]))


