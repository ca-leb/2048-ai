#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *

def AI(mat):
    def random_move(board):
        moves = [merge_left, merge_right, merge_up, merge_down]
        while len(moves) > 0:
            move_index = randint(0, len(moves)-1)
            move = moves[move_index]
            board, is_valid, score = move(board)
            if is_valid:
                return board, True, score
            moves.pop(move_index)
        return board, False, score
             
    keys = ["a", "d", "w", "s"]
    moves = [merge_left, merge_right, merge_up, merge_down]
    scores = [0,0,0,0]

    for i in range(4):
        first_move = moves[i]
        first_board, first_valid, first_score = first_move(mat)
        if first_valid:
            first_board = add_two(first_board)
            scores[i] += first_score
        else:
            continue

        for later_moves in range(50):
            move_num = 1
            search_board = first_board.copy()
            is_valid = True

            while is_valid and move_num < 25:
                search_board, is_valid, search_score = random_move(search_board)
                if is_valid:
                    search_board = add_two(search_board)
                    scores[i] += search_score
                    move_num += 1

    best_move_index = scores.index(max(scores))
    best_move = keys[best_move_index]

    
    return best_move                 
    


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
game_logic['AI'] = AI
gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)
