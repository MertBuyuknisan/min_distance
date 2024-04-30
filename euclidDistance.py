import math
points=[(2,3),(1,4),(5,6),(3,5)]
def euclidean_distance(point1,point2):
    x1,y1=point1
    x2,y2=point2
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
distances=[]
for i in range (len(points)):
    for j in range (i+1,len(points)):
        distance=euclidean_distance(points[i],points[j])
        distances.append(distance)

min_distance=min(distances)
print("Minimum distance: ",min_distance)





