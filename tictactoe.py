board=[['-','-','-'],['-','-','-'],['-','-','-']]
def main():
    print("Welcome")
    flag=1
    i=0
    c=0
    while(i<9):
        x=play_game(flag);
        if(x==0):
            i=i+1
            flag*=-1
        if(x==1):
            c=1
            break
    if(c==0):
        print("Tie")
    print("Hope you enjoyed the game")
    
    
def board_update(m,n,a):
    if(m>3 or n>3):
        print("PLEASE TRY AGAIN!!!!")
        return 0
    if(board[m-1][n-1]!='-'):
        print("PLEASE TRY AGAIN!!!!")
        return 0
    else:
        board[m-1][n-1]=a
        return 1
    
    
def check_win():
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0]!='-'):
            return 1
        elif(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i]!='-'):
            return 1
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!='-'):
        return 1
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]!='-'):
        return 1
    return 0


def display():
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print("")
        
        
def play_game(f):
    if(f==1):
        print("\n\nPlayer A")
        x='A'
        print("Enter position")
        m=int(input("Enter row:"))
        n=int(input("Enter column:"))
        check=board_update(m,n,'x')
        if(check==1):
            display()
        else:
            return -1

    else:
        print("\n\nPlayer B")
        x='B'
        print("Enter position")
        m=int(input("Enter row:"))
        n=int(input("Enter column:"))
        check=board_update(m,n,'o')
        if(check==1):
            display()
        else:
            return -1
    if(check_win()==1):
        print("Conratualions",x,"won")
        return 1
    return 0

main()    