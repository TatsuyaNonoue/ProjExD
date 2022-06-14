import random

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
    ans = input("答えるんだ:")
    if ans in seikai:
        print("正解！")
    else:
        print("出直してこい！！")
    
if __name__ == "__main__":
    main() 

