import pygame
import os
#########################################################################################
pygame.init() # 초기화 (반드시 필요)
# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("설이 Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
#########################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환
# current_path = "C:/projectWeb/pythonworkspace/project/frame_background_stage_character" # 현재 파일의 위치 반환

# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))
# 캐릭터 불러오기
character = pygame.image.load(os.path.join(image_path, "character.png"))

# 캐릭터 이동 
to_x = 0
to_y = 0

# 이동 속도
character_speed = 1

# 적 캐릭터


# 폰트 정의

# 총 시간

# 시작 시간 정보

# 이벤트 루트
running = True # 게임이 진행중인가?

while running:
    dt  = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    # print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


    # 가로 경계값 처리


    # 세로 경계값 처리

        
    # 충돌 처리를 위한 rect 정보 업데이트


    # 충돌 체크


    # screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255)) # 배경을 파란색으로 채우기
    screen.blit(background, (0, 0))


    # 타이머 집어 넣기  
    # 경과 시간 계산 start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴

    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    # 출력할 글자, True, 글자 색상

    # 시간이 0 이하이면 게임 종료



    pygame.display.update() # 화면 업데이트

# 잠시 대기
pygame.time.delay(1000) # 1초 정도 대기 (ms)

# pygame 종료
pygame.quit()
