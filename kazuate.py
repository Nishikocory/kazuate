import random
range = input("整数の範囲を設定してね\n")
print(f"範囲は {range}  だね！ゲームスタート！\n数字を入力してね！")
answer = random.randint(1, int(range))
response = input()
count = 1
while True:
    if int(response) == answer:
        print(f"正解！ {count} 回目で当たったね！")
        break
    else:
        while int(response) != answer:
            if int(response) > answer:
                print("それより小さいよ")
                response = input()
                count += 1
            else:
                print("それより大きいよ")
                response = input()
                count += 1
