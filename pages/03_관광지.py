import streamlit as st
import folium
from streamlit_folium import st_folium

# -------------------------------
# 페이지 기본 설정
# -------------------------------
st.set_page_config(page_title="서울 관광 명소 지도", layout="wide")
st.title("🗺️ 외국인이 좋아하는 서울 주요 관광지 TOP 10")

st.markdown("""
서울을 방문한 외국인들이 가장 많이 찾는 인기 관광지 10곳을 지도에 표시했습니다.  
각 마커를 클릭하면 관광지 이름을 볼 수 있습니다.
""")

# -------------------------------
# 서울 주요 관광지 데이터
# -------------------------------
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041},
    {"name": "명동 (Myeongdong Shopping Street)", "lat": 37.563757, "lon": 126.982685},
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566479, "lon": 127.009185},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998},
    {"name": "홍대거리 (Hongdae Street)", "lat": 37.556866, "lon": 126.923690},
    {"name": "이태원 (Itaewon)", "lat": 37.534540, "lon": 126.994930},
    {"name": "창덕궁 (Changdeokgung Palace)", "lat": 37.579414, "lon": 126.991063},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.512476, "lon": 127.102628},
    {"name": "청계천 (Cheonggyecheon Stream)", "lat": 37.570028, "lon": 126.991998},
]

# -------------------------------
# Folium 지도 생성
# -------------------------------
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=place["name"],
        tooltip=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

# -------------------------------
# Streamlit에 Folium 지도 표시
# -------------------------------
st_data = st_folium(m, width=900, height=600)
