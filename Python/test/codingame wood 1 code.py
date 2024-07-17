



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
crystals=[]
eggs=[]
base=[]
neigh=[]
base_neigh=[]
base_neigh_2=[]
base_neigh_3=[]
base_neigh_4=[]
base_neigh_5=[]
_resources=[]
egg_resources=[]
base_resources=[]
exploring_tiles=[]
stop=False

amount_neigh=0
go=-1
res=False
move=''
number_of_cells = int(input())  # amount of hexagonal cells in this map

mants = [0] * number_of_cells
oants = [0] * number_of_cells

for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    neigh+=[neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]
    if _type==1 or _type==2:
        _resources.append(initial_resources)
    else:
        _resources.append(0)
    if _type==1:
        egg_resources.append(initial_resources)
    else:
        egg_resources.append(0)
    
    if _type==1 and i not in eggs:
        eggs.append(i)
    if _type==2 and i not in crystals:
        crystals.append(i)
    

            
number_of_bases = int(input())
for i in input().split():
    my_base_index = int(i)
    if my_base_index not in base:
        base.append(my_base_index)
for i in input().split():
    opp_base_index = int(i)

def find_neighbours(_tile,_list):
    if _list=='no':
        return [neigh[_tile*6],neigh[_tile*6+1],neigh[_tile*6+2],neigh[_tile*6+3],neigh[_tile*6+4],neigh[_tile*6+5]]
    else:
        _list+=[neigh[_tile*6],neigh[_tile*6+1],neigh[_tile*6+2],neigh[_tile*6+3],neigh[_tile*6+4],neigh[_tile*6+5]]

find_neighbours(base[0],base_neigh)
find_neighbours(base[0],exploring_tiles)
for i in base_neigh:
    base_resources+=[_resources[i]]


for i in base_neigh:
    if i != -1 and i not in base_neigh_2:
        find_neighbours(i,base_neigh_2)
        find_neighbours(i,exploring_tiles)
for i in base_neigh_2:
    if i != -1 and i not in base_neigh_3:
        find_neighbours(i,base_neigh_3)
        find_neighbours(i,exploring_tiles)
for i in base_neigh_3:
    if i != -1 and i not in base_neigh_4:
        find_neighbours(i,base_neigh_4)
        find_neighbours(i,exploring_tiles)
for i in base_neigh_4:
    if i != -1 and i != base[0]:
        find_neighbours(i,exploring_tiles)



def make_move(start,end):
    
    move=''
    if end==go:
        for j in crystals:
            move+="LINE {} {} {} ;".format(start,j,1)
        for j in eggs:
            move+="LINE {} {} {} ;".format(start,j,1)
    else:
        move+="LINE {} {} {} ;".format(start,end,1)
    print(move)
    move=''

def remove(i,resource):
    if i in eggs and resource<=0:
        eggs.remove(i)
        
    if i in crystals and resource<=0:
        crystals.remove(i)


# game loop
while True:  
    
    for i in range(number_of_cells):
        
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        for k in range(number_of_cells):
            resources,my_ants, opp_ants = [int(j) for j in input().split()]
            _resources[k]=resources
            if k in eggs:
                egg_resources[k]=resources
            mants[k]=my_ants
            oants[k]=opp_ants
           
            # Print the cell index and its corresponding resources
        for j in crystals:
            if _resources[j]<1:
                crystals.remove(j)
        for j in eggs:
            if _resources[j]<1:
                eggs.remove(j)

        for j in crystals:
            if mants[j]>=_resources[j]:
                _resources[j]-=mants[j]+oants[j]
                crystals.remove(j) 
                stop=True
                make_move(base[0],go)
                
                   
        for j in eggs:
            if mants[j]+oants[j]>=_resources[j]:
                _resources[j]-=mants[j]+oants[j]
                egg_resources[j]-=mants[j]+oants[j]
                
                eggs.remove(j) 
                stop=True  
                make_move(base[0],go)

        for j in base_neigh:
            if egg_resources[j]>0 and j!=-1 and stop==False:
                move+="LINE {} {} {} ;".format(base[0],j,1)
                _resources[j]-=mants[j]+oants[j]
                egg_resources[j]-=mants[j]+oants[j]
            
                
                               
        if move!='':
            print(move)
            move=''
        else:
            make_move(base[0],go)
            move=''
            for j in crystals:
                _resources[j]-=mants[j]+oants[j]
                
            for j in eggs:
                _resources[j]-=mants[j]+oants[j]
                egg_resources[j]-=mants[j]+oants[j]
                

                
           
        
             
       
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
