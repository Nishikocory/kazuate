import random
range = input("整数の範囲を設定してね\n")
print(f"範囲は {range}  だね！ゲームスタート！\n数字を入力してね！")
answer = random.randint(1, int(range))

response = input()
while (response != str(answer)):
    if response > str(answer):
        print("それより小さいよ")
        response = input()
    else:
        print("それより大きいよ")