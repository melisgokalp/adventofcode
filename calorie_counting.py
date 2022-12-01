
import heapq
import time
start_time = time.time()

f = open("calories.txt", "r")

text = f.readlines()

maxcal = 0
current = 0
line = ''
top3 = [float('-inf'),float('-inf'),float('-inf')]
# data = []
for line in text:
    line = line.strip()
    if line == '':
        #part 1
        # maxcal = max(current, maxcal)

        #part 2
        if current > top3[0]:
            top3.pop(0)
            top3.append(current)
            top3.sort()
        # heapq.heappush(data, -current)
        # data.append(current)

        current = 0
    else:
        current += int(line) 

# part1_ans = maxcal
# part2_ans = sum(top3)

# maxheap sol
# part2_ans = -sum(data[:3])

# data.sort()
# part2_ans = sum(data[-3:])
print("Process finished --- %s seconds ---" % (time.time() - start_time))
