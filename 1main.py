import streamlit as st
import pandas as pd

# --- 페이지 설정 ---
st.set_page_config(
    page_title="🍞 오늘의 디저트 추천 🍰",
    page_icon="🥐",
    layout="centered"
)

# --- 스타일 ---
st.markdown("""
<style>
body {
    background-color: #f5e0c3; /* 연한 갈색 배경 */
    color: black; /* 글씨 검정색 */
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
h1, h2, h3, p {
    color: black;
    text-align: center;
}
.stButton>button {
    background-color: #f0d8b3; /* 버튼 연한 갈색 */
    color: black;
    font-weight: bold;
    border-radius: 18px;
    padding: 12px 24px;
    font-size: 20px;
}
.stSelectbox>div {
    background-color: #f0e0c3; /* 선택박스 연한 갈색 */
    border-radius: 12px;
    padding: 5px;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# --- 첫 화면 타이틀 ---
st.title("🍞🥐 오늘의 몽글몽글 디저트 🧁🍪")
st.markdown("""
환영해요! 🥰  
아래에서 먹고 싶은 디저트를 선택하면,  
귀엽게 🍩 만드는 방법과 영상이 나타나요! 🥖🍫
""")

# --- 디저트 선택 ---
dessert = st.selectbox(
    "🍰 디저트를 선택해 주세요 🥯🍪:",
    ["초코소라빵 🍫", "소금빵 🧂", "케이크 🎂", "토스트 🍞", "마카롱 🌈", "쿠키 🍪"]
)

# --- 디저트 정보 ---
dessert_info = {
    "초코소라빵 🍫": {
        "description": "부드러운 소라껍질 속에 초코슈크림이 가득한 인기 디저트예요! 🍫🥐",
        "ingredients": ["강력분", "우유", "버터", "설탕", "이스트", "소금", "초코소스"],
        "recipe": [
            "1️⃣ 반죽을 준비하여 1차 발효합니다.",
            "2️⃣ 반죽을 분할하여 둥글린 후 2차 발효합니다.",
            "3️⃣ 초코소스를 준비하여 반죽에 채웁니다.",
            "4️⃣ 오븐에서 구워 완성합니다! 🔥"
        ],
        "video": "https://www.youtube.com/watch?v=lO-ZwMgb7cY"
    },
    "소금빵 🧂": {
        "description": "겉은 바삭, 속은 부드러운 소금빵이에요! 🥖",
        "ingredients": ["강력분", "우유", "버터", "설탕", "이스트", "소금", "물"],
        "recipe": [
            "1️⃣ 반죽을 준비하여 1차 발효합니다.",
            "2️⃣ 반죽을 분할하고 둥글린 후 2차 발효합니다.",
            "3️⃣ 소금물에 담가 소금을 입힙니다.",
            "4️⃣ 오븐에서 구워 완성! 🔥"
        ],
        "video": "https://www.youtube.com/watch?v=zgqGlO1hdZ4"
    },
    "케이크 🎂": {
        "description": "부드럽고 촉촉한 케이크, 여러 맛으로 즐길 수 있어요! 🍰",
        "ingredients": ["박력분", "설탕", "버터", "계란", "우유", "베이킹파우더"],
        "recipe": [
            "1️⃣ 재료를 준비하여 혼합합니다.",
            "2️⃣ 반죽을 틀에 붓고 2차 발효합니다.",
            "3️⃣ 오븐에서 구워 완성! 🔥"
        ],
        "video": "https://www.youtube.com/watch?v=zgqGlO1hdZ4"
    },
    "토스트 🍞": {
        "description": "간단하고 맛있는 아침 토스트예요! 🥪",
        "ingredients": ["식빵", "버터", "잼", "치즈", "햄"],
        "recipe": [
            "1️⃣ 식빵에 버터를 바릅니다.",
            "2️⃣ 원하는 재료를 올리고 토스트합니다.",
            "3️⃣ 완성된 토스트를 서빙합니다! 🍴"
        ],
        "video": "https://www.youtube.com/watch?v=gsVNi4Uwrp0"
    },
    "마카롱 🌈": {
        "description": "부드럽고 달콤한 마카롱, 색감도 예뻐요! 🧁",
        "ingredients": ["아몬드가루", "설탕", "계란흰자", "설탕", "버터", "식용색소"],
        "recipe": [
            "1️⃣ 아몬드가루와 설탕을 체에 칩니다.",
            "2️⃣ 계란흰자를 휘핑하여 머랭을 만듭니다.",
            "3️⃣ 머랭에 아몬드가루 혼합물을 섞어 반죽합니다.",
            "4️⃣ 반죽을 짜서 마카롱을 만들고 건조시킵니다.",
            "5️⃣ 오븐에서 구워 완성! 🔥"
        ],
        "video": "https://www.youtube.com/watch?v=Yt_YyU9A3v8"
    },
    "쿠키 🍪": {
        "description": "바삭하고 달콤한 쿠키, 간식으로 최고예요! 🍪",
        "ingredients": ["박력분", "설탕", "버터", "계란", "베이킹소다", "초콜릿칩"],
        "recipe": [
            "1️⃣ 재료를 준비하여 혼합합니다.",
            "2️⃣ 반죽을 동그랗게 만들어 팬에 올립니다.",
            "3️⃣ 오븐에서 구워 완성! 🔥"
        ],
        "video": "https://www.youtube.com/watch?v=F5SgFJjN2yc"
    }
}

# --- 선택한 디저트 정보 표시 ---
if dessert:
    st.subheader(f"{dessert} 🍰")
    st.write(dessert_info[dessert]["description"])
    
    st.markdown("### 🥣 필요한 재료")
    # 재료 표로 보기
    df = pd.DataFrame(dessert_info[dessert]["ingredients"], columns=["재료"])
    st.dataframe(df)
    
    st.markdown("### 📝 만드는 방법")
    for step in dessert_info[dessert]["recipe"]:
        st.write(f"- {step}")
    
    st.markdown("### 🎬 만드는 영상")
    st.video(dessert_info[dessert]["video"])
