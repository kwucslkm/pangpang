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
# 볼 사이즈
# ball1 : 160, 160
# ball2 : 80, 80
# ball3 : 40, 40
# ball4 : 20, 20
# 공 크기에 따른 속도 조절 필요
#########################################################################################
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환
# current_path = "C:/projectWeb/pythonworkspace/project/frame_background_stage_character" # 현재 파일의 위치 반환

# 배경 이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))
# 스테이지 불러오기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 불러오기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x = screen_width /2  - character_width / 2
character_y = screen_height - stage_height - character_height

# 캐릭터 이동 
to_x = 0
# to_y = 0

# 이동 속도
character_speed = 0.6
weapon_speed = 10
# 무기
weapons = []
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x = character_x + character_width/2 - weapon_width/2
weapon_y = screen_height - stage_height
# 무기 이동

to_weapon = 0
# 볼 가져오기 

# 폰트 정의

# 총 시간

# 시작 시간 정보

# 이벤트 루트
running = True # 게임이 진행중인가?

while running:
    dt  = clock.tick(30) # 게임화면의 초당 프레임 수를 설정
    # print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x = character_x + character_width/2 - weapon_width/2
                weapon_y = screen_height - stage_height
                weapons.append([weapon_x, weapon_y])

            # elif event.key == pygame.K_UP: # 캐릭터를 위로
            #     to_y -= character_speed
            # elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
            #     to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 케릭터 위치 정의

    character_x += to_x * dt
    # 가로 경계값 처리    # 세로 경계값 처리
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width
    # 무기 위치 정의
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올림

    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
        
    # 충돌 처리를 위한 rect 정보 업데이트

    # 충돌 체크

    # screen.fill((0, 0, 255)) # 배경을 파란색으로 채우기
    screen.blit(background, (0, 0)) # 배경 그리기
    for weapon_x, weapon_y in weapons:
        screen.blit(weapon, (weapon_x, weapon_y))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x, character_y))


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
