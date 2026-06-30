num = [6,19,0]
while True:
    print("数字を入力してください")
    b = input("")
    if b =="q":
        break
    else:
        if int(b) in num:
            print("正解")
        else:
            print("不正解！'q'で終了することができます")

