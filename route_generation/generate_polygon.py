import json
import math
import random
import time

import matplotlib.pyplot as plt


numberOfEdges = 6  # Number of edges on polygon
radius = 0.02  # Radius (polar co-ordinates)
deltaTheta = (2 * math.pi) / numberOfEdges  # Change in angle per point (polar co-ordinates)
start = [51.51252708580286, -0.23775554620156397]

# Hacked together using the code sample from https://stackoverflow.com/questions/63374864/random-circular-route-generator

# For each delta theta defining a list of X and Y co-ordinates for the unit circle polygon and
# generating a random polygon by varying the radius

currentTheta = 0
coordsPolygon = [[0, 0]]
coordsRandomPolygon = [[0, 0]]
perimeterPolygon = 0
perimeterRandomPolygon = 0
randomRadiusLst = []
for i in range(numberOfEdges):
    currentTheta += deltaTheta
    randomRadius = radius - random.uniform(0, (0.2 * radius))
    randomRadiusLst.append(randomRadius)

    if (i == (numberOfEdges - 1)):
        coordsPolygon.append([0, 0])
        coordsRandomPolygon.append([0, 0])
    else:
        coordsPolygon.append([radius * math.cos(currentTheta), radius * math.sin(currentTheta)])
        coordsRandomPolygon.append([randomRadius * math.cos(currentTheta), randomRadius * math.sin(currentTheta)])

        # Distance between points for unit circle polygon and random polygon
    perimeterPolygon += math.sqrt((coordsPolygon[i][0]-coordsPolygon[i-1][0])**2 + (coordsPolygon[i][1]-coordsPolygon[i-1][1])**2)
    perimeterRandomPolygon += math.sqrt((coordsRandomPolygon[i][0]-coordsRandomPolygon[i-1][0])**2 + (coordsRandomPolygon[i][1]-coordsRandomPolygon[i-1][1])**2)


# Scaling the random polygon to the perimeter of the original unit circle
scalingFactor = perimeterPolygon / perimeterRandomPolygon
currentTheta = 0
coordsRandomPolygonScaled = [[0, 0]]
perimeterScaledRandomPolygon = 0
for i in range(numberOfEdges):
    currentTheta += deltaTheta
    if (i ==  (numberOfEdges - 1)):
        coordsRandomPolygonScaled.append([0, 0])
    else:
        coordsRandomPolygonScaled.append([(randomRadiusLst[i] * scalingFactor) * math.cos(currentTheta), (randomRadiusLst[i] * scalingFactor) * math.sin(currentTheta)])

    perimeterScaledRandomPolygon += math.sqrt((coordsRandomPolygonScaled[i][0]-coordsRandomPolygonScaled[i-1][0])**2 + (coordsRandomPolygonScaled[i][1]-coordsRandomPolygonScaled[i-1][1])**2)


def perturb_alternating_points(coords, noise_factor=1):
    lims = (noise_factor * radius)
    print(coords)
    for idx, val in enumerate(coords):
        if idx % 2 == 1:
            print("HI", idx)
            xpert = random.uniform(-lims, lims)
            ypert = random.uniform(-lims, lims)
            print(coords[idx])
            coords[idx] = [coords[idx][0]+xpert, coords[idx][1]+ypert]
            print(coords[idx])
    print(coords)
    return coords


def snap_coord(coord):
    print(f"coord{coord}")
    import requests
    time.sleep(2)
    params = (
    )
    request = f'https://router.project-osrm.org/nearest/v1/walking/{coord[1]},{coord[0]}'
    print(request)
    response = requests.get(request, params=params)

    json = response.json()
    return json['waypoints'][0]['location']


coordsRandomPolygon = [[i[0]+start[0], i[1]+start[1]] for i in coordsRandomPolygon]

xs, ys = zip(*coordsRandomPolygon)
perturbed = perturb_alternating_points(coordsRandomPolygon.copy())
xs2, ys2 = zip(*perturbed)
plt.figure()
plt.plot(xs, ys)
plt.plot(xs2, ys2, color="r")
plt.savefig("test.png")

with open('original.json', 'w') as outfile:
    json.dump([snap_coord(i) for i in coordsRandomPolygon], outfile)
with open('perturbed.json', 'w') as outfile:
    json.dump([snap_coord(i) for i in perturbed], outfile)
