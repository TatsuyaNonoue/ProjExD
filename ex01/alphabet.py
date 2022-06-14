maxkaisu = 5
sel_moji = 10
kake_moji = 2
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
import random

def main():
    kesu = quiz()
    ans(kesu)

def quiz():
    global sel_moji, kake_moji, alphabet
    kesumozi = []
    taisyo = (random.sample(alphabet,sel_moji)) #対象文字リスト作成
    print(f"対象文字:\n{taisyo}")
    hyozi = taisyo.copy()                       #表示文字のためにコピー
    for i in range(kake_moji):
        kake_place = random.randint(0,sel_moji)
        kesumoziyouso = hyozi[kake_place]
        kesumozi.append(kesumoziyouso)
        hyozi.pop(kake_place)                   #表示文字完成
    print(f"表示文字:\n{hyozi}")
    print(f"書けた文字:\n{kesumozi}")
    return kesumozi

def ans(kesu):
    global maxkaisu
    kaisu = 1
    while kaisu <= maxkaisu:
        ans_lenn = input("欠損文字はいくつあるでしょうか？")
        if int(ans_lenn) == kake_moji:
            print("正解です。それでは具体的に欠損文字を入力してください。")
            mozi1 = input("1つめ文字を入力してください:")
            mozi2 = input("2つ目の文字を入力してください:") 
            if mozi1 in kesu:
                if mozi2 in kesu:
                    print("正解です！おめでとう。")
                    break
            else:
                print("違います。もう一度入力してください。")
                print(f"残り回数:{maxkaisu-kaisu}")
                kaisu += 1
                continue
        else:
            print("違います。もう一度入力してください。")
            print(f"残り回数:{maxkaisu-kaisu}")
            kaisu += 1
            continue
if __name__ == "__main__":
    main() 