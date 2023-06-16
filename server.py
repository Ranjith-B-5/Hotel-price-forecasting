# Import flask and datetime module for showing date and time
from flask import Flask, jsonify ,request
from flask_cors import CORS
import datetime
import pandas as pd
import numpy as np
import time
import pickle
import geopandas as gpd
from shapely.geometry import Point
import osmnx as ox 
import os
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
import time
from scipy import spatial
from scipy.spatial import KDTree
from pyproj import Transformer
from time import sleep
import asyncio

 
x = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
CORS(app)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})




def get_local_crs(y,x):  
    x = ox.utils_geo.bbox_from_point((y, x), dist = 500, project_utm = True, return_crs = True)
    return x[-1]

def find_points_closeby(lat_lon, u ,k = 500, max_distance = 1000):
    '''
    Queries a pre-existing kd tree and returns the number of points within x distance
    of long/lat point.
    lat_lon:        A longitude and latitude pairings in the (y, x) tuple form.
    k:              The maximum number of closest points to query
    max_distance:   The maximum distance (in meters)
    '''
    
    file_name = f'D:\React-Projects\Mini-project\pickled_kdtree\kdtree_{u}.pkl'
    if os.path.exists(file_name):
        print("The file exists.")
    else:
        print("The file does not exist.")
    with open(file_name, 'r+b') as file:
        tree = pickle.load(file)
    print(tree)
    results = tree.query((lat_lon), k = k, distance_upper_bound= max_distance)
    print("here is the resutl")
    print(u)
    zipped_results = list(zip(results[0], results[1])) 
    zipped_results = [i for i in zipped_results if i[0] != np.inf]
    print(len(zipped_results))
    return len(zipped_results)


# Route for seeing a data
@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()
    lat = data['location']['lat']
    lon = data['location']['long']
    print(lon)
    lon_latitude = 51.509865
    lon_longitude = -0.118092
    local_utm_crs = get_local_crs(lon_latitude, lon_longitude)

    # Create a transformer for the conversion
    # transformer = Transformer.from_crs('EPSG:4326', 'EPSG:3857', always_xy=True)
    # # Convert the coordinates to Web Mercator projection
    # x, y = transformer.transform(lon, lat)
    amenity_list = ['latitude','longitude','restaurant','bar','pub','hospital','cinema','nightclub','theatre','marketplace','place_of_worship','artwork','attraction','gallery','information','museum','picnic_site','viewpoint']
    air_df = pd.DataFrame(columns=amenity_list)
    air_df.at[0,'latitude'] = lat
    air_df.at[0,'longitude'] = lon
    print('jellyyyyyyyyyyyyyyyyyyyy')
    print(air_df['latitude'])
    print(air_df.head())
    # coordinates = [(lat,lon)]
    # points = [Point(coord) for coord in coordinates]
    air_gdf = gpd.GeoDataFrame(air_df, geometry=gpd.points_from_xy(air_df.longitude, air_df.latitude), crs=4326)
    air_gdf = air_gdf.to_crs(local_utm_crs)
    print(air_gdf.iloc[:1])
    

    # Import
    for u in amenity_list:
        if u not in ['latitude','longitude']:
            import time 
            t0 = time.time()
            #Apply the function
            air_gdf[u] = air_gdf.apply(lambda row: find_points_closeby((row.geometry.y, row.geometry.x),u) , axis = 1)
            #gdf[u] = find_points_closeby((lat,lon),u)
            print("hello hello")
            # Report the time
            time_passed = round(time.time() - t0, 2)
            print ("Completed in %s seconds" % (time_passed))

        # print(air_df.head())
    print(air_gdf.head(1))
    return jsonify({'df':"phew"})
    

     
# Running app
if __name__ == '__main__':
    app.run(debug=True)