def draw_board(char_list):
    ''' PRINT BOARD ON TERMINAL'''

    print('\n\t    Tic-Tac-Toe \n')
    print('\t -----------------')
    print(f'\t || {char_list[0]} || {char_list[1]} || {char_list[2]} || ')
    print('\t -----------------')
    print(f'\t || {char_list[3]} || {char_list[4]} || {char_list[5]} || ')
    print('\t -----------------')
    print(f'\t || {char_list[6]} || {char_list[7]} || {char_list[8]} || ')
    print('\t -----------------')

def get_player_input(player_char,char_list):
    ''' RETURNS PLAYER'S INPUT '''

    while True:
        player_move = int(input(player_char + " : Where would you like to place your piece (1-9) : "))
        if 0<player_move<10:
            if char_list[player_move-1] == ' ':
                return player_move
            else:
                print('Place Already Chosen...TRY AGAIN')
        else:
            print('Place Doesnot Exist ! TRY AGAIN')

def place_char_onboard(player_char,player_move,char_list):
    ''' UPDATE BOARD '''
    char_list[player_move-1] = player_char

def is_winner(player,List):
    ''' RETURN TRUE IF player WIN '''

    return (( List[0] == player and List[1] == player and List[2] == player ) or 
            ( List[3] == player and List[4] == player and List[5] == player ) or 
            ( List[6] == player and List[7] == player and List[8] == player ) or 
            ( List[0] == player and List[3] == player and List[6] == player ) or 
            ( List[1] == player and List[4] == player and List[7] == player ) or 
            ( List[2] == player and List[5] == player and List[8] == player ) or 
            ( List[0] == player and List[4] == player and List[8] == player ) or 
            ( List[2] == player and List[4] == player and List[6] == player )
    )


# GAME VARIABLE

player1 = 'X'
player2 = '0'

num_list = ['1','2','3','4','5','6','7','8','9']
char_list = [' ']*9

# GAMELOOP

draw_board(char_list)
draw_board(num_list)

while True:

    move = get_player_input(player1,char_list) # GET PLAYER1'S MOVE 
    place_char_onboard(player1,move,char_list) # UPDATE PLAYER1'S MOVE

    draw_board(char_list)
    draw_board(num_list)

    if is_winner(player1,char_list): # CHECK
        print(player1 , 'WON !!!')
        break

    move = get_player_input(player2,char_list) # GET PLAYER2'S MOVE
    place_char_onboard(player2,move,char_list) # UPDATE PLAYER2'S MOVE

    draw_board(char_list)
    draw_board(num_list)

    if is_winner(player2,char_list): # CHECK
        print(player1 , 'WON !!!')
        break