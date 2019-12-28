import time
class pos(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)


with open('./input.txt', 'r') as f:
    wire_1 = f.readline().rstrip('\n\r').split(',');
    wire_2 = f.readline().rstrip('\n\r').split(',');

def getPositions(wire):
    positions = []
    positions.append([0,0])
    for step in wire:
        direction = step[0]
        distance = int(step[1:])
        if(direction=='L'):
            for d in range(0,distance):
                last_x = positions[-1][0]
                last_y = positions[-1][1]
                positions.append([last_x-1, last_y])
        elif(direction=='R'):
            for d in range(0,distance):
                last_x = positions[-1][0]
                last_y = positions[-1][1]
                positions.append([last_x+1, last_y])
        elif(direction=='U'):
            for d in range(0,distance):
                last_x = positions[-1][0]
                last_y = positions[-1][1]
                positions.append([last_x, last_y+1])
        elif(direction=='D'):
            for d in range(0,distance):
                last_x = positions[-1][0]
                last_y = positions[-1][1]
                positions.append([last_x, last_y-1])
    return positions

pos_wire_1 = getPositions(wire_1)
pos_wire_2 = getPositions(wire_2)

manhattan_distance_cross_pos = []


time_start = time.time();

for index_pos_1, pos_1 in enumerate(pos_wire_1):
    if(index_pos_1%1000 == 0):
        print('time: ', index_pos_1, time.time()-time_start)
    if pos_1 in pos_wire_2:
        manhattan_distance_cross_pos.append([abs(pos_1[0])+abs(pos_1[1]), index_pos_1+pos_wire_2.index(pos_1)])

manhattan_distance_cross_pos = manhattan_distance_cross_pos[1:]
print(manhattan_distance_cross_pos)

