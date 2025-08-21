import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🍞 오늘의 디저트 추천 🍰",
    page_icon="🥐",
    layout="centered"
)

# 스타일 설정
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

# 타이틀
st.title("🥐 오늘 먹고 싶은 디저트는? 🥰")
st.markdown("버튼을 눌러 오늘의 디저트를 랜덤으로 추천받고, 만드는 영상을 확인해보세요!")

# 디저트 종류와 영상 링크 매핑
dessert_videos = {
    "초코소라빵": "https://www.youtube.com/watch?v=6bcYeU17n7k",
    "소금빵": "https://www.youtube.com/watch?v=zgqGlO1hdZ4",
    "케이크": "https://www.youtube.com/watch?v=zgqGlO1hdZ4",
    "토스트": "https://www.youtube.com/watch?v=gsVNi4Uwrp0",
    "마카롱": "https://www.youtube.com/watch?v=Yt_YyU9A3v8",
    "쿠키": "https://www.youtube.com/watch?v=F5SgFJjN2yc"
}

# 랜덤 추천 및 영상 재생
if st.button("🎲 오늘의 디저트 추천!"):
    dessert = random.choice(list(dessert_videos.keys()))
    st.success(f"오늘의 디저트는 **{dessert}**! 😋")
    st.video(dessert_videos[dessert])
