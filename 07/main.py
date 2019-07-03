score = input("Enter Score: ")
try:
	fscore = float(score)
except:
    print("Please, enter a valid number ;)")
    quit()

if fscore > 1:
    print("Value too high! :(")
elif fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")    
elif fscore >= 0.6:
    print("D")
elif fscore >= 0:
    print("E")
else:
	print("Value too low! :(")