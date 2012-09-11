def game():
    import random
    value = random.randint(2, 4294967295)
    init = 1
    print 'You vs. the computer. Whoever exceeds', value, 'wins.'
    print 'Required:', value, '| Current:', init
    turn = 0
    while True:
        if turn == 0:
            x = raw_input('Enter a number: ')
            try: 
                x = int(x)
            except: 
                print 'That is not valid.'
                break
            if x not in range(2,10):
                print 'That is not valid.'
                break
            turn = 1
            init *= x            
            print 'Required:', value, '| Current:', init
            if init >= value:
                print 'You win!'
                return
        if turn == 1:
            i = 10
            ouch = 0
            while i != 2:
                i -= 1
                if init * i >= value:
                    init *= i
                    print 'Opponent chooses', i
                    print 'Required:', value, '| Current:', init
                    print 'You lost.'
                    return
                if init * i * 9 < value:
                    init *= i
                    turn = 0
                    print 'Opponent chooses', i
                    print 'Required:', value, '| Current:', init                  
                    i = 2
                    ouch = 1
            if ouch ==  0:
                print 'Opponent resigns. You win!'
                return
                    
game()            
