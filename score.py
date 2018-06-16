import random
global yn
global val
score=0
p1getin=0
p2getin=0
val=0
chp1=0
chp2=0
p1score=0
p2score=0
switch=2

#player 1 
def p1():
    global switch,e
    switch=1
    print '__________________________________________________________________________________________________'
    print '_________________________________',pl1,'__________________________________PLAYER !__________'
    print '--------player-score before this round=',p1score
    #throw dice switching of player
    print '...'
    e=raw_input('Press... """enter"""... to throw dice')
    if e!="q":
        throw_dice()
    else:
        exit()

#player 2    
def p2():
    global switch,e
    switch=2
    print '__________________________________________________________________________________________________'
    print '__________________________________',pl2,'_________________________________PLAYER 2___________'
    print '--------player 2'
    print '-------  player2-score before this round=',p2score
    #throw a dice or get entry
    print '...'
    e=raw_input('Press ..."""enter"""... to throw dice')
    if e!="q":
        throw_dice()
    else:
        exit()

#switch between 2 players
def switchp():
    global switch
    if switch==1:
        p2()
    if switch==2:
        p1()


def throw_dice():  
    global k
    k=[ random.randint(1,6) for i in range (1,6)]
    print '-------',k
    no_of_times()

#to count no of times a number on dice occurs
def no_of_times():
    global n1,n2,n3,n4,n6,n5,k,n
    n1=k.count(1)
    n2=k.count(2)
    n3=k.count(3)
    n4=k.count(4)
    n5=k.count(5)
    n6=k.count(6)
    n=[n1,n2,n3,n4,n5,n6]
    count_score()

#count the score
def count_score():
    global score,n1,n5,n,p1getin,p2getin,p1score,p2score,val
    val=0
    if n1>2:
        val+=1000
        n1=n1-3

    else:
        for i in k:
            if k.count(i)>2:
                val+=100*i
                if i==5:
                        n5=n5-3
                break

    if n5>0:
        for i in range (n5):
                val+=50

    if n1>0:    
        for i in range (0,n1):
            val+=100
  
    n[0]=0
    n[4]=0
    
    print ' You scored---**---',val,'---**---in this round'
    
    # if a 0 is scored all the progress is lost
    #player1
    if val==0 and switch==1:
        val=0
        p1score=0
        switchp()
    #player2
    if val==0 and switch==2:
        val=0
        p2score=0
        switchp()
    decide()

def decide():
    
    global score,n1,n5,n,p1getin,p2getin,p1score,p2score
    global val
    
#player1 gets in if 1st throw score is > 300
    if switch==1 and val>=300 and p1getin==0:
        p1getin=1
        print "-----------------player1 YOU ARE IN------------------"

#player2 gets in if 1st throw score is > 300       
    if switch==2 and val>=300 and p2getin==0:
        p2getin=1
        print "-----------------player2 YOU ARE IN --------------------"
 
# if a player has got in already add his scores and get to next round
    #player1
    if  p1getin==1 and switch==1 and p1score<3000:
        p1score=p1score+val
        round_next()
        
    #player2
    if p2getin==1 and switch==2 and p2score<3000:
        p2score=p2score+val
        round_next()        
    else:
        print '__________BETTER LUCK NEXT TIME__________'
        switchp()

#compare scores
def winner():
    print pl1,'scored....',p1score,'points'
    print pl2,'scored....',p2score,'points'
    if p1score>p2score:
        print pl1,'wins'
    if p2score>p1score:
        print pl2,'wins'
    if p1score==p2score:
        print 'It is a tie'
    exit()

#next round 
def round_next():
    global switch,p1score,p2score

    #when any player has a score greater than 3000, other player will get chance to play
    if p1score>=3000:
        switch=1
    if p1score>=3000:
        switch=2
    #when both the players have their score above 3000, display results
    if p1score>=3000 and p2score>=3000:
        winner()
        
    print '______________________________________'

    print '__________ROUND 2___________'
    
    yn = raw_input('want to throw another dice?  (Y/N/EXIT)....')
    if yn=='Y' or yn=='y':
        throw_next()
    if yn=='N' or yn=='n':
        switchp()
    if yn=='EXIT' or yn=='exit':
        winner()
    else:
        round_next()

# calculate number of non-scoring dices again
def throw_next():
    for i in k:
        # if dices are sccoring throw all of them 
        if i>1 & i<5 & i>5 & k.count(i)==3:
            throw_dice()
            break
        else:
            throw_dice2()
            break
# throw the number of non scoring dices       
def throw_dice2():
        global n
        tot=0
        print '....'
        global k
        for i in n:
            tot=tot+i
        print 'you can throw',tot,' dices'
        k=[ random.randint(1,6) for i in range (tot)]
        print k
        no_of_times()



print '__________________________________________________________________________________________________'


pl1=raw_input("Enter the name of player 1....")
pl2=raw_input("Enter the name of player 2....")
switchp()
print '____________________________________________________________________________________________________'



            
        

        
                


        
        
           
    
