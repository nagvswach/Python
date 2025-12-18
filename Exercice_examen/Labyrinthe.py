
def find_path(board,x,y,explored):
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return False
    if board[x][y] =="X":
        return False

    if (x,y)in explored:
        return False
    
    explored.append((x,y))

    if board[x][y] == 'F':
        return True

    if (find_path(board,x-1,y,explored) or find_path(board,x+1,y,explored) or find_path(board,x,y-1,explored) or find_path(board,x,y+1,explored)):
        return True
    explored.pop()
    return False






board = [["X", "X", "X", "F", "X"],
         [".", ".", ".", ".", "."],
         ["X", "X", "X", "X", "."],
         [".", ".", ".", ".", "."],
         [".", ".", ".", ".", "."]]

board2 = [
    [".", "X", ".", ".", "."],
    [".", "X", ".", "X", "."],
    [".", ".", ".", "X", "."],
    ["X", "X", ".", ".", "F"]]

board3 = [
    [".", ".", ".", "X", "."],
    ["X", "X", ".", "X", "."],
    [".", ".", ".", ".", "."],
    ["X", ".", "X", ".", "."]]




if __name__=="__main__":
    explored = []
    print(find_path(board2, 1, 0, explored))
    print(explored)
