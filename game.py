class Game:
    def __init__(self):
        self.board = list(range(1, 10))
        self.picks_human = []
        self.picks_computer = []
        self.is_human = True

    @staticmethod
    def evaluate(board):
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                for k in range(j + 1, len(board)):
                    if board[i] + board[j] + board[k] == 15:
                        return 10

    @staticmethod
    def minimax(board, board_human, board_computer, depth, isMax):

        score = Game.evaluate(board_human)
        if score:
            return 10

        score = Game.evaluate(board_computer)
        if score:
            return -10

        if not board:
            return 0

        if isMax:
            best = -1000
            for i in board:
                new_board = board[:]
                new_board.remove(i)
                new_board_human = board_human[:]
                new_board_human.append(i)
                new_board_computer = board_computer[:]
                best = max(best, Game.minimax(new_board, new_board_human, new_board_computer, depth+1, not isMax))

            return best
        else:
            best = 1000
            for i in board:
                new_board = board[:]
                new_board.remove(i)
                board_computer.append(i)
                new_board_human = board_human[:]
                new_board_computer = board_computer[:]
                new_board_computer.append(i)
                best = min(best, Game.minimax(new_board, new_board_human, new_board_computer, depth+1, not isMax))
            return best

    def find_best_move(self, board, board_human, board_computer):
        best_val = 1000
        best_piece = None
        for i in board:
            new_board = board[:]
            new_board.remove(i)
            move_val = Game.minimax(new_board, board_human, board_computer, 0, True)
            if move_val < best_val:
                best_val = move_val
                best_piece = i

        if best_piece is not None:
            return best_piece
        return board[0]

    def play(self):
        while self.board:
            print(f'Available numbers {self.board}')
            num = int(input('pick a number '))
            while num not in self.board:
                num = int(input('pick a different number '))

            self.board.remove(num)
            self.picks_human.append(num)

            if Game.evaluate(self.picks_human):
                print('You won!')
                return
            if not self.board:
                print('Draw')
                return

            new_board = self.board[:]
            new_human_picks = self.picks_human[:]
            new_computer_picks = self.picks_computer[:]

            computer_move = self.find_best_move(new_board, new_human_picks, new_computer_picks)
            print(f'Computer chose {computer_move}')
            self.picks_computer.append(computer_move)

            self.board.remove(computer_move)

            if Game.evaluate(self.picks_computer):
                print('Computer beat you!')
                return



