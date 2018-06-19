import random
#import tabulate
global yn
global val
global for_i
j=0
temp=0
val=0
score=[]

def players():
    global playerns,score
    playerns={}
    pln=int(input("Enter the number of players.."))
    for i in range (pln) :
        
        print 'Enter the name of player. ',i+1
        name=raw_input("..")
        playerns[name]='Name'
        score.append(0)

    switch_players()

def switch_players():
    global playerns
    global score,j,for_i
    for_i=0
    plen=len(playerns)
    for_i=j
    print '************************************************************************************************************************************************************************************************************'
    print '_',(list(playerns)[j]),'_'
    print '_________________________________________________________________________PLAYER__',j+1,' ___________'
    j+=1
    if j==plen:
        j=0
    throw()
    
def throw():
    print '...'
    e=raw_input('Press ..."""enter"""... to throw dice')
    if e!="q":
        throw_dice()
    else:
        exit()

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
    global score,n1,n5,n,val
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

    if val==0:
        switch_players()
    decide()

def decide():  
    global score
    global val,for_i
    temp=0
    
    #player gets in if 1st throw score is > 300
    if score[for_i]<300 and val>=300:
        print "-----------------player1 YOU ARE IN------------------"
        total()

    if score[for_i]>=300:
        total()
        
    else:
        print '__________BETTER LUCK NEXT TIME__________'
        switch_players() 

def total():
        global val,for_i,score
        temp=0
        temp=score[for_i]
        temp=val+temp
        score[for_i]=temp
        round_next()
 
#compare scores
def winner():
    global playerns,plen
    i=0
    j=0
    k=0
    print '*********************************************************SCORE BOARD:*****************************************************'
    '''for name in playerns:
        for i in score:
            if k==j:
                k=0
                print name,'',i
                k=1
                j=1
        j=0'''

    for name in playerns:
        print [name]
    print score

    print 'the winner is'
    #print max(score),'winner'
    index=score.index(max(score))
    print '_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_',(list(playerns)[index]),'_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_'

    exit()

#next round 
def round_next():
    global score

    #when any player has a score greater than 3000, other player will get chance to play
    for i in score:
        if i>=3000:
            winner()
       
    print '______________________________________'

    print '__________ROUND 2___________'
    
    yn = raw_input('want to throw another dice?  (Y/N/EXIT)....')
    if yn=='Y' or yn=='y':
        throw_next()
    if yn=='N' or yn=='n':
        switch_players()
    if yn=='EXIT' or yn=='exit':
        winner()
    else:
        round_next()

# calculate number of non-scoring dices again
def throw_next():
    for i in k:
        # if dices are sccoring throw all of them 
        if i>1 & i<5 & i>5 & k.count(i)==3 or i==1 or i==5:
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


print '************************************************************************************************************************************************************************************************************'
players()

print '____________________________________________________________________________________________________'



            
        

        
                


        
        
           
    
