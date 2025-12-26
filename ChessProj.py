# x: Capture (e.g., Bxe5 - Bishop captures on e5).
# -: Move to (sometimes used in older notation, e.g., Qd8-g5).
# +: Check (e.g., Qxf7+).
# #: Checkmate (e.g., Qxf7#).
# O-O: Kingside castling.
# O-O-O: Queenside castling.
# e8=Q: Pawn promotion (e.g., pawn reaches e8 and becomes a Queen). 
# Examples
# 1. e4 e5: Pawn to e4, then pawn to e5 (first moves).
# 2. Nf3 Nc6: Knight to f3, then Knight to c6.
# Bxc4: Bishop captures on c4.
# Rxf8#: Rook captures on f8, delivering checkmate. 
import string
class Chess_Main:
    def move_dec(self, move):
        col_dict = {"a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", "g":"7", "h":"8"}
        cap_move = ["x", "-", "+"]
        return_move = ""
        for item in move:
            if item in cap_move:
                return_move += item
            elif item.isupper():
                return_move += item
            elif item.islower():
                return_move += col_dict[item]
            else:
                return_move += item 
        return return_move
    

    def init_board(self):
        board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                 ["P", "P", "P", "P", "P", "P", "P", "P"],
                 ["1", "1", "1", "1", "1", "1", "1", "1"],
                 ["1", "1", "1", "1", "1", "1", "1", "1"],
                 ["1", "1", "1", "1", "1", "1", "1", "1"],
                 ["1", "1", "1", "1", "1", "1", "1", "1"],
                 ["P", "P", "P", "P", "P", "P", "P", "P"],
                 ["R", "N", "B", "K", "Q", "B", "N", "R"]
                 ]
        return board
    
    
    def make_move (self, board, move):
        if len(move) == 6:
            mv_pic = move[0]
            ori_col = move[1] 
            ori_row = move[2]
            tar_col = move[4]
            tar_row = move[5]
        else:
            mv_pic = move[0]
            ori_col = move[1] 
            ori_row = move[2]
            tar_col = move[5]
            tar_row = move[6]
        
        board[abs(int(ori_row)-8)][(int(ori_col)-1)] = 1
        board[abs(int(tar_row)-8)][int(tar_col)- 1] = mv_pic

        return board
    
    def chess_pawn(self):
        return
    def chess_king(self):
        return
    def chess_rook(self):
        return
    def chess_bishop(self):
        return
    def chess_queen(self):
        return
    def chess_knight(self):
        return
    def curr_chess_board(self):  
        return 
    def check_legal_move(self, board, move):
        return 

if __name__ == "__main__":
    Chess = Chess_Main()
    board = Chess.init_board()
    print(Chess.move_dec("Qe1-d1"))
    move = Chess.move_dec("Qe8-f6")
    print(Chess.make_move(board, move))