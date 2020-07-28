import chess

class Evaluate:
 def __init__(self):
    self.board = chess.Board()
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

callEvaluate = Evaluate()

