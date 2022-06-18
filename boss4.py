import pygame
import random
from time import sleep



# 게임에 사용되는 전역 변수 정의
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
CLARET = (255, 0, 255)
BLUE = (0,0,255)
pad_width = 480
pad_height = 640
fight_width = 40
fight_height = 49
fight1_width = 50
fight1_height = 70
enemy_width = 26
enemy_height = 20
heart_width = 25
heart_height = 24
meteor_width = 30
meteor_height = 24
meteor_hp= 2
explosionSound=['explosion01.wav','explosion03.wav']
enemyboss_width = 500
enemyboss_height= 200
enemyboss_hp=20
missile1_width = 35
missile1_height = 80


def gameover():
    global gamepad
    dispMessage('Game Over')

# 적을 맞춘 개수 계산
def drawScore1(count):
    global gamepad

    font = pygame.font.SysFont(None, 20)
    text = font.render('Player1: ' + str(count), True, BLUE)
    gamepad.blit(text, (0, 0))
def drawScore2(count):
    global gamepad

    font = pygame.font.SysFont(None, 20)
    text = font.render('Player2: ' + str(count), True, CLARET)
    gamepad.blit(text, (0, 15))
def drawPassed(count):
    global gamepad

    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Passed: ' + str(count), True, LIME)
    gamepad.blit(text, (360, 0))


# 화면에 글씨 보이게 하기
def dispMessage(text):
    global gamepad

    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(text, True, LIME)    
    textpos = text.get_rect()
    textpos.center = (pad_width/2, pad_height/2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()


def crash():
    global gamepad
    dispMessage('Crashed!')
    
def gameclear1() :    
    global gamepad
    dispMessage('Player 1 win') 
    sleep(100)
def gameclear2() :    
    global gamepad
    dispMessage('Player 2 win')    
    sleep(100)
# 게임에 등장하는 객체를 그려줌
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

# 게임 실행 메인 함수
def runGame():
    global gamepad, fighter, clock ,fighter1
    global bullet, enemy, heart, enemyboss, bullet2, missile1


    isShot1 = False
    isShot2 = False

    shotcount1 = 0
    shotcount2 = 0
    enemypassed = 0

    x = pad_width*0.3
    y = pad_height*0.9
    x_change = 0
    x1= pad_width*0.6
    y1= pad_height*0.9
    x1_change = 0

    bullet_xy = []
    bullet2_xy= []
    enemy_x = random.randrange(0, pad_width-enemy_width)
    enemy_y = 0
    enemy_speed = 1
    heart_x = random.randrange(0, pad_width-heart_width)
    heart_y = 0
    heart_speed = 4
    meteor_x= random.randrange(0, pad_width-meteor_width)
    meteor_y = 0
    meteor_speed = 2    
    meteor_hp= 2
    enemyboss_hp=20
    enemyboss_y=1  
    enemyboss_x=0
    missile1_x = random.randrange(0, pad_width-missile1_width)
    missile1_y=0
    missile1_speed = 4

        
    ongame = False
    while not ongame:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                ongame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 7
                elif event.key == pygame.K_RIGHT:
                    x_change += 7
                elif event.key == pygame.K_a:
                    x1_change -= 5
                elif event.key == pygame.K_d:
                    x1_change += 5    

                elif event.key == pygame.K_RSHIFT:
                    missileSound.play()
                    if len(bullet_xy) < 3:                        
                        bullet_x = x + fight_width/2
                        bullet_y = y - fight_height
                        bullet_xy.append([bullet_x, bullet_y])
                        
                elif event.key == pygame.K_LSHIFT:
                    missileSound.play()
                    if len(bullet2_xy) < 1:                        
                        bullet2_x = x1 + 5
                        bullet2_y = y1 - fight1_height
                        bullet2_xy.append([bullet2_x, bullet2_y])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    x1_change = 0
        gamepad.fill(BLACK)
        gamepad.blit(background,(0,40))
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fight_width:
            x = pad_width - fight_width
        x1 += x1_change
        if x1 < 0:
            x1 = 0
        elif x1 > pad_width - fight1_width:
            x1 = pad_width - fight1_width

       # 게이머 전투기1 가 적과 충돌했는지 체크
        if y < enemy_y + enemy_height:
            if (enemy_x > x and enemy_x < x + fight_width) or \
               (enemy_x + enemy_width > x and enemy_x+ enemy_width < x + fight_width):
                crash()
                
        if y < meteor_y + meteor_height:
            if (meteor_x > x and meteor_x < x + meteor_width) or \
               (meteor_x + meteor_width > x and meteor_x+ meteor_width < x + fight_width):
                crash()


        if y < heart_y + heart_height:
            if (heart_x > x and heart_x < x + fight_width) or \
               (heart_x + heart_width > x and heart_x+ heart_width < x + fight_width):
                   if enemypassed >=1:                       
                       enemypassed -=1
                       heart_x = random.randrange(0, pad_width-heart_width)
                       heart_y = 0
                              
        if shotcount1+shotcount2 >= 16 :
            if y < missile1_y + missile1_height:
                if (missile1_x > x and missile1_x < x + missile1_width) or \
                    (missile1_x + missile1_width > x and missile1_x+ missile1_width < x + fight_width):
                        crash()                       
                       
       # 게이머 전투기2 가 적과 충돌했는지 체크
        if y1 < enemy_y + enemy_height:
            if (enemy_x > x1 and enemy_x < x1 + fight1_width) or \
               (enemy_x + enemy_width > x1 and enemy_x+ enemy_width < x1 + fight1_width):
                crash()

        if y1 < meteor_y + meteor_height:
            if (meteor_x > x1 and meteor_x < x1 + meteor_width) or \
               (meteor_x + meteor_width > x1 and meteor_x+ meteor_width < x1 + fight1_width):
                crash()                
    
        if y1 < heart_y + heart_height:
            if (heart_x > x1 and heart_x < x + fight1_width) or \
               (heart_x + heart_width > x1 and heart_x+ heart_width < x1 + fight1_width):
                   if enemypassed >=1:                       
                       enemypassed -=1
                       heart_x = random.randrange(0, pad_width-heart_width)
                       heart_y = 5
                       
        if shotcount1+shotcount2 >= 16 :
            if y1 < missile1_y + missile1_height:
                if (missile1_x > x1 and missile1_x < x1 + missile1_width) or \
                    (missile1_x + missile1_width > x1 and missile1_x+ missile1_width < x1 + fight1_width):
                        crash()       

        drawObject(fighter, x, y)
        drawObject(fighter1, x1, y1)
        

       # 전투기 무기 발사 구현
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]
                if shotcount1+shotcount2>=15:
                    if bxy[1] < enemyboss_y+ enemyboss_height-45 :
                        if bxy[0] > enemyboss_x and bxy[0] < enemyboss_x + enemyboss_width:
                            bullet_xy.remove(bxy)
                            enemyboss_hp -= 1
                            if enemyboss_hp == 0:
                                shotcount1 += 5
                                if shotcount2> shotcount1:
                                    gameclear2()
                                else:
                                    gameclear1()
                    if bxy[1] < enemy_y:
                        if bxy[0] > enemy_x-2 and bxy[0] < enemy_x + enemy_width+2:
                            bullet_xy.remove(bxy)
                            isShot1 = True
                            shotcount1 += 1
                    if bxy[1] < meteor_y:
                        if bxy[0] > meteor_x-2 and bxy[0] < meteor_x + meteor_width+2:
                            bullet_xy.remove(bxy)
                            meteor_hp -= 1
                            if meteor_hp ==0:
                                isShot2 = True
                                shotcount1 += 1
                if bxy[1] < enemy_y:
                    if bxy[0] > enemy_x-2 and bxy[0] < enemy_x + enemy_width+2:
                        if bxy in bullet_xy :
                            bullet_xy.remove(bxy)
                        else : pass
                        isShot1 = True
                        shotcount1 += 1
                if bxy[1] < meteor_y:
                    if bxy[0] > meteor_x-2 and bxy[0] < meteor_x + meteor_width+2:
                        if bxy in bullet_xy :
                            bullet_xy.remove(bxy)
                        else : 
                            pass                                                
                        meteor_hp -= 1
                        if meteor_hp ==0:
                            isShot2 = True
                            shotcount1 += 1
                

                
                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass

              
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)




        if len(bullet2_xy) != 0:
            for j, bxy2 in enumerate(bullet2_xy):
                bxy2[1] -= 7
                bullet2_xy[j][1] = bxy2[1]
                if shotcount2+shotcount1>=15:
                    if bxy2[1] < enemyboss_y+ enemyboss_height-45 :
                        if bxy2[0] > enemyboss_x-20 and bxy2[0] < enemyboss_x + enemyboss_width+20:
                            bullet2_xy.remove(bxy2)
                            enemyboss_hp -= 2
                            if enemyboss_hp <= 0:
                                shotcount2 += 5
                                if shotcount2> shotcount1:
                                    gameclear2()
                                else:
                                    gameclear1()
                            
                    if bxy2[1] < enemy_y:
                        if bxy2[0] > enemy_x-20 and bxy2[0] < enemy_x + enemy_width+20:
                            bullet2_xy.remove(bxy2)
                            isShot1 = True
                            shotcount2 += 1
                    if bxy2[1] < meteor_y:
                        if bxy2[0] > meteor_x-20 and bxy2[0] < meteor_x + meteor_width+20:
                            bullet2_xy.remove(bxy2)
                            meteor_hp -= 2
                            if meteor_hp <=0:
                                isShot2 = True
                                shotcount2 += 1
                if bxy2[1] < enemy_y:
                    if bxy2[0] > enemy_x-20 and bxy2[0] < enemy_x + enemy_width+20:
                        if bxy2 in bullet2_xy :
                            bullet2_xy.remove(bxy2)
                        else : 
                            pass                                                
                        isShot1 = True
                        shotcount2 += 1
                if bxy2[1] < meteor_y:
                    if bxy2[0] > meteor_x-20 and bxy2[0] < meteor_x + meteor_width+20:
                        if bxy2 in bullet2_xy :
                            bullet2_xy.remove(bxy2)
                        else : pass    
                        meteor_hp -= 2
                        if meteor_hp <=0:
                            isShot2 = True
                            shotcount2 += 1
                

                
                if bxy2[1] <= 0:
                    try:
                        bullet2_xy.remove(bxy2)
                    except:
                        pass

              
        if len(bullet2_xy) != 0:
            for bx2, by2 in bullet2_xy:
                drawObject(bullet2, bx2, by2)

        drawScore1(shotcount1)
        drawScore2(shotcount2)

        # 적 구현
        enemy_y += enemy_speed   
        heart_y += heart_speed
        meteor_y += meteor_speed
        missile1_y +=missile1_speed
        if enemy_y > pad_height:
            enemy_x = random.randrange(0, pad_width-enemy_width)
            enemy_y = 0
            enemypassed += 1           
        if heart_y > pad_height:
            heart_x = random.randrange(0, pad_width-heart_width)
            heart_y = 0
        if enemypassed == 3:
            gameover()
        drawPassed(enemypassed)        
        if  meteor_y > pad_height:
            meteor_x = random.randrange(0, pad_width-meteor_width)
            meteor_y = 0
            meteor_hp = 2
            enemypassed += 1
        if enemypassed == 3:
            gameover()
        drawPassed(enemypassed)
        if missile1_y > pad_height:
            missile1_x = random.randrange(0, pad_width-missile1_width)
            missile1_y = 0        
        if isShot1:
            destroySound=pygame.mixer.Sound(explosionSound[0]) 
            destroySound.play()
            enemy_speed += 0.5
            if enemy_speed >= 6:
                enemy_speed = 6                
            enemy_x = random.randrange(0, pad_width-enemy_width)
            enemy_y = 0 
            isShot1 = False 
        if isShot2:
            destroySound=pygame.mixer.Sound(explosionSound[1]) 
            destroySound.play()
            meteor_x = random.randrange(0, pad_width-meteor_width)
            meteor_y = 0   
            meteor_hp= 2                    
            isShot2 = False
            
           

        drawObject(enemy, enemy_x, enemy_y)
        drawObject(heart, heart_x, heart_y)    
        drawObject(meteor, meteor_x, meteor_y)
        if shotcount1+shotcount2 >= 15 :        
            drawObject(enemyboss, enemyboss_x, enemyboss_y)
            drawObject(missile1, missile1_x, missile1_y)
                
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, fighter, clock, fighter1,background
    global bullet, enemy , heart, meteor, missileSound, enemyboss, bullet2, missile1

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    background= pygame.image.load('background.png')
    fighter = pygame.image.load('valkyrie.png')
    fighter1 = pygame.image.load('battle1.png')
    enemy = pygame.image.load('enemy.png')
    bullet = pygame.image.load('bullet.png')
    bullet2 =pygame.image.load('bullet2.png')
    heart = pygame.image.load('heart.png')
    meteor= pygame.image.load('meteor.png')
    missile1= pygame.image.load('missile1.png')
    enemyboss=pygame.image.load('enemyboss1.png')
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)
    missileSound= pygame.mixer.Sound("missile.wav")     
    clock = pygame.time.Clock()   



initGame()
runGame()
