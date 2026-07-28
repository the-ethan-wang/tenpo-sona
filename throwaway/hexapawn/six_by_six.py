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
            if point[1]==self.n:
                if self.turn==1:
                    return 1
                else:
                    return -1
        for point in self.p2:
                if self.turn==2:
                    return 1
                else:
                    return -1
        return 0 # no direct win

    def is_stalemate(self):
        if len(self.get_moves())==0:
            return -1
        return 0 # no stalemate win

    def display_board(self):
        board=[[0]*self.m for _ in range(self.n)]
        for point in self.p1:
            board[point[1]-1][point[0]-1]=1
        for point in self.p2:
            board[point[1]-1][point[0]-1]=2
        for i in range(self.n-1, -1):
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

            new_p2 = set()
            for item in self.p2:
                new_p2.add(item)
            if((move[2], move[3]) in new_p2):
                new_p2.remove((move[2], move[3]))
            new_state = State(self.n, self.m, new_p1, new_p2, (self.turn)%2+1, self.turns+1)
        else:
            new_p2 = set()
            for item in self.p2:
                new_p2.add(item)    
            new_p2.remove((move[0], move[1]))
            new_p2.add((move[2], move[3]))
            new_p1 = set()
            for item in self.p1:
                new_p1.add(item)
            if((move[2], move[3]) in new_p1):
                new_p1.remove((move[2], move[3]))
            new_state = State(self.n, self.m, new_p1, new_p2, (self.turn)%2+1, self.turns+1)
        return new_state

    def get_hashable_state(self):
        return (frozenset(self.p1), frozenset(self.p2), self.turns,self.turn)

    def recursion_state(self):
        global data

        if self.get_hashable_state() in data:
            return data[self.get_hashable_state()]

        if(self.is_win()>0):
            data[self.get_hashable_state()]=self.is_win()
            return self.is_win()

        if(self.is_stalemate()>0):
            data[self.get_hashable_state()]=self.is_stalemate()
            return self.is_stalemate()

        if(self.turn==1):
            for move in self.get_moves():
                post_move = self.factory_apply(move)
                if post_move.recursion_state()==1:
                    data[self.get_hashable_state()]=1
                    return 1
        else:
            for move in self.get_moves():
                post_move = self.factory_apply(move)
                if post_move.recursion_state()==2:
                    data[self.get_hashable_state()]=1
                    return 1
        data[self.get_hashable_state()]=-1
        return -1

global data
data={}
state = State(6, 6, {(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)}, {(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)}, 1, 0)
print(state.recursion_state())
print(data)
print(data[state.get_hashable_state()])
for move in state.get_moves():
    post_move = state.factory_apply(move)
    if post_move.get_hashable_state() in data:
        post_move.display_board()
        print(data[post_move.get_hashable_state()], move)



# pretty unoptimised and jank code. add depth checking (no. moves), alpha-beta pruning
# and memoisation for cases. try to find symmetries
# also add checking for a winning move, or winning sequences/patterns.