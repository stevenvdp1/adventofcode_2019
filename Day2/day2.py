with open('./input.txt','r') as f:
    data =  f.read().split(',');
data = list(map(int, data))

def getOutput(noun, verb):
    _data = list(data)
    print(noun, verb)
    _data[1] = noun
    _data[2] = verb

    index = 0
    print()
    while True:
        if(_data[index] == 1):
            p_1 = _data[index+1]
            p_2 = _data[index+2]
            p_3 = _data[index+3]
            _data[p_3] = _data[p_1] + _data[p_2]
        elif(_data[index] == 2):
            p_1 = _data[index+1]
            p_2 = _data[index+2]
            p_3 = _data[index+3]
            _data[p_3] = _data[p_1] * _data[p_2]
        else:
            break
        index = index + 4
    return _data[0]

def findValue(value):
    for n in range (0,value):
        for v in range (0,100):
            output = getOutput(n,v)
            if(output == value):
                return 100*n+v

print(findValue(19690720))
