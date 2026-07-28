#include<bits/stdc++.h>
#define fi first
#define se second
using namespace std;

class State {
    public:
        int n;
        int m;
        set<pair<int,int>>p1;
        set<pair<int,int>>p2;
        int turn;
        int turns;

        int is_win(){
            for(auto point:p1){
                if(point.se==n){return 1;}
            }
            for(auto point:p2){
                if(point.se==1){return 2;}
            }
            return 0;
        }

        int is_stalemate(){
            if(get_moves().size()==0){
                return (turn)%2+1;
            }
            return 0;
        }

        void display_board(){
            vector<vector<int>>board(n,vector<int>(m));
            for(auto point:p1){
                board[point.se-1][point.fi-1]=1;
            }
            for(auto point:p2){
                board[point.se-1][point.fi-1]=2;
            }
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    cout<<board[i][j]<<" ";
                }
                cout<<"\n";
            }
            cout<<turns<<"\n\n";
        }

        set<pair<pair<int,int>,pair<int,int>>> get_moves(){
            if(is_win()>0){return {};}
            set<pair<pair<int,int>,pair<int,int>>>moves;
            if(turn==1){
                for(auto point:p1){
                    int x=point.fi;
                    int y=point.se;
                    int dy=1;
                    for(int dx=-1;dx<=1;dx++){
                        if(1<=x+dx && x+dx<=m && y+dy<=n){
                            bool ok=true;
                            pair<int,int>new_point(x+dx, y+dy);
                            if(dx==0){
                                if(p1.contains(new_point)||p2.contains(new_point)){
                                    ok=false;
                                }
                            }else{
                                if(!(p2.contains(new_point))){
                                    ok=false;
                                }
                            }
                            if(ok){
                                pair<pair<int,int>,pair<int,int>>move(point, new_point);
                                moves.insert(move);
                            }
                        }
                    }
                }
            }else{
                for(auto point:p2){
                    int x=point.fi;
                    int y=point.se;
                    int dy=1;
                    for(int dx=-1;dx<=1;dx++){
                        if(1<=x+dx && x+dx<=m && y+dy>=1){
                            pair<int,int>new_point(x+dx, y+dy);
                            bool ok=true;
                            if(dx==0){
                                if(p1.contains(new_point)||p2.contains(new_point)){
                                    ok=false;
                                }
                            }else{
                                if(!(p1.contains(new_point))){
                                    ok=false;
                                }
                            }
                            if(ok){
                                pair<pair<int,int>,pair<int,int>>move(point, new_point);
                                moves.insert(move);
                            }
                        }
                    }
                }
            }
            return moves;
        }

        State factory_apply(pair<pair<int,int>,pair<int,int>> move){
            State new_state;
            if(turn==1){
                set<pair<int,int>>new_p1;
                for(auto item:p1){
                    new_p1.insert(item);
                }
                new_p1.erase(move.fi);

                set<pair<int,int>>new_p2;
                for(auto item:p2){
                    new_p2.insert(item);
                }
                if(new_p2.contains(move.se)){
                    new_p2.erase(move.se);
                }

                new_state.n = n;
                new_state.m = m;
                new_state.p1 = new_p1;
                new_state.p2 = new_p2;
                new_state.turn = turn%2+1;
                new_state.turns = turns+1;
            }else{
                set<pair<int,int>>new_p2;
                for(auto item:p2){
                    new_p2.insert(item);
                }
                new_p2.erase(move.fi);

                set<pair<int,int>>new_p1;
                for(auto item:p1){
                    new_p1.insert(item);
                }
                if(new_p1.contains(move.se)){
                    new_p1.erase(move.se);
                }

                new_state.n = n;
                new_state.m = m;
                new_state.p1 = new_p1;
                new_state.p2 = new_p2;
                new_state.turn = turn%2+1;
                new_state.turns = turns+1;
            }
            return new_state;
        }

        int recursion_state(){
            if(is_win()>0){
                return is_win();
            }
            if(is_stalemate()>0){
                return is_stalemate();
            }

            if(turn==1){
                for(auto move:get_moves()){
                    State post_move = factory_apply(move);
                    if(post_move.recursion_state()==1){
                        return 1;
                    }
                }
            }else{
                for(auto move:get_moves()){
                    State post_move = factory_apply(move);
                    if(post_move.recursion_state()==2){
                        return 1;
                    }
                }
            }
            return -1;
        }
};


int main(){
    State state;
    state.n=3;
    state.m=3;
    for(int i=1;i<=3;i++){
        pair<int,int>point_1;
        point_1.fi=i;
        point_1.se=1;
        state.p1.insert(point_1);
        pair<int,int>point_2;
        point_2.fi=i;
        point_2.se=3;
        state.p2.insert(point_2);
    }
    cout<<state.recursion_state();
}