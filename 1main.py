import streamlit as st
import pandas as pd

# -----------------------------
# 업데이트된 빵 레시피 with 새로운 유튜브 영상
# -----------------------------
RECIPES = {
    "스콘": {
        "yield_text": "스콘 약 8개 분량",
        "base_servings": 8,
        "ingredients": [
            {"재료": "박력분", "수량": 250, "단위": "g"},
            {"재료": "베이킹파우더", "수량": 10, "단위": "g"},
            {"재료": "버터", "수량": 80, "단위": "g"},
            {"재료": "설탕", "수량": 40, "단위": "g"},
            {"재료": "우유", "수량": 120, "단위": "g"},
        ],
        "steps": [
            "가루류를 체쳐서 섞기.",
            "차가운 버터 넣고 잘게 쪼개기.",
            "우유 넣고 반죽 뭉치기.",
            "모양 잡아 자르기.",
            "180℃에서 15~20분 굽기.",
        ],
        "videos": [
            "https://youtu.be/cEyl4WDfkWs?si=tnB-t7Semhzd1NST"
        ],
        "time_total_min": 40,
        "level": "초급",
    },
    "마카롱": {
        "yield_text": "마카롱 약 20개 분량",
        "base_servings": 20,
        "ingredients": [
            {"재료": "아몬드 가루", "수량": 100, "단위": "g"},
            {"재료": "슈가파우더", "수량": 100, "단위": "g"},
            {"재료": "달걀 흰자", "수량": 80, "단위": "g"},
            {"재료": "설탕", "수량": 100, "단위": "g"},
        ],
        "steps": [
            "아몬드가루와 슈가파우더 체치기.",
            "달걀흰자에 설탕 넣어 머랭 만들기.",
            "가루 넣고 마카로나주.",
            "짜주머니로 팬닝 후 건조.",
            "150℃에서 12~15분 굽기.",
        ],
        "videos": [
            "https://youtu.be/XzC1aN6jpsI?si=dMtHORuvKmQpHrqt"
        ],
        "time_total_min": 120,
        "level": "고급",
    },
    "쿠키": {
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
        "steps": [
            "버터와 설탕 크림화.",
            "달걀 넣고 섞기.",
            "가루류 넣고 섞기.",
            "초코칩 넣어 반죽 완성.",
            "180℃에서 12분 굽기.",
        ],
        "videos": [
            "https://youtu.be/ZbptGNeo-mk?si=EylMm6c7N3SJ_sra"
        ],
        "time_total_min": 30,
        "level": "초급",
    },
    "케이크": {
        "yield_text": "케이크 1호 사이즈",
        "base_servings": 6,
        "ingredients": [
            {"재료": "박력분", "수량": 120, "단위": "g"},
            {"재료": "달걀", "수량": 3, "단위": "개"},
            {"재료": "설탕", "수량": 100, "단위": "g"},
            {"재료": "버터", "수량": 80, "단위": "g"},
            {"재료": "우유", "수량": 50, "단위": "g"},
        ],
        "steps": [
            "달걀과 설탕 중탕으로 거품.",
            "가루 넣고 섞기.",
            "녹인 버터와 우유 넣기.",
            "틀에 넣고 170℃에서 30분 굽기.",
        ],
        "videos": [
            "https://youtu.be/CkkaCdEV5nY?si=3Mgjovb2MYIhXlWO"
        ],
        "time_total_min": 60,
        "level": "중급",
    },
    "초코소라빵": {
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
        "steps": [
            "반죽하여 1차 발효.",
            "분할, 둥글리기 후 휴지.",
            "밀대로 펴서 소라 모양 성형.",
            "초코크림 채우기.",
            "180℃에서 15분 굽기.",
        ],
        "videos": [
            "https://youtu.be/FaSJFZsYzEM?si=a3TzEOu2CuQiHbog"
        ],
        "time_total_min": 150,
        "level": "중급",
    },
    "소금빵": {
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
        "steps": [
            "반죽하여 1차 발효.",
            "분할, 둥글리기 후 휴지.",
            "삼각형으로 밀어서 롤링 성형.",
            "소금 솔솔 뿌리기.",
            "180℃에서 15분 굽기.",
        ],
        "videos": [
            "https://youtu.be/OoKzyOJLygo?si=Bzx4o8eiCMrBhzmg"
        ],
        "time_total_min": 120,
        "level": "중급",
    },
}

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="빵 레시피 도우미", layout="wide")
st.title("🥐 빵 레시피 & 영상 도우미")

choice = st.sidebar.selectbox("빵 종류 선택", list(RECIPES.keys()))
recipe = RECIPES[choice]

st.header(f"📌 {choice} 레시피")
st.write(recipe["yield_text"])

# 재료표
st.subheader("재료")
df = pd.DataFrame(recipe["ingredients"])
st.table(df)

# 단계별 레시피
st.subheader("만드는 법")
for i, step in enumerate(recipe["steps"], 1):
    st.checkbox(f"{i}. {step}", key=f"{choice}_{i}")

# 영상
st.subheader("영상으로 배우기 🎥")
for url in recipe["videos"]:
    st.video(url)
