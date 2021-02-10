import requests
import time
import json

with open("original.json", "r") as infile:
    initial_coords = json.load(infile)
with open("perturbed.json", "r") as infile:
    perturbed_coords = json.load(infile)

def get_snapped_route(coords):
    time.sleep(2)
    coords_as_str= []
    for coord in coords:
        coords_as_str.append(f"{coord[0]},{coord[1]}")
    coordsstr = ";".join(coords_as_str)

    params = {
        ('overview', 'full'),
        ('alternatives', 'false')
    }
    request = f'https://router.project-osrm.org/route/v1/walking/{coordsstr}'
    response = requests.get(request, params=params)

    json = response.json()
    return json


perturbed = get_snapped_route(perturbed_coords)['routes'][0]['geometry']
with open("perturbed.txt", 'w') as outfile:
    outfile.write(perturbed)
original = get_snapped_route(initial_coords)['routes'][0]['geometry']
with open("original.txt", 'w') as outfile:
    outfile.write(original)
