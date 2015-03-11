s1 = [100000, 7000, 3000, 300]
s2 = [100000, 7000, 3000, 90000]

def cosine(data):
    return AUB/(A*B)**.5

#print cosine(s1)
#print cosine(s2)

s3 = [10000, 5000, 600, 100000]
s4 = [100, 100, 1, 200]
s5 = [100000/2, 100000/2, 1, 100000]
s6 = [1000000, 10000, 100, 1000000000]

def epsilon(data):
    AUB = float(data[2])
    A = float(data[0])
    B = float(data[1])
    total = float(data[3])
    PA = A/total
    PB = B/total
    PAUB = AUB/total
    PAB = PAUB/PB
    PBA = PAUB/PA
    print PAB, PBA
    return (PAB + PBA)/2

print epsilon(s3)

