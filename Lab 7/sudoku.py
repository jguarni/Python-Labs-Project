#Lab 7
#File 2 of 3
#Joe Guarni
#CISC106 - 7/22/13

from cisc106 import *

#AssertEquals can be found in the main function.

class Sudoku:
    def __init__(self,board):

        """
        A sudoku board is a 9x9 multi dimensional list that follows a set
        of duplicate rules. No row, column, or box can have the same number
        repeated in them.
        
        board - multidimensional list

        """
        self.__board = board

        """

        def Sudoku_function(aBoard):
            return Sudoku.board

        """
        
    def get_board(self):

        """
        Get the private variable.

        """
        return self.__board

    def set_board(self,newboard):
       
        """
        Set the private variable.

        """
        self.__board = newboard

    def rowCheck(self,rownum):

        """
        This function will check if there are no duplicates in a given
        row. Rownum is the row being checked.

        rownum -- integer

        return -- boolean

        """

        checkrow = []
    
        for ele in self.__board[rownum-1]:
            if ele in checkrow:
                print('Duplicates Found')
                checkrow = []
                return False
            else:
                checkrow.append(ele)
                   
        print('No Duplicates Found')
        return True


    def columnCheck(self,columnnum):

        """

        This function will check if there are no duplicates in a given
        column. Columnum is the column being checked.

        Columnnum -- integer

        return -- boolean

        """

        columncheck = [self.__board[0][columnnum-1],self.__board[1][columnnum-1],self.__board[2][columnnum-1],self.__board[3][columnnum-1],self.__board[4][columnnum-1], \
                      self.__board[5][columnnum-1],self.__board[6][columnnum-1],self.__board[7][columnnum-1],self.__board[8][columnnum-1]]

        checkcolumn = []
    
        for ele in columncheck:
            if ele in checkcolumn:
                print('Duplicates Found')
                return False
            else:
                checkcolumn.append(ele)          
        print('No Duplicates Found')
        return True

    def boxcheck(self,boxnum):
       
        """

        This function will check if there are no duplicates in a given
        box. Boxnum is the box that is being checked

        boxnum -- integer

        return -- boolean

        """
        if (boxnum == 0):
            cbox = self.__board[0][0:3] + self.__board[1][0:3] + self.__board[2][0:3]
        elif(boxnum == 1):
            cbox = self.__board[0][3:6] + self.__board[1][3:6] + self.__board[2][3:6]
        elif(boxnum == 2):
            cbox = self.__board[0][6:9] + self.__board[1][6:9] + self.__board[2][6:9]
        elif(boxnum == 3):
            cbox = self.__board[3][0:3] + self.__board[4][0:3] + self.__board[5][0:3]
        elif(boxnum == 4):
            cbox = self.__board[3][3:6] + self.__board[4][3:6] + self.__board[5][3:6]
        elif(boxnum == 5):
            cbox = self.__board[3][6:9] + self.__board[4][6:9] + self.__board[5][6:9]
        elif(boxnum == 6):
            cbox = self.__board[6][0:3] + self.__board[7][0:3] + self.__board[8][0:3]
        elif(boxnum == 7):
            cbox = self.__board[6][3:6] + self.__board[7][3:6] + self.__board[8][3:6]
        elif(boxnum == 8):
            cbox = self.__board[6][6:9] + self.__board[7][6:9] + self.__board[8][6:9]

        checkbox = []

    
        for ele in cbox:
            if ele in checkbox:
                print('Duplicates Found')
                return False
            else:
                checkbox.append(ele)          
        print('No Duplicates Found')
        return True 


def main():
    
    """

    This function will create a sudoku board and run each function to check validity.

    """

    board1 = Sudoku([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,1,4,3,6,5,8,9,7],[3,6,5,8,9,7,2,1,4],[8,9,7,2,1,4,3,6,5],[5,3,1,6,4,2,9,7,8],[6,4,2,9,7,8,5,3,1],[9,7,8,5,3,1,6,4,2]])
    board2 = Sudoku([[1,2,3,4,5,6,7,9,9],[1,5,6,7,8,9,1,2,3],[7,8,9,1,2,3,4,5,6],[2,1,4,3,6,5,8,9,7],[3,6,5,8,9,7,2,1,4],[8,9,7,2,1,4,3,6,5],[5,3,1,6,4,2,9,7,8],[6,4,2,9,7,8,5,9,1],[9,7,8,5,3,1,6,4,9]])
    
    assertEqual(Sudoku.rowCheck(board1,1),True)
    assertEqual(Sudoku.rowCheck(board1,2),True)
    assertEqual(Sudoku.rowCheck(board2,1),False)

    assertEqual(Sudoku.columnCheck(board1,1),True)
    assertEqual(Sudoku.columnCheck(board2,1),False)
    assertEqual(Sudoku.columnCheck(board1,5),True)

    assertEqual(Sudoku.boxcheck(board1,0),True)
    assertEqual(Sudoku.boxcheck(board1,5),True)
    assertEqual(Sudoku.boxcheck(board2,8),False)

    print("Testing Complete\n")
    print("-----------------------------------")
    

main()
