# excersis 6 rock paper scissor game
play='y'
def askuser():
    cont = str(input('wanna play again: ???'))
    return cont
def chechequal(p1,p2):
    if p1==p2:
        print('Drawn!')
def checkall(p1,p2):
    if p1=='scissors' and p2=='rock':
        print('You loose,Rock beats Scissors')
    elif p2=='scissors' and p1=='rock':
        print('You win Rock beats Scissors')
    elif p1=='paper' and p2=='scissors':
        print('You Loose Scissors beats Paper')
    elif p2=='paper' and p1=='scissors':
        print('You Win Scissors beats Paper')
    elif p1=='paper' and p2=='rock':
        print('You win Paper beats Rock')
    elif p2=='paper' and p1=='rock':
        print('You loose Rock beats Scissors')
while play=='y':
    p1=str(input('Player 1 turn: Rock Paper or Scissors??: '))
    p2=str(input('Player 2 turn: Rock Paper or Scissors??: '))
    chechequal(p1,p2)
    checkall(p1,p2)
    play=askuser()
print("Thank you,play again!!")
