import chess
from copy import deepcopy
from math import sqrt
def fk(pos, color, totmat):
    #y then x (rank then file)
    t = (7 if color==1 else 0)
    if totmat<9:
        return -sqrt((3.5-pos[0])**2+(3.5-pos[1])**2) * 0.2 + 100
    #print('t',pos,t)
    return ((-0.2*abs(t-pos[0])) + sqrt((3.5-pos[0])**2+(3.5-pos[1])**2) * 0.14)+100
def fp(pos, color, totmat):
    t = (1 if color==1 else 6)
    try:
        return [0.7,0.8,0.9,1.0,1.0,0.9,0.8,0.7][pos[1]] * (1+[0.0,0.1,0.3,0.5,1.0,3.0][abs(t-pos[0])])
    except:
        print(pos, color, totmat)
        raise ValueError
def fb(pos, color, totmat):
    #print(pos,color,totmat)
    return -sqrt((3.5-pos[0])**2+(3.5-pos[1])**2) * 0.2 + 3.4 
def fn(pos, color, totmat):
    return -sqrt((3.5-pos[0])**2+(3.5-pos[1])**2) * 0.2 + 3
def fq(pos, color, totmat):
    return -sqrt((3.5-pos[0])**2+(3.5-pos[1])**2) * (min(totmat/100,0.3)-0.2) + 9
def fr(pos, color, totmat):
    return -sqrt((3.5-pos[0])**2+(3.5-pos[1])**2) * (min(totmat/100,0.3)-0.2) + 5
board = chess.Board()
inf = 100
total_nodes = 0
values = {'k':inf,'r':5,'q':9,'b':3,'n':3,'p':1,'K':-inf,'R':-5,'Q':-9,'B':-3,'N':-3,'P':-1}
heatmaps = {'k':fk, 'b':fb, 'n':fn, 'q':fq,'r':fr,'p':fp} #pos in all these is (x,y)
ALPHA = -inf
BETA = -inf
def total_material(position):
    s = 0
    for i in str(position):
        if i[0]!=' ' and i[0]!='\n' and i[0]!='.' and i[0].lower()!='k':
            s+=values[i[0].lower()]
    return s
def material(position):
    s = 0
    for i in str(position):
        if i[0]!=' ' and i[0]!='\n' and i[0]!='.':
            s+=values[i[0]]
    return s
def material(position):
    s = 0 #-1 for color is black; 1 is white
    totmat = total_material(position)
    for i in range(7,-1,-1):
        for j in range(8):
            k = i*8+j
            t = str(position.piece_at(k))
            if t!='None':
                s+=(-1 if t==t.lower() else 1)*(heatmaps[t.lower()])((i,j),(-1 if t==t.lower() else 1),totmat)
                #print((-1 if t==t.lower() else 1)*(heatmaps[t.lower()])((i,j),(-1 if t==t.lower() else 1),totmat))
    return s
def value(position, depth, qiav): #THE EVAL OF THE CURRENT POSITION FOR THE CURRENT PLAYER
    #qiav = quit if above val. If an opponent punishes to above val then ignore that subtree.
    white_to_move = position.turn
    k = (1 if white_to_move else -1)
    if depth==0:
        #print(material(position))
        return (k*material(position))
    
    max_val = -inf
    for i in position.legal_moves:
        #if max_val<cur_max:
        #    #print(max_val)
        #    return cur_max
        board2 = deepcopy(position)
        board2.push_san(str(i))
        #print(board2)
        max_val = max(-value(board2,depth-1,-max_val),max_val)
        if max_val>qiav:
            return inf #just quit the subtree
    return max_val
def move(value_function, position, depth=1):
    values = {}
    for i in position.legal_moves:
        board2 = deepcopy(position)
        board2.push_san(str(i))
        values[str(i)] = -value_function(board2,depth,inf)
        #print(str(i),values[str(i)])
    #print(values)
    return str(max(values, key=values.get)) 
def run_move(position):
    return position.push_san(move(value, position, depth=1))