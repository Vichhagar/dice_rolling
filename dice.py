from random import randint as r
class Dice:
	def __init__(self, side=6):
		self.side = side

	def show_side(self):
		print(f"This dice have {self.side} side(s) by default")

	def change_side(self):
		new_side = int(input("How many side you want your dice to be: "))
		if new_side > self.side:
			self.side = new_side
		else:
			print("Dice cannot have less than 6 sides, set to 6 sides by default")
		return new_side

	def roll(self):
		time = int(input("How many time you want to roll the dice: "))
		print(f"This is the result of rolling a dice {time} times is: ")
		for i in range(time):
			#ran = r(1,self.side)
			print (r(1,self.side))
		#print (ran)


test_roll = Dice()
test_roll.show_side()
#test_roll.change_side()
test_roll.roll()