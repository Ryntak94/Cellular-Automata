import pygame, random, math, random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

pygame.init()

curr_state = [0]*625
# curr_state[54+79] = 1
# curr_state[55+79] = 1
# curr_state[56+79] = 1
# curr_state[60+79] = 1
# curr_state[61+79] = 1
# curr_state[62+79] = 1
# curr_state[102+79] = 1
# curr_state[107+79] = 1
# curr_state[109+79] = 1
# curr_state[114+79] = 1
# curr_state[127+79] = 1
# curr_state[132+79] = 1
# curr_state[134+79] = 1
# curr_state[139+79] = 1
# curr_state[152+79] = 1
# curr_state[157+79] = 1
# curr_state[159+79] = 1
# curr_state[164+79] = 1
# curr_state[179+79] = 1
# curr_state[180+79] = 1
# curr_state[181+79] = 1
# curr_state[185+79] = 1
# curr_state[186+79] = 1
# curr_state[187+79] = 1
# curr_state[229+79] = 1
# curr_state[230+79] = 1
# curr_state[231+79] = 1
# curr_state[235+79] = 1
# curr_state[236+79] = 1
# curr_state[237+79] = 1
# curr_state[252+79] = 1
# curr_state[257+79] = 1
# curr_state[259+79] = 1
# curr_state[264+79] = 1
# curr_state[277+79] = 1
# curr_state[282+79] = 1
# curr_state[284+79] = 1
# curr_state[289+79] = 1
# curr_state[302+79] = 1
# curr_state[307+79] = 1
# curr_state[309+79] = 1
# curr_state[314+79] = 1
# curr_state[354+79] = 1
# curr_state[355+79] = 1
# curr_state[356+79] = 1
# curr_state[360+79] = 1
# curr_state[361+79] = 1
# curr_state[362+79] = 1
for i in range(625):
    curr_state[i] = random.randint(0, 1)
original = curr_state
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE+100)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# text renders
font = pygame.font.SysFont("arial", 24)
selected = "paused"
paused = False
tps = 5
generationNum = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    hold = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos[0])
            print(pos[1])
            if pos[0] > 0 and pos[0] <= 125 and pos[1] > WIN_SIZE:
                    if selected == "paused":
                        paused = True
                        selected = "resume"
                    else:
                        paused = False
                        selected = "paused"
            if pos[0] > 125 and pos[0] <= 250 and pos[1] > WIN_SIZE:
                tps = tps + 1
            if pos[0] > 250 and pos[0] <= 375 and pos[1] > WIN_SIZE:
                if tps > 1:
                    tps = tps - 1
            if pos[0] > 375 and pos[1] > WIN_SIZE:
                curr_state = original
                hold = True
                generationNum = 0





    # --- Game logic should go here
    next_state = [0]*625
    if paused == False and hold == False:
        for i in range(625):
            live = 0
            if i > 25:
                if curr_state[i-26] and math.floor((i-26)/25) < math.floor(i/25) and curr_state[i-26] == 1:
                    live = live + 1
            if i > 24:
                if curr_state[i-25] and curr_state[i-25] == 1:
                    live = live + 1
            if i > 23:
                if curr_state[i-24] and math.floor((i-24)/25) < math.floor(i/25) and curr_state[i-24] == 1:
                    live = live + 1
            if i > 0:
                if curr_state[i-1] and math.floor((i-1)/25) == math.floor(i/25) and curr_state[i-1] == 1:
                    live = live + 1
            if i < 624:
                if curr_state[i+1] and math.floor((i+1)/25) == math.floor(i/25) and curr_state[i+1] == 1:
                    live = live + 1
            if i < 601:
                if curr_state[i+24] and math.floor((i+24)/25) > math.floor(i/25) and curr_state[i+24] == 1:
                    live = live + 1
            if i < 600:
                if curr_state[i+25] and curr_state[i+25] == 1:
                    live = live + 1
            if i < 599:
                if curr_state[i+26] and math.floor((i+26)/25) > math.floor(i/25) and curr_state[i+26] == 1:
                    live = live + 1
            if curr_state[i] == 1:
                if live < 2:
                    next_state[i] = 0
                if live > 3:
                    next_state[i] = 0
                if live == 2 or live == 3:
                    next_state[i] = 1
            else:
                if live == 3:
                    next_state[i] = 1
        curr_state = next_state
        generationNum = generationNum + 1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    for i in range(len(curr_state)):
        x = i
        while x > 24:
            x-=25
        x= x*20
        y = math.floor(i/25)
        y = y*20
        if curr_state[i] == 1:
            pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
        else:
            pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, WIN_SIZE,WIN_SIZE/4, 50))

    pause = font.render("Pause", True, BLACK)
    resume = font.render("Resume", True, BLACK)
    if selected == "paused":
        screen.blit(pause, (WIN_SIZE/12*.8, WIN_SIZE+12))
    else:
        screen.blit(resume, (WIN_SIZE/12*.5, WIN_SIZE+12))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(WIN_SIZE/4, WIN_SIZE,WIN_SIZE/4, 50))
    faster = font.render("Faster", True, BLACK)
    screen.blit(faster, (WIN_SIZE/12*3.75, WIN_SIZE+12))
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(WIN_SIZE/2, WIN_SIZE,WIN_SIZE/4, 50))
    slower = font.render("Slower", True, BLACK)
    screen.blit(slower, (WIN_SIZE/12*6.65, WIN_SIZE+12))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(WIN_SIZE/4*3, WIN_SIZE,WIN_SIZE/4, 50))
    restart = font.render("Restart", True, BLACK)
    screen.blit(restart, (WIN_SIZE/12*9.55, WIN_SIZE+12))
    pygame.draw.rect(screen, GRAY, pygame.Rect(0, WIN_SIZE+50,WIN_SIZE, 50))
    generations = font.render("Generations: " + str(generationNum), True, WHITE)
    screen.blit(generations, (WIN_SIZE/3-10, WIN_SIZE+62))
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(tps)

# Close the window and quit.
pygame.quit()
