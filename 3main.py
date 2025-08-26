import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="💻 스트림릿 코드 해석 발표용",
    page_icon="🖥️",
    layout="centered"
)

# --- 스타일 ---
st.markdown("""
<style>
body { background-color: #f5f5f5; color: black; font-family: 'Arial', sans-serif; }
h1, h2, h3, p { color: black; text-align: left; }
code { background-color: #eaeaea; padding: 2px 4px; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.title("스트림릿 앱 코드 해석 발표용 💡")
st.markdown("아래는 내가 만든 디저트 추천 스트림릿 앱의 코드 역할과 설명입니다.")

# --- 코드 해석 ---
slides = {
    "페이지 설정": "st.set_page_config() → 앱 제목, 아이콘, 레이아웃 설정",
    "스타일 지정": "st.markdown(<style>) → 글자색, 배경색, 폰트, 버튼 디자인 지정",
    "제목과 안내문": "st.title / st.markdown → 제목과 안내문 출력",
    "디저트 선택 메뉴": "st.selectbox → 사용자가 원하는 디저트 선택",
    "디저트 정보 저장": "딕셔너리(dictionary) → 디저트별 설명, 재료, 레시피, 팁, 영상 링크 관리",
    "반복 출력": "for문 → 재료, 레시피, 팁 반복 출력",
    "영상 삽입": "st.video() → 디저트 영상 삽입"
}

st.markdown("### 🔹 코드 해석 슬라이드")
for title, explanation in slides.items():
    st.markdown(f"**{title}**")
    st.markdown(f"- {explanation}")

# --- 추가 안내 ---
st.markdown("---")
st.markdown("이 페이지를 통해, 내가 만든 스트림릿 앱 코드의 역할을 한 눈에 확인하고 발표할 수 있습니다.")
