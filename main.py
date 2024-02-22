import pygame # pygame 모듈의 임포트
import sys # 외장 모듈
from pygame.locals import * # QUIT 등의 pygame 상수들을 로드한다.
from block import block_size, block

width = block_size * 10 # 상수 설정
height = width * 2
white = (255, 255, 255)
black = (0, 0, 0)
fps = 30

pygame.init() # 초기화

pygame.display.set_caption('Tetris Beta') # 창 제목 설정
display = pygame.display.set_mode((width, height), 0, 32) # 메인 디스플레이를 설정한다
clock = pygame.time.Clock() # 시간 설정

is_block_alive = False

while True: # 게임 메인 로직
    if not is_block_alive:
        new_block = block()
        is_block_alive = True

    for event in pygame.event.get(): # 발생한 입력 event 목록의 event마다 검사
        if event.type == QUIT: # event의 type이 QUIT에 해당할 경우
            pygame.quit() # pygame을 종료한다
            sys.exit() # 창을 닫는다

    display.fill(white) # displaysurf를 하얀색으로 채운다

    if is_block_alive:
        for x, y in new_block.get_pos():
            pygame.draw.rect(display, new_block.color, [x, y, block_size, block_size])
        new_block.move_pos()
        if new_block.ypos >= height:
            is_block_alive = False

    # 격자무늬 만들기
    for x in range(block_size, width, block_size):  # 세로줄 긋기
        pygame.draw.line(display, black, (x, 0), (x, 400))
    for y in range(block_size, height, block_size):  # 가로줄 긋기
        pygame.draw.line(display, black, (0, y), (400, y))

    pygame.display.update() # 화면을 업데이트한다
    clock.tick(fps) # 화면 표시 회수 설정만큼 루프의 간격을 둔다
