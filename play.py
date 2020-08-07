
import chess
import chess.polyglot
import random
class Game:
  def __init__(self):
        self.board = chess.Board() 
        self.move = list(self.board.legal_moves)
  def evaluate(self):
    wp = len(self.board.pieces(chess.PAWN, chess.WHITE))
    bp = len(self.board.pieces(chess.PAWN, chess.BLACK))
    wn = len(self.board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(self.board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(self.board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(self.board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(self.board.pieces(chess.ROOK, chess.WHITE))
    br = len(self.board.pieces(chess.ROOK, chess.BLACK))
    wq = len(self.board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(self.board.pieces(chess.QUEEN, chess.BLACK))
    material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)

    pawnsq = sum([self.pawntable[i] for i in self.board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-self.pawntable[chess.square_mirror(i)] 
                                    for i in self.board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([self.knightstable[i] for i in self.board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-self.knightstable[chess.square_mirror(i)] 
                                    for i in self.board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([self.bishopstable[i] for i in self.board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-self.bishopstable[chess.square_mirror(i)] 
                                    for i in self.board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([self.rookstable[i] for i in self.board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-self.rookstable[chess.square_mirror(i)] 
                                    for i in self.board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([self.queenstable[i] for i in self.board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-self.queenstable[chess.square_mirror(i)] 
                                    for i in self.board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([self.kingstable[i] for i in self.board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-self.kingstable[chess.square_mirror(i)] 
                                    for i in self.board.pieces(chess.KING, chess.BLACK)])
    eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
    return -eval
  pawntable = [
 0,  0,  0,  0,  0,  0,  0,  0,
 5, 10, 10,-20,-20, 10, 10,  5,
 5, -5,-10,  0,  0,-10, -5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
 0,  0,  0,  0,  0,  0,  0,  0]

  knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

  bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

  rookstable = [
  0,  0,  0,  5,  5,  0,  0,  0,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  5, 10, 10, 10, 10, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

  queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
  0,  0,  5,  5,  5,  5,  0, -5,
 -5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

  kingstable = [
 20, 30, 10,  0,  0, 10, 30, 20,
 20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]
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
     sp = self.evaluate()
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
        print(self.board.unicode())
        try:
              while not self.board.is_game_over(claim_draw=True):
                  if self.board.turn == chess.WHITE:
                      uci = self.human_player()
                  else:
                      uci = self.random()
                  name = self.who(self.board.turn)
                  self.board.push_uci(uci)
                  print("################")
                  board_stop = print(self.board.unicode())
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
