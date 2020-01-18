with open('./input.txt', 'r') as f:
   line = f.readline()

width=25
heigth=6

layers = list()

index = 0

while index < len(line) :
    layer = ''
    for h in range(0,heigth):
        layer += line[index:index+width] + '\n'
        index += width
    layers.append(layer)

best_layer = min(layers, key=lambda x: x.count('0'))
answer = best_layer.count('1') * best_layer.count('2')
print('part1: ',answer)

final_image = list()


for index in range(0,len(best_layer)):
    final_image.append('');
    print(index)
    for layer in layers:
        digit = layer[index]
        if(digit=='0'):
            final_image[index] = ' '
            break;
        elif(digit=='1'):
            final_image[index] = '1'
            break;
        elif(digit=='2'):
            final_image[index] = '2'
        else:
            final_image[index] = '\n'
            break;

print(''.join(str(e) for e in final_image))