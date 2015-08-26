def direction_d(d,turn):
    if ( d == "east" and turn == "1" ):
        d = "north"
        return d

    if ( d == "east" and turn == "2" ):
        d = "south"
        return d

    if ( d == "west" and turn == "1" ):
        d = "south"
        return d

    if ( d == "west" and turn == "2" ):
        d = "north"
        return d

    if ( d == "north" and turn == "1" ):
        d = "west"
        return d

    if ( d == "north" and turn == "2" ):
        d = "east"
        return d

    if ( d == "south" and turn == "1" ):
        d = "east"
        return d

    if ( d == "south" and turn == "2" ):
        d = "west"
        return d

    return d

def direction_x(d,x,turn,delta):

    if ( d == "east" and turn == "1" ):
        x += delta*10
        return x

    if ( d == "east" and turn == "2" ):
        x += delta*10
        return x

    if ( d == "east" and turn == "3" ):
        x += delta*10
        return x

    if ( d == "west" and turn == "1" ):
        x += delta*(-10)
        return x

    if ( d == "west" and turn == "2" ):
        x += delta*(-10)
        return x

    if ( d == "west" and turn == "3" ):
        x += delta*(-10)
        return x

    return x

def direction_y(d,y,turn,delta):

    if ( d == "north" and turn == "1" ):
        y += delta*10
        return y

    if ( d == "north" and turn == "2" ):
        y += delta*10
        return y

    if ( d == "north" and turn == "3" ):
        y += delta*10
        return y

    if ( d == "south" and turn == "1" ):
        y += delta*(-10)
        return y

    if ( d == "sourh" and turn == "2" ):
        y += delta*(-10)
        return y

    if ( d == "south" and turn == "3" ):
        y += delta*(-10)
        return y

    return y


turn = "1"
d = "north"
begin = 0
delta = 0
time = 0
x = 0
y = 0



while ( turn >= "1" and turn <= "3" ) :
    begin = time
    time = int(raw_input())
    delta = time - begin

    while ( delta < 0 ) :
        print "Your car should not go backwards,please eset your time again"
        time = int(raw_input("time: "))
        delta = time - begin
    
    turn = str(raw_input())

    while (turn > "3" or turn < "1"):
        print "Please reset your \"turn\""
        turn = str(raw_input("turn: "))
        
    x = direction_x(d,x,turn,delta)
    y = direction_y(d,y,turn,delta)
    d = direction_d(d,turn)


    if (turn == "3"):
        print x, y
        break


    



