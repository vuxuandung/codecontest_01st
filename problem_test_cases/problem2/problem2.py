import sys

n = int(raw_input())
bills = map(int, raw_input().split())

got25 = 0
got50 = 0

for b in bills:
	if b == 25:
		got25 += 1
	elif b == 50:
		if got25 > 0:
			got25 -= 1
			got50 += 1
		else:
			print "NO"
			sys.exit(0)
	elif b == 100:
		if got25 > 0 and got50 > 0:
			got50 -= 1
			got25 -= 1
		elif got25 > 2:
			got25 -= 3
		else:
			print "NO"
			sys.exit(0)

print "YES"