
# initialize board as dictionary with spaces in each spot
board = {'top-L': ' ',
         'top-M': ' ',
         'top-R': ' ',
         'mid-L': ' ',
         'mid-M': ' ',
         'mid-R': ' ',
         'low-L': ' ',
         'low-M': ' ',
         'low-R': ' '
         }

# function to print out the game board (but wouldn't it be better
# to inerate throught the dictionary instead of WET-ing this?
# I liked using an array for something like this in C
def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printboard(board)

