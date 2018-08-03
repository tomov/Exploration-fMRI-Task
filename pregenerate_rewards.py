nTrials = 10
nBlocks = 4
nRuns = 8
Trial = 0
reward = 0
b = 0
sd = [0, Math.sqrt(16)]
L = ["S", "R"]
sd0 = Math.sqrt(100)
mu = new Array()
mode = 0
k1 = random.randint(0, 49)*2
k2 = random.randint(0, 49)*2

#generate a list of random numbers ----
import random

k1_list = []
k2_list = []

for i in range(0,49):
	k1 = random.randint(1, 49, size = 10)*2
	k2 = random.randint(1, 49, size = 10)*2
	list.append(k1)
	list.append(k2)

print(k1_list)
print(k2_list)


