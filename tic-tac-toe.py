import os
import copy
import time
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

w= 3
Table = [[0 for x in range(w)] for y in range(w)] 
turn =2
for i in range(len(Table)):
  for j in range(len(Table[i])):
    Table[i][j]=0





#print_table
def print_Table():
   
    cls()
    for i in range(len(Table)):
        for j in range(len(Table[i])):
            if Table[i][j] == 1:
                print("X",end =" ")
            if Table[i][j] == 2:
                print("O",end =" ")
            if Table[i][j] == 0:  
                print("_",end =" ")   
        print("\n")

def print_Table2(table):
    time.sleep(1)
    cls()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                print("X",end =" ")
            if table[i][j] == 2:
                print("O",end =" ")
            if table[i][j] == 0:  
                print("_",end =" ")   
        print("\n")
#fill_check

def fill_Check(table):
    #notBreaked = False
    notFill= False
   
    try:
        for i in range(len(table)):
            for j in range(len(table[i])):
                if  table[i][j]==0:
                    notFill = True
                    raise StopIteration
    except StopIteration:
        pass         
    return notFill


#win_function
def win_Check():
    game_over = 0
    one_counter=0
    two_counter=0
    for i in range(len(Table)):
        for j in range(len(Table[i])):
               if  Table[i][j] == 1:
                     one_counter+=1
               if  Table[i][j] == 2:
                     two_counter+=1      
        if one_counter ==3 or two_counter==3 :
            break
        one_counter =two_counter = 0
    if one_counter==3:
        game_over =1
    if two_counter==3:
        game_over =2    
    one_counter=0
    two_counter=0 

          
    for i in range(len(Table)):
        for j in range(len(Table[i])):
            if  Table[j][i] == 1:
                        one_counter+=1
            if  Table[j][i] == 2:
                        two_counter+=1      
        if one_counter ==3 or two_counter==3 :
            break
        one_counter =two_counter = 0
    if one_counter==3:
        game_over =1
    if two_counter==3:
        game_over =2    
    one_counter=0
    two_counter=0            

    for i in range(len(Table)):               
            if  Table[i][i] == 1:
                     one_counter+=1
            if  Table[i][i] == 2:
                     two_counter+=1      
            if one_counter ==3 or two_counter==3 :
                break
           
    if one_counter==3:
        game_over =1
    if two_counter==3:
        game_over =2    
    one_counter=0
    two_counter=0            
    for i in range(len(Table)):   
          
            if  Table[2-i][i] == 1:
                     one_counter+=1
            if  Table[2-i][i] == 2:
                     two_counter+=1      

            
    if one_counter==3:
        game_over =1
    if two_counter==3:
        game_over =2    
                   
    return game_over




#get_input
def get_Input():
    global turn
    if turn ==1:
        while True:
            try:
                print ("it player number " , turn , " turns")
                number = input("Enter a number between 1 and 9: ")
                if number.isdigit():
                    number=int(number)
                else:   
                    raise ValueError()
                if 1 <= number <= 9:
                    chosenList =value_Finder(number)
                    if chosenList[3]:
                        break
                    else:  
                        raise ValueError()  
                        
                raise ValueError()

                 
            except ValueError:
                print("Input must be an integer between 1 and 9.")
    else :
        aiFunction(Table)
    if turn==2:
        turn =1
    else:
        turn =2     
    #changing turns        
            

    
#value_finder
def value_Finder(g):
    global turn
    global Table
    counter =1
    for i in range(len(Table)):
        for j in range(len(Table[i])):
            if counter == g:
                if Table[i][j]==0:
                    Table[i][j] = turn
                    return [i,j,g,True]
                else:
                    return [i,j,g,False]
            counter+=1   

def hueristic(table,mark):
    for i in range(len(table)):
        for j in range(len(table[i])):
               if  table[i][j] == 0:    
                    table[i][j]=mark
    winCounter =0                 
    counter= 0
    for i in range(len(table)):
        for j in range(len(table[i])):
               if  table[i][j] == mark:    
                    counter+=1
        if counter == 3:
            winCounter+=1
        counter=0
     
    for i in range(len(table)):
        for j in range(len(table[i])):
            if  table[j][i] == mark:    
                    counter+=1
        if counter == 3:
            winCounter+=1
        counter=0
    
    for i in range(len(table)):               
           if  table[i][i] == mark:    
                    counter+=1
    if counter == 3:
        winCounter+=1
    counter=0
           
    for i in range(len(table)):   
          
           if  table[2-i][i] == mark:    
                    counter+=1
    if counter == 3:
        winCounter+=1
    counter=0     
            
    return winCounter

def state_Maker(table,mark):
    newList= []
    mark =mark_switcher(mark)
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j]==0:
                table[i][j]=mark
                newList.append(copy.deepcopy(table))
                table[i][j]=0
    return newList

def mark_switcher(mark ):
    if mark == 1:
        return 2
    else:
        return 1
def max(table,level,mark):
    points =[]
    states ={}
    #mark =mark_switcher(mark)
    if  not fill_Check(table):
        first=hueristic(table,mark)
        mark = mark_switcher(mark)
        second=hueristic(table,mark)
        return first-second    
    myList = state_Maker(copy.deepcopy(table),mark)
    for i in range(len(myList)):
        states[str(min(myList[i],level+1,mark_switcher(mark)))] = myList[i]
        #points.aend(min(myList[i],level+1,mark))
    for i in   states.keys():
        points.append(i)  
    points.sort()
    if level ==0:
       return states[points[-1]] 
    return int(points[-1])  

def min(table,level,mark):
    points =[]
    states ={}
    #mark = mark_switcher(mark)
    if  not fill_Check(table):
        first=hueristic(table,mark)
        mark = mark_switcher(mark)
        second=hueristic(table,mark)
        return first-second     
    myList = state_Maker(copy.deepcopy(table),mark)
    for i in  range(len(myList)):
        states[str(max(myList[i],level+1,mark_switcher(mark)))] = myList[i]
        #points.append(min(myList[i],level+1,mark))
    for i in   states.keys():
        points.append(i)  
    points.sort()
    return int(points[0])



def aiFunction(table):
    answer = max(copy.deepcopy(table),0,1)
    for i in range(len(table)):
        for j in range(len(table[i])):    
            if table[i][j] == 0 and answer[i][j]!=0:
                table[i][j]= answer[i][j]
    #turn should be swaped



while True:
    get_Input()
    print_Table()
    temp = win_Check()
    alreadydone =fill_Check(Table)    
    if temp !=0 :
        print("player ", temp," won")
        break
    if not alreadydone:
        print("draw ")
        break
    #print (hueristic(copy.deepcopy(Table),2) )

