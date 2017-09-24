print "Hi! Welcome to game.py"
name = raw_input("What's your name? ")
print "Hi Mr/Miss: " + name
world_size = 5
current_position = 0

print "Your current position is " + str(current_position)

command = raw_input("What do you want to do? ")
if command == 'f':
    next_position = current_position+1
    current_position=next_position
    print "Your current position is " + str(current_position)

print "The End"
print "Copyright 2017"