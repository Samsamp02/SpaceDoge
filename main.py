import pygame, time, random
pygame.font.init()

pygame.init
WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")
PLAYER_HEIGHT = 40 
PLAYER_WIDTH = 60
PLAYER_SPEED = 5
FONT = pygame.font.SysFont("comicsans", 30)
STAR_WIDTH = 40
STAR_HEIGHT = 150
STAR_SPEED = 7

def draw(Player, TimeElapsed, Stars):
    WINDOW.fill((20, 30, 45))
    
    TimeText = FONT.render(f"Time: {int(TimeElapsed)}s", 1, "white")
    WINDOW.blit(TimeText, (10,10))

    pygame.draw.rect(WINDOW, "orange", Player)

    for Star in Stars:
        pygame.draw.rect(WINDOW, (90,90,90), Star)
        
    pygame.display.update()

def lose():
    LostText = FONT.render("Game Over", 1, "white")
    WINDOW.blit(LostText, (WIDTH/2 - LostText.get_width()/2, HEIGHT/2 - LostText.get_height()/2))
    pygame.display.update()
    pygame.time.delay(500)

    RestartText = FONT.render(f"Restarting in 5 seconds", 1, "white")
    WINDOW.blit(RestartText, (WIDTH/2 - RestartText.get_width()/2, HEIGHT/2 - LostText.get_height()/2 + 50))
    pygame.display.update()
    pygame.time.wait(5000)

    main()




def main():
    run = True
   
    player = pygame.Rect(15, (HEIGHT-PLAYER_HEIGHT)/2, PLAYER_WIDTH, PLAYER_HEIGHT )
    clock = pygame.time.Clock()

    TimeStart = time.time()
    TimeElapsed = 0
    AddStarIncrement = 2000#ms
    StarCount = 0
    Stars = []
    hit = False


    while run:
        StarCount += clock.tick(60)
        TimeElapsed = time.time() - TimeStart

        if StarCount >= AddStarIncrement:
            for i in range(3):
                StarY = random.randint(0, HEIGHT - STAR_HEIGHT)
                Star = pygame.Rect(WIDTH, StarY, STAR_WIDTH, STAR_HEIGHT)
                Stars.append(Star)

            StarCount = 0
            AddStarIncrement = max(200, AddStarIncrement-50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                break
        
        keys = pygame.key.get_pressed() 
      
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - PLAYER_SPEED >= 0:
            player.y -= PLAYER_SPEED 
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + PLAYER_SPEED <= 800-PLAYER_HEIGHT:
            player.y += PLAYER_SPEED
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - PLAYER_SPEED >= 0:
            player.x -= PLAYER_SPEED
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + PLAYER_SPEED <= 1000-PLAYER_WIDTH:
            player.x += PLAYER_SPEED
        

        for Star in Stars[:]:
            Star.x -= STAR_SPEED
            if Star.x > WIDTH:
                Stars.remove(Star)
            elif Star.x + Star.height >= player.x and Star.colliderect(player):
                Stars.remove(Star)
                hit = True
                break

        if hit:
            lose()
            break
            
        draw(player, TimeElapsed, Stars)
        
    pygame.quit()

if __name__ == "__main__":
    main()