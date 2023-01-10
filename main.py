from Framework import *

def main():
    framework = Framework(1280, 720)
    framePerSecond = 60
    loop = True
    while loop:
        # 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            else:
                framework.handleEvent(event)
        # 업데이트 & 그리기
        framework.update()
        framework.draw()
        framework.fps.tick(framePerSecond)
    pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
