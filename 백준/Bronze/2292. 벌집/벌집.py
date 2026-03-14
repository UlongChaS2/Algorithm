import sys

n = int(sys.stdin.readline())
layer = 1
max_room_in_layer = 1

while n > max_room_in_layer:
    max_room_in_layer += 6 * layer
    layer += 1   
        
print(layer)