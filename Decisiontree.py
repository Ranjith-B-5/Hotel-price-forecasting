# Import
import osmnx as ox 
import os
import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
import time
from scipy import spatial
from scipy.spatial import KDTree
import pickle
import asyncio


  # Set up query
amenity_list = ['restaurant','bar','pub','hospital','cinema','nightclub','theatre','marketplace','place_of_worship']

for u in amenity_list:
  print(u)
  query = {'amenity':u}

  # Run query
  restaurants_gdf = ox.geometries.geometries_from_place(
              'Greater London, UK',
              tags = query)

  restaurants_gdf.head(5)

  london_gdf = ox.geocoder.geocode_to_gdf('Greater London, UK')
  london_gdf['geometry'] = london_gdf['geometry'].apply(
    lambda x: x.centroid if type(x) == Polygon else (
    x.centroid if type(x) == MultiPolygon else x)
  )


  def get_local_crs(y,x):  
      x = ox.utils_geo.bbox_from_point((y, x), dist = 500, project_utm = True, return_crs = True)
      return x[-1]
    
  # Set London longitude and latitude
  lon_latitude = 51.509865
  lon_longitude = -0.118092

  local_utm_crs = get_local_crs(lon_latitude, lon_longitude)

  #Convert amenities into local projection (amenities already had an initial CRS set when we downloaded it via OSMnx)
  restaurants_gdf = restaurants_gdf.to_crs(local_utm_crs)

  points = restaurants_gdf[restaurants_gdf.geometry.type == 'Point']
  Lon = points.geometry.apply(lambda x: x.x).values
  Lat = points.geometry.apply(lambda x: x.y).values
  coords = list(zip(Lat,Lon))
  tree = spatial.KDTree(coords)

  Lon = []
  Lat = []
  for geom in restaurants_gdf.geometry:
      if geom.geom_type == 'Point':
          Lon.append(geom.x)
          Lat.append(geom.y)
      elif geom.geom_type == 'Polygon':
          Lon.append(geom.centroid.x)
          Lat.append(geom.centroid.y)
  coords = list(zip(Lat, Lon))

  tree = spatial.KDTree(coords)
  if isinstance(tree, KDTree):
    print("KD tree successfully loaded.")
  else:
    print("Failed to load KD tree.")

  file_name = f'./pickled_kdtree/kdtree_{u}.pkl'
  with open(file_name, 'wb') as file:
    pickle.dump(tree, file)



# tourist-------------------------

# Set up query
amenity_list = ['artwork','attraction','gallery','information','museum','picnic_site','viewpoint']

for u in amenity_list:
  print(u)
  query = {'tourism':u}

  # Run query
  restaurants_gdf = ox.geometries.geometries_from_place(
              'Greater London, UK',
              tags = query)

  restaurants_gdf.head(5)

  london_gdf = ox.geocoder.geocode_to_gdf('Greater London, UK')
  london_gdf['geometry'] = london_gdf['geometry'].apply(
    lambda x: x.centroid if type(x) == Polygon else (
    x.centroid if type(x) == MultiPolygon else x)
  )


  def get_local_crs(y,x):  
      x = ox.utils_geo.bbox_from_point((y, x), dist = 500, project_utm = True, return_crs = True)
      return x[-1]
    
  # Set London longitude and latitude
  lon_latitude = 51.509865
  lon_longitude = -0.118092

  local_utm_crs = get_local_crs(lon_latitude, lon_longitude)

  #Convert amenities into local projection (amenities already had an initial CRS set when we downloaded it via OSMnx)
  restaurants_gdf = restaurants_gdf.to_crs(local_utm_crs)

  
  points = restaurants_gdf[restaurants_gdf.geometry.type == 'Point']
  Lon = points.geometry.apply(lambda x: x.x).values
  Lat = points.geometry.apply(lambda x: x.y).values
  coords = list(zip(Lat,Lon))
  tree = spatial.KDTree(coords)
  Lon = []
  Lat = []
  for geom in restaurants_gdf.geometry:
      if geom.geom_type == 'Point':
          Lon.append(geom.x)
          Lat.append(geom.y)
      elif geom.geom_type == 'Polygon':
          Lon.append(geom.centroid.x)
          Lat.append(geom.centroid.y)
  coords = list(zip(Lat, Lon))
  


  # demo = [1,2,3,4]
  tree = spatial.KDTree(coords)

  if isinstance(tree, KDTree):
    print("KD tree successfully loaded.")
  else:
    print("Failed to load KD tree.")
  
  file_name = f'./pickled_kdtree/kdtree_{u}.pkl'
  with open(file_name, 'wb') as file:
    pickle.dump(tree, file)

