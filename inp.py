def int_input(message="> "):
	i = input(message)
	try:
		i = int(i)
	except:
		print("Not an integer. Please try again.")
		return int_input(message)
	return i
