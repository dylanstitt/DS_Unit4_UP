# Dylan Stitt
# Unit 4 Unit Project
# Tower of Hanoi

import os, time
from Stack import ArrayStack

def rules():
    print("Rules:\n")
    print("You are given 3 rods to move blocks of various size")
    time.sleep(.5)
    print("Your goal is to move all the blocks from rod A to rod C")
    time.sleep(.5)
    print("You are able to move the block on top of a stack of blocks to another, but smaller blocks must be placed on bigger blocks")
    time.sleep(.5)
    print("There will be 5 blocks to move around the rods")
    time.sleep(.5)
    print("GOODLUCK!")
    time.sleep(.5)

def displayGame(rods):
    print('~~~ TOWERS ~~~')

    letters = ['A', 'B', 'C']
    for i, rod in enumerate(rods):
        rod.displayRod(letters[i])

def playAgain(rods):
    os.system('cls' if os.name == 'nt' else 'clear')
    displayGame(rods)

    print('YOU WON!\n')
    again = input('Would you like to play again? [y/n]: ').lower()
    while again not in ['y', 'n']:
        again = input('Please enter y or n: ').lower()

    if again == 'y':
        main()

def main():
    print("Welcome to the Tower of Hanoi")
    option = input("If you would like to hear the rules enter 'R': ").upper()

    os.system('cls' if os.name == 'nt' else 'clear')
    if option == 'R':
        rules()
        input('Press ENTER to continue')
    os.system('cls' if os.name == 'nt' else 'clear')

    playing = True
    rod1 = ArrayStack()
    rod2 = ArrayStack()
    rod3 = ArrayStack()

    for i in range(5, 0, -1):
        rod1.push(str(i))

    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        displayGame([rod1, rod2, rod3])

        rods = []
        currentRod = input('Select from (A, B, C): ').upper()
        while currentRod not in ['A', 'B', 'C']:
            currentRod = input('Select from (A, B, C): ').upper()

        nextRod = input('Destination (A, B, C): ').upper()
        while nextRod not in ['A', 'B', 'C']:
            nextRod = input('Destination (A, B, C): ').upper()

        if currentRod == nextRod:
            input('You cannot select the same rod. Press ENTER to continue')
            continue

        for i in [currentRod, nextRod]:
            if i == 'A':
                rods.append(rod1)
            elif i == 'B':
                rods.append(rod2)
            else:
                rods.append(rod3)

        if len(rods[0]) == 0:
            input('The rod selected does not currently have any blocks to move. Press ENTER to continue')
            continue

        if len(rods[1]) != 0:
            if rods[1].top() < rods[0].top():
                input('The current block you are trying to move is too big to put on top of the destination rod. Press ENTER to continue')
                continue

        ele = rods[0].pop()
        rods[1].push(ele)

        if len(rod3) == 5:
            playing = False

    playAgain([rod1, rod2, rod3])


if __name__ == '__main__':
    main()
