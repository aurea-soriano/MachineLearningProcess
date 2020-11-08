import geopandas as gpd
import pandas as pd
import numpy as np
import requests
from shapely.geometry import Point
import json
from geopandas.tools import sjoin

shapefile = '../map_data/countries_110m/ne_110m_admin_0_countries.shp'
#Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
#Rename columns.
gdf.columns = ['country_name', 'country_code', 'geometry']
print(gdf.head())

print(gdf[gdf['country_name'] == 'Antarctica'])
#Drop row corresponding to 'Antarctica'
gdf = gdf.drop(gdf.index[159])


grid_crs=gdf.crs
grid_crs

pathtoCSV='../map_data/Covid19 - Situation_update_ECDC.csv'
#Read csv file using pandas
df1 = pd.read_csv(pathtoCSV, encoding='utf8',names = ['continent', 'country/territory', 'confirmed_cases', 'deaths'], index_col=False,skiprows=1,skipfooter=1)
df1['scaled_confirmed_cases'] = np.log(df1['confirmed_cases']+1)*1.5
df1


datafile_2='../map_data/country_geocodes.csv'
df2 = pd.read_csv(datafile_2, names = ['country', 'latitude', 'longitude'], skiprows = 1)
df2.head()

points = pd.merge(df1, df2, left_on='country/territory',right_on='country', how='left')
points_df = points.drop(['continent','country'],axis=1)
points_df.head()


# creating a geometry column
geometry_centroids = [Point(xy) for xy in zip(points_df['longitude'], points_df['latitude'])]

# Coordinate reference system : WGS84
crs = {'init': 'epsg:4326'}

# Creating a Geographic data frame
points_gdf = gpd.GeoDataFrame(points_df, crs=crs, geometry=geometry_centroids)
points_gdf.head()

#tener instalado  spatialindex
joined = gpd.sjoin(gdf, points_gdf, how="left", op='intersects')
joined.head()

joined.fillna("None", inplace=True)



#Read data to json.
joined_json = json.loads(joined.to_json())
#Convert to String like object.
json_data = json.dumps(joined_json)

from bokeh.io import curdoc, output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource
from bokeh.models import HoverTool
#Input GeoJSON source that contains features for plotting.
geosource = GeoJSONDataSource(geojson = json_data)


#Create figure object.
p = figure(title = 'Worldwide distribution of nCov cases, 2020',plot_height = 600 , plot_width = 1050,
           background_fill_color="#2b8cbe", background_fill_alpha=0.4)
p.title.text_font = "helvetica"
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

#Add patch renderer to figure.
patch=p.patches('xs','ys', source = geosource,fill_color = '#fff7bc',
          line_color = '#d95f0e', line_width = 0.35, fill_alpha = 1,
                hover_fill_color="#fec44f")
point=p.circle('longitude','latitude',source=geosource, radius='scaled_confirmed_cases',
               fill_color="firebrick", alpha=0.7)
p.add_tools(HoverTool(tooltips=[('Country','@country_name'),('Confirmed Cases','@confirmed_cases'),
                                ('Deaths','@deaths')], renderers=[patch]))



#Display figure.
show(p)
