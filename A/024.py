five = ten = 0
for num in bills:
	if num == 5:
		five += 1
	elif num == 10 and five:
		five -= 1
		ten += 1
	elif num == 20 and ten and five:
		five -= 1
		ten -= 1
	elif num == 20 and five > 3:
		five -= 3
	else:
		return False
return True