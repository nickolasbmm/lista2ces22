import random
import time

def share_diagonal(x0,y0,x1,y1):
    dy = abs(y1-y0)
    dx = abs(x1-x0)
    return dx == dy

def col_clashes(bs,c):

    for i in range(c):
        if share_diagonal(i,bs[i],c,bs[c]):
            return True
    return False

def has_clashes(the_board):

    for col in range(1,len(the_board)):
        if col_clashes(the_board,col):
            return True
    return False

def find_solutions(n,want_to_print=True):
    
    rng = random.Random()

    bd = list(range(n))
    num_found = 0
    tries = 0
    while num_found<10:
        rng.shuffle(bd)
        tries+=1
        if not has_clashes(bd):
            if(want_to_print):
                print("Found solultion {0} in {1} tries.".format(bd,tries))
            tries = 0
            num_found+=1


#Solve for n = 4
print("Solutions for n = 4") 
find_solutions(4)
#Solve for n = 12 
print("Solutions for n = 12") 
find_solutions(12)
#Solve for n = 16 
print("Solutions for n = 16") 
find_solutions(16)

print("Bruteforce to find the size so the calculations are done in less than a minute")
t1 = time.time()
t2 = time.time()
n=3
t_ant = t2-t1
while t2-t1 <= 60:
    print("A board of size {0} runs at time {1} seconds".format(n,t_ant))
    t_ant = t2-t1
    n+=1
    t1 = time.time()
    find_solutions(n,False)
    t2 = time.time()
print("A board of size {0} runs at time {1} seconds".format(n,t_ant))

n-=1
print("Answer: Board of size n = ",n)