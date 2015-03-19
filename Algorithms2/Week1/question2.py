def read_file(filename):
    jobs = []
    with open(filename) as f:
        number_of_jobs = int(f.readline())
        count = 1
        for line in f.readlines():
            job = line.split()
            weight = int(job[0])
            length = int(job[1])
            jobs.append((float(weight)/length, weight, length, count))
            count += 1
    return jobs

def weighted_completion_time(jobs):
    total = 0
    current_time = 0
    for job in jobs:
        weight = job[1]
        length = job[2]
        current_time += length
        total += current_time * weight
    return total

jobs = read_file('jobs.txt')
jobs.sort(reverse=True)
print weighted_completion_time(jobs)