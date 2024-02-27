import random

block_size = 20
START_POS = [0, 0] # 블럭 시작 좌표
shapes = ( # 테트리미노 모양
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 2), (1, 0), (1, 1), (1, 2)),
    ((0, 0), (0, 1), (0, 2), (1, 2)),
    ((0, 0), (0, 1), (1, 0), (1, 1)),
    ((0, 1), (1, 0), (1, 1), (2, 0)),
    ((0, 0), (1, 0), (1, 1), (2, 0)),
    ((0, 0), (1, 0), (1, 1), (2, 1))
)
colors = [
    (0, 0, 241), # Blue
    (2, 241, 241), # Sky
    (240, 162, 0), # Orange
    (240, 240, 1), # Yellow
    (2, 241, 0), # Green
    (162, 0, 241), # Purple
    (241, 1, 1) # red

]

class block():
    def __init__(self):
        # 블럭 top 좌표
        self.xpos = START_POS[0]
        self.ypos = START_POS[1]

        #블럭 모양과 색상을 랜덤으로 설정
        self.shape = shapes[random.randint(0, 6)]
        self.color = colors[random.randint(0, 6)]

    def get_pos(self): # 좌표를 캡슐화 해서 접근 하도록
        result = []
        for x, y in self.shape:
            result.append([x * block_size + self.xpos, y * block_size + self.ypos])

        return result

    def move_pos(self, direct): # direct가 0이면 왼쪽으로 1이면 오른쪽으로 이동
        if direct == 0:
            self.xpos -= block_size
        else:
            self.xpos += block_size

    def down_pos(self):
        self.ypos += block_size // 10


if __name__ == "__main__":
    new = block()
    print(new.shape)
    print(new.get_pos())
