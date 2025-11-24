import solara
import leafmap.leafmap as leafmap
import json
from pathlib import Path


def create_map():
    print("...正在建立地圖...")
    
    # 建立地圖
    m = leafmap.Map(
        center=[23.6995, 121.2955],
        zoom=7,
        layout_height="600px",
        basemap="OpenStreetMap"
    )

    # 優先以本機檔案載入（容器內可直接使用），避免 HTTP 404
    geojson_path = Path(__file__).resolve().parents[1] / "data" / "ma_river.geojson"
    if geojson_path.exists():
        with open(geojson_path, "r", encoding="utf-8") as f:
            gj = json.load(f)
        m.add_geojson(gj, name="馬太鞍溪", layer_control=True)
    else:
        # fallback: 使用遠端 raw URL（請確認 URL 可存取）
        url = "https://raw.githubusercontent.com/lwyi2929/20251119Solara_WebGIS_Demo/main/ma_river_wgs84.geojson"
        m.add_geojson(url, name="馬太鞍溪", layer_control=True)

    return m



@solara.component
def Page():
    solara.Markdown("## 顯示 Leafmap (ipywidget)")
    
    # 使用 memo 避免 map 重建
    map_object = solara.use_memo(create_map, dependencies=[])

    with solara.Column(style={"width": "100%", "height": "650px"}):
        solara.display(map_object)

