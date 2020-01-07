from anytree import Node, RenderTree, search, find

with open('./input.txt', 'r') as f:
   lines = f.readlines()

orbits = list()

orbits.append(Node('COM'))

while len(lines)>0:
   for l in lines:
      line = l.rstrip('\n\r').split(')')
      parent_node = find(orbits[0], lambda node: node.name == line[0])
      if parent_node:
         lines.remove(l)
         orbits.append(Node(line[1], parent=parent_node))

count = 0
for o in orbits:
   count += len(o.path) - 1

print('part1 :', count)

path_you = find(orbits[0], lambda node: node.name == 'YOU').path
path_san = find(orbits[0], lambda node: node.name == 'SAN').path

for index, l in enumerate(path_you):
   if(path_you[index] is not path_san[index]):
          moves = len(path_san)-index + len(path_you)-index - 2
          print('part2 :', moves)
          break
