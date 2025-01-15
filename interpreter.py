from os.path import isfile as exist
from os import system as cmd

functions = ['개', '딱', '서', '아', '우', '현']

while True:
    var = 0
    string = ""

    dir = input(">>> ").split(maxsplit=1)
    # 예외 처리
    if len(dir) != 2: # 명령어가 올바르지 않으면
        raise SyntaxError("서랭 파일 실행은 'stand example.shw' 같은 식으로 해야 합니다.")
    if not dir[1].endswith(".shw"): # 확장자가 올바르지 않으면
        raise OSError("서랭 파일만 실행할 수 있습니다.")
    if exist(dir[1]):
        code = open(dir[1], 'r', encoding="UTF8").read().replace("\n", "").replace(" ", "")
    else: # 파일이 없으면
        raise FileNotFoundError("그런 파일은 없습니다. 잘못 입력한 게 아닐까요?")
    if dir[0] != "stand": # 명령어가 올바르지 않으면
        raise SyntaxError("서랭 파일 실행은 'stand example.shw' 같은 식으로 해야 합니다.")
    if not (code.startswith("코") and code.endswith("아이")): # 코드의 시작과 끝이 "코"와 "아이"가 아니면
        raise SyntaxError("서랭 코드는 '코'로 시작하고 '아이'로 끝나야 합니다. 아니면 겸상 안 합니다.")
    if code.count("코") != 1 or code.count("아이") != 1: # 코드에 "코"나 "아이"가 한 개가 아니면
        raise SyntaxError("코드에 '코'와 '아이'는 한 번만 써야 됩니다.")
    code = code[1:-2]
    if not (all(i in functions for i in code) or code == ""):  # 이상한 글자 있으면
        raise SyntaxError("멋대로 함수를 만드시면 안 됩니다.")
    
    for i in code:
        if i == "서":
            var *= 2
        if i == "현":
            var = 0
        if i == "우":
            var += 1
        if i == "아":
            print(chr(var), end="")
            string += str(chr(var))
        if i == "개":
            var -= 1
        if i == "딱":
            with open("temp.py", 'w', encoding="UTF8") as f:
                f.write(string)
            cmd("python temp.py")
            cmd("del temp.py")
    print()
