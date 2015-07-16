import random
import math

def make_s(filename):
    S = list()
    with open(filename) as f:
        total = f.readline()
        for line in f.readlines():
            S.append([int(x) for x in line.split()])
    return S

def make_vars(S):
    vars = dict()
    locs = dict()
    for i in xrange(len(S)):
        vars[abs(S[i][0])] = random.choice([-1,1])
        vars[abs(S[i][1])] = random.choice([-1,1])
        if abs(S[i][0]) not in locs:
            locs[abs(S[i][0])] = list()
        locs[abs(S[i][0])].append(i)
        if abs(S[i][1]) not in locs:
            locs[abs(S[i][1])] = list()
        locs[abs(S[i][1])].append(i)
    return vars, locs

def check_sat(clause, vars):
    if ((clause[0]^vars[abs(clause[0])]) >= 0) or ((clause[1]^vars[abs(clause[1])]) >= 0):
        return True
    else:
        return False

def make_bad_list(vars, S):
    bad_sat = []
    for clause in S:
        if not check_sat(clause, vars):
            bad_sat.append(clause)
    return bad_sat

def count_change(vars, S, locs, node):
    former = 0
    later = 0
    for x in locs[node]:
        if check_sat(S[x], vars):
            former += 1
    vars[node] = -vars[node]
    for x in locs[node]:
        if check_sat(S[x], vars):
            later += 1
    if later > former:
        return later - former
    else:
        vars[node] = -vars[node]
        return later - former

def edit_bad_sat(bad_sat, vars, S, locs, node):
    for x in locs[node]:
        if check_sat(S[x], vars):
            if S[x] in bad_sat:
                bad_sat.remove(S[x])
        else:
            bad_sat.append(S[x])
    return bad_sat

def flip(bad_sat, vars):
    change = list()
    for i in bad_sat:
        change.append(abs(i[0]))
        change.append(abs(i[1]))
    change = set(change)
    for i in change:
        vars[i] = random.choice([-1,1])
    return vars

def pap(S):
    vars, locs = make_vars(S)
    print len(vars), len(S)
    bad_sat = make_bad_list(vars, S)
    if len(bad_sat) == 0:
        return vars
    x = len(vars)
    y = x**2
    z = 2*y
    i = 0
    curr_count = 0
    while i < z:
        i += 1    
        if i%1000 == 0:
            print i, len(bad_sat)  
        selection = random.randint(0,len(bad_sat)-1)
        side = random.choice([0,1])
        if count_change(vars, S, locs, abs(bad_sat[selection][side])) > 0:
            bad_sat = edit_bad_sat(bad_sat, vars, S, locs, abs(bad_sat[selection][side]))
            curr_count = 0
        else:
            curr_count += 1
        if curr_count == 5000:
            print 'broke'
            vars = flip(bad_sat, vars)
            bad_sat = make_bad_list(vars, S)
            curr_count = 0
        if len(bad_sat) == 0:
            return vars
    return False

def solve_2_sat(S):
    for i in range(int(math.log(len(S),2))):
        print i
        sat = pap(S)
        if sat: return sat
    return False


S = make_s('2sat6.txt')


vars, locs = pap(S)