

def direction_d(d,turn):

	if ( d == "east" , turn == "1" ):
		d = "north"
	return d

	if ( d == "east" , turn == "2" ):
		d = "south"
	return d

	if ( d == "west" , turn == "1" ):
		d = "south"
	return d

	if ( d == "west" , turn == "2" ):
		d = "north"
	return d

	if ( d == "north" , turn == "1" ):
		d = "west"
	return d

	if ( d == "north" , turn == "2" ):
		d = "east"
	return d

	if ( d == "south" , turn == "1" ):
		d = "east"
	return d

	if ( d == "sourh" , turn == "2" ):
		d = "west"
	return d

def direction_x(d,x,turn,delta_x,delta):

	if ( d == "east" , turn == "1" ):
		d = "north"
		x += delta*10
	return x

	if ( d == "east" , turn == "2" ):
		d = "south"
		x += delta*10
	return x

	if ( d == "west" , turn == "1" ):
		d = "south"
		x += delta*(-10)
	return x

	if ( d == "west" , turn == "2" ):
		d = "north"
		x += delta*(-10)
	return x

def direction_y(d,y,turn,delta_y,delta):

	if ( d == "north" , turn == "1" ):
		d = "west"
		y += delta*10
	return y

	if ( d == "north" , turn == "2" ):
		d = "east"
		y += delta*10
	return y

	if ( d == "south" , turn == "1" ):
		d = "east"
		y += delta*(-10)
	return y

	if ( d == "sourh" , turn == "2" ):
		d = "west"
		y += delta*(-10)
	return y


turn = "1"
d = "north"
begin = 0
delta = int()
time = int()
delta_x = int()
delta_y = int()




while ( turn >= "1" and turn <= "3" ) :
	x = int()
	y = int()
	begin = time
	time = int(raw_input())
	delta = time - begin
	delta *= 10
	turn = str(raw_input())
	if ( turn == "3" ) :
		print x, y
		break
	print d
	

	
	direction_x(d,x,turn,delta_x,delta)
	x = direction_x
	direction_y(d,y,turn,delta_y,delta)
	y = direction_y
	direction_d(d,turn)
	d = direction_d
	



	