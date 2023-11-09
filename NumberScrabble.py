class NumberScrabble:
    def __init__(self):
        self.board = [0] * 9
        self.player_turn = True
        self.player_numbers = []
        self.ai_numbers = []

    def make_move(self, number):
        if 1 <= number <= 9 and self.board[number - 1] == 0:
            self.board[number - 1] = number

            if self.player_turn:
                self.player_numbers.append(number)
            else:
                self.ai_numbers.append(number)

            self.player_turn = not self.player_turn
            return True
        else:
            print("Invalid move. Please try again.")
            return False

    def play_game(self):
        print("Enter a number between 1 and 9 to make your move.")
        while not self.is_game_over():
            self.display_board()
            available_numbers = [i for i in range(1, 10) if self.board[i - 1] == 0]
            print(available_numbers)
            current_player = "Player" if self.player_turn else "AI"
            print(f"{current_player}'s turn:")
            if self.player_turn:
                number = int(input("Enter your move: "))
            else:
                number = self.ai_move()
                print(f"AI chooses {number}")
            self.make_move(number)
        self.display_board()
        print("Game Over!")

    def ai_move(self):
        available_numbers = [i for i in range(1, 10) if self.board[i - 1] == 0]
        best_move = None
        best_eval = float('-inf')
        for number in available_numbers:
            child_node = self.copy()
            child_node.make_move(number)
            eval_ = self.minimax(child_node, 15, True, float('-inf'), float('inf'), len(self.ai_numbers),
                                 len(self.player_numbers))
            # print(f'eval is {eval_} for number {number}')
            if eval_ > best_eval:
                best_eval = eval_
                best_move = number
        return best_move

    def display_board(self):
        print("Board:")
        for i in range(1, 10):
            print(f"{i}: {self.board[i - 1]}", end=" | ")
            if i % 3 == 0:
                print()
        print()

    def copy(self):
        child_node = NumberScrabble()
        child_node.board = self.board.copy()
        child_node.player_numbers = self.player_numbers.copy()
        child_node.ai_numbers = self.ai_numbers.copy()
        child_node.player_turn = False
        return child_node

    def is_game_over(self):
        if len(self.player_numbers) >= 3 or len(self.ai_numbers) >= 3:
            if self.has_combination(self.player_numbers):
                print("Player wins!")
                return True
            if self.has_combination(self.ai_numbers):
                print("AI wins!")
                return True
            return False
        if all(self.board):
            print("It's a draw!")
            return True
        return False

    @staticmethod
    def has_combination(arr):
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if arr[i] + arr[j] + arr[k] == 15:
                        return True
        return False

    @staticmethod
    def minimax(node, depth, maximizing_player, alpha, beta, len_ai_numbers, len_player_numbers):
        if depth == 0 or node.is_game_over():
            return node.evaluate()

        if maximizing_player:
            max_eval = float('-inf')
            available_numbers = [i for i in range(1, 10) if node.board[i - 1] == 0]
            for number in available_numbers:
                child_node = node.copy()
                child_node.make_move(number)
                eval_ = NumberScrabble.minimax(child_node, depth - 1, False, alpha, beta, len_ai_numbers,
                                               len_player_numbers)
                alpha = max(alpha, eval_)
                if beta <= alpha:
                    break
                max_eval = max(max_eval, eval_)
            return max_eval
        else:
            min_eval = float('inf')
            available_numbers = [i for i in range(1, 10) if node.board[i - 1] == 0]
            for number in available_numbers:
                child_node = node.copy()
                child_node.make_move(number)
                eval_ = NumberScrabble.minimax(child_node, depth - 1, True, alpha, beta, len_ai_numbers,
                                               len_player_numbers)
                beta = min(beta, eval_)
                if beta <= alpha:
                    break
                min_eval = min(min_eval, eval_)
            return min_eval

    def evaluate(self):
        score_diff = 0

        available_numbers = len([num for num in range(1, 10) if num not in self.player_numbers
                                 and num not in self.ai_numbers])
        score_diff += available_numbers

        player_winning_combos = self.count_winning_combinations(self.player_numbers)
        ai_winning_combos = self.count_winning_combinations(self.ai_numbers)
        score_diff += ai_winning_combos - player_winning_combos

        return score_diff

    @staticmethod
    def count_winning_combinations(numbers):
        winning_combinations = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                for k in range(j + 1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] == 15:
                        winning_combinations += 1
        return winning_combinations
