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
dicsPerReticle=details[temp[6][0]]
num1=(diameter/size[0])+2
num2=(diameter/size[1])+2
if num1%2!=0:
    num1+=1
if num2%2!=0:
    num2+=1
num1=int(num1)
num2=int(num2)
def rectangle_corners(center_x, center_y, width, height):
    top_left = (center_x - width / 2, center_y + height / 2)
    top_right = (center_x + width / 2, center_y + height / 2)
    bottom_left = (center_x - width / 2, center_y - height / 2)
    bottom_right = (center_x + width / 2, center_y - height / 2)
    return top_left, top_right, bottom_left, bottom_right
def is_point_inside_circle(point, circle_origin, diameter):
    distance = math.sqrt((point[0] - circle_origin[0])**2 + (point[1] - circle_origin[1])**2)
    return distance < diameter / 2
firstCoord=(distance[0]-size[0]*num1,distance[1]+size[1]*num2)
index=(-num1,num2)
points={}
temp=list(firstCoord)
for i in range(0,num1+num1+1):
    for j in range(0,num2+num2+1):
        topLeft,topRight,bottomLeft,bottomRight=rectangle_corners(temp[0],temp[1],size[0],size[1])
        if(is_point_inside_circle(topLeft,(0,0),diameter) or is_point_inside_circle(topRight,(0,0),diameter) or is_point_inside_circle(bottomLeft,(0,0),diameter) or is_point_inside_circle(bottomRight,(0,0),diameter)):
            points[(index[0]+i,index[1]-j)]=bottomLeft
        temp[1]-=size[1]
        if((j+1)%dicsPerReticle[1]==0):
            temp[1]-=recticleStreet[1]
    temp[1]=firstCoord[1]+dieStreet[1]
    temp[0]=firstCoord[0]+(size[0]*(i+1))+dieStreet[0]
    if((i+1)%dicsPerReticle[0]==0):
        temp[0]+=recticleStreet[0]
with open('Output3-1.txt', 'w') as f:
    for point in points:
        f.write(str(point))
        f.write(" : ")
        f.write(str(points[point]))
        f.write('\n')