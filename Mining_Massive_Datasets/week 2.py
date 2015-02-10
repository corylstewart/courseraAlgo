def euclid(x1, y1, x2, y2):
    return pow((pow(x2-x1,2) + pow(y2-y1,2)), .5)

def manhat(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1)

def question_3a():
    x = [55, 61, 53, 51]
    y = [5, 10, 10, 18]


    for i in range(len(x)):
        print (x[i],y[i])
        print euclid(0, 0, x[i], y[i]), euclid(100, 40, x[i], y[i]), euclid(0, 0, x[i], y[i]) > euclid(100, 40, x[i], y[i])
        print manhat(0, 0, x[i], y[i]), manhat(100, 40, x[i], y[i]), manhat(0, 0, x[i], y[i]) < manhat(100, 40, x[i], y[i])

def question1_b():
    items = 1000000
    n = [100000, 50000, 10000, 20000]
    m = [40000000, 200000000, 50000000, 60000000]
    s = [800000000, 2500000000, 600000000, 1000000000]
    n = [10000]
    m = [40000000]
    s = [200000000]

    for i in range(len(n)):
        total = 0
        total += 4*2*items #item names to integers
        total += 4*1000000 #all names
        total += 4*10000 #frequent items
        total += 4*m[i]
        print total/100000000., s[i]/100000000.


#question1_b()

def question1_c():
    frequent_buckets = 1e6
    s = [500000000, 500000000, 200000000, 100000000]
    p = [3200000000, 5000000000, 1600000000, 120000000]

    for i in range(len(s)):
        pairs = s[i]*s[i]/5e7-p[i]
        print pairs

question1_c()