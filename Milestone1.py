import math
import numpy as np
temp=[]
f = open("Milestone1\Input\Testcase1.txt", "r")
for x in f:
  temp.append(x.replace('\n', ' ').split(":"))
details={}
for i in range(0,len(temp)):
  details[temp[i][0]]=int(temp[i][1])
f.close()
diamater=details[temp[0][0]]
num=details[temp[1][0]]
angle=details[temp[2][0]]
radius=diamater/2
x1=-(radius*math.cos((math.radians(angle))))
y1=-(radius*math.sin((math.radians(angle))))
x2=radius*math.cos(math.radians(angle))
y2=radius*math.sin(math.radians(angle))
distance=diamater/(num-1)
points=[]
def get_point_on_vector(initial_pt, terminal_pt, distance):
    v = np.array(initial_pt, dtype=float)
    u = np.array(terminal_pt, dtype=float)
    n = v - u
    n /= np.linalg.norm(n, 2)
    point = v - distance * n
    return tuple(point)
dt=0
for i in range(0,num):
  points.append(get_point_on_vector((x1,y1),(x2,y2),dt))
  dt+=distance
with open('Output1-1.txt', 'w') as f:
    for point in points:
        f.write(str(point))
        f.write('\n')