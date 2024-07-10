import pgzrun
import random



WIDTH = 600
HEIGHT = 500

score=0
gameover=False
bee = Actor("beeimg")
flower = Actor("flowerimg")
cat = Actor("catimg")
mouse = Actor("mouseimg")

flower.x = random.randint(50,450)
flower.y = random.randint(50,450)

bee.x = 300
bee.y = 250

def flowerrandom():
    flower.x = random.randint(50,450)
    flower.y = random.randint(50,450)

def timer():
    global gameover
    gameover = True



def draw():
    global score
    screen.blit("backgroundimg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(str(score),center = (575, 20), fontsize = 40)
    if gameover==True:
        screen.fill("black")
        screen.draw.text("Game Over! Your final score was "+str(score), center = (300,250), fontsize = 50, color = "red") 

def update():
    global score
    if keyboard.left and bee.x >-10 :
        bee.x = bee.x-2

    if keyboard.right and bee.x <600:
        bee.x = bee.x+2

    if keyboard.up and bee.y >-10:
        bee.y= bee.y-2

    if keyboard.down and bee.y <500:
        bee.y = bee.y+2
    
    if bee.colliderect(flower):
        flowerrandom()
        score=score+1



clock.schedule(timer,20.0)
pgzrun.go()