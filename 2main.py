import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="📌 코드 핵심 요약 발표용",
    page_icon="💻",
    layout="centered"
)

# --- 스타일 ---
st.markdown("""
<style>
body {
    background-color: #f5f5f5;
    color: black;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3, p {
    color: black;
    text-align: left;
}
.stButton>button {
    background-color: #f0d8b3;
    color: black;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# --- 슬라이드 데이터 ---
slides = [
    ("앱 설정", "`st.set_page_config()` → 앱 제목, 아이콘, 레이아웃을 설정"),
    ("디자인 꾸미기", "`st.markdown(<style>)` → 글자 색, 배경색, 폰트 등 디자인 적용"),
    ("제목과 안내문", "`st.title()` / `st.markdown()` → 제목과 안내문 출력"),
    ("사용자 선택 메뉴", "`st.selectbox()` → 사용자가 선택할 수 있는 메뉴 생성"),
    ("데이터 관리", "`dict (딕셔너리)` → 디저트별 재료, 레시피, 팁, 영상 링크 관리"),
    ("반복 출력", "`for문` → 재료, 레시피, 팁 반복 출력"),
    ("영상 삽입", "`st.video()` → 유튜브 영상 앱에 삽입")
]

# --- 세션 상태 초기화 ---
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

# --- 현재 슬라이드 표시 ---
slide_index = st.session_state.slide_index
title, desc = slides[slide_index]
st.subheader(f"{slide_index + 1}. {title}")
st.write(desc)

# --- 버튼으로 슬라이드 이동 ---
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅ 이전"):
        if st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1
with col2:
    if st.button("다음 ➡"):
        if st.session_state.slide_index < len(slides) - 1:
            st.session_state.slide_index += 1
