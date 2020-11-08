from datetime import datetime
import time

# A burger takes 1 second to prepare + 3 seconds more for each layer we have.
def makeBurger(layers):
	print("Flipping Burgers 🍔, hold on to your pants!")
	time.sleep(1 + (3 * len(layers)))
	message = f"Your burger with {', '.join(map(str, layers))} is ready"
	return message

def deliverBurger(address):
	if address != None:
		print(f"Order will be delivered on {datetime.now()}")
	else:
		print("Address can't be empty, we gonna eat this!")


def packBurger():
	print("Adding extra fries 🍟")
	time.sleep(2)
	print("Adding candy 🍭 \n")


def orderBurger(layers, address):
	# Making sure we get the return value from the function!
	print(makeBurger(layers))
	packBurger()
	deliverBurger(address)


layers = ["🥬", "🧀", "🥔", "🍅", "🧂", "wholewheat fried buns"]
address = "bro"
orderBurger(layers, address)
