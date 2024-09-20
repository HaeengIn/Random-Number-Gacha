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
repeat_result_len = 0
result_len = 0

# 메인 실행
def main():
    print("시작 / 연속 / 옵션 / 도움말 / 위키 / 나가기")
    a = input()
    if a == "시작":
        run()
    if a == "연속":
        stream()
    if a == "옵션":
        options()
    if a == '위키':
        web.open_new_tab('https://bit.ly/h_gacha')
        main()
    if a == "나가기":
        c = input("프로그램을 종료할까요?(예/아니오) ")
        if c == "예":
            print("종료되었습니다.")
            print('창이 5초 후에 닫힙니다.')
            time.sleep(5)
            exit()
        if c == "아니오":
            main()
        else:
            print("잘못된 입력값임니다")
    if a == '도움말':
        web.open_new_tab('https://docs.google.com/document/d/1uTJ_CcZwjVotc079VKp-H8oWn0KryKNOM2E5vRGZ-gw/edit?usp=sharing')
        main()
    else:
        print("잘못된 입력값임니다")
        main()

# 랜덤 뽑기 실행
def run():
    while True:
        global student
        global num
        global restart
        if student == 0:
            student = int(input("마지막 번호를 입력해주세요: "))
            num = ran.randint(1, student)
            print(num)
            again()
        if student != 0:
            num = ran.randint(1, student)
            print(num)
            again()

# 다시 뽑기 실행
def again():
    restart = input("다시 뽑을까요?(예/아니오) ")
    if restart == "예":
        run()
    if restart == "아니오":
        main()
    else:
        print("잘못된 입력값입니다")
        again()

# 연속 뽑기 실행
def stream():
    while True:
        global student
        global num
        repeat = 0
        repeat_result = [] # 중복값 제거 X
        result = [] # 중복값 제거 O
        repeat_result_len = 0
        result_len = 0

        if student == 0:
            student = int(input("마지막 번호를 입력해주세요: "))
            repeat = int(input("몇 번 뽑을까요?  "))
            for x in range(repeat):
                num = ran.randint(1, student)
                repeat_result.append(num)
                repeat_result_len = len(repeat_result)
            a = input('중복 번호를 삭제할까요? (예/아니오) ')
            if a  == '예':
                result = list(dict.fromkeys(repeat_result))
                result_len = len(result)
                print(result)
                print('뽑힌 번호 개수:', repeat_result_len, '개')
                print('삭제된 중복 번호 개수:', repeat_result_len - result_len, '개')
            if a == '아니오':
                print(repeat_result)
                print('뽑힌 번호 개수:', repeat_result_len, '개')
            again_stream()

        if student != 0:
            repeat = int(input("몇 번 뽑을까요?  "))
            for x in range(repeat):
                num = ran.randint(1, student)
                repeat_result.append(num)
                repeat_result_len = len(repeat_result)
            a = input('중복 번호를 삭제할까요? (예/아니오) ')
            if a  == '예':
                result = list(dict.fromkeys(repeat_result))
                result_len = len(result)
                print(result)
                print('뽑힌 번호 개수:', repeat_result_len, '개')
                print('삭제된 중복 번호 개수:', repeat_result_len - result_len, '개')
            if a == '아니오':
                print(repeat_result)
                print('뽑힌 번호 개수:', repeat_result_len, '개')
            again_stream()

# 다시 연속 뽑기 실행
def again_stream():
    restart = input("다시 뽑을까요?(예/아니오) ")
    if restart == "예":
        stream()
    if restart == "아니오":
        main()
    else:
        print('잘못된 입력값입니다.')
        again_stream()

# 옵션 실행
def options():
    print("수정 / 현황 / 메인으로")
    b = input("")
    if b == "수정":
        global student
        student = int(input("수정할 마지막 번호: "))
        print("수정되었습니다")
        options()
    if b == "현황":
        if student == 0:
            print("마지막 번호가 설정되어 있지 않습니다.")
            options()
        if student != 0:
            print("현재 설정된 마지막 번호:", student)
            options()
    if b == "메인으로":
        main()
    else:
        print('잘못된 입력값입니다.')
        options()

# 메인 실행
print("---Random Numbers---")
main()