name =input('type your name: ')
print('welcome' ,name, 'to this adventure!')

answer = input(
    'you are on a dirt road, it has come to an end and you can go left or right. Which way do you like to go? ')
answer =input()
if answer == 'left' :
    answer =input('you came to a river,you can walk around it or swim across? Type walk to walk around and swim to swim across: ')
    answer =input()
    
    if answer =='swim':
        print('you swam across and were eaten by an alligator')
        
    elif answer =='walk':
          print('you walked for many miles,ran out of water and you lost the game.')
    else:
        print('Not a valid option. You lose')
        
elif answer =='right':
    answer =input('you came to a bridge, it looks wobbly,do you want to cross it or head back(cross/back)? ')
    
    if answer =='back':
        print('you go back and lose')
        
        
    elif answer =='cross':
        answer =input('you cross the bridge and meet a stranger. Do you wanna talk to them (yes/np)? ')
          
        if answer =='yes':
            print('you talk to the stranger and they give you gold. You win!!')
        
        elif answer =='no':
              print('You ignored the strangerb and you lose. ')
          
        else:
            print('Not a valid option. You lose')
        
    else:
        print('Not a valid option. You lose')
else:
    print('Not a valid option. You lose')  
    
print('thankyou for trying', name)
    