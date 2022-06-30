
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point

# Rio de Janeiro map can be found here
# https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2017/UFs/RJ/
rj = gpd.read_file("Mapas/RJ/33MUE250GC_SIR.shp")

def plotMap(dataframe, map=rj, maxval=1):
    fig, ax = plt.subplots( figsize = (15, 10)  )
    ax.set_xlim( -43.5, -43.15 )
    ax.set_ylim( -23.05, -22.75 )
    map.plot(ax = ax, alpha = 0.1, color='grey', edgecolor="black")

    dataframe.plot(
        ax = ax,
        kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.4,
        # s=dataframe["accommodates"],
        # s=dataframe["beds"] * 2,
        # s=dataframe["accommodates"] * 2,
        s=dataframe["price"]/maxval,
        # label="price per guest",
        label="price",
        # c="price_per_guest",
        c="price",
        cmap=plt.get_cmap("jet"),
        colorbar=True,
    )
    plt.show()
#


# Brazil coast
# https://gismaps.com.br/en/downloads/limites-costeiro-e-continental-do-brasil-shp/
coast = gpd.read_file("Mapas/BR/costa_continente_shp.shp")
coast = coast[ coast.NOME1 == "Costa" ].reset_index().to_crs('EPSG:3857')
def getDistanceToCoast( longitude, latitude, coast=coast ):
    point = gpd.GeoDataFrame({
        'geometry': [ Point( longitude, latitude ) ]
        }, crs='EPSG:4326')    
    point = point.to_crs('EPSG:3857')
    return point.distance( coast )
#
# example:
#
# pFar = gpd.GeoDataFrame({
#     'geometry': [ Point( -43.35, -22.90  ) ]
#     }, crs='EPSG:4326')

# getDistanceToCoast( pFar, coast=coastBR )
# 12994.242467 (meters)


