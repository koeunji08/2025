import streamlit as st
import pandas as pd

# -----------------------------
# 업데이트된 빵 레시피 with 새로운 유튜브 영상
# -----------------------------
RECIPES = {
    "스콘": {...},  # (여기에는 기존 코드 그대로 두면 돼요!)
    "마카롱": {...},
    "쿠키": {...},
    "케이크": {...},
    "초코소라빵": {...},
    "소금빵": {...},
    "식빵": {
        "yield_text": "식빵 1개 분량",
        "base_servings": 6,
        "ingredients": [
            {"재료": "강력분", "수량": 300, "단위": "g"},
            {"재료": "설탕", "수량": 30, "단위": "g"},
            {"재료": "소금", "수량": 5, "단위": "g"},
            {"재료": "드라이이스트", "수량": 5, "단위": "g"},
            {"재료": "우유", "수량": 180, "단위": "g"},
            {"재료": "버터", "수량": 30, "단위": "g"},
        ],
        "steps": [
            "재료 섞어 반죽 후 1차 발효.",
            "성형 후 식빵틀에 넣기.",
            "2차 발효 후 180℃에서 30분 굽기.",
        ],
        "videos": [
            "https://youtu.be/5dmiKojDJA8?si=6vSxsUWuw9r50nYz"
        ],
        "time_total_min": 150,
        "level": "중급",
    },
}

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="빵 레시피 도우미", layout="wide")

# CSS 꾸미기
st.markdown(
    """
    <style>
    body {
        background-color: #fffbea;
    }
    .title {
        font-size: 36px;
        color: #5c4033;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #8b5e3c;
        margin-bottom: 30px;
    }
    .recipe-card {
        background-color: #fff3c4;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 2px 2px 10px rgba(92,64,51,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 첫 화면 헤더
st.markdown("<div class='title'>🥖 빵 레시피 도우미 🍪</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>포근한 카페처럼, 아기자기한 분위기 속에서 즐기는 홈베이킹 ✨</div>", unsafe_allow_html=True)

# 사이드바
choice = st.sidebar.selectbox("🍩 빵 종류 선택", list(RECIPES.keys()))
recipe = RECIPES[choice]

# 본문 레시피 카드
st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)

st.header(f"📌 {choice} 레시피")
st.write(recipe["yield_text"])

# 재료표
st.subheader("🥣 재료")
df = pd.DataFrame(recipe["ingredients"])
st.table(df)

# 단계별 레시피
st.subheader("🪄 만드는 법")
for i, step in enumerate(recipe["steps"], 1):
    st.checkbox(f"{i}. {step}", key=f"{choice}_{i}")

# 영상
st.subheader("영상으로 배우기 🎥")
for url in recipe["videos"]:
    st.video(url)

st.markdown("</div>", unsafe_allow_html=True)
