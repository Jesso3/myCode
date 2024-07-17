from cmu_graphics import*
app.background = gradient('midnightBlue', 'dodgerBlue', start='top')


platform = Rect(-50,150,300,300,fill=gradient('grey','gainsboro',start='top-left'))
ball = Circle(100,130,20,fill='crimson')
speed=5
def onStep():
    global speed
    def Jump(sped):
        platform.rotateAngle-=sped
        ball.bottom=platform.top
        
    
    Jump(speed)
    speed+=0.05
cmu_graphics.run()