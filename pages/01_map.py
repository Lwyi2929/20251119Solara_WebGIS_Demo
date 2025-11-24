import solara
import leafmap.leafmap as leafmap # 使用 ipyleaflet (重量級) 後端
import json

# 1. 定義「繁重」的地圖建立函式
def create_map():
    print("...正在建立地圖...")
    m = leafmap.Map(
        center=[23.6995, 121.2955], 
        zoom=7, 
        layout_height="600px",
        basemap="OpenStreetMap" # 先設一個保證會成功的預設值
    )

    with open("data/ma_river.geojson") as f:
        gj = json.load(f)
    m.add_geojson(gj, name="river")


@solara.component
def Page():
    solara.Markdown("## 顯示 Leafmap (ipywidget)")
    
    # 2. 使用 use_memo 快取地圖物件
    map_object = solara.use_memo(create_map, dependencies=[])
    
    # 3. 我們不直接 return map_object，而是建立一個 Column 來包裝它
    # 並且使用 solara.display() 來顯示渲染 widget
    with solara.Column(style={"width": "100%", "height": "650px"}):
        solara.display(map_object)

