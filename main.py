name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
	"You are on a dirt road, it has come to an end and you can go "
	"left or right. Which way would you like to go? ").lower()
if answer == "left":
	answer = input(
		"You come to a river, you can walk around it or swim across? "
		"Type walk to walk around and swim to swim across: ")
	if answer == "swim":
		print("There was a crocodile in the river. You have died.")

	elif answer == "walk":
		answer = input(
			"You reach the end of the river. You've been lost for hours. You find a bush of berries. Do you eat "
			"the berries or continue your journey? Type eat to eat the berries. Type continue to continue"
			"your journey.")
		if answer == "eat":
			print("You ate the berries and have died from poisoning.")
		elif answer == "walk":
			answer = input(
				"You continue walking for another mile and have found a city. Your adventure has ended successfully.")
	else:
		print("Not a valid option. You lose.")
elif answer == "right":
	print("You found the city. Your adventure has ended successfully.")
else:
	print("Not a valid option. You lose.")