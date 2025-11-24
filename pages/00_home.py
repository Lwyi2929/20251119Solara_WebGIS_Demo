import solara
import leafmap.leafmap as leafmap # 使用 ipyleaflet (重量級) 後端


@solara.component
def Page():
    solara.Title("我的 Solara_WebGIS_Demo")
    solara.Markdown("馬太鞍溪堰塞湖 事件於 2025 年 9 月 23 日 下午約 2 點 50 分 發生壩頂溢流，因豪雨帶來的暴漲溪水，造成馬太鞍溪河岸堤防出現破口，導致周邊低窪地區淹水。潰堤主要與短時間內大量降雨、上游集水區排水不及，以及堤防老化或結構受損等因素有關。事故發生後，相關單位進行緊急搶修與疏散，並加強後續堤防的安全檢查與整治。")




# 1. 定義「繁重」的地圖建立函式
def create_map():
    print("...正在建立地圖...")
    m = leafmap.Map(
        center=[23.6995, 121.2955],
        zoom=7,
        layout_height="600px",
        basemap="OpenStreetMap" # 先設一個保證會成功的預設值
    )
    return m

@solara.component
def Page():
    solara.Markdown("## 顯示 Leafmap (ipywidget)")

    # 2. 使用 use_memo 快取地圖物件
    map_object = solara.use_memo(create_map, dependencies=[])

    # 3. 我們不直接 return map_object，而是建立一個 Column 來包裝它
    # 並且使用 solara.display() 來顯示渲染 widget
    with solara.Column(style={"width": "100%", "height": "650px"}):
        solara.display(map_object)