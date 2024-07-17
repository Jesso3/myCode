from cmu_graphics import*
app.red=252
app.green=3
app.blue=3
app.b1=2
app.g1=2
app.r1=2

snake = Circle(200,200,15,fill='lime')

def onStep():
    if(app.red>250)and(app.green<250)and(app.blue<10):
        app.g1=1
        
    elif(app.red<10)and(app.green>10)and(app.blue>250):
        app.g1=3
    else:
        app.g1=2
        
    if(app.red>10)and(app.green>250)and(app.blue<10):
        app.r1=3
    
    elif(app.red<250)and(app.green<10)and(app.blue>250):
        app.r1=1
    else:
        app.r1=2
        
    if(app.red<10)and(app.green>250)and(app.blue<250):
        app.b1=1
    elif(app.red>250)and(app.green<10)and(app.blue>10):
        app.b1=3
    else:
        app.b1=2
    
    
    if(app.r1==1):
        app.red+=5
    elif(app.r1==3):
        app.red-=5
        
    if(app.b1==1):
        app.blue+=5
    elif(app.b1==3):
        app.blue-=5
        
    if(app.g1==1):
        app.green+=5
    elif(app.g1==3):
        app.green-=5
        
        
    snake.fill=rgb(app.red,app.green,app.blue)



body = []
_score = Label('Score:',50,15,size = 30)
score = Label(0,115,15,size = 30)
def applePosition():
    appleX = randrange(40,380)
    appleY = randrange(40,380)
    while appleX%20!= 0:
        appleX = randrange(40,380)
    while appleY%20!= 0:
        appleY = randrange(40,380)
    for i in body:
        if i.hits(appleX,appleY):
            appleX = randrange(40,380)
            appleY = randrange(40,380)
            while appleX%20!= 0:
                appleX = randrange(40,380)
            while appleY%20!= 0:
                appleY = randrange(40,380)
    return appleX,appleY
apple_x, apple_y = applePosition()
apple = Circle(apple_x,apple_y,15,fill = 'red')
snake.length = 1
xPos = [200]
yPos = [200]
app.stepsPerSecond = 10
speed = 20
snake.dx=speed
snake.dy=0
app.step = 0
def onKeyPress(key):
    if key == 'up' or key == 'w':
        snake.dy = -speed
        snake.dx = 0
    elif key == 'right' or key == 'd':
        snake.dx = speed
        snake.dy = 0
    elif key == 'down' or key == 's':
        snake.dy = speed
        snake.dx = 0
    elif key =='left' or key == 'a':
        snake.dx = -speed
        snake.dy = 0
def onStep():
    if(app.red>250)and(app.green<250)and(app.blue<10):
        app.g1=1
        
    elif(app.red<10)and(app.green>10)and(app.blue>250):
        app.g1=3
    else:
        app.g1=2
        
    if(app.red>10)and(app.green>250)and(app.blue<10):
        app.r1=3
    
    elif(app.red<250)and(app.green<10)and(app.blue>250):
        app.r1=1
    else:
        app.r1=2
        
    if(app.red<10)and(app.green>250)and(app.blue<250):
        app.b1=1
    elif(app.red>250)and(app.green<10)and(app.blue>10):
        app.b1=3
    else:
        app.b1=2
    
    
    if(app.r1==1):
        app.red+=10
    elif(app.r1==3):
        app.red-=10
        
    if(app.b1==1):
        app.blue+=10
    elif(app.b1==3):
        app.blue-=10
        
    if(app.g1==1):
        app.green+=10
    elif(app.g1==3):
        app.green-=10
    

    snake.fill=rgb(app.red,app.green,app.blue)    
    for i in body: 
        i.fill=rgb(app.red,app.green,app.blue)
    app.step+=1
    xPos.append(snake.centerX)
    yPos.append(snake.centerY)
    snake.centerX+=snake.dx
    snake.centerY+=snake.dy

    if snake.left<0 or snake.right>400 or snake.top<0 or snake.bottom>400: app.stop()
    if snake.hitsShape(apple):
        snake.length+=1
        score.value+=1
        body.append(Circle(xPos[app.step-2],yPos[app.step-2],15,fill='lime'))
        apple_x,apple_y = applePosition()
        apple.centerX = apple_x
        apple.centerY = apple_y
    for i in range(len(body)):
        body[i].centerX = xPos[app.step-i]
        body[i].centerY = yPos[app.step-i]
    for i in body:
        if snake.centerX == i.centerX and snake.centerY == i.centerY:
            app.stop()
    
    
cmu_graphics.run()