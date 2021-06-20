import copy
import random
import cProfile #for timing measure purpose 
u="Up"
f="Front"
r="Right"
l="Left"
b="Back"
d="Down"

raw_Cube={
    "Front":['r' for _ in range(9)],
    "Right":['g' for _ in range(9)],
    "Left":['b' for _ in range(9)],
    "Back":['o' for _ in range(9)],
    "Up":['y' for _ in range(9)],
    "Down":['w' for _ in range(9)]
}
cube=copy.deepcopy(raw_Cube)
 

def Scramble():    
    for i in range(20):
        choice=random.randint(1,14)
        if choice==1:
            R()
        elif choice==2:
            Ri()
        elif choice==3:
            U()
        elif choice==4:
            Ui()
        elif choice==5:
            L()
        elif choice==6:
            Li()
        elif choice==7:
            F()
        elif choice==8:
            Fi()
        elif choice==9:
            B()
        elif choice==10:
            Bi()
        elif choice==11:
            D()
        elif choice==12:
            Di()
        elif choice==13:
            X()
        elif choice==14:
            Y()
######################
def R():
    t_cube=copy.deepcopy(cube)
    #RRRRRRRRRRRRRR
    cube[r][0]=t_cube[r][6]
    cube[r][1]=t_cube[r][3]
    cube[r][2]=t_cube[r][0]
    cube[r][3]=t_cube[r][7]
    cube[r][4]=t_cube[r][4]
    cube[r][5]=t_cube[r][1]
    cube[r][6]=t_cube[r][8]
    cube[r][7]=t_cube[r][5]
    cube[r][8]=t_cube[r][2]

    cube[f][2]=t_cube[d][2]
    cube[f][5]=t_cube[d][5]
    cube[f][8]=t_cube[d][8]

    cube[u][2]=t_cube[f][2]
    cube[u][5]=t_cube[f][5]
    cube[u][8]=t_cube[f][8]

    cube[b][2]=t_cube[u][2]
    cube[b][5]=t_cube[u][5]
    cube[b][8]=t_cube[u][8]

    cube[d][2]=t_cube[b][2]
    cube[d][5]=t_cube[b][5]
    cube[d][8]=t_cube[b][8]
    return cube

def Ri():
    t_cube=copy.deepcopy(cube)
    #R'R'R'R'R'R'R'R'R'R'R'
    cube[r][0]=t_cube[r][2]
    cube[r][1]=t_cube[r][5]
    cube[r][2]=t_cube[r][8]
    cube[r][3]=t_cube[r][1]
    cube[r][4]=t_cube[r][4]
    cube[r][5]=t_cube[r][7]
    cube[r][6]=t_cube[r][0]
    cube[r][7]=t_cube[r][3]
    cube[r][8]=t_cube[r][6]

    cube[f][2]=t_cube[u][2]
    cube[f][5]=t_cube[u][5]
    cube[f][8]=t_cube[u][8]

    cube[u][2]=t_cube[b][2]
    cube[u][5]=t_cube[b][5]
    cube[u][8]=t_cube[b][8]

    cube[b][2]=t_cube[d][2]
    cube[b][5]=t_cube[d][5]
    cube[b][8]=t_cube[d][8]

    cube[d][2]=t_cube[f][2]
    cube[d][5]=t_cube[f][5]
    cube[d][8]=t_cube[f][8]
    return cube
#######################
def U():
    t_cube=copy.deepcopy(cube)
    #UUUUUUUUUUU
    cube[u][0]=t_cube[u][6]
    cube[u][1]=t_cube[u][3]
    cube[u][2]=t_cube[u][0]
    cube[u][3]=t_cube[u][7]
    cube[u][4]=t_cube[u][4]
    cube[u][5]=t_cube[u][1]
    cube[u][6]=t_cube[u][8]
    cube[u][7]=t_cube[u][5]
    cube[u][8]=t_cube[u][2]

    cube[f][0]=t_cube[r][0]
    cube[f][1]=t_cube[r][1]
    cube[f][2]=t_cube[r][2]

    cube[l][0]=t_cube[f][0]
    cube[l][1]=t_cube[f][1]
    cube[l][2]=t_cube[f][2]

    cube[b][8]=t_cube[l][0]
    cube[b][7]=t_cube[l][1]
    cube[b][6]=t_cube[l][2]
    
    cube[r][0]=t_cube[b][8]
    cube[r][1]=t_cube[b][7]
    cube[r][2]=t_cube[b][6]
    return cube

def Ui():
    t_cube=copy.deepcopy(cube)
    #U'U'U'U'U'U'U'U''U'U'U'
    cube[u][0]=t_cube[u][2]
    cube[u][1]=t_cube[u][5]
    cube[u][2]=t_cube[u][8]
    cube[u][3]=t_cube[u][1]
    cube[u][4]=t_cube[u][4]
    cube[u][5]=t_cube[u][7]
    cube[u][6]=t_cube[u][0]
    cube[u][7]=t_cube[u][3]
    cube[u][8]=t_cube[u][6]

    cube[f][0]=t_cube[l][0]
    cube[f][1]=t_cube[l][1]
    cube[f][2]=t_cube[l][2]

    cube[l][0]=t_cube[b][8]
    cube[l][1]=t_cube[b][7]
    cube[l][2]=t_cube[b][6]

    cube[b][8]=t_cube[r][0]
    cube[b][7]=t_cube[r][1]
    cube[b][6]=t_cube[r][2]
    
    cube[r][0]=t_cube[f][0]
    cube[r][1]=t_cube[f][1]
    cube[r][2]=t_cube[f][2]
    return cube
#######################
def L():
    
    t_cube=copy.deepcopy(cube)
    #LLLLLLLLLLLL
    cube[l][0]=t_cube[l][6]
    cube[l][1]=t_cube[l][3]
    cube[l][2]=t_cube[l][0]
    cube[l][3]=t_cube[l][7]
    cube[l][4]=t_cube[l][4]
    cube[l][5]=t_cube[l][1]
    cube[l][6]=t_cube[l][8]
    cube[l][7]=t_cube[l][5]
    cube[l][8]=t_cube[l][2]

    cube[f][0]=t_cube[u][0]
    cube[f][3]=t_cube[u][3]
    cube[f][6]=t_cube[u][6]

    cube[u][0]=t_cube[b][0]
    cube[u][3]=t_cube[b][3]
    cube[u][6]=t_cube[b][6]

    cube[b][0]=t_cube[d][0]
    cube[b][3]=t_cube[d][3]
    cube[b][6]=t_cube[d][6]
    
    cube[d][0]=t_cube[f][0]
    cube[d][3]=t_cube[f][3]
    cube[d][6]=t_cube[f][6]
    return cube

def Li():
    t_cube=copy.deepcopy(cube)
    #L'L'L'L'L'L'L'L'L'L'L'
    cube[l][0]=t_cube[l][2]
    cube[l][1]=t_cube[l][5]
    cube[l][2]=t_cube[l][8]
    cube[l][3]=t_cube[l][1]
    cube[l][4]=t_cube[l][4]
    cube[l][5]=t_cube[l][7]
    cube[l][6]=t_cube[l][0]
    cube[l][7]=t_cube[l][3]
    cube[l][8]=t_cube[l][6]

    cube[f][0]=t_cube[d][0]
    cube[f][3]=t_cube[d][3]
    cube[f][6]=t_cube[d][6]

    cube[u][0]=t_cube[f][0]
    cube[u][3]=t_cube[f][3]
    cube[u][6]=t_cube[f][6]

    cube[b][0]=t_cube[u][0]
    cube[b][3]=t_cube[u][3]
    cube[b][6]=t_cube[u][6]
    
    cube[d][0]=t_cube[b][0]
    cube[d][3]=t_cube[b][3]
    cube[d][6]=t_cube[b][6]
    return cube
#######################
def D():
    t_cube=copy.deepcopy(cube)
    #DDDDDDDDDDDDDDDD
    cube[d][0]=t_cube[d][6]
    cube[d][1]=t_cube[d][3]
    cube[d][2]=t_cube[d][0]
    cube[d][3]=t_cube[d][7]
    cube[d][4]=t_cube[d][4]
    cube[d][5]=t_cube[d][1]
    cube[d][6]=t_cube[d][8]
    cube[d][7]=t_cube[d][5]
    cube[d][8]=t_cube[d][2]

    cube[f][6]=t_cube[l][6]
    cube[f][7]=t_cube[l][7]
    cube[f][8]=t_cube[l][8]

    cube[r][6]=t_cube[f][6]
    cube[r][7]=t_cube[f][7]
    cube[r][8]=t_cube[f][8]

    cube[b][2]=t_cube[r][6]
    cube[b][1]=t_cube[r][7]
    cube[b][0]=t_cube[r][8]
    
    cube[l][6]=t_cube[b][2]
    cube[l][7]=t_cube[b][1]
    cube[l][8]=t_cube[b][0]
    return cube

def Di():
    t_cube=copy.deepcopy(cube)
    #D'D'D'D'D'D'D'D'D'D'D'D'D'D'D'D'
    cube[d][0]=t_cube[d][2]
    cube[d][1]=t_cube[d][5]
    cube[d][2]=t_cube[d][8]
    cube[d][3]=t_cube[d][1]
    cube[d][4]=t_cube[d][4]
    cube[d][5]=t_cube[d][7]
    cube[d][6]=t_cube[d][0]
    cube[d][7]=t_cube[d][3]
    cube[d][8]=t_cube[d][6]

    cube[f][6]=t_cube[r][6]
    cube[f][7]=t_cube[r][7]
    cube[f][8]=t_cube[r][8]

    cube[r][6]=t_cube[b][2]
    cube[r][7]=t_cube[b][1]
    cube[r][8]=t_cube[b][0]

    cube[b][2]=t_cube[l][6]
    cube[b][1]=t_cube[l][7]
    cube[b][0]=t_cube[l][8]
    
    cube[l][6]=t_cube[f][6]
    cube[l][7]=t_cube[f][7]
    cube[l][8]=t_cube[f][8]
    return cube
#######################
def F():
    t_cube=copy.deepcopy(cube)
    #FFFFFFFFFFFFFFFFF
    cube[f][0]=t_cube[f][6]
    cube[f][1]=t_cube[f][3]
    cube[f][2]=t_cube[f][0]
    cube[f][3]=t_cube[f][7]
    cube[f][4]=t_cube[f][4]
    cube[f][5]=t_cube[f][1]
    cube[f][6]=t_cube[f][8]
    cube[f][7]=t_cube[f][5]
    cube[f][8]=t_cube[f][2]

    cube[u][6]=t_cube[l][8]
    cube[u][7]=t_cube[l][5]
    cube[u][8]=t_cube[l][2]

    cube[l][8]=t_cube[d][2]
    cube[l][5]=t_cube[d][1]
    cube[l][2]=t_cube[d][0]

    cube[d][2]=t_cube[r][0]
    cube[d][1]=t_cube[r][3]
    cube[d][0]=t_cube[r][6]
    
    cube[r][0]=t_cube[u][6]
    cube[r][3]=t_cube[u][7]
    cube[r][6]=t_cube[u][8]
    return cube

def Fi():
    t_cube=copy.deepcopy(cube)
    #F'F'F'F'F''F'F'F'F'F'F'F'F'F'F'F'F'
    cube[f][0]=t_cube[f][2]
    cube[f][1]=t_cube[f][5]
    cube[f][2]=t_cube[f][8]
    cube[f][3]=t_cube[f][1]
    cube[f][4]=t_cube[f][4]
    cube[f][5]=t_cube[f][7]
    cube[f][6]=t_cube[f][0]
    cube[f][7]=t_cube[f][3]
    cube[f][8]=t_cube[f][6]

    cube[u][6]=t_cube[r][0]
    cube[u][7]=t_cube[r][3]
    cube[u][8]=t_cube[r][6]

    cube[l][8]=t_cube[u][6]
    cube[l][5]=t_cube[u][7]
    cube[l][2]=t_cube[u][8]

    cube[d][2]=t_cube[l][8]
    cube[d][1]=t_cube[l][5]
    cube[d][0]=t_cube[l][2]
    
    cube[r][0]=t_cube[d][2]
    cube[r][3]=t_cube[d][1]
    cube[r][6]=t_cube[d][0]
    return cube
#######################
def B():
    t_cube=copy.deepcopy(cube)
    #BBBBBBBBBBBBB
    cube[b][0]=t_cube[b][6]
    cube[b][1]=t_cube[b][3]
    cube[b][2]=t_cube[b][0]
    cube[b][3]=t_cube[b][7]
    cube[b][4]=t_cube[b][4]
    cube[b][5]=t_cube[b][1]
    cube[b][6]=t_cube[b][8]
    cube[b][7]=t_cube[b][5]
    cube[b][8]=t_cube[b][2]

    cube[u][0]=t_cube[r][2]
    cube[u][1]=t_cube[r][5]
    cube[u][2]=t_cube[r][8]

    cube[l][6]=t_cube[u][0]
    cube[l][3]=t_cube[u][1]
    cube[l][0]=t_cube[u][2]

    cube[d][8]=t_cube[l][6]
    cube[d][7]=t_cube[l][3]
    cube[d][6]=t_cube[l][0]
    
    cube[r][2]=t_cube[d][8]
    cube[r][5]=t_cube[d][7]
    cube[r][8]=t_cube[d][6]
    return cube

def Bi():
    t_cube=copy.deepcopy(cube)
    #B'B'B'B'B'B'B'B'B'B'B'B'B'
    cube[b][0]=t_cube[b][2]
    cube[b][1]=t_cube[b][5]
    cube[b][2]=t_cube[b][8]
    cube[b][3]=t_cube[b][1]
    cube[b][4]=t_cube[b][4]
    cube[b][5]=t_cube[b][7]
    cube[b][6]=t_cube[b][0]
    cube[b][7]=t_cube[b][3]
    cube[b][8]=t_cube[b][6]

    cube[u][0]=t_cube[l][6]
    cube[u][1]=t_cube[l][3]
    cube[u][2]=t_cube[l][0]

    cube[l][6]=t_cube[d][8]
    cube[l][3]=t_cube[d][7]
    cube[l][0]=t_cube[d][6]

    cube[d][8]=t_cube[r][2]
    cube[d][7]=t_cube[r][5]
    cube[d][6]=t_cube[r][8]
    
    cube[r][2]=t_cube[u][0]
    cube[r][5]=t_cube[u][1]
    cube[r][8]=t_cube[u][2]
    return cube
######################
def X():
    t_cube=copy.deepcopy(cube)
    #XXXXXXXXXXXXXXXXX
    cube[f]=t_cube[r]
    cube[l]=t_cube[f]

    cube[r][0]=t_cube[b][8]
    cube[r][1]=t_cube[b][7]
    cube[r][2]=t_cube[b][6]
    cube[r][3]=t_cube[b][5]
    cube[r][4]=t_cube[b][4]
    cube[r][5]=t_cube[b][3]
    cube[r][6]=t_cube[b][2]
    cube[r][7]=t_cube[b][1]
    cube[r][8]=t_cube[b][0]

    cube[b][0]=t_cube[l][8]
    cube[b][1]=t_cube[l][7]
    cube[b][2]=t_cube[l][6]
    cube[b][3]=t_cube[l][5]
    cube[b][4]=t_cube[l][4]
    cube[b][5]=t_cube[l][3]
    cube[b][6]=t_cube[l][2]
    cube[b][7]=t_cube[l][1]
    cube[b][8]=t_cube[l][0]

    cube[u][0]=t_cube[u][6]
    cube[u][1]=t_cube[u][3]
    cube[u][2]=t_cube[u][0]
    cube[u][3]=t_cube[u][7]
    cube[u][4]=t_cube[u][4]
    cube[u][5]=t_cube[u][1]
    cube[u][6]=t_cube[u][8]
    cube[u][7]=t_cube[u][5]
    cube[u][8]=t_cube[u][2]

    cube[d][0]=t_cube[d][2]
    cube[d][1]=t_cube[d][5]
    cube[d][2]=t_cube[d][8]
    cube[d][3]=t_cube[d][1]
    cube[d][4]=t_cube[d][4]
    cube[d][5]=t_cube[d][7]
    cube[d][6]=t_cube[d][0]
    cube[d][7]=t_cube[d][3]
    cube[d][8]=t_cube[d][6]
    return cube

def Xi():
    t_cube=copy.deepcopy(cube)
    #X'X'X'X'X'X'X'X'X'
    cube[f]=t_cube[l]
    cube[r]=t_cube[f]

    cube[l][0]=t_cube[b][8]
    cube[l][1]=t_cube[b][7]
    cube[l][2]=t_cube[b][6]
    cube[l][3]=t_cube[b][5]
    cube[l][4]=t_cube[b][4]
    cube[l][5]=t_cube[b][3]
    cube[l][6]=t_cube[b][2]
    cube[l][7]=t_cube[b][1]
    cube[l][8]=t_cube[b][0]

    cube[b][0]=t_cube[r][8]
    cube[b][1]=t_cube[r][7]
    cube[b][2]=t_cube[r][6]
    cube[b][3]=t_cube[r][5]
    cube[b][4]=t_cube[r][4]
    cube[b][5]=t_cube[r][3]
    cube[b][6]=t_cube[r][2]
    cube[b][7]=t_cube[r][1]
    cube[b][8]=t_cube[r][0]

    cube[u][0]=t_cube[u][2]
    cube[u][1]=t_cube[u][5]
    cube[u][2]=t_cube[u][8]
    cube[u][3]=t_cube[u][1]
    cube[u][4]=t_cube[u][4]
    cube[u][5]=t_cube[u][7]
    cube[u][6]=t_cube[u][0]
    cube[u][7]=t_cube[u][3]
    cube[u][8]=t_cube[u][6]

    cube[d][0]=t_cube[d][6]
    cube[d][1]=t_cube[d][3]
    cube[d][2]=t_cube[d][0]
    cube[d][3]=t_cube[d][7]
    cube[d][4]=t_cube[d][4]
    cube[d][5]=t_cube[d][1]
    cube[d][6]=t_cube[d][8]
    cube[d][7]=t_cube[d][5]
    cube[d][8]=t_cube[d][2]
    return cube
######################
def Y():
    t_cube=copy.deepcopy(cube)
    #YYYYYYYYYYYYYYYYYYYYY
    cube[f]=t_cube[u]
    cube[u]=t_cube[b]
    cube[b]=t_cube[d]
    cube[d]=t_cube[f]

    cube[r][0]=t_cube[r][2]
    cube[r][1]=t_cube[r][5]
    cube[r][2]=t_cube[r][8]
    cube[r][3]=t_cube[r][1]
    cube[r][4]=t_cube[r][4]
    cube[r][5]=t_cube[r][7]
    cube[r][6]=t_cube[r][0]
    cube[r][7]=t_cube[r][3]
    cube[r][8]=t_cube[r][6]

    cube[l][0]=t_cube[l][6]
    cube[l][1]=t_cube[l][3]
    cube[l][2]=t_cube[l][0]
    cube[l][3]=t_cube[l][7]
    cube[l][4]=t_cube[l][4]
    cube[l][5]=t_cube[l][1]
    cube[l][6]=t_cube[l][8]
    cube[l][7]=t_cube[l][5]
    cube[l][8]=t_cube[l][2]

def Yi():
    Y()
    Y()
    Y()

def M():
    R()
    Li()
    Y()

def Mi():
    Ri()
    L()
    Yi()

def whiteUp():
    for face in cube:
        if cube[face][4]=='w':
            if face==u:
                continue
            elif face==b:
                Y()
                break
            elif face==f:
                Y() 
                Y() 
                Y()
                break
            elif face==d:
                Y()
                Y()
                break
            elif face==r:
                Xi()
                Y()
            else :
                X()
                Y()

def cross():
    whiteCross=0
    #Make a Cross on Up
    while whiteCross<4:
        whiteCross=0
        for i in (1,3,5,7):
            if cube[u][i]=='w':
                whiteCross+=1
        if cube[f][3]=='w':
            while(cube[u][3]=='w'):
                U()
            Li()
            continue
        if cube[f][5]=='w':
            while(cube[u][5]=='w'):
                U()
            R()
            continue
        if cube[f][1]=='w':
            F()
            continue
        if cube[f][7]=='w':
            while(cube[u][5]=='w'):
                U()
            Fi()
            R()
            F()
            continue
        if cube[d][1]=='w':
            while(cube[u][7]=='w'):
                U()
            F()
            F()
            continue
        X()
    numOfCorrectCrossPart=0
    while numOfCorrectCrossPart<2:
        numOfCorrectCrossPart=0
        U()
        if cube[f][1]==cube[f][4]:
            numOfCorrectCrossPart+=1
        if cube[r][1]==cube[r][4]:
            numOfCorrectCrossPart+=1
        if cube[l][1]==cube[l][4]:
            numOfCorrectCrossPart+=1
        if cube[b][7]==cube[b][4]:
            numOfCorrectCrossPart+=1

    if numOfCorrectCrossPart==2:
        while cube[f][1]==cube[f][4]:
            X()
        if cube[r][1]!=cube[r][4]:
            Ri()
            Ui()
            R()
            U()
            Ri()
            return
        elif cube[l][1]!=cube[l][4]:
            Xi()
            Ri()
            Ui()
            R()
            U()
            Ri()
            return
        else:
            R()
            R()
            L()
            L()
            U()
            U()
            R()
            R()
            L()
            L()
            return

def formula(fomula):
    fomula=fomula.split(' ')
    for step in fomula:
        if step=='R': R()
        elif step =='Ri': Ri()
        elif step =='L': L()
        elif step =='Li': Li()
        elif step =='U': U()
        elif step =='Ui': Ui()
        elif step =='D': D()
        elif step =='Di': Di()
        elif step =='F': F()
        elif step =='Fi': Fi()
        elif step =='B': B()
        elif step =='Bi': Bi()
        elif step =='X': X()
        elif step =='Xi': Xi()
        elif step =='Y': Y()
        elif step =='Yi': Yi()
        elif step =='M': M()
        elif step =='Mi': Mi()

def edgetoUp(paircolors):
    if cube[f][5] in paircolors and cube[r][3] in paircolors:
        formula('U U R Ui Ri Ui')
    elif cube[f][3] in paircolors and cube[l][5] in paircolors:
        formula('F U Fi')
    elif cube[l][3] in paircolors and cube[b][3] in paircolors:
        formula('L Ui Li U')
    elif cube[r][5] in paircolors and cube[b][5] in paircolors:
        formula('Ri Ui R')

def check_f2l():
    if [[cube[f][i] for i in range(3,9)],[cube[r][i] for i in range(3,9)],[cube[l][i] for i in range(3,9)],[cube[b][i] for i in range(6)]]!=[[cube[f][4] for _ in range(6)],[cube[r][4] for _ in range(6)],[cube[l][4] for _ in range(6)],[cube[b][4] for _ in range(6)]] :
        return 'Unfinish'
    else:
        return 'Finish'

def f2l():
    #the cross must be at bottom
    completeColor=[]
    loop=0
    #find corner
    while check_f2l()=='Unfinish':
        loop+=1
        if cube[u][8]=='w' and cube[f][2] != cube[r][4] and cube[r][0]!=cube[f][4]:
            U()
            Xi()
        if cube[u][8]=='w' and cube[f][2] == cube[r][4] and cube[r][0]==cube[f][4]:
            formula('R Ui Ri U U')
            continue

     
        if cube[f][2]=='w': #white in Front
            pairCorlor=(cube[u][8],cube[r][0])
            #find right corner
            while(cube[f][4] not in pairCorlor or cube[r][4] not in pairCorlor):
                U()
                Xi()
            if cube[u][1] in pairCorlor and cube[b][7] in pairCorlor:
                if cube[u][1]==pairCorlor[0]: #== cube[u][8]
                    formula('Ui R U Ri U U R Ui Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('Ui R Ui Ri U Fi Ui F')
                    
                    completeColor.append((pairCorlor))
                    continue
            if cube[u][3] in pairCorlor and cube[l][1] in pairCorlor:
                if cube[u][3]==pairCorlor[0]: #== cube[u][8]
                    formula('Ui R U U Ri U U R Ui Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('Fi Ui F')
                    
                    continue
            if cube[u][5] in pairCorlor and cube[r][1] in pairCorlor:
                if cube[u][5]==pairCorlor[0]: #== cube[u][8]
                    formula('U R Ui Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('Ui R U U Ri U Fi Ui F')
                    
                    completeColor.append((pairCorlor))
                    continue
            if cube[u][7] in pairCorlor and cube[f][1] in pairCorlor:
                if cube[u][7]==pairCorlor[0]: #== cube[u][8]
                    formula('U Ri F R Fi U R U Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('U Fi U F Ui Fi Ui F')
                    
                    completeColor.append((pairCorlor))
                    continue
            edgetoUp(pairCorlor)
            continue

        if cube[r][0]=='w': #white in Right
            pairCorlor=(cube[u][8],cube[f][2])
            #find right corner
            while(cube[f][4] not in pairCorlor or cube[r][4] not in pairCorlor):
                U()
                Xi()
            if cube[u][1] in pairCorlor and cube[b][7] in pairCorlor:
                if cube[u][1]==pairCorlor[0]: #== cube[u][8]
                    formula('U Fi U U F U U Fi U F')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('R U Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
            if cube[u][3] in pairCorlor and cube[l][1] in pairCorlor:
                if cube[u][3]==pairCorlor[0]: #== cube[u][8]
                    formula('U Fi Ui F U U Fi U F')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('U Fi U F Ui R U Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
            if cube[u][5] in pairCorlor and cube[r][1] in pairCorlor:
                if cube[u][5]==pairCorlor[0]: #== cube[u][8]
                    formula('Ui R Ui Ri U U Fi U U F U U Fi U F')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('Ui R Ui Ri U R U Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
            if cube[u][7] in pairCorlor and cube[f][1] in pairCorlor:
                if cube[u][7]==pairCorlor[0]: #== cube[u][8]
                    formula('Ui Fi U F')
                    
                    completeColor.append((pairCorlor))
                    continue
                else:
                    formula('U Fi U U F Ui R U Ri')
                    
                    completeColor.append((pairCorlor))
                    continue
            edgetoUp(pairCorlor)
            continue


        if cube[f][8]=='w': 
            formula('R U Ri Ui')
            continue

        if cube[r][6]=='w': 
            formula('R U Ri Ui')
            continue

        if cube[d][2]=='w' and (cube[f][8]!=cube[f][4] or cube[r][6]!=cube[r][4]) :
            formula('R U Ri Ui')
            continue
        
        if cube[d][2]=='w' and (cube[f][8]==cube[f][4] or cube[r][6]==cube[r][4]) :
            if cube[d][2]=='w' and (cube[f][5]!=cube[f][4] or cube[r][3]!=cube[r][4]) :
                formula('R U Ri Ui')
                continue
        Xi()
            
def UpCross():
    while True:
        if (cube[u][1],cube[u][3],cube[u][5],cube[u][7])==('y','y','y','y'):
            break
        if cube[u][1]!='y' and cube[u][3]!='y' and cube[u][5]!='y' and cube[u][7] !='y' :
            formula('F R U Ri Ui Fi X R Y Xi R U Ri Ui Xi Li Y X')
            break
        if (cube[u][3],cube[u][5])==('y','y') and (cube[u][1],cube[u][7])!=('y','y'):
            formula('F R U Ri Ui Fi')
            break
        if (cube[u][7],cube[u][5])==('y','y') and (cube[u][1],cube[u][3])!=('y','y'):
            formula('X R Y Xi R U Ri Ui Xi Li Y X')
            break
        U()

def oll():
    while cube[u]!=['y' for _ in range(9)]:
        if cube[u][6]=='y' and (cube[u][0]!='y' and cube[u][2]!='y' and cube[u][8]!='y'): #fish
            if cube[f][2]=='y':
                formula('R U Ri U R U U Ri')
                break
            else:
                formula('Xi Li Ui L Ui Li U U L')
                break
        if cube[u][0]!='y' and cube[u][2]!='y' and cube[u][8]!='y' and cube[u][6]!='y': #cross
            if cube[f][0]=='y' and cube[f][2]=='y' and cube[b][6]=='y' and cube[b][8]=='y':
                formula('F R U Ri Ui R U Ri Ui R U Ri Ui Fi')
                break
            if cube[f][0]=='y' and cube[f][2]=='y' and cube[l][0]=='y' and cube[r][2]=='y':
                formula('U R U U R R Ui R R Ui R R U U R')
                break
        if cube[u][0]!='y' and cube[u][2]=='y' and cube[u][8]!='y' and cube[u][6]=='y' and cube[f][2]=='y': #balance
            formula('R R D Ri U R Di Ri Ui Ri')
            break
        if cube[u][0]!='y' and cube[u][2]!='y' and cube[u][8]=='y' and cube[u][6]=='y' : #tank
            if cube[l][0]=='y' and cube[r][2]=='y':
                formula('R U R D Ri Ui R Di R R')
                break
            if cube[b][6]=='y' and cube[b][8]=='y':
                formula('R R Di R U U Ri D R U U R')
                break
        U()

def check():
    if [cube[f][i] for i in range(0,9)]!=[cube[f][4] for _ in range(9)]:
        return False
    if [cube[r][i] for i in range(0,9)]!=[cube[r][4] for _ in range(9)]:
        return False
    if [cube[l][i] for i in range(0,9)]!=[cube[l][4] for _ in range(9)]:
        return False
    if [cube[u][i] for i in range(0,9)]!=[cube[u][4] for _ in range(9)]:
        return False
    if [cube[d][i] for i in range(0,9)]!=[cube[d][4] for _ in range(9)]:
        return False
    if [cube[b][i] for i in range(0,9)]!=[cube[b][4] for _ in range(9)]:
        return False
    return 'FINISH'

def pll():
    #switch conners
    correctConners=0
    pos=[]
    while correctConners<2:
        correctConners=0
        pos=[]
        U()
        if (cube[f][0],cube[l][2])==(cube[f][4],cube[l][4]):
            correctConners+=1
            pos.append('fl')
        if (cube[f][2],cube[r][0])==(cube[f][4],cube[r][4]):
            correctConners+=1
            pos.append('fr')
        if (cube[l][0],cube[b][6])==(cube[l][4],cube[b][4]):
            correctConners+=1
            pos.append('lb')
        if (cube[r][2],cube[b][8])==(cube[r][4],cube[b][4]):
            correctConners+=1
            pos.append('rb')
    if correctConners==2:
        if 'fl' in pos and 'rb' in pos:
            formula('F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi')
        elif 'fr' in pos and 'lb' in pos:
            formula('X F R Ui Ri Ui R U Ri Fi R U Ri Ui Ri F R Fi')
        elif 'fl' in pos and 'lb' in pos:
            formula('R U Ri Fi R U Ri Ui Ri F R R Ui Ri Ui')
        elif 'rb' in pos and 'lb' in pos:
            formula('Xi R U Ri Fi R U Ri Ui Ri F R R Ui Ri Ui')
        elif 'rb' in pos and 'fr' in pos:
            formula('X X R U Ri Fi R U Ri Ui Ri F R R Ui Ri Ui')
        elif 'fr' in pos and 'fl' in pos:
            formula('X R U Ri Fi R U Ri Ui Ri F R R Ui Ri Ui')
    
    #switch edges
    while check()==False:
        if cube[f][1]==cube[l][4] and cube[l][1]==cube[r][4] and cube[r][1]==cube[f][4] and cube[b][7]==cube[b][4]:
            formula('R R U R U Ri Ui Ri Ui Ri U Ri')
            continue
        if cube[f][1]==cube[r][4] and cube[l][1]==cube[f][4] and cube[r][1]==cube[l][4] and cube[b][7]==cube[b][4]:
            formula('R Ui R U R U R Ui Ri Ui R R')
            continue
        if cube[f][1]==cube[b][4] and cube[l][1]==cube[r][4] and cube[r][1]==cube[l][4] and cube[b][7]==cube[f][4]:
            formula('M M U M M U U M M U M M')
            continue
        if cube[f][1]==cube[r][4] and cube[l][1]==cube[b][4] and cube[r][1]==cube[f][4] and cube[b][7]==cube[l][4]:
            formula('M M U M M U Mi U U M M U U Mi U U')
            continue
        X()

def main():
    Scramble()
    if check()=='FINISH':
        print('Finish')
    else:
        print('Unsolve Rubik!\n')
        print(cube)
        print('PROCESS : WHITE UP')
        whiteUp()
        print(cube)
        print('PROCESS : CROSS')
        cross()
        print(cube)
        print('PROCESS : UP-SIDE-DOWN')
        formula('Y Y')#up-side-down
        print(cube)
        print('PROCESS : F2L')
        f2l()
        print(cube)
        print('PROCESS : YELLOW CROSS')
        UpCross()
        print(cube)
        print('PROCESS : OLL')
        oll()
        print(cube)
        print('PROCESS : PLL')
        pll()
        print(cube)
        print(check()+'!\n')



main()


