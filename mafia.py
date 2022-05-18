from multiprocessing.sharedctypes import Value
from operator import truediv
from os import kill, system
from pickle import FALSE
from random import shuffle
from tabnanny import check
from tkinter import E
import winsound
from time import sleep
from random import randrange


def initial_setting():

    while(1):
        try:
            player_number = int(input("인원수 입력 : "))
            break
        except ValueError:
            print("잘못된 숫자입니다. 다시 입력하세요.")
        
    print("선택하신 인원수는 " + str(player_number) + "명 입니다.")
    current_survivor = player_number
    mafia_number = player_number//3
    current_mafia_number = mafia_number
    police_number = 1
    doctor_number = 1
    

    print("마피아는 " + str(mafia_number) + "명, 경찰은 "+str(police_number)+"명, 의사는 "+str(doctor_number)+"명 입니다. 나머지 " + str(player_number-mafia_number-police_number-doctor_number) + "명은 일반 시민입니다.")
    for i in range(0,player_number):
        if(i<mafia_number):
            playerlist.append(1)
        if(i<police_number):
            playerlist.append(2)
        if(i<doctor_number):
            playerlist.append(3)
        if(i>=mafia_number and i>=police_number and i>=doctor_number and len(playerlist) < player_number):
            playerlist.append(0)
        #print("현재 생성된 리스트 : "+str(playerlist))
    shuffle(playerlist)
    while(1):
        day_conference_time = input("낮 회의 시간 입력(분): ")
        try:
            int(day_conference_time)
            is_day_conference_time_int = True
        except ValueError:
            is_day_conference_time_int = False
        if(is_day_conference_time_int):
            print("시간이 "+str(day_conference_time)+"분으로 설정되었습니다.\n")
            break
        else:
            print("잘못된 시간입니다. 정수를 입력하세요")
    return day_conference_time, player_number, current_survivor, current_mafia_number
def role_setting():
    print("각자 역할을 고르겠습니다. 첫 번째 사람부터 순서대로 자신만 볼 수 있는 상태에서 엔터를 클릭하세요.")
        
    for i in range(len(playerlist)):
        trash = str(input("준비가 되었다면 엔터를 누르세요..."))
        system('cls')
        if(playerlist[i]==0):
            print("당신은 시민입니다. 마피아를 찾아 처형시키세요.")
        elif(playerlist[i]==1):
            print("당신은 마피아입니다. 시민을 죽이고 사람들을 속이세요. 마피아와 시민의 수가 같아지면 승리합니다.")
            one_list=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            pos = [i for i in range(len(playerlist)) if playerlist[i]==1]
            pos = [x+y for x,y in zip(pos, one_list)]
            print("마피아: "+str(pos))
        elif(playerlist[i]==2):
            print("당신은 경찰입니다. 밤에 사람들을 조사하여 마피아를 찾으세요. 마피아를 처형시키세요.")
        elif(playerlist[i]==3):
            print("당신은 의사입니다. 마피아에게 살해당할 것 같은 사람을 살리세요. 마피아를 찾아 처형시키세요.")
        if (i==len(playerlist)):
            trash = str(input("이제 모두에게 화면을 돌리고 엔터를 누르세요."))
        else:
            trash = str(input("엔터를 누르고 다른 사람에게 화면을 넘기세요."))
            system('cls')
    print("모든 직업이 결정되었습니다.")
def day_timer():
    print(day_conference_time+"분 동안 회의할 수 있습니다. 누구를 처형시킬지 회의해주세요.")
    trash=str(input("회의를 시작하려면 엔터를 누르세요."))
    remaining_seconds = int(day_conference_time)*60
        
    while(1):
        print("남은 시간 : "+str(remaining_seconds)+"초")
        if (remaining_seconds<=0):
            print("회의 시간이 종료되었습니다.\n")
            break
        remaining_seconds = remaining_seconds-1
        sleep(1)
def day_vote(current_mafia_number, current_survivor):
    while(1):
        print("투표할 사람을 골라주세요.")
        print("맨 처음 직업을 뽑은 사람 순서대로 1번~"+str(player_number)+"번 까지입니다.\n0은 투표가 무효가 되었을 때입니다(동점, 사형 반대)")
        execution_selection = input("숫자 입력: ")
        try:
            int(execution_selection)
            is_execution_selection_int = True
        except ValueError:
            is_execution_selection_int = False
            
        if(is_execution_selection_int == False):
            print("잘못된 숫자입니다. 다시 입력하세요.\n")
        elif(int(execution_selection) < 0 or int(execution_selection) > player_number):
            print("잘못된 숫자입니다. 다시 입력하세요.\n")
        elif(int(execution_selection) == 0):
            is_tie = True
            break
        else:
            is_tie = False
            break
    if(is_tie == False):
        print(str(execution_selection)+"번이 처형되었습니다.")
        print(str(execution_selection)+"번은 마피아가....")
        current_survivor = current_survivor-1
        sleep(2.5)
        if(playerlist[int(execution_selection)-1] == 1):
            print("맞았습니다!")
            sleep(1.5)
            current_mafia_number = current_mafia_number-1
            print("남은 마피아: " + str(current_mafia_number) + "명")
            playerlist[int(execution_selection)-1] = 4
                
        else:
            print("아니였습니다!")
            sleep(1.5)
            print("이렇게 무고한 시민 한 명이 희생되었습니다...")
            sleep(1)
            print("남은 마피아: "+str(current_mafia_number) + "명")
            playerlist[int(execution_selection)-1] = 4
    else:
        print("투표가 무효화되었습니다.")
        is_tie = False
    return current_mafia_number, current_survivor
def night_vote():
    print("밤이 되었습니다.")
    sleep(1)
    print("맨 처음 직업을 뽑은 사람부터 순서대로 자신만 볼 수 있는 상태에서 엔터를 누르세요.")
    trash = str(input("1번부터 준비가 되었다면 엔터를 누르세요..."))
    kill_list = []
    for i in range(len(playerlist)):
        system('cls')
        trash = str(input("준비가 되었다면 엔터를 누르세요..."))
        system('cls')
        if(playerlist[i]==4): #뒤진놈
            continue
        elif(playerlist[i]==1): #마피아일 때
            print("당신은 마피아입니다. 죽일 사람을 선택하세요.")
            
                
            while(1):
                kill_target = input("숫자 입력: ")
                try:
                    int(kill_target)
                    is_kill_target_int = True
                except ValueError:
                    is_kill_target_int = False
                if(is_kill_target_int==False):
                        print("잘못된 숫자입니다. 다시 입력하세요.")
                elif(0>=int(kill_target) or int(kill_target)> len(playerlist)):
                    print("잘못된 숫자입니다. 다시 입력하세요.")
                elif(int(playerlist[int(kill_target)-1])==4): #아 꼴받네 나중에 고침
                    print("그 사람은 이미 죽었습니다. 다른 사람을 선택하세요.")
                else:
                    print("죽일 사람이 선택되었습니다.")
                    kill_list.append(int(kill_target)-1)
                    #print(kill_list)
                    break
                
        elif(playerlist[i]==2): #경찰일 때
            print("당신은 경찰입니다. 조사할 사람을 선택하세요.")

            while(1):
                check_target = input("숫자 입력: ")
                try:
                    int(check_target)
                    is_check_target_int = True
                except ValueError:
                    is_check_target_int = False
                if(is_check_target_int==False):
                    print("잘못된 숫자입니다. 다시 입력하세요.")
                elif(0>=int(check_target) or int(check_target)> len(playerlist)):
                    print("잘못된 숫자입니다. 다시 입력하세요.")
                elif(int(playerlist[int(check_target)-1])==4):
                    print("그 사람은 죽었습니다. 다른 사람을 선택하세요.")
                else:
                    if(playerlist[int(check_target)-1]==1):
                        print("그 사람은 마피아입니다!")
                    else:
                        print("그 사람은 마피아가 아닙니다.")
                    break
        
        elif(playerlist[i]==3): #의사일 때
            print("당신은 의사입니다. 살릴 사람을 선택하세요.")

            while(1):
                heal_target = input("숫자 입력: ")
                try:
                    int(heal_target)
                    is_heal_target_int = True
                except ValueError:
                    is_heal_target_int = False
                if(is_heal_target_int==False):
                    print("잘못된 숫자입니다. 다시 입력하세요.")
                elif(int(heal_target) <=0 or int(heal_target)> len(playerlist)):
                    print("잘못된 숫자입니다. 다시 입력하세요.")
                elif(int(playerlist[int(heal_target)-1])==4):
                    print("그 사람은 죽었습니다. 다른 사람을 선택하세요.")
                else:
                    print("살릴 대상이 선택되었습니다.")
                    heal_target = int(heal_target)-1
                    break
        elif(playerlist[i]==0): #시민일 때
            print("당신은 시민입니다.")
            print("수학 문제를 맞추세요!")
            while(1):
                math_question_number_a = int(randrange(1,10))
                math_question_number_b = int(randrange(1,10))
                math_question_answer = math_question_number_a + math_question_number_b
                print(str(math_question_number_a)+"+"+str(math_question_number_b)+"=?")
                math_user_answer = input("답 입력: ")
                try:
                    if(int(math_user_answer)==math_question_answer):
                        print("정답입니다!")
                        break
                    else:
                        print("틀렸습니다! 다시 맞춰보세요!")
                except ValueError:
                    print("틀렸습니다! 다시 맞춰보세요!")
        
        print("다음 사람에게 컴퓨터를 넘기기 전 엔터를 누르세요...")
        trash = str(input("엔터를 눌러 계속..."))
    real_kill_target = more_than_half(kill_list)
    #print(real_kill_target)
    return real_kill_target, heal_target
def night_vote_calculate(kill_target, heal_target, current_mafia_number):

    for i in range(len(playerlist)):
        if(i==kill_target and i==heal_target):
            is_doctor_saved = True
            killed_player = 0 #아무도 안 죽었다는 뜻임
        elif(i==kill_target and i!=heal_target):
            if(playerlist[i]==1):
                current_mafia_number = current_mafia_number -1
            killed_player = int(i)+1
            playerlist[i]=4
            is_doctor_saved = False
        else:
            is_doctor_saved = False
            killed_player = 0
    return is_doctor_saved, killed_player, current_mafia_number        
def more_than_half(nums): #과반수 측정하는 함수
	majority_count = len(nums)//2
	for num in nums:
		count = sum(1 for elem in nums if elem == num)
		if count > majority_count:
			return num
system('cls')
playerlist = [] # 0이 시민, 1이 마피아, 2가 경찰, 3이 의사, 4는 사망
is_tie = False
while(1):
    print("(1) 게임 시작 (2) 게임 설명 (3) 종료")
    user_input = input(">>>")
    if(user_input=="1"):
        settings_return = initial_setting()
        day_conference_time, player_number, current_survivor, current_mafia_number = settings_return

        role_setting()
        print("낮이 되었습니다.")
        day_timer()
        day_vote_result = day_vote(current_mafia_number, current_survivor)
        current_mafia_number, current_survivor = day_vote_result

        sleep(1)
        vote_result = night_vote()
        kill_target, heal_target = vote_result
        night_vote_result = night_vote_calculate(kill_target, heal_target, current_mafia_number)
        is_doctor_saved, killed_player, current_mafia_number = night_vote_result

        
        while(1):
            system('cls')
            print("낮이 되었습니다.")
            sleep(1)
            if(killed_player!=0):
                print(killed_player+"번이 죽었습니다...")
                current_survivor = current_survivor -1
                
            elif(killed_player == 0 and is_doctor_saved == True):
                print("마피아에게 죽을 뻔 한 사람을 의사가 살렸습니다!")
            else:
                print("왠지는 모르겠지만 아무도 죽지 않았습니다.")
            if(current_mafia_number <=0 or current_mafia_number >= current_survivor - current_mafia_number):
                break
            day_timer()
            day_vote_result = day_vote(current_mafia_number, current_survivor)
            current_mafia_number, current_survivor = day_vote_result
            if(current_mafia_number <=0 or current_mafia_number >= current_survivor - current_mafia_number):
                break
            sleep(1)
            vote_result = night_vote()
            kill_target, heal_target = vote_result
            night_vote_result = night_vote_calculate(kill_target, heal_target, current_mafia_number)
            is_doctor_saved, killed_player, current_mafia_number = night_vote_result
        if(current_mafia_number <=0):
            print("마피아가 모두 사망하였습니다! 시민이 승리하였습니다!")
        elif(current_mafia_number >= current_survivor-current_mafia_number):
            print("마피아와 시민의 수가 같아졌습니다! 마피아가 승리하였습니다!")
    if(user_input=='2'):
        print("남들의 정체를 모르는 다수파의 시민과 서로의 정체를 아는 소수파의 마피아가 서로 죽이는 심리 추리 파티 게임입니다.\n")
        print("1. 마피아\n")
        print("시민을 죽여 마피아의 수와 시민의 수가 같게 만들면 승리합니다. 밤마다 토의를 통해 한 명을 죽일 수 있습니다.\n")
        print("2. 경찰\n")
        print("시민에 속합니다. 밤마다 사람 한 명을 골라 마피아인지 아닌지 조사할 수 있습니다. 결과는 경찰 본인에게만 알려집니다. 마피아를 모두 죽이면 승리합니다.\n")
        print("3. 의사\n")
        print("시민에 속합니다. 밤마다 사람 한 명을 골라 마피아로부터 보호할 수 있습니다. 보호한 사람이 마피아에게 공격당할 경우 죽지 않습니다. 마피아를 모두 죽이면 승리합니다.\n")
        print("4. 시민\n")
        print("(당연히)시민에 속합니다. 아무 능력을 가지고 있지 않습니다. 마피아를 모두 죽이면 승리합니다.\n")        
            


