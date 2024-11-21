import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point

# Crear un GeoDataFrame
data = {
    "ghi": [191.112708, 191.112708, 191.112708, 191.112708],
    "lat": [-12.0, -12.0, -11.5, -11.5],
    "lon": [-76.0, -75.5, -76.0, -75.5],
}
gdf = gpd.GeoDataFrame(
    data,
    geometry=[Point(xy) for xy in zip(data["lon"], data["lat"])],
    crs="EPSG:4326",
)

# Graficar con un mapa base alternativo
fig, ax = plt.subplots(figsize=(10, 6))
gdf.plot(ax=ax, markersize=50, alpha=0.7)
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.CartoDB.Positron)

# Personalizar
plt.title("Puntos de Irradiancia en el Mapa")
plt.show()

