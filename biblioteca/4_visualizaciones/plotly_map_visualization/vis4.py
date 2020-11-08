import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

print(df["district"][2])
print(geojson["features"][0]["properties"])

import plotly.express as px
import geopandas as gpd

geo_df = gpd.read_file(gpd.datasets.get_path('nybb')).to_crs("EPSG:4326")

fig = px.choropleth_mapbox(geo_df,
                           geojson=geo_df.geometry,
                           locations=geo_df.index,
                           color='Shape_Leng',
                           hover_name="BoroName",
                           center={"lat": 40.71, "lon": -74.00},
                           mapbox_style="open-street-map",
                           zoom=8)
fig.show()
