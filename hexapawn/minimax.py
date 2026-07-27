class State:
    def __init__(self, n, m, p1: set[tuple[int,int]], p2: set[tuple[int,int]], turn, turns):
        self.n=n
        self.m=m
        self.p1=p1
        self.p2=p2
        self.turn=turn
        self.turns=turns

    def is_win(self):
        for point in self.p1:
            if point[1]==self.n: return 1
        for point in self.p2:
            if point[1]==1: return 2
        return 0 # no direct win

    def is_stalemate(self):
        if len(self.get_moves())==0:
            return (self.turn)%2+1
        return 0 # no stalemate win

    def display_board(self):
        board=[[0]*self.m for _ in range(self.n)]
        for point in self.p1:
            board[point[1]-1][point[0]-1]=1
        for point in self.p2:
            board[point[1]-1][point[0]-1]=2
        for i in range(self.n):
            print(*board[i])
        print(self.turns,end="\n\n")

    def get_moves(self):
        if self.is_win()>0:
            return set()
        moves=set()
        if self.turn==1:
            for point in self.p1:
                x,y=point
                dy=1
                for dx in range(-1, 2):
                    if(1<=x+dx and x+dx<=self.m and y+dy<=self.n):
                        ok=True
                        if(dx==0):
                            if(((x+dx, y+dy) in self.p1 or (x+dx, y+dy) in self.p2)):
                                ok=False
                        else:
                            if(not((x+dx, y+dy) in self.p2)):
                                ok=False
                        if ok:
                            moves.add((x, y, x+dx, y+dy))
        else:
            for point in self.p2:
                x,y=point
                dy=-1
                for dx in range(-1, 2):
                    if(1<=x+dx and x+dx<=self.m and y+dy>=1):
                        ok=True
                        if(dx==0):
                            if(((x+dx, y+dy) in self.p1 or (x+dx, y+dy) in self.p2)):
                                ok=False
                        else:
                            if(not((x+dx, y+dy) in self.p1)):
                                ok=False
                        if ok:
                            moves.add((x, y, x+dx, y+dy))

        return moves

    def factory_apply(self, move):
        if self.turn==1:
            new_p1 = set()
            for item in self.p1:
                new_p1.add(item)
            new_p1.remove((move[0], move[1]))
            new_p1.add((move[2], move[3]))
            if((move[2], move[3]) in self.p2):
                self.p2.remove((move[2], move[3]))
            new_state = State(self.n, self.m, new_p1, self.p2, (self.turn)%2+1, self.turns+1)
        else:
            new_p2 = set()
            for item in self.p2:
                new_p2.add(item)    
            new_p2.remove((move[0], move[1]))
            new_p2.add((move[2], move[3]))
            if((move[2], move[3]) in self.p1):
                self.p1.remove((move[2], move[3]))
            new_state = State(self.n, self.m, self.p1, new_p2, (self.turn)%2+1, self.turns+1)
        return new_state

    def recursion_state(self):
        if(self.is_win()>0):
            return self.is_win()

        if(self.is_stalemate()>0):
            return self.is_stalemate()

        if(self.turn==1):
            for move in self.get_moves():
                post_move = self.factory_apply(move)
                if post_move.recursion_state()==1:
                    return 1
        else:
            for move in self.get_moves():
                post_move = self.factory_apply(move)
                if post_move.recursion_state()==2:
                    return 1
        return -1

state = State(2, 2, {(1, 1), (2, 1)}, {(1, 2), (2, 2)}, 1, 0)
print(state.recursion_state())

state = State(3, 3, {(1, 1), (2, 1), (3, 1)}, {(1, 3), (2, 3), (3, 3)}, 1, 0)
print(state.recursion_state())

state = State(4, 4, {(1, 1), (2, 1), (3, 1), (4, 1)}, {(1, 4), (2, 4), (3, 4), (4, 4)}, 1, 0)
print(state.recursion_state())

# pretty unoptimised and jank code. add depth checking (no. moves), alpha-beta pruning
# and memoisation for cases. try to find symmetries
# also add checking for a winning move, or winning sequences/patterns.