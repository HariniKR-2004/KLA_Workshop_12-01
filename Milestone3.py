import math
import numpy as np
temp = []
with open("Milestone3/Input/Testcase1.txt", "r") as f:
    for x in f:
        temp.append(x.replace('\n', '').split(":"))

details = {}
for i in range(0, len(temp)):
    dkey, value = temp[i][0], temp[i][1].strip()
    if "x" in value:
        details[dkey] = tuple(map(int, value.split("x")))
    else:
        if value.startswith("(") and value.endswith(")"):
            details[dkey] = tuple(map(int, value[1:-1].split(',')))
        else:
            details[dkey] = int(value)
f.close()
print(details)
diameter=details[temp[0][0]]
size=details[temp[1][0]]
shiftVector=details[temp[2][0]]
distance=details[temp[3][0]]
dieStreet=details[temp[4][0]]
recticleStreet=details[temp[5][0]]
diesPerReticle=details[temp[6][0]]
tempSize=[size[0]*diesPerReticle[1]+dieStreet[0]*diesPerReticle[1]+recticleStreet[0],size[1]*diesPerReticle[0]+dieStreet[1]*diesPerReticle[0]+recticleStreet[1]]
print(tempSize)
dieSize=[tempSize[0]-recticleStreet[0],tempSize[1]-recticleStreet[1]]
print(dieSize)
num1=(diameter/tempSize[0])+2
num2=(diameter/tempSize[1])+2
num1=int(num1)
num2=int(num2)
def rectangle_corners(top_left_x, top_left_y, width, height):
    top_left = (top_left_x, top_left_y)
    top_right = (top_left_x + width, top_left_y)
    bottom_left = (top_left_x , top_left_y + height)
    bottom_right = (top_left_x + width, top_left_y + height)
    return top_left, top_right, bottom_left, bottom_right
def is_point_inside_circle(point, circle_origin, diameter):
    distance = math.sqrt((point[0] - circle_origin[0])**2 + (point[1] - circle_origin[1])**2)
    return distance < diameter / 2
referBleft=[distance[0] - dieSize[0] / 2, distance[1] - dieSize[1] / 2]
print(referBleft)
x_local=distance[0]-referBleft[0]
y_local=distance[1]-referBleft[1]
referDiePosition=[y_local//(dieSize[1]/diesPerReticle[0]),x_local//(dieSize[0]/diesPerReticle[1])]
misplace=[int((referBleft[0]-shiftVector[0])/tempSize[0]), int((referBleft[1]-shiftVector[1])/tempSize[1])]
misplace=[int(misplace[0]*diesPerReticle[1]+referDiePosition[0]),int(misplace[1]*diesPerReticle[0]+referDiePosition[1])]
firstCoord=(shiftVector[0]-tempSize[0]*num1,shiftVector[1]+tempSize[1]*num2)
print(firstCoord)
firstCoord=(firstCoord[0],firstCoord[1]+tempSize[1])
print(firstCoord)
print(num1,num2)
index=(-num1*diesPerReticle[1],num2*diesPerReticle[0])
print(index)
points={}
temp=list(firstCoord)
for i in range(0,num1+num1+1):
    temp[1]-=recticleStreet[1]
    for j in range(0,num2+num2+1):
        harini=list(temp)
        for k in range(0,diesPerReticle[0]):
            temp[1]-=dieStreet[1]
            for l in range(0,diesPerReticle[1]):
                topLeft,topRight,bottomLeft,bottomRight=rectangle_corners(temp[0],temp[1],size[0],size[1])
                print((index[0]+i)+l+(i*(diesPerReticle[1]-1)), (index[1]-j)-k-(j*(diesPerReticle[0]-1)))
                if(is_point_inside_circle(topLeft,(0,0),diameter) or is_point_inside_circle(topRight,(0,0),diameter) or is_point_inside_circle(bottomLeft,(0,0),diameter) or is_point_inside_circle(bottomRight,(0,0),diameter)):
                    points[((index[0]+i)+l+(i*(diesPerReticle[1]-1))-misplace[0],(index[1]-j)-k-(j*(diesPerReticle[0]-1))-misplace[1])]=bottomLeft
                temp[0]+=(size[0]+dieStreet[0])
            temp[0]=harini[0]
            temp[1]-=size[1]
        temp[1]-=tempSize[1]
    temp[1]=firstCoord[1]
    temp[0]=firstCoord[0]+(tempSize[0]*(i+1))+recticleStreet[0]
with open('Output3-1.txt', 'w') as f:
    for point in points:
        f.write(str(point))
        f.write(" : ")
        f.write(str(points[point]))
        f.write('\n')