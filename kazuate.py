import random
import os

range = input("整数の範囲を設定してね\n")
print(f"範囲は {range}  だね！ゲームスタート！\n数字を入力してね！")
answer = random.randint(1, int(range))
response = input()
count = 1
while True:
    if int(response) == answer:
        print(f"正解！ {count} 回目で当たったね！")
        if os.path.exists('数当てゲーム履歴.txt'):
            with open('数当てゲーム履歴.txt', "r+", encoding='utf-8') as f:
                f.seek(0)
                lines = f.readlines()
                f.write(str(count)+"\n")
                last_line = lines[-1].strip()
                print(f"前回は {last_line} 回目で正解したよ")
        else:
            f = open('数当てゲーム履歴.txt', 'a', encoding='UTF-8')
            f.write(str(count)+"\n")
            f.close
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