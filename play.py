import chess
import chess.pgn
import chess.polyglot
import random
from ai import callEvaluate
class Game:
  def __init__(self):
        self.board = chess.Board() 
        self.move = list(self.board.legal_moves)
    
  def who(self,player):
        return "White" if player == chess.WHITE else "Black"
    
  def get_move(self,prompt):
        uci = input(prompt)
        if uci and uci[0] == "q":
            raise KeyboardInterrupt()
        try:
            chess.Move.from_uci(uci)
        except:
            uci = None
        return uci
  def human_player(self):
        uci = self.get_move("%s's move [q to quit]> " % self.who(self.board.turn))
        legal_uci_moves = [self.move.uci() for self.move in self.board.legal_moves]
        while uci not in legal_uci_moves:
             print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
             uci = self.get_move("%s's move[q to quit]> " % self.who(self.board.turn))
        return uci
  def random(self):
    return self.findmove(3).uci()
  def alphabeta(self,a, b, depth):
        bestscore = -9999
        if(depth == 0):
            return self.qsearch(a, b)
        for move in self.board.legal_moves:
            self.board.push(move)
            score = -self.alphabeta(-b, -a, depth -1)
            self.board.pop()
            if(score >= b):
                return score
            if(score>bestscore):
                bestscore = score
            if(score > a):
                a = score
        return bestscore
  def qsearch(self,a, b):
     sp = callEvaluate.evaluate()
     if (sp >= b):
         return b
     if(a< sp):
         a= sp

     for move in self.board.legal_moves:
        if self.board.is_capture(move):
            self.board.push(move)
            score = -self.qsearch(-b,-a)
            self.board.pop()

            if(score >= b):
                return b
            if(score > a):
                a = score
     return a
  def findmove(self,depth):
      movehistory=[]
      try:
          move = chess.polyglot.MemoryMappedReader("bookfish.bin").weighted_choice(self.board).move()
          movehistory.append(move)
          return move
      except:
          bestmove = chess.Move.null()
          bestvalue = -99999
          a = -100000
          b = 100000
          for move in self.board.legal_moves:
              self.board.push(move)
              boardV = -self.alphabeta(-b, -a, depth-1)
              if boardV > bestvalue:
                  bestvalue = boardV
                  bestmove = move
              if(boardV > a):
                  a = boardV
              self.board.pop()
          movehistory.append(bestmove)
          return bestmove
  def play_game(self):
        try:
              while not self.board.is_game_over(claim_draw=True):
                  if self.board.turn == chess.WHITE:
                      uci = self.human_player()
                  else:
                      uci = self.random()
                  name = self.who(self.board.turn)
                  self.board.push_uci(uci)
                  print("################")
                  board_stop = print(self.board)
                  print("a b c d e f g h")
        except KeyboardInterrupt:
             print("Game interrupted!")
             return (None, self.board)
        result = None
        if self.board.is_checkmate():
            print("checkmate: " + self.who(not self.board.turn) + " wins!")
            result = not self.board.turn
        elif self.board.is_stalemate():
            print("draw: stalemate")
        elif self.board.is_fivefold_repetition():
            print("draw: 5-fold repetition")
        elif self.board.is_insufficient_material():
            print("draw: insufficient material")
        elif self.board.can_claim_draw():
            print("draw: claim")
        return(result)
        print(self.board)

y =Game()
y.play_game()
