import streamlit as st
import pandas as pd

# -----------------------------
# 빵 레시피 데이터
# -----------------------------
RECIPES = {
    "스콘": {
        "emoji": "🫶",
        "yield_text": "스콘 약 8개 분량",
        "base_servings": 8,
        "ingredients": [
            {"재료": "박력분", "수량": 250, "단위": "g"},
            {"재료": "베이킹파우더", "수량": 10, "단위": "g"},
            {"재료": "버터", "수량": 80, "단위": "g"},
            {"재료": "설탕", "수량": 40, "단위": "g"},
            {"재료": "우유", "수량": 120, "단위": "g"},
        ],
        "steps": ["가루류를 체쳐서 섞기.", "차가운 버터 넣고 잘게 쪼개기.", "우유 넣고 반죽 뭉치기.", "모양 잡아 자르기.", "180℃에서 15~20분 굽기."],
        "videos": ["https://youtu.be/cEyl4WDfkWs?si=tnB-t7Semhzd1NST"],
    },
    "마카롱": {
        "emoji": "💗",
        "yield_text": "마카롱 약 20개 분량",
        "base_servings": 20,
        "ingredients": [
            {"재료": "아몬드 가루", "수량": 100, "단위": "g"},
            {"재료": "슈가파우더", "수량": 100, "단위": "g"},
            {"재료": "달걀 흰자", "수량": 80, "단위": "g"},
            {"재료": "설탕", "수량": 100, "단위": "g"},
        ],
        "steps": ["아몬드가루와 슈가파우더 체치기.", "달걀흰자에 설탕 넣어 머랭 만들기.", "가루 넣고 마카로나주.", "짜주머니로 팬닝 후 건조.", "150℃에서 12~15분 굽기."],
        "videos": ["https://youtu.be/XzC1aN6jpsI?si=dMtHORuvKmQpHrqt"],
    },
    "쿠키": {
        "emoji": "🍪",
        "yield_text": "쿠키 약 15개 분량",
        "base_servings": 15,
        "ingredients": [
            {"재료": "버터", "수량": 100, "단위": "g"},
            {"재료": "설탕", "수량": 80, "단위": "g"},
            {"재료": "달걀", "수량": 1, "단위": "개"},
            {"재료": "박력분", "수량": 200, "단위": "g"},
            {"재료": "베이킹파우더", "수량": 5, "단위": "g"},
            {"재료": "초코칩", "수량": 80, "단위": "g"},
        ],
        "steps": ["버터와 설탕 크림화.", "달걀 넣고 섞기.", "가루류 넣고 섞기.", "초코칩 넣어 반죽 완성.", "180℃에서 12분 굽기."],
        "videos": ["https://youtu.be/ZbptGNeo-mk?si=EylMm6c7N3SJ_sra"],
    },
    "케이크": {
        "emoji": "🎂",
        "yield_text": "케이크 1호 사이즈",
        "base_servings": 6,
        "ingredients": [
            {"재료": "박력분", "수량": 120, "단위": "g"},
            {"재료": "달걀", "수량": 3, "단위": "개"},
            {"재료": "설탕", "수량": 100, "단위": "g"},
            {"재료": "버터", "수량": 80, "단위": "g"},
            {"재료": "우유", "수량": 50, "단위": "g"},
        ],
        "steps": ["달걀과 설탕 중탕으로 거품.", "가루 넣고 섞기.", "녹인 버터와 우유 넣기.", "틀에 넣고 170℃에서 30분 굽기."],
        "videos": ["https://youtu.be/CkkaCdEV5nY?si=3Mgjovb2MYIhXlWO"],
    },
    "초코소라빵": {
        "emoji": "🥐🍫",
        "yield_text": "초코소라빵 6개 분량",
        "base_servings": 6,
        "ingredients": [
            {"재료": "강력분", "수량": 250, "단위": "g"},
            {"재료": "설탕", "수량": 40, "단위": "g"},
            {"재료": "소금", "수량": 5, "단위": "g"},
            {"재료": "드라이이스트", "수량": 5, "단위": "g"},
            {"재료": "우유", "수량": 150, "단위": "g"},
            {"재료": "버터", "수량": 50, "단위": "g"},
            {"재료": "초코크림", "수량": 100, "단위": "g"},
        ],
        "steps": ["반죽하여 1차 발효.", "분할, 둥글리기 후 휴지.", "밀대로 펴서 소라 모양 성형.", "초코크림 채우기.", "180℃에서 15분 굽기."],
        "videos": ["https://youtu.be/FaSJFZsYzEM?si=a3TzEOu2CuQiHbog"],
    },
    "소금빵": {
        "emoji": "🥨",
        "yield_text": "소금빵 6개 분량",
        "base_servings": 6,
        "ingredients": [
            {"재료": "강력분", "수량": 250, "단위": "g"},
            {"재료": "설탕", "수량": 20, "단위": "g"},
            {"재료": "소금", "수량": 5, "단위": "g"},
            {"재료": "드라이이스트", "수량": 5, "단위": "g"},
            {"재료": "우유", "수량": 150, "단위": "g"},
            {"재료": "버터", "수량": 50, "단위": "g"},
        ],
        "steps": ["반죽하여 1차 발효.", "분할, 둥글리기 후 휴지.", "삼각형으로 밀어서 롤링 성형.", "소금 솔솔 뿌리기.", "180℃에서 15분 굽기."],
        "videos": ["https://youtu.be/OoKzyOJLygo?si=Bzx4o8eiCMrBhzmg"],
    },
    "식빵": {
        "emoji": "🍞",
        "yield_text": "식빵 1개 분량",
        "base_servings": 1,
        "ingredients": [
            {"재료": "강력분", "수량": 300, "단위": "g"},
            {"재료": "설탕", "수량": 30, "단위": "g"},
            {"재료": "소금", "수량": 5, "단위": "g"},
            {"재료": "드라이이스트", "수량": 6, "단위": "g"},
            {"재료": "우유", "수량": 180, "단위": "g"},
            {"재료": "버터", "수량": 30, "단위": "g"},
        ],
        "steps": ["재료 섞어 반죽 만들기.", "1차 발효 (약 1시간).", "가스 빼고 성형.", "식빵틀에 넣어 2차 발효.", "180℃에서 30분 굽기."],
        "videos": ["https://youtu.be/5dmiKojDJA8?si=6vSxsUWuw9r50nYz"],
    },
}

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="빵 레시피 도우미", layout="wide")

# 귀여운 테마 CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF9E6; /* 파스텔 옐로우 */
        color: #5C4033; /* 브라운 글씨 */
        font-family: "Comic Sans MS", "Arial Rounded MT Bold", cursive;
    }
    .recipe-card {
        background-color: #FFEFD5;
        padding: 15px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 2px 2px 10px #e5c9a8;
        margin: 10px;
    }
    .recipe-card:hover {
        background-color: #FFE2B7;
        transform: scale(1.02);
        transition: 0.2s;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 메인 타이틀
st.title("🍞 아기자기한 빵 레시피 도우미 🥐")
st.markdown("**따뜻한 파스텔 옐로우 × 브라운 톤으로 준비했어요 ✨**")

# 첫 화면 빵 카드 보여주기
st.subheader("오늘 어떤 빵을 만들어볼까요? 🥰")
cols = st.columns(4)
for i, (name, data) in enumerate(RECIPES.items()):
    with cols[i % 4]:
        if st.button(f"{data['emoji']} {name}", key=name):
            st.session_state["selected"] = name

# 선택된 빵 레시피 보여주기
if "selected" in st.session_state:
    choice = st.session_state["selected"]
    recipe = RECIPES[choice]

    st.header(f"{recipe['emoji']} {choice} 레시피")
    st.write(recipe["yield_text"])

    # 재료표
    st.subheader("📝 재료")
    df = pd.DataFrame(recipe["ingredients"])
    st.table(df)

    # 단계별 레시피
    st.subheader("🥣 만드는 법")
    for i, step in enumerate(recipe["steps"], 1):
        st.checkbox(f"{i}. {step}", key=f"{choice}_{i}")

    # 영상
    st.subheader("🎥 영상으로 배우기")
    for url in recipe["videos"]:
        st.video(url)
