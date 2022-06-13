#variables
direction = 0 #0 N, 1 W, 2 S, 3 E
distance_x = 0 #displacement
distance_y = 0 #displacement

n = int(input())

for x in range(n):
    while 1:
        a = int(input())
        if a == 0:
            break
        if a == 2:
            direction -= 1
            if direction == -1:
                direction = 3
        elif a == 3:
            direction += 1
            if direction == 4:
                direction = 0
            
        else:
            b = int(input())
            #move forward b units in variable direction way
            if direction == 0:
                distance_y += b#displacement travelled not displacement needed to be travelled
            elif direction == 1:
                distance_x += b
            elif direction == 2:
                distance_y -= b
            else:
                distance_x -= b
 
    print(f'Distance is {abs(distance_x)+abs(distance_y)}')
    while 1:
        if distance_x == 0 and distance_y == 0:
            break

        elif direction == 0:

            if distance_y < 0:
                print(1)
                print(abs(distance_y))
                distance_y = 0
            
            else:
                if distance_x > 0:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                elif distance_x < 0:
                    print(3)#
                    direction += 1
                    if direction == 4:
                        direction = 0
                elif distance_x == 0:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3

        elif direction == 2:

            if distance_y > 0:
                print(1)
                print(abs(distance_y))
                distance_y = 0
            
            else:
                if distance_x > 0:
                    print(3)
                    direction += 1 
                    if direction == 4:
                        direction = 0
                elif distance_x < 0:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                else:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                #else change direction twice
        elif direction == 3:

            if distance_x > 0:
                print(1)
                print(abs(distance_x))
                distance_x = 0
            
            else:
                if distance_y > 0:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                elif distance_y < 0:
                    print(3)
                    direction += 1
                    if direction == 4:
                        direction = 0
                else:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3

        elif direction == 1:

            if distance_x < 0:
                print(1)
                print(abs(distance_x))
                distance_x = 0
            
            else:
                if distance_y < 0:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                elif distance_y > 0:
                    print(3)
                    direction += 1
                    if direction == 4:
                        direction = 0
                else:
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
                    print(2)
                    direction -= 1
                    if direction == -1:
                        direction = 3
    if x != n-1:
        print()