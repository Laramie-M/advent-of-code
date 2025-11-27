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
similarity = 0
for i in left:
	if i in right:
		#print(similarity)
		similarity += i*right.count(i)
		#print(i, "Count:", right.count(i), similarity)

print(similarity)

