import tkinter as tk
import math
class Gomoku:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gomoku")
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        self.player = 'X'
        self.game_over = False
        self.create_board()
  
    def create_board(self):
        self.buttons = [[tk.Button(self.root, text=' ', font=('Arial', 20), width=2, height=1,
                                   command=lambda row=row, col=col: self.on_click(row, col)) 
                         for col in range(15)] for row in range(15)]
        #布置按钮
        for i in range(15):
            for j in range(15):
                self.buttons[i][j].grid(row=i, column=j)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.grid(row=15, column=7)

    def on_click(self, row, col):
        if not self.game_over and self.board[row][col] == ' ':
            self.board[row][col] = self.player
            self.buttons[row][col]['text'] = self.player
            if self.check_win(row, col):
                self.game_over = True
                print(f'The winner is {self.player}')
            self.player = 'O' if self.player == 'X' else 'X'

    def check_win(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            r, c = row, col
            count = 1
            count += self.count_in_direction(r, c, dr, dc)
            count += self.count_in_direction(r, c, -dr, -dc)
            if count >= 5:
                return True
        return False

    def count_in_direction(self, row, col, dr, dc):
        count = 0
        while 0 <= row < 15 and 0 <= col < 15 and self.board[row][col] == self.player:
            count += 1
            row, col = row + dr, col + dc
        return count

    def reset(self):
        self.board = [[' ' for _ in range(15)] for _ in range(15)]
        for i in range(15):
            for j in range(15):
                self.buttons[i][j]['text'] = ' '
        self.game_over = False
        self.player = 'X'

    def run(self):
        self.root.mainloop()
class GomokuAI:
    def __init__(self, depth):
        self.depth = depth
    
    def find_best_move(self, board):
        best_score = -math.inf
        best_move = None
        for i in range(15):
            for j in range(15):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # 在空位上尝试落子
                    score = self.minimax(board, self.depth, False)  # 调用 MiniMax 算法
                    board[i][j] = ' '  # 恢复空位
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, board, depth, maximizing_player):
        if depth == 0:
            return self.evaluate(board)
      
        if maximizing_player:
            best_score = -math.inf
            for i in range(15):
                for j in range(15):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth - 1, False)
                        board[i][j] = ' '
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(15):
                for j in range(15):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth - 1, True)
                        board[i][j] = ' '
                        best_score = min(best_score, score)
            return best_score

    def evaluate(self, board):
        # 添加一些启发式评估函数的评估规则，用于评估当前棋局的优劣
        # 可以考虑评估连续的棋子数量、双方威胁程度等因素
        pass
game = Gomoku()
game.run()



