import pygame
import sys
import random

# initialize the constructor
pygame.init()
res = (720, 720)

# Randomly assigns a value to variables
c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Colox Game") # Tambahan caption window
clock = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color_list = [red, green, blue]

colox_c1 = 0
colox_c2 = 0
colox_c3 = 254
colox_c4 = 254

# Player color
player_c = random.choice(color_list)

# Colors for buttons
startl = (169, 169, 169)
startd = (100, 100, 100)
white = (255, 255, 255)
start = (255, 255, 255)

width = screen.get_width()
height = screen.get_height()

# Initial position variables (Global)
lead_x = 40
lead_y = height / 2
x = 300
y = 290
width1 = 100
height1 = 40
enemy_size = 50

# Fonts
smallfont = pygame.font.SysFont('Corbel', 35)

# Game Texts
text = smallfont.render('Start', True, white)
text1 = smallfont.render('Options', True, white)
exit1 = smallfont.render('Exit', True, white)
colox = smallfont.render('Colox', True, (c3, c2, c1))

x1 = random.randint(int(width / 2), width)
y1 = random.randint(100, int(height / 2))
x2 = 40
y2 = 40
speed = 15
count = 0

# Enemy positions
e_p = [width, random.randint(50, height - 50)]
e1_p = [random.randint(width, width + 100), random.randint(50, height - 100)]


def game_over():
    while True:
        # FIX 1: Ambil posisi mouse di AWAL loop
        mouse1 = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Tombol Exit di Game Over
                if 100 < mouse1[0] < 140 and height - 100 < mouse1[1] < height - 80:
                    pygame.quit()
                    sys.exit()

                # Tombol Restart
                if width - 180 < mouse1[0] < width - 100 and height - 100 < mouse1[1] < height - 80:
                    # Reset variable posisi musuh saat restart agar tidak langsung menabrak
                    e_p[0] = width
                    e1_p[0] = width + 100
                    # Panggil game dengan parameter yang benar (X dulu, baru Y)
                    game(lead_x, lead_y, 15, 0)

        screen.fill((65, 25, 64))
        
        # Font definitions local to function
        over_font = pygame.font.SysFont('Corbel', 60)
        btn_font = pygame.font.SysFont('Corbel', 25)
        
        game_over_text = over_font.render('GAME OVER', True, white)
        game_exit_text = btn_font.render('exit', True, white)
        restart_text = btn_font.render('restart', True, white)

        # Draw Buttons (Hover Effect)
        # Exit Button Logic
        if 100 < mouse1[0] < 140 and height - 100 < mouse1[1] < height - 80:
            pygame.draw.rect(screen, startl, [100, height - 100, 40, 20])
        else:
            pygame.draw.rect(screen, startd, [100, height - 100, 40, 20])

        # Restart Button Logic
        if width - 180 < mouse1[0] < width - 100 and height - 100 < mouse1[1] < height - 80:
            pygame.draw.rect(screen, startl, [width - 180, height - 100, 80, 20])
        else:
            pygame.draw.rect(screen, startd, [width - 180, height - 100, 80, 20])

        screen.blit(game_exit_text, (100, height - 100))
        screen.blit(restart_text, (width - 180, height - 100))
        screen.blit(game_over_text, (width / 2 - 150, 295))

        pygame.display.update()


# FIX 2: Ubah urutan parameter jadi (curr_lead_x, curr_lead_y) biar standar
def game(curr_lead_x, curr_lead_y, curr_speed, curr_count):

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            curr_lead_y -= 10
        if keys[pygame.K_DOWN]:
            curr_lead_y += 10

        screen.fill((65, 25, 64))
        clock.tick(curr_speed)

        # Draw Player
        pygame.draw.rect(screen, player_c, [curr_lead_x, curr_lead_y, 40, 40])
        
        # Draw Borders
        pygame.draw.rect(screen, (c1, c2, c3), [0, 0, width, 40])
        pygame.draw.rect(screen, (c3, c2, c1), [0, height - 40, width, 40])
        
        # Exit Button in Game
        mouse = pygame.mouse.get_pos()
        if width - 100 < mouse[0] < width and 0 < mouse[1] < 40:
            pygame.draw.rect(screen, startl, [width - 100, 0, 100, 40])
            if pygame.mouse.get_pressed()[0]: # Check click
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, startd, [width - 100, 0, 100, 40])
            
        exit_text_game = smallfont.render('Exit', True, white)
        screen.blit(exit_text_game, (width - 80, 5))

        # --- Enemy Logic ---
        
        # Enemy 1 Movement
        if e_p[0] > 0 and e_p[0] <= width:
            e_p[0] -= 10
        else:
            if e_p[1] <= 40 or e_p[1] >= height - 40:
                e_p[1] = height / 2
            e_p[1] = random.randint(enemy_size, height - enemy_size)
            e_p[0] = width

        # Enemy 2 Movement
        if e1_p[0] > 0 and e1_p[0] <= width + 100:
            e1_p[0] -= 10
        else:
            if e1_p[1] <= 40 or e1_p[1] >= height - 40:
                e1_p[1] = height / 2
            e1_p[1] = random.randint(enemy_size, height - 40)
            e1_p[0] = width + 100

        # Draw Enemies
        pygame.draw.rect(screen, red, [e_p[0], e_p[1], enemy_size, enemy_size])
        pygame.draw.rect(screen, blue, [e1_p[0], e1_p[1], enemy_size, enemy_size])

        # --- Collision Detection ---
        
        # Collision with Enemy 1 (Red)
        if curr_lead_x <= e_p[0] <= curr_lead_x + 40 and curr_lead_y <= e_p[1] <= curr_lead_y + 40:
             game_over()
        # Cek sudut tabrakan lain (bounding box simple)
        player_rect = pygame.Rect(curr_lead_x, curr_lead_y, 40, 40)
        enemy1_rect = pygame.Rect(e_p[0], e_p[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy1_rect):
            game_over()

        # Collision with Enemy 2 (Blue) - Passing through gives points?
        # Logika asli Anda agak unik: nabrak biru nambah point? 
        # Saya asumsikan ini koin/bonus karena nambah count.
        # Jika ini musuh, harusnya game over. Jika ini bonus, kodenya:
        
        player_rect = pygame.Rect(curr_lead_x, curr_lead_y, 40, 40)
        enemy2_rect = pygame.Rect(e1_p[0], e1_p[1], enemy_size, enemy_size)
        
        if player_rect.colliderect(enemy2_rect):
            e1_p[0] = width + 100
            e1_p[1] = random.randint(40, height - 40)
            curr_count += 1
            curr_speed += 1
            
        if curr_count >= 45:
            curr_speed = 60

        # Border Collision
        if curr_lead_y <= 40 or curr_lead_y >= height - 40 - 40: # -40 untuk ukuran player
            game_over()

        # Score display
        score_text = smallfont.render('Score: ' + str(curr_count), True, white)
        screen.blit(score_text, (width - 150, height - 40))
        
        pygame.display.update()


def intro():
    # Menggunakan global variables untuk animasi warna teks
    global colox_c1, colox_c2
    
    intro_loop = True
    while intro_loop:
        mouse = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Start Button Click
                if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
                    game(lead_x, lead_y, speed, count)
                # Quit Button Click
                if x < mouse[0] < x + width1 and y + 140 < mouse[1] < y + 140 + height1:
                    pygame.quit()
                    sys.exit()

        screen.fill((65, 25, 64))

        # --- Button Drawings ---
        # Start Button
        if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
            pygame.draw.rect(screen, startl, [x, y, width1, height1])
        else:
            pygame.draw.rect(screen, startd, [x, y, width1, height1])
            
        # Options Button (Placeholder)
        if x < mouse[0] < x + width1 + 40 and y + 70 < mouse[1] < y + 70 + height1:
             pygame.draw.rect(screen, startl, [x, y + 70, width1 + 40, height1])
        else:
             pygame.draw.rect(screen, startd, [x, y + 70, width1 + 40, height1])
             
        # Exit Button
        if x < mouse[0] < x + width1 and y + 140 < mouse[1] < y + 140 + height1:
            pygame.draw.rect(screen, startl, [x, y + 140, width1, height1])
        else:
            pygame.draw.rect(screen, startd, [x, y + 140, width1, height1])

        # --- Color Breezing Effect ---
        if 0 <= colox_c1 <= 254 or 0 <= colox_c2 <= 254:
            colox_c1 += 1
            colox_c2 += 1
        if colox_c1 >= 254 or colox_c2 >= 254:
            colox_c1 = c3
            colox_c2 = c3

        # Decoration Side Bars
        pygame.draw.rect(screen, (c2, colox_c1, colox_c2), [0, 0, 40, height])
        pygame.draw.rect(screen, (c2, colox_c1, colox_c2), [width - 40, 0, 40, height])

        # Text Rendering
        sig = smallfont.render('Designed by :- Antriksh', True, white)
        title_text = smallfont.render('Colox', True, (c1, colox_c1, colox_c2))
        
        screen.blit(title_text, (312, 50))
        screen.blit(text, (x + 10, y + 5)) # Start
        screen.blit(text1, (x + 10, y + 75)) # Options
        screen.blit(exit1, (x + 10, y + 145)) # Exit
        screen.blit(sig, (320, height - 50))

        clock.tick(60)
        pygame.display.update()

# Start the game
intro()