import sys
sys.setrecursionlimit(10000)

with open('/Users/jesse/Desktop/python_code/coding_quest_2024/9(1).txt','r')as f:
   lines = f.readlines()
floor1 = [[lines[i][j] for j in range(len(lines[0])-1)] for i in range(len(lines))] 

with open('/Users/jesse/Desktop/python_code/coding_quest_2024/9(2).txt','r')as f:
   lines = f.readlines()
floor2 = [[lines[i][j] for j in range(len(lines[0])-1)] for i in range(len(lines))] 

start = [0,0]
end = [len(lines),len(lines[0])-1]

def next(x,y,floor,down):

   if (x == 19 and y == 20 and floor == floor1):
      floor[x][y] = 'F'
      return

   directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
   if x == 0: directions.remove((-1,0))
   if y == 0: directions.remove((0,-1))
   if x == 20: directions.remove((1,0))
   if y == 20: directions.remove((0,1))

   if isinstance(floor[x][y],int):
      d = floor[x][y]
   else:
      d = 0
   if (floor[x][y] != '$'):floor[x][y] = d

   if down == False:
      for i in directions:
         if floor[x+i[0]][y+i[1]] == '$':
            g=False
            for j in directions:
               if (isinstance(floor[(x+i[0])+j[0]][(y+i[1])+j[1]],int) and floor[(x+i[0])+j[0]][(y+i[1])+j[1]] > 1):
                  g = True
            if g == False:
               d+=1
               # floor1[x+i[0]][y+i[1]] = 1
               # floor2[x+i[0]][y+i[1]] = 1

            if floor == floor1:
               next(x+i[0],y+i[1],floor2,False)
            else:
               next(x+i[0],y+i[1],floor1,False)
            
            

      for i in directions:
         if floor[x+i[0]][y+i[1]] == '.':
            d+=1
            if (floor[x][y] != '$'):floor[x][y] = d
       
      for i in directions:
         if floor[x+i[0]][y+i[1]] == '.':
            next(x+i[0],y+i[1],floor,False)
            d = floor[x][y]
      
      if d == 0:
         for i in directions:
            if isinstance(floor[x+i[0]][y+i[1]],int) and floor[x+i[0]][y+i[1]] > 0:
               next(x+i[0],y+i[1],floor,True)
      
   else:
      if (d > 0): d-=1

   if (floor[x][y] != '$'):floor[x][y] = d

lengths = [] 
r = False

def search(x,y,floor,count):
   global r
   print(x,y,floor[x][y])
   if (isinstance(floor[x][y],int)):floor[x][y] -= 1
   if (floor[x][y] == 'F'):
   #if x == 1 and y == 1:# and r == True and floor == floor1:
      print("hi")
      lengths.append(count)
      return 
   else:
      directions = [(1, 0), (-1, 0),(0, 1),(0,-1)]
   # if x == 1: directions.remove((-1,0))
   # if y == 0: directions.remove((0,-1))
   # if x == 19: directions.remove((1,0))
   # if y == 20: directions.remove((0,1))

   r = True

   for i in directions:
         if floor[x+i[0]][y+i[1]] == '$':
            print("switch",x,y)
            if floor == floor1:
               search(x+i[0],y+i[1],floor2,count)
            else:
               search(x+i[0],y+i[1],floor1,count)
         
         if (isinstance(floor[x+i[0]][y+i[1]],int) and floor[x+i[0]][y+i[1]] > 0) or floor[x+i[0]][y+i[1]] == 'F' or floor[x+i[0]][y+i[1]] == '$':
            count+=1
            directions.remove(i)
            search(x+i[0],y+i[1],floor,count)
            

next(1,1,floor1,False)
#search(1,1,floor1,0)

sum = 0

for i in floor1:
   print(i)
   for j in i:
      if j == 1:
         sum+=1
print("")

for i in floor2:
   print(i)
   for j in i:
      if j == 1:
         sum+=1
print(sum)
print(lengths)