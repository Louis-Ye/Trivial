#7 comparisons to sort 5 elements:

def swap(i, j, xx):
	tmp = xx[i]
	xx[i] = xx[j]
	xx[j] = tmp


# ------------------------------initialized the array here---------------------
ss = raw_input('Please input five numbers splitted with space: ').split()
a = []
for item in ss:
	a.append(float(item))

#----------------using 1 comparison--------------------
if a[0] > a[1]:
	swap(0, 1, a)
#----------------using 1 comparison--------------------
if a[2] > a[3]:
	swap(2, 3, a)
#----------------using 1 comparison--------------------
if a[0] > a[2]:
	swap(0, 2, a)
	swap(1, 3, a)
#----------------using at most 4 comparisons--------------------
if a[4] > a[2]:
	if a[3] > a[4]:
		swap(3, 4, a)
	if a[1] > a[3]:
		swap(1, 2, a)
		swap(2, 3, a)
		if a[3] > a[4]:
			swap(3, 4, a)
	else:
		if a[1] > a[2]:
			swap(1, 2, a)
else:
	swap(3, 4, a)
	swap(2, 3, a)
	if a[0] > a[2]:
		swap(1, 2, a)
		swap(0, 1, a)
		if a[2] > a[3]:
			swap(2, 3, a)
			if a[3] > a[4]:
				swap(3, 4, a)
	else:
		if a[1] > a[3]:
			swap(1, 2, a)
			swap(2, 3, a)
			if a[3] > a[4]:
				swap(3, 4, a)
		else:
			if a[1] > a[2]:
				swap(1, 2, a)
#------------------------------------
print a

