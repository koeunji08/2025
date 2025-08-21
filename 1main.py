import streamlit as st

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
st.markdown("아래에서 원하는 디저트를 선택하고, 만드는 영상을 확인해보세요!")

# 디저트 종류 선택
dessert = st.selectbox(
    "디저트를 선택하세요:",
    ["초코소라빵", "소금빵", "케이크", "토스트", "마카롱", "쿠키"]
)

# 디저트 정보 및 영상 링크
dessert_info = {
    "초코소라빵": {
        "description": "부드러운 소라껍질 속에 초코슈크림이 가득한 인기 디저트입니다.",
        "ingredients": ["강력분", "우유", "버터", "설탕", "이스트", "소금", "초코소스"],
        "video": "https://www.youtube.com/watch?v=6bcYeU17n7k"
    },
    "소금빵": {
        "description": "겉은 바삭하고 속은 부드러운 소금빵입니다.",
        "ingredients": ["강력분", "우유", "버터", "설탕", "이스트", "소금", "물"],
        "video": "https://www.youtube.com/watch?v=zgqGlO1hdZ4"
    },
    "케이크": {
        "description": "부드럽고 촉촉한 케이크로, 다양한 맛으로 즐길 수 있습니다.",
        "ingredients": ["박력분", "설탕", "버터", "계란", "우유", "베이킹파우더"],
        "video": "https://www.youtube.com/watch?v=zgqGlO1hdZ4"
    },
    "토스트": {
        "description": "간단하고 맛있는 아침 식사로 좋은 토스트입니다.",
        "ingredients": ["식빵", "버터", "잼", "치즈", "햄"],
        "video": "https://www.youtube.com/watch?v=gsVNi4Uwrp0"
    },
    "마카롱": {
        "description": "부드럽고 달콤한 마카롱으로, 다양한 색상과 맛으로 즐길 수 있습니다.",
        "ingredients": ["아몬드가루", "설탕", "계란흰자", "설탕", "버터", "식용색소"],
        "video": "https://www.youtube.com/watch?v=Yt_YyU9A3v8"
    },
    "쿠키": {
        "description": "바삭하고 달콤한 쿠키로, 간식으로 좋습니다.",
        "ingredients": ["박력분", "설탕", "버터", "계란", "베이킹소다", "초콜릿칩"],
        "video": "https://www.youtube.com/watch?v=F5SgFJjN2yc"
    }
}

# 선택한 디저트 정보 표시
if dessert:
    st.subheader(f"{dessert} 🍰")
    st.write(dessert_info[dessert]["description"])
    st.markdown("### 필요한 재료")
    for ingredient in dessert_info[dessert]["ingredients"]:
        st.write(f"- {ingredient}")
    st.markdown("### 만드는 영상")
    st.video(dessert_info[dessert]["video"])
