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
    # if os.path.exists(file_name):
    #     print("The file exists.")
    # else:
    #     print("The file does not exist.")
    with open(file_name, 'rb') as file:
        tree = pickle.load(file)
    results = tree.query((lat_lon), k = k, distance_upper_bound= max_distance)
    print(u)
    zipped_results = list(zip(results[0], results[1])) 
    zipped_results = [i for i in zipped_results if i[0] != np.inf]
    print(len(zipped_results))
    return len(zipped_results)

# def iqr_capping(df, cols , factor):
#     for col in cols:
#         q1 = df[col].quantile(0.25)
#         q3 = df[col].quantile(0.75)
#         iqr = q3 - q1
#         ul = q3 + (factor * iqr)
#         ll = q1 - (factor * iqr)
        
#         df[col] = np.where(df[col]>ul , ul , np.where(df[col] <ll ,ll ,df[col]))


# Route for seeing a data
@app.route('/', methods=['POST'])
def receive_data():
    proplist = {'Apartment':0 , 'House':2 , 'Townhouse':4 , 'Condominium':1 , 'Serviced apartment':3}
    data = request.get_json()
    print(data)
    lat = data['location']['lat']
    lon = data['location']['long']
    bed = int(data['Bedrooms'])
    proptype = proplist[data['PropertyType']]
    acc = int(data['Accommodates'])

    lon_latitude = 51.509865
    lon_longitude = -0.118092
    local_utm_crs = get_local_crs(lon_latitude, lon_longitude)

    # Create a transformer for the conversion
    # transformer = Transformer.from_crs('EPSG:4326', 'EPSG:3857', always_xy=True)
    # # Convert the coordinates to Web Mercator projection
    # x, y = transformer.transform(lon, lat)
    amenity_list = ['latitude','longitude','property_type', 'accommodates', 'bedrooms', 'viewpoint','restaurant', 'bar', 'pub', 'cinema', 'nightclub', 'theatre','marketplace','place_of_worship','artwork', 'attraction', 'gallery', 'information','museum', 'picnic_site', 'entertainment', 'property_size','nearby_amenities', 'amenities_count', 'religious_sites_count', 'fun','historic']
    air_df = pd.DataFrame(columns=amenity_list)
    air_df.at[0,'latitude'] = lat
    air_df.at[0,'longitude'] = lon
    air_df.at[0,'bedrooms'] = bed
    air_df.at[0,'property_type'] = proptype
    air_df.at[0,'accommodates'] = acc


    # coordinates = [(lat,lon)]
    # points = [Point(coord) for coord in coordinates]
    air_gdf = gpd.GeoDataFrame(air_df, geometry=gpd.points_from_xy(air_df.longitude, air_df.latitude), crs=4326)
    air_gdf = air_gdf.to_crs(local_utm_crs)
 
    

    # Import
    for u in amenity_list:
        if u not in ['latitude','longitude','accommodates','property_type','bedrooms','entertainment', 'nearby_amenities', 'amenities_count', 'religious_sites_count', 'fun','historic','property_size']:
            import time 
            t0 = time.time()
            #Apply the function
            air_gdf[u] = air_gdf.apply(lambda row: find_points_closeby((row.geometry.y, row.geometry.x),u) , axis = 1)
            #gdf[u] = find_points_closeby((lat,lon),u)
            # Report the time
            time_passed = round(time.time() - t0, 2)
            # print ("Completed in %s seconds" % (time_passed))
    air_gdf['entertainment'] = air_gdf['cinema'] + air_gdf['theatre']
    air_gdf['property_size'] = air_gdf['bedrooms'] * air_gdf['accommodates']
    air_gdf['nearby_amenities'] = air_gdf['restaurant'] + air_gdf['bar'] + air_gdf['pub']
    air_gdf['amenities_count'] = air_gdf[['restaurant', 'bar', 'pub']].sum(axis=1)
    # air_gdf['religious_sites_count'] = air_gdf[['place_of_worship', 'museum']].sum(axis=1)
    air_gdf['fun'] = air_gdf['bar'] + air_gdf['pub'] + air_gdf['nightclub']
    air_gdf['historic'] = air_gdf['gallery']+air_gdf['museum']+air_gdf['place_of_worship']+air_gdf['artwork']
    print(air_gdf.columns)
    air_gdf.drop(columns=['latitude','longitude','geometry'],axis = 1,inplace = True)
    with open('D:\React-Projects\mp_hp\ml\model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    new_data=air_gdf.to_numpy()
    predictions = loaded_model.predict(new_data)
    pred = predictions.tolist()
    print(pred)
    return jsonify({'pp':pred})
    

     
# Running app
if __name__ == '__main__':
    app.run(debug=True)