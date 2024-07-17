# 모듈 임포트
import random as ran
import webbrowser as web
import time

# 변수 선언
student = 0
num = 0
restart = ""
repeat = 0
repeat_result = [] # 중복값 제거 X
result = [] # 중복값 제거 O

# 다시 뽑기 실행
def again():
    restart = input("Restart?(y/n) ")
    if restart == "y":
        run()
    if restart == "n":
        main()
    else:
        print('Invalid Input')
        again()

# 다시 연속 뽑기 실행
def again_stream():
    restart = input("Restart?(y/n) ")
    if restart == "y":
        stream()
    if restart == "n":
        main()
    else:
        print('Invalid Input')
        again_stream()

# 메인 실행
def main():
    print("Start / Repeat / Options / Help / Exit / 한국어")
    a = input()
    if a == "Start":
        run()
    if a == "Repeat":
        stream()
    if a == "Options":
        options()
    if a == "Exit":
        c = input("Exit Program?(y/n) ")
        if c == "y":
            print("Program Stopped")
            print("Window will be shut in 5 seconds")
            time.sleep(5)
            exit()
        if c == "n":
            main()
        else:
            print('Invalid Input')
    if a == 'Help':
        web.open_new_tab('https://haeengin.netlify.app/gahca_help.html')
    if a == "한국어":
        main_kor()
    else:
        print('Invalid Input')
        main()
    
# 랜덤 뽑기 실행
def run():
    while True:
        global student
        global num
        if student == 0:
            student = int(input("Last Number? "))
            num = ran.randint(1, student)
            print("Picked Number:", num)
            again()
        if student != 0:
            num = ran.randint(1, student)
            print("Picked Number:", num)
            again()

# 연속 뽑기 실행
def stream():
    while True:
        global student
        global num
        global repeat
        if student == 0:
            student = int(input("Last Number? "))
            repeat = int(input("Repeat Number? "))
            for x in range(repeat):
                num = ran.randint(1, student)
                repeat_result.append(num)
            a = input('Delete Duplicates? (y/n) ')
            if a  == 'y':
                result = list(dict.fromkeys(repeat_result))
                print(result)
            if a == 'n':
                print(repeat_result)
            again_stream()
        if student != 0:
            repeat = int(input("Repeat Number? "))
            for x in range(repeat):
                num = ran.randint(1, student)
                repeat_result.append(num)
            a = input('Delete Duplicates? (y/n) ')
            if a  == 'y':
                result = list(dict.fromkeys(repeat_result))
                print(result)
            if a == 'n':
                print(repeat_result)
            again_stream()

# 옵션 실행
def options():
    print("Fix / Current / Back")
    b = input("")
    if b == "Fix":
        global student
        student = int(input("Fix Last Number: "))
        print("Last Number Fixed")
        options()
    if b == "Current":
        if student == 0:
            print("Last Number Is Not Set")
            options()
        if student != 0:
            print("Current Last Number:", student)
            options()
    if b == "Back":
        main()
    else:
        print('Invalid Input')
        options()

# 다시 뽑기 실행
def again_kor():
    restart = input("다시 뽑을까요?(예/아니오) ")
    if restart == "예":
        run_kor()
    if restart == "아니오":
        main_kor()
    else:
        print("잘못된 입력값입니다")
        again_kor()

# 다시 연속 뽑기 실행
def again_stream_kor():
    restart = input("다시 뽑을까요?(예/아니오) ")
    if restart == "예":
        stream_kor()
    if restart == "아니오":
        main_kor()
    else:
        print('잘못된 입력값입니다.')
        again_stream_kor()

# 랜덤 뽑기 실행
def run_kor():
    while True:
        global student
        global num
        global restart
        if student == 0:
            student = int(input("마지막 번호를 입력해주세요: "))
            num = ran.randint(1, student)
            print(num)
            again_kor()
        if student != 0:
            num = ran.randint(1, student)
            print(num)
            again_kor()

# 연속 뽑기 실행
def stream_kor():
    while True:
        global student
        global num
        global repeat
        if student == 0:
            student = int(input("마지막 번호를 업력해주세요: "))
            repeat = int(input("몇 번 뽑을까요? "))
            for x in range(repeat):
                num = ran.randint(1, student)
                repeat_result.append(num)
            a = input('중복 번호를 삭제할까요? (예/아니오) ')
            if a  == '예':
                result = list(dict.fromkeys(repeat_result))
                print(result)
            if a == '아니오':
                print(repeat_result)
            again_stream_kor()
        if student != 0:
            repeat = int(input("몇 번 뽑을까요? "))
            for x in range(repeat):
                num = ran.randint(1, student)
                repeat_result.append(num)
            a = input('중복 번호를 삭제할까요?  (예/아니오) ')
            if a  == '예':
                result = list(dict.fromkeys(repeat_result))
                print(result)
            if a == '아니오':
                print(repeat_result)
            again_stream_kor()

# 옵션 실행
def options_kor():
    print("수정 / 현황 / 뒤로가기")
    b = input("")
    if b == "수정":
        global student
        student = int(input("수정할 마지막 번호: "))
        print("수정되었습니다")
        options_kor()
    if b == "현황":
        if student == 0:
            print("마지막 번호가 설정되어 있지 않습니다.")
            options_kor()
        if student != 0:
            print("현재 설정된 마지막 번호:", student)
            options_kor()
    if b == "뒤로가기":
        main_kor()
    else:
        print('잘못된 입력값입니다.')
        options_kor()

# 메인 실행
def main_kor():
    print("시작 / 연속 / 옵션 / 도움말 / 나가기 / English")
    a = input()
    if a == "시작":
        run_kor()
    if a == "연속":
        stream_kor()
    if a == "옵션":
        options_kor()
    if a == "나가기":
        c = input("프로그램을 종료할까요?(예/아니오) ")
        if c == "예":
            print("종료되었습니다.")
            print('창이 5초 후에 닫힙니다.')
            time.sleep(5)
            exit()
        if c == "아니오":
            main_kor()
        else:
            print("잘못된 입력값임니다")
    if a == "English":
        main()
    if a == '도움말':
        web.open_new_tab('https://haeengin.netlify.app/gacha_help.html')
    else:
        print("잘못된 입력값임니다")
        main_kor()

# 메인 실행
print("---Random Numbers---")
main()