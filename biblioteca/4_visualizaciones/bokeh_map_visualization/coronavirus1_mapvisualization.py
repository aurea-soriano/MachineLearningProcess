import geopandas as gpd
import json
import pandas as pd
import numpy as np
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, ColumnDataSource
from bokeh.models import HoverTool

shapefile = '../map_data/countries_110m/ne_110m_admin_0_countries.shp'
#Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
#Rename columns.
gdf.columns = ['country', 'country_code', 'geometry']
print(gdf.head())


print(gdf[gdf['country'] == 'Antarctica'])
#Drop row corresponding to 'Antarctica'
gdf = gdf.drop(gdf.index[159])

print(gdf[gdf['country'] == 'Singapore'])

grid_crs=gdf.crs
grid_crs



#Read data to json.
gdf_json = json.loads(gdf.to_json())
#Convert to String like object.
grid = json.dumps(gdf_json)


datafile = '../map_data/coronavirus.csv'
#Read csv file using pandas
df1 = pd.read_csv(datafile, names = ['continent', 'country/territory', 'confirmed_cases', 'deaths'], skiprows = 1)
df1['scaled_confirmed_cases'] = np.log(df1['confirmed_cases']+1)*1.5
print(df1.head())

datafile_2='../map_data/country_geocodes.csv'
df2 = pd.read_csv(datafile_2, names = ['country', 'latitude', 'longitude'], skiprows = 1)
print(df2.head())

points = pd.merge(df1, df2, left_on='country/territory',right_on='country', how='left')
print(points)



#Input GeoJSON source that contains features for plotting.
geosource = GeoJSONDataSource(geojson = grid)
pointsource = ColumnDataSource(points)

#Create figure object.
p = figure(title = 'Worldwide spread of Coronavirus', plot_height = 600 , plot_width = 1050)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
#Add patch renderer to figure.
patch=p.patches('xs','ys', source = geosource,fill_color = '#fff7bc',
          line_color = 'black', line_width = 0.35, fill_alpha = 1,
                hover_fill_color="#fec44f")

#point=p.circle('longitude','latitude',source=pointsource, radius='scaled_confirmed_cases',
               #fill_color="firebrick", alpha=0.7)
p.add_tools(HoverTool(tooltips=[('Country','@country'),('Confirmed Cases','@confirmed_cases'), ('Deaths','@deaths')], renderers=[patch]))


#Display figure.
show(p)
