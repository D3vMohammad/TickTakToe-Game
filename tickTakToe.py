from random import choice
from time import sleep

welcome_messages = [
    "Welcome to the ultimate tic-tac-toe showdown!",
    "Get ready for a tic-tac-toe adventure!",
    "Time to unleash your tic-tac-toe skills!",
    "Let's play tic-tac-toe and have a blast!",
    "Welcome, superstar! It's tic-tac-toe time!",
    "Prepare to challenge the computer in a tic-tac-toe duel!",
    "Get your game face on, it's tic-tac-toe o'clock!",
    "A warm welcome to the world of tic-tac-toe excitement!",
    "Hello, player extraordinaire! Tic-tac-toe awaits!",
    "You're just a tic-tac-toe away from big smiles and fun!",
]

player_win_messages = [
    "You're on fire! Victory is yours!",
    "Victory dance time! You've outsmarted the computer!",
    "You're the champ! Keep up the winning streak!",
    "Congratulations on a spectacular win! You rock!",
    "Boom! You just took tic-tac-toe to a whole new level!",
    "Winner, winner, tic-tac-toe conqueror!",
    "You're not just playing, you're winning hearts!",
    "Way to go! The champion of tic-tac-toe is YOU!",
    "Your strategy paid off! Victory tastes sweet!",
    "You've got the moves, and the victory to prove it!",
]

computer_win_messages = [
    "The computer got lucky this time, but you'll get 'em next time!",
    "Don't worry, the computer practiced really hard for this. Challenge accepted?",
    "The computer is celebrating its virtual victory. Time for a rematch!",
    "The computer's victory dance is purely virtual. Your turn to shine!",
    "Tic-tac-whoa! The computer surprised us all this time.",
    "The computer is smiling in binary code after that win!",
    "Impressive computer tactics! Your turn to strategize!",
    "The computer is flexing its digital muscles, but the game's not over!",
    "Computer: 1, Player: 0. Let's even the score!",
    "The computer thinks it's clever, but you're the real game master!",
]

tie_messages = [
    "It's a tie! A battle of wits, well fought!",
    "A draw? You're both at the top of your game!",
    "A friendly handshake in the form of a tie. Keep the excitement alive!",
    "Tied up like a perfect bow! You both played brilliantly!",
    "Tie game! No winner, but tons of fun!",
    "The board is filled, but so is the room with laughter!",
    "Tic-tac-toe decided to play a prank and call it a tie!",
    "Even Steven! It's like the universe couldn't pick a winner either!",
    "Two minds, one tie. The journey continues!",
    "Tie game: A rare treasure in the world of tic-tac-toe!",
]

player_move_messages = [
    "Excellent choice! Your strategy is on point!",
    "A strategic move! You've got this!",
    "Your move is like a ray of sunshine on the board!",
    "Bravo! Your move just turned up the heat!",
    "Strategy in motion! Your moves are music to the board's ears!",
    "Spectacular move! Keep the momentum going!",
    "You're playing like a tic-tac-toe maestro!",
    "Calculating, contemplating, and conquering! Your move rocks!",
    "You're one step closer to victory with that move!",
    "Your moves are like poetry in motion. Keep it up!",
]

computer_move_messages = [
    "The computer is plotting its next move... or is it just doing a virtual dance?",
    "The computer is pondering the mysteries of tic-tac-toe. Or maybe just picking a spot randomly?",
    "The computer's move is in! Can you outsmart its digital brain?",
    "Computer's turn! Let's see what clever strategy it has up its sleeve!",
    "The computer just made a move, but your next one will be even smarter!",
    "The computer's gears are turning. What's its next cunning move?",
    "Virtual brain cells activated! The computer is strategizing!",
    "Will the computer's move be a masterpiece or a random stroke of genius?",
    "The computer is on the move, but the board is your playground!",
    "The computer moves, you counter. The battle of wits continues!",
]

final_score_messages = [
    "Final scores are in! You're both winners in the game of fun!",
    "The scoreboard is smiling. Keep those games coming!",
    "It's not just about the numbers, it's about enjoying the game together!",
    "The numbers may change, but the excitement stays constant!",
    "Congratulations on another round of exciting gameplay!",
    "No matter the outcome, every game is a step towards fun!",
    "Numbers don't define the experience—laughter and fun do!",
    "With every game, the joy multiplies. Let's keep playing!",
    "Keep those smiles coming! Tic-tac-toe is all about enjoyment!",
    "Game on! The adventure continues with every new match!",
]

def DisplayMessage(comment_list):
    if comment_list:
        selected_comment = choice(comment_list)
        comment_list.remove(selected_comment)
        return selected_comment
    return None

def Welcome():
    print(DisplayMessage(welcome_messages))
    sleep(1)
    print()
    print('Computer will decide who will play first')
    print()
    print('If you need Hint in the middle of game \npress any of this [Hint,hint,H,h]')
    sleep(1)
    print()
    print('''      ******* Format of Game ******
    
          |    |         1 | 2 | 3
       - - - - - -      - - - - - - 
          |    |         4 | 5 | 6
       - - - - - -      - - - - - - 
          |    |         7 | 8 | 9
                                           ''')

player_score = 0
computer_score = 0
ties = 0

def DrawBoard(board, NeedSleep=True):
    if NeedSleep:
        sleep(1)
    print()
    print('             '+board[1]+'  |  '+board[2]+'  |  '+board[3])
    print('             - - - - - - - ')
    print('             '+board[4]+'  |  '+board[5]+'  |  '+board[6])
    print('             - - - - - - - ')
    print('             '+board[7]+'  |  '+board[8]+'  |  '+board[9])
    print()

def InputPlayerLetter():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    if letter == 'O':
        return ['O', 'X']

def WhoFirst():
    opponents = ['computer', 'player']
    if choice(opponents) == 'computer':
        return 'computer'
    else:
        return 'player'

def PlayAgain():
    print()
    print('Do you want to Play Again (y or n)')
    playagain = input().lower().startswith('y')
    return playagain

def MakeMove(board, letter, move):
    board[move] = letter

def IsWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter))

def GetBoardCopy(board):
    DupeBoard = []
    for i in board:
        DupeBoard.append(i)
    return DupeBoard

def IsSpaceFree(board, move):
    return board[move] == ' '

def GetPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board, int(move)):
        print()
        print('Enter your move (1 - 9)')
        move = input()
        if move in HintInput:
            return move
            break
    return int(move)

def ChooseRandomFromList(board, MoveList):
    PossibleMoves = []
    for i in MoveList:
        if IsSpaceFree(board, i):
            PossibleMoves.append(i)
    if len(PossibleMoves) != 0:
        return choice(PossibleMoves)
    else:
        return None

def GetComputerMove(board, ComputerLetter):
    if ComputerLetter == 'X':
        PlayerLetter = 'O'
    else:
        PlayerLetter = 'X'

    for i in range(1, 10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy, i):
            MakeMove(copy, ComputerLetter, i)
            if IsWinner(copy, ComputerLetter):
                return i

    for i in range(1, 10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy, i):
            MakeMove(copy, PlayerLetter, i)
            if IsWinner(copy, PlayerLetter):
                return i

    move = ChooseRandomFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if IsSpaceFree(board, 5):
        return 5

    return ChooseRandomFromList(board, [2, 4, 6, 8])

def IsBoardFull(board):
    for i in range(1, 10):
        if IsSpaceFree(board, i):
            return False
    return True

def FinalBoard(board, NeedSleep=True):
    print('            |-------------|')
    DrawBoard(board, NeedSleep)
    print('            |-------------|')

Welcome()
while True:
    TheBoard = [' '] * 10
    PlayerLetter, ComputerLetter = InputPlayerLetter()
    turn = WhoFirst()
    print(f'The {turn} will go first')

    Playing = True
    while Playing:
        if turn == 'player':
            print(f"    Turn => {turn}")
            HintInput = ['Hint', 'hint', 'H', 'h']
            move = GetPlayerMove(TheBoard)
            print(DisplayMessage(player_move_messages))
            while move in HintInput:
                HintBox = []
                for i in TheBoard:
                    HintBox.append(i)
                hint = GetComputerMove(HintBox, PlayerLetter)
                MakeMove(HintBox, PlayerLetter, hint)
                print(f'HINT : placing at {hint} is better')
                FinalBoard(HintBox, False)
                move = GetPlayerMove(TheBoard)

            MakeMove(TheBoard, PlayerLetter, move)

            if IsWinner(TheBoard, PlayerLetter):
                FinalBoard(TheBoard)
                print(DisplayMessage(player_win_messages))
                player_score += 1
                print(f"Player Score: {player_score}, Computer Score: {computer_score}, Ties: {ties}")
                Playing = not Playing
            elif IsBoardFull(TheBoard):
                FinalBoard(TheBoard)
                print(DisplayMessage(tie_messages))
                ties += 1
                print(f"Player Score: {player_score}, Computer Score: {computer_score}, Ties: {ties}")
                Playing = not Playing
            else:
                DrawBoard(TheBoard)
                turn = 'computer'

        else:
            print(f"    Turn => {turn}")
            move = GetComputerMove(TheBoard, ComputerLetter)
            print(DisplayMessage(computer_move_messages))
            MakeMove(TheBoard, ComputerLetter, move)

            if IsWinner(TheBoard, ComputerLetter):
                FinalBoard(TheBoard)
                print(DisplayMessage(computer_win_messages))
                computer_score += 1
                print(f"Player Score: {player_score}, Computer Score: {computer_score}, Ties: {ties}")
                Playing = not Playing
            elif IsBoardFull(TheBoard):
                FinalBoard(TheBoard)
                print(DisplayMessage(tie_messages))
                ties += 1
                print(f"Player Score: {player_score}, Computer Score: {computer_score}, Ties: {ties}")
                Playing = not Playing
            else:
                DrawBoard(TheBoard)
                turn = 'player'

    if not PlayAgain():
        print("bye bye :")
        break

print(DisplayMessage(final_score_messages))
print(f"Player Score: {player_score}, Computer Score: {computer_score}, Ties: {ties}")
