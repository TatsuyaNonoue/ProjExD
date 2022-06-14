import random
import datetime
def main():
    seikai = shutudai()
    kaitou(seikai)

def shutudai():
    qas =[{"q":"サザエの旦那の名前は?","a":["ますお","マスオ"]},
          {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
          {"q":"タラオはカツオからみてどんな関係？","a":["甥っ子","甥","おいっこ","おい"]},
         ]
    print("問題:")
    r = random.randint(0,2)
    print(qas[r]["q"])
    return qas[r]["a"]

def kaitou(seikai):
    st = datetime.datetime.now()
    ans = input("答えるんだ:")
    if ans in seikai:
        print("正解！")
        ed = datetime.datetime.now()
        print((ed-st).seconds)
    else:
        print("出直してこい！！")
        ed = datetime.datetime.now()
        print(f"{(ed-st).seconds}秒")
if __name__ == "__main__":
    main() 

