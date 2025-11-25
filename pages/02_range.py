import solara
import leafmap.maplibregl as leafmap

def create_map():
    m = leafmap.Map(
        center=[121.5319, 25.0478],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("OpenStreetMap")
    m.add_geojson("https://raw.githubusercontent.com/Lwyi2929/20251119Solara_WebGIS_Demo/main/ma_river_wgs84.geojson", name="river")
    

    return m

@solara.component
def Page():
    m = create_map()
    return m.to_solara()