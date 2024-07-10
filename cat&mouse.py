import pgzrun
import random



WIDTH = 600
HEIGHT = 500

score=0
gameover=False
mouse = Actor("mouseimg")
cat = Actor("catimg")


mouse.x = random.randint(50,450)
mouse.y = random.randint(50,450)

cat.x = 300
cat.y = 250

def mouserandom():
    mouse.x = random.randint(50,450)
    mouse.y = random.randint(50,450)



def timer():
    global gameover
    gameover = True



def draw():
    global score
    screen.blit("backgroundimg",(0,0))
    cat.draw()
    mouse.draw()
    screen.draw.text(str(score),center = (575, 20), fontsize = 40)
    if gameover==True:
        screen.fill("black")
        screen.draw.text("Game Over! Your final score was "+str(score), center = (300,250), fontsize = 50, color = "red") 

def update():
    global score
    if keyboard.left and cat.x >-10 :
        cat.x = cat.x-2

    if keyboard.right and cat.x <600:
        cat.x = cat.x+2

    if keyboard.up and cat.y >-10:
        cat.y= cat.y-2

    if keyboard.down and cat.y <500:
        cat.y = cat.y+2
    
    if cat.colliderect(mouse):
        mouserandom()
        score=score+1
    
    for i in range (2):
        mouserandom()




clock.schedule(timer,20.0)
pgzrun.go()