import random
rsp = ["","グー","チョキ","パー"]
you = int(input("じゃんけんぽん！グー:1,チョキ:2,パー:3"))

ai = random.randint(1,3)

print(f"あなたの手: {rsp[you] } コンピュータ:{rsp[ai]}")
if you == 1 :
    if ai == 1:
        print("あいこです")
    elif ai == 2:
        print("あなたの勝ちです")
    else:
        print("あなたの負けです")
elif you == 2:
    if ai == 1:
        print("あなたの負けです")
    elif ai == 2:
        print("あいこです")
    else:
        print("あなたの勝ちです")
elif you == 3:
    if ai == 1:
        print("あなたの勝ちです")
    elif ai == 2:
        print("あなたの負けです")
    else:
        print("あいこです")
