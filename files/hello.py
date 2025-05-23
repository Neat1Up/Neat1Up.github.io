import sys, pygame
import random
pygame.init()
clock = pygame.time.Clock()

width = 640
height = 360

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Game of Games")

cyanframe = pygame.image.load("cyanframe.png")
grass = pygame.image.load("grassbackground.png")
titlescreen = pygame.image.load("titlegameofgames.png")
playmenubutton = pygame.image.load("playbutton.png")
rulesbutton = pygame.image.load("rulesbutton.png")
rules = pygame.image.load("rules.png")
nextbutton = pygame.image.load("nextbutton.png")
backbutton = pygame.image.load("backbutton.png")
redball = pygame.image.load("redball.png")
blueball = pygame.image.load("blueball.png")
gameover = pygame.image.load("gameover.png")
levelup = pygame.image.load("levelup.png")
congrats = pygame.image.load("congrats.png")

updatedcyanframe = pygame.transform.scale(cyanframe, (cyanframe.get_width() // 2, cyanframe.get_height() // 2))
updatedgrass = pygame.transform.scale(grass, (grass.get_width() // 2, grass.get_height() // 2))
updatedtitle = pygame.transform.scale(titlescreen, (titlescreen.get_width() // 2, titlescreen.get_height() // 2))
updatedmenuplay = pygame.transform.scale(playmenubutton, (playmenubutton.get_width() // 2, playmenubutton.get_height() // 2))
updatedrules = pygame.transform.scale(rulesbutton, (rulesbutton.get_width() // 2, rulesbutton.get_height() // 2))
updaterule1 = pygame.transform.scale(rules, (rules.get_width() // 2, rules.get_height() // 2))
updatednextbutton = pygame.transform.scale(nextbutton, (nextbutton.get_width() // 2, nextbutton.get_height() // 2))
updatedbackbutton = pygame.transform.scale(backbutton, (backbutton.get_width() // 2, backbutton.get_height() // 2))
updatedredball = pygame.transform.scale(redball, (redball.get_width() // 2, redball.get_height() // 2))
updatedblueball = pygame.transform.scale(blueball, (blueball.get_width() // 2, blueball.get_height() // 2))
updatedgameover = pygame.transform.scale(gameover, (gameover.get_width() // 2, gameover.get_height() // 2))
updatedlevelup = pygame.transform.scale(levelup, (levelup.get_width() // 2, levelup.get_height() // 2))
updatedcongrats = pygame.transform.scale(congrats, (congrats.get_width() // 2, congrats.get_height() // 2))

menuplaybuttoncoordx = 100
menuplaybuttoncoordy = 200
menuplaybuttonwidth = updatedmenuplay.get_width()
menuplaybuttonheight = updatedmenuplay.get_height()

menuplayrect = pygame.Rect(menuplaybuttoncoordx, menuplaybuttoncoordy, menuplaybuttonwidth, menuplaybuttonheight)

rulesbuttoncoordx = 400
rulesbuttoncoordy = 200
rulesbuttonwidth = updatedrules.get_width()
rulesbuttonheight = updatedrules.get_height()

rulesrect = pygame.Rect(rulesbuttoncoordx, rulesbuttoncoordy, rulesbuttonwidth, rulesbuttonheight)

screen.blit(updatedgrass, (0, 0))
screen.blit(updatedcyanframe, (0, 0))
screen.blit(updatedtitle, ((width // 2) - (titlescreen.get_width() // 4), (height // 2) - (titlescreen.get_height() // 4)))
screen.blit(updatedmenuplay, (100, 200))
screen.blit(updatedrules, (400, 200))
menuscreen = True
rulesscreen = False
ruleslide = 1

running = True

def game_code():

    screen.blit(updatedgrass, (0, 0))
    screen.blit(updatedcyanframe, (0, 0))

    balls = [updatedredball, updatedblueball]
    directions = ["horizontal", "vertical"]
    randomy = [30, 130, 230]
    randomx = [30, 120, 255, 385, 510]
    ball1visible = True
    imageisset = False
    ball_count = 0
    loopcounter = 0

    GAME_SCORE = 0
    GAME_TIMER = 50

    randomball = balls[random.randint(0, 1)]
    randomdirection = directions[random.randint(0, 1)]
    ycoord = randomy[random.randint(0, 2)]
    xcoord = randomx[random.randint(0, 4)]
    ball_rect = randomball.get_rect()
    if randomdirection == "horizontal":
        ball_rect.topleft = (0, ycoord)
    elif randomdirection == "vertical":
        ball_rect.topleft = (xcoord, 0)
    speedx = 7.5
    speedy = 7.5
    imageisonscreen = True
    gameisrunning = True

    textfont = pygame.font.Font(None, 36)

    while gameisrunning == True:
        loopcounter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameisrunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball1visible == True and ball_rect.collidepoint(event.pos):
                    randomball = balls[random.randint(0, 1)]
                    randomdirection = directions[random.randint(0, 1)]
                    ycoord = randomy[random.randint(0, 2)]
                    xcoord = randomx[random.randint(0, 4)]
                    ball_rect = randomball.get_rect()

                    if randomdirection == "horizontal":
                        ball_rect.topleft = (0, ycoord)
                    elif randomdirection == "vertical":
                        ball_rect.topleft = (xcoord, 0)

                    GAME_SCORE += 1

        screen.blit(updatedgrass, (0, 0))
        screen.blit(updatedcyanframe, (0, 0))

        if randomdirection == "horizontal":
            ball_rect.x += speedx
            if ball_rect.right > width or ball_rect.left < 0:
                imageisonscreen = False
                GAME_SCORE -= 1
        elif randomdirection == "vertical":
            ball_rect.y += speedy
            if ball_rect.bottom > height or ball_rect.top < 0:
                imageisonscreen = False
                GAME_SCORE -= 1

        screen.blit(randomball, ball_rect)

        BLACK = (0, 0, 0)

        score = textfont.render(f"Score: {GAME_SCORE}/40", True, BLACK)
        timer = textfont.render(f"Time: {GAME_TIMER}", True, BLACK)

        screen.blit(score, (100, 0))
        screen.blit(timer, (400, 0))

        if imageisonscreen == False:
            randomball = balls[random.randint(0, 1)]
            randomdirection = directions[random.randint(0, 1)]
            ycoord = randomy[random.randint(0, 2)]
            xcoord = randomx[random.randint(0, 4)]
            ball_rect = randomball.get_rect()

            if randomdirection == "horizontal":
                ball_rect.topleft = (0, ycoord)
            elif randomdirection == "vertical":
                ball_rect.topleft = (xcoord, 0)
            imageisonscreen = True

        if loopcounter == 60:
            GAME_TIMER -= 1
            loopcounter = 0

        if GAME_SCORE < 0 or GAME_TIMER < 0:
            game_over("onfirstlevel")
            gameisrunning = False

        if GAME_SCORE == 40:
            levelup("beatfirstlevel")
            gameisrunning = False

        pygame.display.flip()
        clock.tick(60)

def game_code2():

    screen.blit(updatedgrass, (0, 0))
    screen.blit(updatedcyanframe, (0, 0))

    balls = [updatedredball, updatedblueball]
    directions = ["horizontal", "vertical"]
    randomy = [30, 130, 230]
    randomx = [30, 120, 255, 385, 510]
    ball1visible = True
    imageisset = False
    ball_count = 0
    loopcounter = 0

    GAME_SCORE = 1
    GAME_TIMER = 60

    randomball = balls[random.randint(0, 1)]
    randomdirection = directions[random.randint(0, 1)]
    ycoord = randomy[random.randint(0, 2)]
    xcoord = randomx[random.randint(0, 4)]
    ball_rect = randomball.get_rect()
    if randomdirection == "horizontal":
        ball_rect.topleft = (0, ycoord)
    elif randomdirection == "vertical":
        ball_rect.topleft = (xcoord, 0)
    speedx = 8.75
    speedy = 8.75
    imageisonscreen = True
    gameisrunning = True

    textfont = pygame.font.Font(None, 36)

    while gameisrunning == True:
        loopcounter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameisrunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball1visible == True and ball_rect.collidepoint(event.pos):
                    randomball = balls[random.randint(0, 1)]
                    randomdirection = directions[random.randint(0, 1)]
                    ycoord = randomy[random.randint(0, 2)]
                    xcoord = randomx[random.randint(0, 4)]
                    ball_rect = randomball.get_rect()

                    if randomdirection == "horizontal":
                        ball_rect.topleft = (0, ycoord)
                    elif randomdirection == "vertical":
                        ball_rect.topleft = (xcoord, 0)

                    GAME_SCORE += 1

        screen.blit(updatedgrass, (0, 0))
        screen.blit(updatedcyanframe, (0, 0))

        if randomdirection == "horizontal":
            ball_rect.x += speedx
            if ball_rect.right > width or ball_rect.left < 0:
                imageisonscreen = False
                GAME_SCORE -= 1
        elif randomdirection == "vertical":
            ball_rect.y += speedy
            if ball_rect.bottom > height or ball_rect.top < 0:
                imageisonscreen = False
                GAME_SCORE -= 1

        screen.blit(randomball, ball_rect)

        BLACK = (0, 0, 0)

        score = textfont.render(f"Score: {GAME_SCORE}/50", True, BLACK)
        timer = textfont.render(f"Time: {GAME_TIMER}", True, BLACK)

        screen.blit(score, (100, 0))
        screen.blit(timer, (400, 0))

        if imageisonscreen == False:
            randomball = balls[random.randint(0, 1)]
            randomdirection = directions[random.randint(0, 1)]
            ycoord = randomy[random.randint(0, 2)]
            xcoord = randomx[random.randint(0, 4)]
            ball_rect = randomball.get_rect()

            if randomdirection == "horizontal":
                ball_rect.topleft = (0, ycoord)
            elif randomdirection == "vertical":
                ball_rect.topleft = (xcoord, 0)
            imageisonscreen = True

        if loopcounter == 60:
            GAME_TIMER -= 1
            loopcounter = 0

        if GAME_SCORE < 0 or GAME_TIMER < 0:
            game_over("onsecondlevel")
            gameisrunning = False

        if GAME_SCORE == 50:
            levelup("beatsecondlevel")
            gameisrunning = False

        pygame.display.flip()
        clock.tick(60)

def game_code3():

    screen.blit(updatedgrass, (0, 0))
    screen.blit(updatedcyanframe, (0, 0))

    balls = [updatedredball, updatedblueball]
    directions = ["horizontal", "vertical"]
    randomy = [30, 130, 230]
    randomx = [30, 120, 255, 385, 510]
    ball1visible = True
    imageisset = False
    ball_count = 0
    loopcounter = 0

    GAME_SCORE = 2
    GAME_TIMER = 70

    randomball = balls[random.randint(0, 1)]
    randomdirection = directions[random.randint(0, 1)]
    ycoord = randomy[random.randint(0, 2)]
    xcoord = randomx[random.randint(0, 4)]
    ball_rect = randomball.get_rect()
    if randomdirection == "horizontal":
        ball_rect.topleft = (0, ycoord)
    elif randomdirection == "vertical":
        ball_rect.topleft = (xcoord, 0)
    speedx = 10
    speedy = 10
    imageisonscreen = True
    gameisrunning = True

    textfont = pygame.font.Font(None, 36)

    while gameisrunning == True:
        loopcounter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameisrunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball1visible == True and ball_rect.collidepoint(event.pos):
                    randomball = balls[random.randint(0, 1)]
                    randomdirection = directions[random.randint(0, 1)]
                    ycoord = randomy[random.randint(0, 2)]
                    xcoord = randomx[random.randint(0, 4)]
                    ball_rect = randomball.get_rect()

                    if randomdirection == "horizontal":
                        ball_rect.topleft = (0, ycoord)
                    elif randomdirection == "vertical":
                        ball_rect.topleft = (xcoord, 0)

                    GAME_SCORE += 1

        screen.blit(updatedgrass, (0, 0))
        screen.blit(updatedcyanframe, (0, 0))

        if randomdirection == "horizontal":
            ball_rect.x += speedx
            if ball_rect.right > width or ball_rect.left < 0:
                imageisonscreen = False
                GAME_SCORE -= 1
        elif randomdirection == "vertical":
            ball_rect.y += speedy
            if ball_rect.bottom > height or ball_rect.top < 0:
                imageisonscreen = False
                GAME_SCORE -= 1

        screen.blit(randomball, ball_rect)

        BLACK = (0, 0, 0)

        score = textfont.render(f"Score: {GAME_SCORE}/60", True, BLACK)
        timer = textfont.render(f"Time: {GAME_TIMER}", True, BLACK)

        screen.blit(score, (100, 0))
        screen.blit(timer, (400, 0))

        if imageisonscreen == False:
            randomball = balls[random.randint(0, 1)]
            randomdirection = directions[random.randint(0, 1)]
            ycoord = randomy[random.randint(0, 2)]
            xcoord = randomx[random.randint(0, 4)]
            ball_rect = randomball.get_rect()

            if randomdirection == "horizontal":
                ball_rect.topleft = (0, ycoord)
            elif randomdirection == "vertical":
                ball_rect.topleft = (xcoord, 0)
            imageisonscreen = True

        if loopcounter == 60:
            GAME_TIMER -= 1
            loopcounter = 0

        if GAME_SCORE < 0 or GAME_TIMER < 0:
            game_over("onthirdlevel")
            gameisrunning = False

        if GAME_SCORE == 60:
            levelup("beatthirdlevel")
            gameisrunning = False

        pygame.display.flip()
        clock.tick(60)

def game_over(levelon: str):
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(updatedgrass, (0, 0))
        screen.blit(updatedcyanframe, (0, 0))
        screen.blit(updatedgameover, ((width // 2) - (updatedgameover.get_width() // 2), (height // 2) - (updatedgameover.get_height() // 2)))
        screen.blit(updatedmenuplay, ((width // 2) - (updatedmenuplay.get_width() // 2), 270))

        menuplaybuttoncoordx = (width // 2) - (updatedmenuplay.get_width() // 4)
        menuplaybuttoncoordy = 270
        menuplaybuttonwidth = updatedmenuplay.get_width()
        menuplaybuttonheight = updatedmenuplay.get_height()

        menuplayrect = pygame.Rect(menuplaybuttoncoordx, menuplaybuttoncoordy, menuplaybuttonwidth, menuplaybuttonheight)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuplayrect.collidepoint(event.pos) and menuscreen == True:
                    if levelon == "onfirstlevel":
                        game_code()
                        running = False
                    elif levelon == "onsecondlevel":
                        game_code2()
                        running = False
                    elif levelon == "onthirdlevel":
                        game_code3()
                    running = False
                    game_code()

        pygame.display.flip()
        clock.tick(60)

def levelup(levelbeaten: str):
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if levelbeaten == "beatthirdlevel":
                screen.blit(updatedgrass, (0, 0))
                screen.blit(updatedcyanframe, (0, 0))
                screen.blit(updatedcongrats, ((width // 2) - (updatedcongrats.get_width() // 2), (height // 2) - (updatedcongrats.get_height() // 2)))
            else:
                screen.blit(updatedgrass, (0, 0))
                screen.blit(updatedcyanframe, (0, 0))
                screen.blit(updatedlevelup, ((width // 2) - (updatedlevelup.get_width() // 2), (height // 2) - (updatedlevelup.get_height() // 2)))
                screen.blit(updatedmenuplay, ((width // 2) - (updatedmenuplay.get_width() // 2), 270))

                menuplaybuttoncoordx = (width // 2) - (updatedmenuplay.get_width() // 4)
                menuplaybuttoncoordy = 270
                menuplaybuttonwidth = updatedmenuplay.get_width()
                menuplaybuttonheight = updatedmenuplay.get_height()

                menuplayrect = pygame.Rect(menuplaybuttoncoordx, menuplaybuttoncoordy, menuplaybuttonwidth, menuplaybuttonheight)

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if menuplayrect.collidepoint(event.pos) and menuscreen == True:
                            if levelbeaten == "beatfirstlevel":
                                game_code2()
                                running = False
                            elif levelbeaten == "beatsecondlevel":
                                game_code3()
                                running = False
                            else:
                                game_code()
                                running = False

        pygame.display.flip()
        clock.tick(60)

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuplayrect.collidepoint(event.pos) and menuscreen == True:
                game_code()
                running = False
            if rulesrect.collidepoint(event.pos):
                screen.blit(updaterule1, (0, 0))
                screen.blit(updatedcyanframe, (0, 0))
                screen.blit(updatedbackbutton, (200, 260))

                menuscreen = False
                rulesscreen = True

        if rulesscreen == True:
            backbuttoncoordx = 200
            backbuttoncoordy = 260
            backbuttonwidth = updatedbackbutton.get_width()
            backbuttonheight = updatedbackbutton.get_height()

            backbuttonrect = pygame.Rect(backbuttoncoordx, backbuttoncoordy, backbuttonwidth, backbuttonheight)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbuttonrect.collidepoint(event.pos) and rulesscreen == True:
                    screen.blit(updatedgrass, (0, 0))
                    screen.blit(updatedcyanframe, (0, 0))
                    screen.blit(updatedtitle, ((width // 2) - (titlescreen.get_width() // 4), (height // 2) - (titlescreen.get_height() // 4)))
                    screen.blit(updatedmenuplay, (100, 200))
                    screen.blit(updatedrules, (400, 200))
                    menuscreen = True
                    rulesscreen = False
                    ruleslide = 1
    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()