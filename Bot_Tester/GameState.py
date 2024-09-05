#This python file defines the gamestate, which a representation of the current state of the game being played
#The player will return its action on the basis of the GameState
import Action

class GameState:
    def __init__(self) -> None:
        #Define the variable to give the initial state of the board...
        
        #Define the self state
        self.pieces = list()
        self.turn = 1

        #0 means blank cell
        for i in range(9):
            self.pieces.append(0)


        pass

    def winner(self)->int:
        '''Returns whether or not the game is over based on the current state of the board...
        0 means the game is not yet over
        1 means that player 1 has won
        2 means that player 2 has won
        -1 means that it is a draw'''

        #Game End Logic goes here
        
        
        for i in range (3):
            
            a = i*3
            
            #Horizontal victory
            if(self.pieces[a]==1 and self.pieces[a+1]==1 and self.pieces [a+2]==1):
                return 1
            
            if(self.pieces[a]==2 and self.pieces[a+1]==2 and self.pieces [a+2]==2):
                return 2
                    
            #Vertical victory
            if(self.pieces[i]==1 and self.pieces[i+3]==1 and self.pieces [i+6]==1):
                return 1
            
            if(self.pieces[i]==2 and self.pieces[i+3]==2 and self.pieces [i+6]==2):
                return 2
            
        #Diagonals 
        if(self.pieces[0]==self.pieces[4]==self.pieces[8]==1):
            return 1
            
        if(self.pieces[0]==self.pieces[4]==self.pieces[8]==2):
            return 2

        if(self.pieces[2]==self.pieces[4]==self.pieces[6]==1):
            return 1
            
        if(self.pieces[2]==self.pieces[4]==self.pieces[6]==2):
            return 2

        
        #Check for draw
        for i in self.pieces:
            if i ==0:
                return 0

        #No free spaces left, return draw
        return -1

    def resolveAction(self,action:Action.Action,player_number:int)->int:
        #Make changes to internal variables based on the actions 
        #Returning 0 means no problem has occured
        #Returning a negative number means that the action is not valid and/or some problem has occured

        if action.move not in range(0,9):
            return -1
        
        if self.pieces[action.move]!=0:
            return -1
        
        self.pieces[action.move] = player_number

        #Change turn to the next player
        if self.turn == 1:
            self.turn = 2
        elif self.turn ==2:
            self.turn = 1 
        return 0
    
    #Draws the current state
    def draw(self):
        
        #Draw the tic tac toe board
        for i in range(len(self.pieces)):
            if(i%3==0):
                print()
            
            if(self.pieces[i]==0):
                if i / 3 < 2:
                    print("___",end="")
                else:
                    print("   ",end="")

            elif(self.pieces[i]==1):
                if i / 3 < 2:
                    print("_O_",end="")
                else:
                    print(" O ",end="")

            elif(self.pieces[i]==2):
                if i / 3 < 2:
                    print("_X_",end="")
                else:
                    print(" X ",end="")

            if i % 3 < 2:
                print('|', end='')



