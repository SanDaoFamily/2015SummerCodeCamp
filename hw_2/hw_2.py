x = int()
y = int()
x_ = int()
y_ = int()
turn = str()
turn_ = str()
time = int()
delta = int()
delta_ = int()

def direction(d,turn_):
	if (d == "north" and turn_ == "1"):
		d = "west"
	elif (d == "north" and turn_ == "2"):
		d = "east"
	elif (d == "east" and turn_ == "1"): 
		d = "north"
	elif (d == "east" and turn_ == "2"):
		d = "south"
	elif (d == "south" and turn_ == "1"):
		d = "east"
	elif (d == "south" and turn_ == "2"):
		d = "west"
	elif (d == "west" and turn_ == "1"):
		d = "south"
	else:
		d = "north"
		return d


def position_x(x_,d):
	if (d == "west"):
		x_ *= -1
	elif (d == "east"):
		x_ *= 1	
	return x_

def position_y(y_,d):
	if (d == "north"):
		y_ *= 1
	elif (d == "south"):
		y_ *= -1	
	return y_


begin = int(raw_input())
begin *= 10
turn = "1"


while (turn>="1" and turn<="3"):
	turn = raw_input()
	if (turn == "3"):
		print x, y
		break
	
	y += begin

	time = int(raw_input())
	
	delta_ = time - begin
	turn_ = turn
	x_ = 1
	y_ = 1
	d = str("north")
	direction(d,turn_)
	d = direction(d,turn_)
	position_x(x_,d)
	x_ = position_x(x_,d)
	x += delta_ * x_ * 10
	position_y(y_,d)
	y_ = position_y(y_,d)
	y += delta_ * y_ * 10

