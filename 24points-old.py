
def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def cmpt(a, b, c):
	if c == 0: 
		return a+b
	if c == 1:
		return a-b
	if c == 2:
		return a*b
	if c == 3:
		if b == 0:
			return 0x7fffffff
		else:
			return a/b


def sym(c):
	if c == 0: 
		return ' + '
	if c == 1:
		return ' - '
	if c == 2:
		return ' * '
	if c == 3:
		return ' / '


def makeAns(nums, i, j, k, br):
	n0 = str(nums[0])
	n1 = str(nums[1])
	n2 = str(nums[2])
	n3 = str(nums[3])
	if br == 0:#ijk
		return '(' + '(' + n0 + sym(i) + n1 + ')' + sym(j) + n2 + ')' + sym(k) + n3
	elif br == 1:#ikj
		return '(' + n0 + sym(i) + n1 + ')' + sym(j) + '(' + n2 + sym(k) + n3 + ')'
	elif br == 2:#jik
		return '(' + n0 + sym(i) + '(' + n1 + sym(j) + n2 + ')' + ')' + sym(k) + n3
	elif br == 3:#jki
		return n0 + sym(i) + '(' + '(' + n1 + sym(j) + n2 + ')' + sym(k) + n3 + ')'
	elif br == 4:#kij
		return '(' + n0 + sym(i) + n1 + ')' + sym(j) + '(' + n2 + sym(k) + n3 + ')'
	elif br == 5:#kji
		return n0 + sym(i) + '(' + n1 + sym(j) + '(' + n2 + sym(k) + n3 + ')' + ')'


def getAns(nums, ans, points):
	for i in range(4):
		for j in range(4):
			for k in range(4):
				a1 = cmpt(nums[0], nums[1], i)
				a2 = cmpt(nums[1], nums[2], j)
				a3 = cmpt(nums[2], nums[3], k)
				b_ij = cmpt(a1, nums[2], j)
				b_ji = cmpt(nums[0], a2, i)
				b_jk = cmpt(a2, nums[3], k)
				b_kj = cmpt(nums[1], a3, j)
				#ijk
				if cmpt(b_ij, nums[3], k) == points:
					ans.append(makeAns(nums, i, j, k, 0))
				#ikj
				if cmpt(a1, a3, j) == 24:
					ans.append(makeAns(nums, i, j, k, 1))
				#jik
				if cmpt(b_ji, nums[3], k) == points:
					ans.append(makeAns(nums, i, j, k, 2))
				#jki
				if cmpt(nums[0], b_jk, i) == points:
					ans.append(makeAns(nums, i, j, k, 3))
				#kij
				#...same with ikj
				#kji
				if cmpt(nums[0], b_kj, i) == points:
					ans.append(makeAns(nums, i, j, k, 5))


def permAndGetAns(nums, h, t, ans, points):
	if h >= t:
		getAns(nums, ans, points)
		#print nums
	else:
		for i in range(h, t+1):
			if i == h:
				permAndGetAns(nums, h+1, t, ans, points)
			elif nums[i] != nums[h]:
				swap(nums, i, h)
				permAndGetAns(nums, h+1, t, ans, points)
				swap(nums, i, h)


ss = raw_input("Please input the points you want to get (default is 24):")
if ss == '':
	points = 24
else:
	points = float(ss)
ss = raw_input("Please input 4 number separated by space:").split()
nums = []
for item in ss:
	nums.append(float(item))

ans = []

permAndGetAns(nums, 0, 3, ans, points)

print 'There are ' + str(len(ans)) + ' solutions:'
for item in ans:
	print item + ' = ' + str(points)
