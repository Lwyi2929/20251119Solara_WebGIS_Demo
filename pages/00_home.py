import solara
import leafmap.leafmap as leafmap # 使用 ipyleaflet (重量級) 後端


@solara.component
def Page():
    with solara.Column(align="center"):
        solara.Title("我的 Solara_WebGIS_Demo")
        solara.Markdown("馬太鞍溪堰塞湖 事件於 2025 年 9 月 23 日 下午約 2 點 50 分 發生壩頂溢流，因豪雨帶來的暴漲溪水，造成馬太鞍溪河岸堤防出現破口，導致周邊低窪地區淹水。潰堤主要與短時間內大量降雨、上游集水區排水不及，以及堤防老化或結構受損等因素有關。事故發生後，相關單位進行緊急搶修與疏散，並加強後續堤防的安全檢查與整治。")



