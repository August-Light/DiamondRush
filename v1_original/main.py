import pygame
import random
pygame.init()
length=460
height=600
size=length,height
screen=pygame.display.set_mode(size)
mode = 2
screen.fill([145,153,255])
man_pic = pygame.transform.scale(pygame.image.load("./v1_original/steve.png"),[60,80])
dia_pic = pygame.transform.scale(pygame.image.load("./v1_original/diamond.png"),[48,52])
clock = pygame.time.Clock()
dida = 0
wait = 0
red = 0
Map = []
pos = [2,2]
alert = False
score = 0
time = 0
shortest_time = 0
impossible = False
man_time = 0
man_appear = False
for i in range(5):
    Map.append([0,0,0,0,0])
diamondx = 0
diamondy = 0
def diamond():
    global diamondx,diamondy
    diamondx = random.randint(0,4)
    diamondy = random.randint(0,4)
    if pos[0] == diamondx and pos[1] == diamondy:
        diamond()
def calc_pos(n):
    return n*80+(n+1)*10
def drawdiamond():
    screen.blit(dia_pic,[calc_pos(diamondx)+15,calc_pos(diamondy)+15])
def drawmap():
    for i in range(25):
        if Map[i%5][i//5] == 1:
            pygame.draw.rect(screen,[255,255-red*8,255-red*8],[calc_pos(i%5),calc_pos(i//5),80,80],0)
        else:
            pygame.draw.rect(screen,[255,255,255],[calc_pos(i%5),calc_pos(i//5),80,80],0)
def drawman(x,y):
    screen.blit(man_pic,[calc_pos(x)+8,calc_pos(y)])
def drawstring(string,where):
    screen.blit(pygame.font.Font(None,100).render(string,1,(255,255,255)),where)
def gameover():
    screen.fill([145,153,255])
    if impossible:
        b_string = "Impossible"
    elif wait == 0:
        b_string = "Master"
    elif wait == 15:
        b_string = "Normal"
    elif wait == 45:
        b_string = "Baby"
    drawstring("["+b_string+"]",[20,20])
    drawstring("GAME OVER",[20,140])
    drawstring("Diamond:"+str(score),[20,200])
    time_s = time/30
    a_string = "%.2f" % time_s
    drawstring("Time:"+a_string+"s",[20,260])
    drawstring("'T'ry again",[20,380])
drawstring("'B'aby",[20,200])
drawstring("'N'ormal",[20,260])
drawstring("'M'aster",[20,320])
drawstring("'I'mpossible",[20,380])
pygame.display.flip()

running = True
while running:
    clock.tick(30)
    if mode == 1:
        time += 1
    if score == 50 and mode == 1:
        mode = 0
        gameover()
        drawstring("50!YOU WIN!",[20,320])
        pygame.display.flip()
    if impossible:
        if time//45 == time/45:
            man_pic = pygame.transform.scale(pygame.image.load("./v1_original/steve.png"),[60,80])
            man_appear = True
        elif man_time == 15 and man_appear:
            man_appear = False
            man_time = 0
            man_pic = pygame.image.load("./v1_original/nothing.png")
        if man_appear:
            man_time += 1
    if red == 30:
        red = 0
    elif alert == True:
        red += 1
    if dida == wait and alert == False and mode == 1:
        dida = 0
        alert = True
        heng_shu = random.choice([True,False])
        q=0
        for i in range(5):
            ran_TF = random.choice([True,False])
            if ran_TF:
                q+=1
                for j in range(5):
                    if heng_shu:
                        Map[i][j] = 1
                    else:
                        Map[j][i] = 1
            if q==5:
                ran_num = random.randint(0,4)
                for j in range(5):
                    if heng_shu:
                        Map[i][j] = 0
                    else:
                        Map[j][i] = 0
    elif dida == 30 and alert == True and mode == 1:
        dida = 0
        alert = False
        if Map[pos[0]][pos[1]] == 1:
            mode = 0
            gameover()
            pygame.display.flip()
        else:
            Map = []
            for i in range(5):
                Map.append([0,0,0,0,0])
    elif mode == 1:
        dida += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and mode == 1:
            last_pos = pos[:]
            if event.key == pygame.K_UP:
                pos[1]-=1
            elif event.key == pygame.K_DOWN:
                pos[1]+=1
            elif event.key == pygame.K_LEFT:
                pos[0]-=1
            elif event.key == pygame.K_RIGHT:
                pos[0]+=1
            if pos[0]<0 or pos[0]>4 or pos[1]<0 or pos[1]>4:
                pos = last_pos[:]
            if pos[0] == diamondx and pos[1] == diamondy:
                score+=1
                diamond()
            drawman(pos[0],pos[1])
        elif event.type == pygame.KEYDOWN and mode == 2:
            if event.key == pygame.K_b:
                mode = 1
                diamond()
                wait = 45
            elif event.key == pygame.K_n:
                mode = 1
                diamond()
                wait = 15
            elif event.key == pygame.K_m:
                mode = 1
                diamond()
                wait = 0
            elif event.key == pygame.K_i:
                mode = 1
                diamond()
                wait = 0
                impossible = True
                man_pic = pygame.image.load("./v1_original/nothing.png")
        elif event.type == pygame.KEYDOWN and mode == 0:
            if event.key == pygame.K_t:
                screen.fill([145,153,255])
                mode = 2
                dida = 0
                wait = 0
                red = 0
                Map = []
                pos = [2,2]
                alert = False
                score = 0
                time = 0
                impossible = False
                man_time = 0
                man_appear = False
                man_pic = pygame.transform.scale(pygame.image.load("./v1_original/steve.png"),[60,80])
                for i in range(5):
                    Map.append([0,0,0,0,0])
                diamondx = 0
                diamondy = 0
                drawstring("'B'aby",[20,200])
                drawstring("'N'ormal",[20,260])
                drawstring("'M'aster",[20,320])
                drawstring("'I'mpossible",[20,380])
                pygame.display.flip()
    if mode == 1:
        screen.fill([145,153,255])
        drawmap()
        drawman(pos[0],pos[1])
        drawdiamond()
        drawstring("Diamond:"+str(score),[10,460])
        time_s = time/30
        a_string = "%.2f" % time_s
        drawstring("Time:"+a_string+"s",[10,520])
        pygame.display.flip()
pygame.quit()
