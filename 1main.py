import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="🍞오늘의 빵 추천🍰",
    page_icon="🥐",
    layout="centered"
)

# --- 스타일 ---
st.markdown("""
<style>
body {
    background-color: #fffaf0;
}
h1 {
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #ff69b4;
    text-align: center;
}
.stButton>button {
    background-color: #ffb6c1;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# --- 타이틀 ---
st.title("🥐 오늘 먹고 싶은 빵은? 🥰")
st.markdown("버튼을 눌러 오늘의 빵을 랜덤으로 추천받고, 만드는 영상을 확인해보세요!")

# --- 빵 리스트 & 영상 매핑 ---
bread_videos = {
    "식빵": "https://www.example.com/bread_shik.mp4",
    "머핀": "https://www.example.com/bread_muffin.mp4",
    "크루아상": "https://www.example.com/bread_croissant.mp4",
    "도넛": "https://www.example.com/bread_donut.mp4",
    "바게트": "https://www.example.com/bread_baguette.mp4"
}

# --- 랜덤 추천 & 영상 재생 ---
if st.button("🎲 오늘의 빵 추천!"):
    bread = random.choice(list(bread_videos.keys()))
    st.success(f"오늘의 빵은 **{bread}**! 😋")
    st.video(bread_videos[bread])
