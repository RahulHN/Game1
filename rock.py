import random
l=["r","p","s"]
while True:
	#taking input from the user
	u=input("Enter your choice,Press n to discontinue")
	#to exit
	if u=='n':
		print("Game Over")
		exit()
	#input from the computer	
	c=random.choice(l)
	print("Computer chooses",c)
	#comparing user and computer choice

	if u==c:
		print("Tie")	
	elif u=="r"	and c=="p":
		print("Comp wins")
	elif u=="r" and c=="s":
		print("User wins")
	elif u=="p" and c=="r":
		print(" user wins")
	elif u=="p" and c=="s":
		print("comp  wins")
	elif u=="s" and c=="r":
		print(" comp wins")
	elif u=="s" and c=="p":
		print("user wins")
