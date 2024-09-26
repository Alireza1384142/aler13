import random

def pause () :

    print('gamePause')
    
    global cpuScore , userScore , app

    pause = input('Aghe q ro bezani kharej mishi va aghe r bezani emtiaz ha reset mishe: ')

    if pause == 'q' :

        app=0

    elif pause == 'r' :

        cpuScore,userScore=0,0

def gameOver () :

    global cpuScore , userScore , app

    app=0

    print('The game is over')

    print(f'Total user score is: {userScore}')

    print('Total cpu score is: '+ str(cpuScore))



list=['rock','scissors','paper']

cpuScore = 0

userScore=0

app=True

while app==True:

    result=''

    userGuess = input('Lets play game,Enter rock or paper or scissors , or pause to stop the game , or (g) to game over :')

    cpu=random.choice(list)

    

    if userGuess==cpu :
        
        result = ('Draw')

        

    elif userGuess=='rock':

        
        
        if cpu=='paper' :

            result=('lose')

        if cpu == 'scissors':

            result=('win')

    elif userGuess == 'paper':

        

        if cpu == 'scissors' :

            result=('lose')

        if cpu == 'rock' :

            result=('win')   

    elif userGuess == 'scissors' :

        
         
        if cpu == 'rock' :
             
                result=('lose')

        if cpu == 'paper' :

            result=('win')   

    elif userGuess in ['pause' , 'p'] :

        pause()

    elif userGuess == 'g' :

        gameOver()

        break

    else :

        result=('wrong answer')  

    

    if result != 'wrong answer' :
         print (f'cpu choice is: {cpu}')

    print (result)


    if result=='Draw' :

        cpuScore+=0

        userScore+=0

    elif result=='win' :

        cpuScore+=0

        userScore+=1

    elif result == 'lose' :

        cpuScore +=1

        userScore +=0

    print('cpu score is: ' +  str(cpuScore))

    print('user score is: ' + str(userScore))









