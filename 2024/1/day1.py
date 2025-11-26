with open("input", 'r') as f:
	lines = f.readlines()
left = []
right = []
for line in lines:
	leftNum, rightNum = line.split()
	left.append(int(leftNum))
	right.append(int(rightNum))
left.sort()
right.sort()
distances = []
distance = 0
for i in range(len(left)):
	distances.append(abs(left[i]-right[i]))
	distance += abs(left[i]-right[i])
#print(right[0:3])
#print(left[0:3])
print(distances[0:3])
print(distance)
