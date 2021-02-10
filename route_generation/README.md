# To generate a Google Polyline for a circular walk around Shepherds Bush run the following commands

This toolchain requires the polyline Python package. To install, run
```bash
python3 -m pip install polyline --user
```

WARNING - there are hard-coded sleep signals in the scripts to adhere to the TOS of the demo OSRM server, used for GPS snapping. Only remove if using a local server..
```bash
python3 generate_polygon.py       # Generates the initial routes in x,y space and snaps them to GPS lat/long coordinates using OSRM server
python3 generate_routes.py        # Generates routes between the polygon waypoints using OSRM routing
python3 plot_snapped_routes.py    # Outputs encoded polylines for final mapping to "original.txt" and "perturbed.txt"
```