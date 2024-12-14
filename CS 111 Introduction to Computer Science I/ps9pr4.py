#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ look ahead some number of moves into the future to assess the impact 
        of each possible move that it could make for its next move, and assign 
        a score to each possible move, obtain a list of scores for each column,
        and choose the column with the maximum score as the next move
    """
    
    # Problem 2
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
            two attributes inherited from Player
            tiebreak: stores a string specifying the player’s tiebreaking 
            strategy ('LEFT', 'RIGHT', or 'RANDOM')
            lookahead: stores an integer specifying how many moves the player 
            looks ahead in order to evaluate possible moves
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    # Problem 3
    def __repr__(self):
        """ override/replace the __repr__ method that is inherited from Player, 
            and returns a string indicating the player’s tiebreaking strategy 
            and lookahead
        """
        s = super().__repr__() +' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s 
    
    # Problem 4
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the 
            board, and that returns the index of the column with the maximum 
            score
        """
        max_indices = [a for a in range(len(scores)) if scores[a] == max(scores)]
        
        if self.tiebreak == 'LEFT':
            max_col = max_indices[0]
        elif self.tiebreak == 'RIGHT':
            max_col = max_indices[-1]
        else:
            max_col = random.choice(max_indices)
            
        return max_col
    
    # Problem 5
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores 
            for the columns in b
        """
        scores = [50] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                oppo = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                oppo_scores = oppo.scores_for(b)
                if max(oppo_scores) == 100:
                    scores[col] = 0
                elif max(oppo_scores) == 0:
                    scores[col] = 100
                elif max(oppo_scores) == 50:
                    scores[col] = 50
                b.remove_checker(col)
        
        return scores
                
    # Problem 6
    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is inherited 
            from Player, and returns the called AIPlayer‘s judgment of its 
            best possible move
        """ 
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
    