import time, json, os, sys

sys.tracebacklimit = 0 # traceback을 띄우지 않음
WAITTIME = 2
NUM_PLAYERS = len(os.listdir())

class MissonNotFinishError(Exception):
    pass

def greeting():
    print("< Tobigs 20 정규세션 git >")
    print("투빅스 20기 여러분들 환영합니다.")
    print("여기는 정규세션 과제 월드입니다.")
    time.sleep(WAITTIME + 1) # 연출을 위해 1초 추가
    print("그리고 저는 당신의 과제 달성을 도와줄 과제 요정입니다 ^^ ")
    print("과제 중 막히는 부분이 있으면 '19기 이영아'에게 언제든지 카톡 주세요~ ")
    time.sleep(WAITTIME)
    print("지시에 따라 여러분들에 대해 알려주시면 됩니다!")

def nameCheck():
    global players # 전역 변수 생성
    players = []

    for i in range(1, NUM_PLAYERS): # 플레이어 5명을 players 배열에 담슴니다.
        try:
            with open("player" + str(i) + "/profile.json", "r", encoding='utf-8') as f:
                data = json.load(f)
                if(data["닉네임"] == "[여기에 별명을 적어주세요]" or data["한마디"] == "[투빅스 20기에 임하는 각오 한 마디 적어 주세요!]"): # 모두의 파일이 작성되지 않음
                    time.sleep(WAITTIME)

