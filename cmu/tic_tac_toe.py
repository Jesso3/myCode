from cmu_graphics import*

app.background='lightBlue'
grid = makeList(3,3)
spaces = Group()
rects = Group()
labels = Group()
turn = 'X'
plays = [None,None,None,None,None,None,None,None,None]

def checkWin(board,turn):
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]!=None:
            rects.clear()
            spaces.clear()
            labels.clear()
            return turn
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]!=None:
            rects.clear()
            spaces.clear()
            labels.clear()
            return turn
    if board[0]==board[4]==board[8]!=None:
        rects.clear()
        spaces.clear()
        labels.clear()
        return turn
    if board[2]==board[4]==board[6]!=None:
        rects.clear()
        spaces.clear()
        labels.clear()
        return turn
    return None    
for row in range(len(grid)):
    for col in range(len(grid)):
        spaces.add(Rect(50+100*row,50+100*col,100,100,fill='lightBlue',border='black',borderWidth=3))
        
def onMousePress(mouseX,mouseY):
    global turn
    for space in spaces:
        if space.hits(mouseX,mouseY)==True:
            rects.add(Rect(space.centerX-50,space.centerY-50,100,100,fill='lightBlue',border='black',borderWidth=3))
            labels.add(Label(turn,space.centerX,space.centerY,size=50))
            if space.centerY==100:
                if plays[((space.centerX+space.centerY)//100)-2]==None:
                    plays[((space.centerX+space.centerY)//100)-2]=turn
            elif space.centerY==200:
                if plays[((space.centerX+space.centerY)//100)]==None:
                    plays[((space.centerX+space.centerY)//100)]=turn
            elif space.centerY==300:
                if plays[((space.centerX+space.centerY)//100)+2]==None:
                    plays[((space.centerX+space.centerY)//100)+2]=turn
            
            winner = checkWin(plays,turn)
            if winner != None:
                Rect(0,0,400,400,fill='lightBlue')
                Label('The winner is '+winner+' !!',200,200,size=50)
                app.stop()
            if turn == 'X':
                turn = 'O'
            else:
                turn='X'
            
            spaces.remove(space)

cmu_graphics.run()