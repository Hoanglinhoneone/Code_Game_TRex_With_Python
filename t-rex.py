#import thu vien
import random
import pygame

pygame.init()
clock = pygame.time.Clock()

#           Setup Ban Đầu:

# Tieu de
pygame.display.set_caption('T-REX OF PTITER')

# Cửa sổ game
# screen_width = 300
# screen_height = 600
screen = pygame.display.set_mode((600, 300)) # x = 600, y = 300. Tỉ lệ khung

#           Load tài nguyên ảnh:

# Mây
cloud1 = pygame.image.load(r'assets\cloud_1.png')
cloud2 = pygame.image.load(r'assets\cloud_2.png')
cloud3 = pygame.image.load(r'assets\cloud_3.png')

# Background
bg= pygame.image.load(r'assets\bg_near.png')
bg1 = pygame.image.load(r'assets\bg_far.png')

# Cây xương rồng
tree1 = pygame.image.load(r'assets\tree1.png') # ảnh 1 cây xương rồng
tree2 = pygame.image.load(r'assets\tree2.png') # Ảnh 1 cây xương rồng tb
tree3 = pygame.image.load(r'assets\tree3.png') # anh 1 cay xuong rong to
tree4 = pygame.image.load(r'assets\tree5.png')
tree5 = pygame.image.load(r'assets\tree6.png')
tree = [tree1, tree1, tree4, tree4, tree4, tree2, tree4, tree2, tree3, tree5, tree5, tree3, tree5, tree5]
tree1 = [tree5, tree5, tree2, tree4, tree4, tree4, tree3, tree5, tree3, tree2, tree2, tree1, tree4, tree4]

# Chim:
bird1 = pygame.image.load(r'assets\bird_1.png') # anh chim 1
bird2 = pygame.image.load(r'assets\bird_2.png') # Anh chim 2
bird3 = pygame.image.load(r'assets\bird_3.png') # Anh chim 2
bird4 = pygame.image.load(r'assets\bird_4.png') # Anh chim 2
bird5 = pygame.image.load(r'assets\bird_5.png') # Anh chim 2
bird6 = pygame.image.load(r'assets\bird_6.png') # Anh chim 2
bird7 = pygame.image.load(r'assets\bird_7.png') # Anh chim 2
bird8 = pygame.image.load(r'assets\bird_8.png') # Anh chim 2
fly = [bird1,bird1, bird2,bird2, bird3, bird3, bird4, bird4, bird5, bird5, bird6, bird6, bird7, bird7, bird8, bird8]

# Thiên thạch:
meteorite1 = pygame.image.load(r'assets\meteorite_3.png')
meteorite2 = pygame.image.load(r'assets\meteorite_5.png')
meteorite3 = pygame.image.load(r'assets\meteorite_6.png')
meteorite4 = pygame.image.load(r'assets\meteorite_7.png')
meteorite = [meteorite2]*3 + [meteorite4]*3
meteoriteone = [meteorite3]*3 + [meteorite4]*3

# Phi Tiêu:
phitieu1 = pygame.image.load(r'assets\kunai1.png')
phitieu2 = pygame.image.load(r'assets\kunai1_4.png')
phitieu = [phitieu1, phitieu1, phitieu1, phitieu2, phitieu2, phitieu2]

# Khủng Long
dino = pygame.image.load(r'assets\dino6.png') # Đứng yên
dinorun1 = pygame.image.load(r'assets\dino1.png') # Khủng long Run 1
dinorun2 = pygame.image.load(r'assets\dino2.png') # Khủng long Run 2
dinocui1 = pygame.image.load(r'assets\dino3.png') # Khủng long cúi 1
dinocui2 = pygame.image.load(r'assets\dino4.png') # Khủng long cúi 2
dinofake = pygame.image.load(r'assets\dino_fake.png')
walk = [dinorun1, dinorun1, dinorun1, dinorun1, dinorun2, dinorun2, dinorun2, dinorun2, dinorun2]
dinocuif1 = [dinocui1]*5
dinocuif2 = [dinocui2]*5
dinocui = dinocuif1+dinocuif2+dinocuif1+dinocuif2+dinocuif1+dinocuif2

# Coin fly:
coin1 = pygame.image.load(r'assets\coin_1.png')
coin2 = pygame.image.load(r'assets\coin_2.png')
coin3 = pygame.image.load(r'assets\coin_3.png')
coin4 = pygame.image.load(r'assets\coin_4.png')
coinf1 = [coin1]*10
coinf2 = [coin2]*10
coinf3 = [coin3]*10
coinf4 = [coin4]*10
coinxoay = coinf1 + coinf2 + coinf3 + coinf4

#Gun:
gun1 = pygame.image.load(r'assets\gun.png')
gun2 = pygame.image.load(r'assets\gun_1.png')
gun3 = pygame.image.load(r'assets\gun_2.png')
gun4 = pygame.image.load(r'assets\gun_3.png')
gun = [gun2]*3+[gun3]*3 + [gun4]*70

#Dép:
dep1 = pygame.image.load(r'assets\sandal.png')
dep2 = pygame.image.load(r'assets\sandal_2.png')
dep3 = pygame.image.load(r'assets\sandal_3.png')
dep4 = pygame.image.load(r'assets\sandal_4.png')
sandal = [dep1]*10+[dep2]*10+[dep3]*10+[dep4]*10

# Phun Lửa:
fire1 = pygame.image.load(r'assets\fire1.png')
fire2 = pygame.image.load(r'assets\fire2.png')
fire3 = pygame.image.load(r'assets\fire3.png')
fire4 = pygame.image.load(r'assets\fire4.png')
fire5 = pygame.image.load(r'assets\fire5.png')
fire7 = pygame.image.load(r'assets\fire7.png')
fireitem = pygame.image.load(r'assets\fire_item_2.png')
fire = [fire1]*3 + [fire2]*3 + [fire3]*3 + [fire4]*5 + [fire5]*5
item = [gun1, dep1, fireitem]

# Other items:
skull = pygame.image.load(r'assets\skull.png')
eggs = pygame.image.load(r'assets\eggs.png')
rock5 = pygame.image.load(r'assets\rock5.png')
randomitem = [skull, eggs, rock5, tree2, dinofake]


#        Load Âm Thanh
sound3 = pygame.mixer.Sound(r'sound\punch.mp3') # Lúc chết
sound5 = pygame.mixer.Sound(r'sound\quack_5.mp3') # Lúc nhảy

#          Biến khởi tạo:

# Toa Do BG
bg_x, bg_y = 0, 0
bg1_x, bg1_y = 0, 0
# Mây
cl_x, cl_y = 0.3, 0.3
cl1_x, cl1_y, cl2_x, cl2_y, cl3_x, cl3_y = 40, 20, 200, 70, 450, 30
# Điểm khi chơi
score, hscore, scorenow = 0, 0, 0
# Coinfly:
cntcoin = 3
coinpoint = 0
x_coin, y_coin = 600, 150
coinlen = False
flypoint = 0
# Thiên thạch
thienthach = False
x_da, y_da = 1200, -300
x_da1, y_da1 = 1200, -300
x_da2, y_da2 = 1200, -300
meteopoint = 0
# Tree
treepoint, tree1point = 0, 12
tree_x, tree_y = 600, 200 # toa do cay
tree1_x, tree1_y = 1200, 200
treeroi = False
tree1roi = False

# Dino T-rex:
dino_x, dino_y = 70, 190 # toa do t-rex
x_def, y_def = 6, 7
x_d, y_d = 3, 3
walkpoint, duckpoint = 0, 0
jump = False
cui = False
jump2 = False
checkjump2 = False
nhaydoi = False

# Chim
bird_x, bird_y = 1800, 100
baylen = True

#Phi Tieu
phitieupoint= 0
pt_x, pt_y = 1800, 159
x_pt = 8
phitieuroi = False

# Vật trang trí nền gần:
randompoint = 0
x_random, y_random = 350, 250

# Fire Gun, dép:
phun = False
nem = False
ban = False
cntfire = 3
firepoint = 0
x_fire, y_fire = 1200, 150
itempoint = 0
cntdep = 3
cntgun = 3
gunpoint = 0
deppoint = 0
x_gun = 80
x_dep, y_dep = 110, 190
roidep = False

# Run Game
gameplay = False
gameStartPlay = False

# Các Hàm check va chạm:
def checkvc():
    if cui:
        if (dinocui_hcn.colliderect(phitieu_hcn) or dino_hcn.colliderect(tree1_hcn) or dino_hcn.colliderect(bird_hcn) or
                dino_hcn.colliderect(tree_hcn) or dinocui_hcn.colliderect(meteorite_hcn) or
                dinocui_hcn.colliderect(meteorite2_hcn) or dinocui_hcn.colliderect(meteorite3_hcn)):
            # pygame.mixer.Sound.play(sound5)
            return False
        else:
            return True
    else:
        if (dino_hcn.colliderect(phitieu_hcn) or dino_hcn.colliderect(tree1_hcn) or dino_hcn.colliderect(bird_hcn) or
                dino_hcn.colliderect(tree_hcn) or dino_hcn.colliderect(meteorite_hcn) or
                dino_hcn.colliderect(meteorite2_hcn) or dino_hcn.colliderect(meteorite3_hcn)):
            # pygame.mixer.Sound.play(sound3)
            return False
        else:
            return True

def checkvcgun():
    if gun_hcn.colliderect(tree_hcn or tree1_hcn):
        return False
    return True
def checkvcnem():
    if nem_hcn.colliderect(tree_hcn) or nem_hcn.colliderect(tree1_hcn) or nem_hcn.colliderect(phitieu_hcn):
        return False
    return True
def checkvcnemtree():
    if nem_hcn.colliderect(tree_hcn):
        return True
    return False
def checkvcnemtree1():
    if nem_hcn.colliderect(tree1_hcn):
        return True
    return False
def checkvcbantree():
    if gun_hcn.colliderect(tree_hcn):
        return True
    return False
def checkvcbantree1():
    if gun_hcn.colliderect(tree1_hcn):
        return True
    return False
def checkvcPhunTree():
    if fire_hcn.colliderect(tree_hcn):
        return True
    return False
def checkvcPhunTree1():
    if fire_hcn.colliderect(tree1_hcn):
        return True
    return False
def checkvcnemphitieu():
    if nem_hcn.colliderect(phitieu_hcn):
        return True
    return False
def checkvccoin():
    if dino_hcn.colliderect(coin_hcn):
        return True
    return False

def checkvcitem():
    if dino_hcn.colliderect(item_hcn):
        return True
    return False

# Đưa TEXT Điểm Vào Game
game_font = pygame.font.Font('04B_19.TTF', 20)

# Hiện Thị Điểm
def score_view():
    if gameplay and gameStartPlay:
        gun_txt = game_font.render(f'GUN: {cntgun}' , True, (0, 0, 0))
        screen.blit(gun_txt, (370, 5))
        dep_txt = game_font.render(f'SANDAL: {cntdep}', True, (0, 0, 0))
        screen.blit(dep_txt, (470, 5))
        fire_txt = game_font.render(f'FIRE: {cntfire}', True, (0, 0 ,0))
        screen.blit(fire_txt, (270, 5))
        coin_txt = game_font.render(f'FLY : {cntcoin}', True, (0, 0, 0))
        screen.blit(coin_txt, (170, 5))
        score_txt = game_font.render(f'P: {int(score)}', True, (0, 0, 0))
        screen.blit(score_txt,(5, 28))
        score_max = game_font.render(f'MP: {int(hscore)}', True, (0, 0, 0))
        screen.blit(score_max, (5, 5))
    elif gameplay == False and gameStartPlay == True:
        score_txt = game_font.render(f'P: {int(scorenow)}', True, (0, 0 ,0))
        score_max = game_font.render(f'MP: {int(hscore)}', True, (0, 0, 0))
        screen.blit(score_txt, (250, 50))
        screen.blit(score_max, (233,70))
        over_txt = game_font.render(f'BAM SPACE DE CHOI LAI',True, (0, 0, 0))
        screen.blit(over_txt, (200, 110))
    elif gameStartPlay == False:
        start_txt = game_font.render(f'BAM SPACE DE CHOI GAME',True, (0, 0, 0))
        screen.blit(start_txt, (170, 120))


# Tạo Vòng Lặp Chạy Game:
running = True
while running:

    # Chỉnh Fps của game
    clock.tick(60)

    # Check Hành Vi Người Chơi
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # neu nguoi dung an nut thoat thi out
            running = False
        if event.type == pygame.KEYDOWN:
            # Nhảy
            if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and gameplay:
                if dino_y == 190 : # Kiem tra neu trex dang duoi san moi nhay
                    jump = True
                    # pygame.mixer.Sound.play(sound5)

            #Nhảy đôi
            if (event.key == pygame.K_d) and gameplay:
                if dino_y > 60 and dino_y < 190 and cntcoin >= 1:
                    jump2 = True
                    checkjump2 = True
                    # pygame.mixer.Sound.play(sound5)
            # Cúi người
            if (event.key == pygame.K_DOWN and gameplay):
                if jump == False and dino_y == 190:
                    cui = True
            # Phun lửa
            if (event.key == pygame.K_RIGHT):
                if jump == False and dino_y == 190 and cntfire >= 1:
                    phun = True
            #Bắn
            if(event.key == pygame.K_s):
                if jump == False and dino_y == 190 and cntgun >= 1:
                    ban = True
            #Ném
            if(event.key == pygame.K_LEFT):
                if jump == False and (dino_y == 190 or dino_y == 210) and cntdep >= 1:
                    nem = True
            # Chơi Lại
            if (event.key == pygame.K_SPACE) and gameplay == False and gameStartPlay == True:
                gameplay = True
            if (event.key== pygame.K_SPACE) and gameStartPlay == False:
                gameplay = True
                gameStartPlay = True
    if gameplay == True and gameStartPlay == True:
        # Background
        bg1_hcn = screen.blit(bg1, (bg1_x, bg1_y))
        bg_hcn = screen.blit(bg, (bg_x, bg_y))
        bg_x -= x_def
        if bg_x == -600: bg_x = 0
        bg11_hcn = screen.blit(bg, (bg_x + 600, bg_y))

        # random item nền gần:
        item_hcn = screen.blit(randomitem[randompoint], (x_random, y_random))
        x_random -= x_def
        if(x_random < -30):
            x_random = 600
            randompoint = random.randint(0, 4)
            y_random = random.randint(240, 260)

        # cloud: Mây chạy
        cl_hcn1 = screen.blit(cloud1, (cl1_x, cl1_y))
        cl1_x -= cl_x
        if(cl1_x < -30):
            cl1_x = 600
        cl_hcn2 = screen.blit(cloud2, (cl2_x, cl2_y))
        cl2_x -= cl_x
        if (cl2_x < -30):
            cl2_x = 600
        cl_hcn3 = screen.blit(cloud3, (cl3_x, cl3_y))
        cl3_x -= cl_x
        if (cl3_x < -50):
            cl3_x = 600

        # Vật cản
        tree_hcn = screen.blit(tree[treepoint], (tree_x, tree_y))
        if treeroi == True:
            tree_y += y_def
        else:
            tree_x -= x_def
        if(tree_x <= -1200):
            tree_x = 600
            treepoint = random.randint(0, 13)
        if(tree_y >= 600):
            treeroi = False
            tree_x = -70
            tree_y = 200
        tree1_hcn = screen.blit(tree1[tree1point], (tree1_x, tree1_y))
        if tree1roi == True:
            tree1_y += y_def
        else:
            tree1_x -= x_def
        if(tree1_x <= -600):
            tree1_x = 1200
            tree1point = random.randint(0, 13)
        if (tree1_y >= 600):
            tree1roi = False
            tree1_x = -70
            tree1_y = 200

        # Khủng Long
        # dino_hcn = screen.blit(dino, (dino_x, dino_y))
        # # dino_hcn2= screen.blit(dinorun2, (dino_x, dino_y))
        if(cui == True):
            dinocui_hcn = screen.blit(dinocui[duckpoint], (dino_x, 210 ))
            duckpoint += 1
            if duckpoint > 25:
                duckpoint = 0
                cui =False
        else:
            dino_hcn = screen.blit(walk[walkpoint], (dino_x, dino_y))
            walkpoint += 1
            if walkpoint > 8:
                walkpoint = 0
            if (dino_y >= 60 and jump):
                dino_y -= y_def
            else:
                jump = False
            if(dino_y >= 0 and jump2):
                dino_y -= y_def
            else:
                jump2 = False
            if dino_y < 190 and jump == False and jump2 == False:
                if(checkjump2):
                    cntcoin-=1
                    checkjump2 = False
                dino_y += y_def
        if phun == True:
            # Phun lửa:
            fire_hcn = screen.blit(fire[firepoint], (125, 195))
            firepoint += 1
            if checkvcPhunTree():
                treeroi = True
            if checkvcPhunTree1():
                tree1roi = True
            if firepoint > 18:
                firepoint = 0
                phun = False
                cntfire -= 1
        if ban == True:
            gun_hcn = screen.blit(gun[gunpoint], (x_gun, 200))
            gunpoint += 1
            x_gun += x_def
            if checkvcbantree():
                treeroi = True
                cntgun -= 1
                ban = False
                x_gun = 80
                gunpoint = 0
            if checkvcbantree1():
                tree1roi = True
                cntgun -= 1
                ban = False
                x_gun = 80
                gunpoint = 0
            if (gunpoint > 75):
                gunpoint = 0
                ban = False
                cntgun -= 1
                x_gun = 90
        if nem == True:
            nem_hcn = screen.blit(sandal[deppoint], (x_dep, y_dep))
            deppoint += 1

            # Vật cản rơi nếu chạm vào dép
            if (checkvcnemtree()):
                treeroi = True
            if (checkvcnemtree1()):
                tree1roi = True
            if (checkvcnemphitieu()):
                phitieuroi = True
            if checkvcnem() == False:
                roidep = True  # Kiểm tra tình trạng dép
            if roidep == False:
                x_dep += x_def  # nếu dép chưa va chạm thì vẫn bay đến hết tầm
            else:
                y_dep += y_def  # nếu ném trúng thì dép rơi
            if (deppoint > 39):
                deppoint = 0
                roidep = False  # Ném hết quãng thì cập nhật lại
                nem = False  #
                cntdep -= 1
                x_dep, y_dep = 110, 190
        if jump == True:
            phun = False

        # Bird:
        bird_hcn = screen.blit(fly[flypoint], (bird_x, bird_y))
        flypoint += 1
        if flypoint > 15:
            flypoint = 0
        bird_x -= x_def
        if baylen == True:
            bird_y -= 2
        else :
            bird_y += 2
        if bird_y <= 0:
            baylen = False
        if bird_y >= 70:
            baylen = True
        if bird_x < -20:
            bird_x = 1800
            bird_y = 70

        # Phi Tiêu:
        phitieu_hcn = screen.blit(phitieu[phitieupoint], (pt_x, pt_y))
        phitieupoint += 1
        if phitieupoint > 5:
            phitieupoint = 0
        if phitieuroi:
            pt_y -= y_def
        else:
            pt_x -= x_def
        if pt_x < -30 :
            pt_x = 1800
        if pt_y <= 0:
            phitieuroi = False
            pt_x = -25
            pt_y = 159

        #Coin:
        coin_hcn = screen.blit(coinxoay[coinpoint], (x_coin, y_coin))
        coinpoint += 1
        if coinpoint > 39:
            coinpoint = 0
        x_coin -= x_def
        if(x_coin < -600):
            x_coin = 600
            y_coin = random.randint(50, 190)
        if checkvccoin():
            x_coin = -50
            cntcoin+=1

        item_hcn = screen.blit(item[itempoint], (x_fire, y_fire))
        x_fire -= x_def
        if(x_fire < -1200):
            itempoint = random.randint(0,2)
            x_fire = 1200
            y_fire = random.randint(50, 190)
        if checkvcitem():
            x_fire = -50
            if itempoint == 0:
                cntgun += 1
            elif itempoint == 1:
                cntdep += 1
            else:
                cntfire += 1

        # Thiên Thạch rơi
        meteorite_hcn = screen.blit(meteorite[meteopoint], (x_da, y_da))
        meteopoint += 1
        if meteopoint > 5:
            meteopoint = 0
        # x_da -= 3
        # y_da += 1
        # if (x_da <= -50 or y_da >= 350):
        #     x_da, y_da = 1200, -300
        if score > 1000 and score < 1500:
            x_da -= 3
            y_da += 1
            if (x_da <= -50 or y_da >= 350):
                x_da, y_da = 1200, -300
        meteorite2_hcn = screen.blit(meteoriteone[meteopoint], (x_da1, y_da1))
        if score > 2000 and score < 2500:
            x_da1 -= 3
            y_da1 += 1
            if (x_da1 <= -50 or y_da1 >= 350):
                x_da1, y_da1 = 1200, -300
        meteorite3_hcn = screen.blit(meteorite1, (x_da2, y_da2))
        if score > 3000 and score < 3500:
            x_da2 -= 3
            y_da2 += 1
            if (x_da2 <= -50 or y_da2 >= 350):
                x_da2, y_da2 = 1200, -300
        score += 1
        scorenow =score
        if hscore < score:
            hscore = score
        gameplay = checkvc()
        score_view()

    elif gameplay == False and gameStartPlay == True: # Reset game sau khi chết:

        # BG
        bg_x, bg_y = 0, 0  # toa do bg
        bg1_x, bg1_y = 0, 0
        bg_far_hcn = screen.blit(bg1, (bg1_x, bg_y))
        bg_near_hcn = screen.blit(bg, (bg_x, bg_y))

        # Dino
        dino_x, dino_y = 70, 190 # toa do t-rex
        dino_hcn = screen.blit(dino, (dino_x, dino_y))

        # Tree
        tree_x, tree_y = 600, 200  # toa do cay
        tree1_x, tree1_y = 1200, 200
        treepoint = random.randint(0, 13)
        tree1point = random.randint(0, 13)
        tree_hcn = screen.blit(tree2, (tree_x, tree_y))
        tree3_hcn = screen.blit(tree3, (480, 200))
        tree2_hcn = screen.blit(tree2, (250, 250))

        # Mây :
        cloud1_hcn = screen.blit(cloud1, (500, 30))
        cloud2_hcn = screen.blit(cloud2, (300, 20))
        cloud3_hcn = screen.blit(cloud3, (30, 20))

        # rock + eggs:
        dinofake_hcn = screen.blit(dinofake, (350, 200))
        skull_hcn = screen.blit(skull, (350, 250))
        rock5_hcn = screen.blit(rock5, (460, 270))
        eggs_hcn = screen.blit(eggs, (400, 230))

        # meteorite:
        meteoritefake = screen.blit(meteorite1, (450, 50))

        pt_x, pt_y = 1200, 159
        bird_x, bird_y = 1800, 70
        score = 0
        score_view()
        x_def = 6
        cntcoin = 3
        cntfire = 3
        cntgun = 3
        cntdep = 3
        x_dep, y_dep = 110, 190
        x_da, y_da = 1200, -300
        x_da1, y_da1 = 1200, -300
        x_da2, y_da2 = 1200, -300
        x_gun = 80
        roidep = False
    elif gameStartPlay == False:
        # BG
        bg_x, bg_y = 0, 0  # toa do bg
        bg1_x, bg1_y = 0, 0
        bg_far_hcn = screen.blit(bg1, (bg1_x, bg_y))
        bg_near_hcn = screen.blit(bg, (bg_x, bg_y))

        # Dino
        dino_x, dino_y = 70, 190  # toa do t-rex
        dino_hcn = screen.blit(dino, (dino_x, dino_y))

        # Tree
        tree_x, tree_y = 600, 200  # toa do cay
        tree1_x, tree1_y = 1200, 200
        treepoint = random.randint(0, 13)
        tree1point = random.randint(0, 13)
        tree_hcn = screen.blit(tree2, (tree_x, tree_y))
        tree3_hcn = screen.blit(tree3, (480, 200))
        tree2_hcn = screen.blit(tree2, (250, 250))

        # Mây :
        cloud1_hcn = screen.blit(cloud1, (500, 30))
        cloud2_hcn = screen.blit(cloud2, (300, 20))
        cloud3_hcn = screen.blit(cloud3, (30, 20))

        # rock + eggs:
        dinofake_hcn = screen.blit(dinofake, (350, 200))
        skull_hcn = screen.blit(skull, (350, 250))
        rock5_hcn = screen.blit(rock5, (460, 270))
        eggs_hcn = screen.blit(eggs, (400, 230))

        # meteorite:
        meteoritefake = screen.blit(meteorite1, (450, 50))

        pt_x, pt_y = 1200, 159
        bird_x, bird_y = 1800, 70
        score = 0
        score_view()
        x_def = 6
        cntcoin = 3
        cntfire = 3
        cntgun = 3
        cntdep = 3
        x_dep, y_dep = 110, 190
        x_da, y_da = 1200, -300
        x_da1, y_da1 = 1200, -300
        x_da2, y_da2 = 1200, -300
        x_gun = 80
        roidep = False

    pygame.display.update()



