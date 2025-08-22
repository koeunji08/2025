import streamlit as st
from datetime import datetime
import pandas as pd
import math

st.set_page_config(page_title="빵 레시피 & 영상 도우미", page_icon="🥖", layout="wide")

# -----------------------------
# 데이터: 레시피 기본값 (1배 기준)
# 단위는 기본적으로 g, 일부는 개수나 큰술/작은술
# -----------------------------
RECIPES = {
    "식빵": {
        "yield_text": "식빵 1개 분량(1.5 파운드 틀)",
        "base_servings": 1,
        "ingredients": [
            {"재료": "강력분", "수량": 400, "단위": "g"},
            {"재료": "우유", "수량": 260, "단위": "g"},
            {"재료": "설탕", "수량": 35, "단위": "g"},
            {"재료": "소금", "수량": 7, "단위": "g"},
            {"재료": "인스턴트 드라이이스트", "수량": 6, "단위": "g"},
            {"재료": "버터", "수량": 30, "단위": "g"},
        ],
        "steps": [
            "우유는 미지근하게(약 30~35℃) 준비해요.",
            "강력분, 설탕, 소금, 이스트를 볼에 넣고 우유를 부어 섞어요.",
            "반죽이 뭉치면 버터를 넣고 매끈해질 때까지 10~15분 반죽해요.",
            "볼에 담아 1차 발효(27~30℃, 60분 내외, 2배).",
            "가스 빼고 분할/둥글리기 → 벤치타임 15분.",
            "틀에 성형하여 2차 발효(35℃, 40~60분).",
            "180℃ 예열 오븐에서 30~35분 굽기.",
            "팬에서 꺼내 식힘망에서 식혀요.",
        ],
        "videos": [
            # 원하는 유튜브 주소로 자유롭게 교체하세요
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        ],
        "time_total_min": 180,
        "level": "초급",
    },
    "바게트": {
        "yield_text": "바게트 2개 분량",
        "base_servings": 2,
        "ingredients": [
            {"재료": "강력분", "수량": 500, "단위": "g"},
            {"재료": "물", "수량": 350, "단위": "g"},
            {"재료": "소금", "수량": 10, "단위": "g"},
            {"재료": "인스턴트 드라이이스트", "수량": 2, "단위": "g"},
        ],
        "steps": [
            "재료 혼합 후 오토리즈 30분.",
            "가볍게 폴드 3~4회(30분 간격).",
            "1차 발효(4℃ 저온 12~18시간 또는 실온 60~90분).",
            "분할/프리셰이핑, 벤치 20분.",
            "성형 후 최종발효(30~45분).",
            "250℃ 충분히 예열, 스팀과 함께 20~25분 굽기.",
        ],
        "videos": [
            "https://www.youtube.com/watch?v=6_b7RDuLwcI"
        ],
        "time_total_min": 300,
        "level": "중급",
    },
    "치아바타": {
        "yield_text": "치아바타 4개 분량",
        "base_servings": 4,
        "ingredients": [
            {"재료": "강력분", "수량": 500, "단위": "g"},
            {"재료": "물", "수량": 400, "단위": "g"},
            {"재료": "소금", "수량": 12, "단위": "g"},
            {"재료": "인스턴트 드라이이스트", "수량": 2, "단위": "g"},
            {"재료": "올리브오일", "수량": 20, "단위": "g"},
        ],
        "steps": [
            "재료 섞고 20분 휴지.",
            "스트레치&폴드 3회(20분 간격).",
            "1차 발효(2배).",
            "듬성듬성 분할, 충분한 가루 위에서 조심히 성형.",
            "230℃ 오븐에서 20~25분 굽기.",
        ],
        "videos": [
            "https://www.youtube.com/watch?v=ZJXh0z6WJbQ"
        ],
        "time_total_min": 210,
        "level": "초급",
    },
    "스콘": {
        "yield_text": "스콘 8개 분량",
        "base_servings": 8,
        "ingredients": [
            {"재료": "박력분", "수량": 300, "단위": "g"},
            {"재료": "베이킹파우더", "수량": 10, "단위": "g"},
            {"재료": "설탕", "수량": 60, "단위": "g"},
            {"재료": "소금", "수량": 3, "단위": "g"},
            {"재료": "차가운 버터", "수량": 120, "단위": "g"},
            {"재료": "우유(또는 생크림)", "수량": 160, "단위": "g"},
            {"재료": "계란", "수량": 1, "단위": "개"},
        ],
        "steps": [
            "가루류 섞고 차가운 버터를 잘라 넣어 사브레 상태로.",
            "우유와 계란 섞어 반죽을 한덩이로 모아요(과반죽 금지).",
            "2~3cm 두께로 펴고 컷팅.",
            "200℃ 예열 오븐에서 15~18분 굽기.",
        ],
        "videos": [
            "https://www.youtube.com/watch?v=J---aiyznGQ"
        ],
        "time_total_min": 50,
        "level": "초급",
    },
}

# -----------------------------
# 유틸 함수
# -----------------------------

def scale_ingredients(ings, scale):
    rows = []
    for i in ings:
        qty = i["수량"]
        unit = i["단위"]
        scaled = qty * scale
        # g 단위는 정수, 나머지는 보기 좋게
        if unit == "g":
            disp = f"{int(round(scaled))}"
        elif unit == "개":
            # 개수는 .5까지 표현
            disp = f"{scaled:.1f}".rstrip("0").rstrip(".")
        else:
            disp = f"{scaled:.1f}".rstrip("0").rstrip(".")
        rows.append({"재료": i["재료"], "수량": disp, "단위": unit})
    return pd.DataFrame(rows)


def make_shopping_list(df, have_items):
    need = []
    for _, r in df.iterrows():
        if r["재료"] not in have_items:
            need.append(f"- {r['재료']}: {r['수량']}{r['단위']}")
    if not need:
        return "✅ 필요한 재료가 모두 있어요!"
    return "\n".join(["🛒 장보기 리스트"] + need)


# -----------------------------
# UI
# -----------------------------
st.title("🥖 빵 레시피 & 영상 도우미")
st.caption("재료·레시피·영상까지 한 번에! 분량 조절과 장보기 리스트도 자동으로 준비해줘요 ✨")

with st.sidebar:
    st.header("레시피 선택")
    recipe_name = st.selectbox("어떤 빵을 만들까요?", list(RECIPES.keys()))
    recipe = RECIPES[recipe_name]

    st.markdown(f"**기준 분량** · {recipe['yield_text']}")
    base = recipe["base_servings"]
    servings = st.number_input("만들 갯수/분량", min_value=1, value=base, step=1)
    scale = servings / base

    st.divider()
    st.subheader("내 냉장고 재료 체크")
    all_items = [i["재료"] for i in recipe["ingredients"]]
    have = st.multiselect("가지고 있는 재료를 선택해 주세요", options=all_items)

    st.divider()
    st.subheader("영상 추가/교체")
    new_video = st.text_input("유튜브/동영상 URL 붙여넣기")
    if new_video:
        videos = [new_video]
    else:
        videos = recipe.get("videos", [])

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("재료 한눈에 보기")
    df = scale_ingredients(recipe["ingredients"], scale)
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "재료 표 CSV로 저장", data=df.to_csv(index=False).encode("utf-8-sig"),
        file_name=f"{recipe_name}_재료표_{servings}배.csv", mime="text/csv"
    )

with col2:
    st.subheader("장보기 리스트")
    shopping = make_shopping_list(df, have)
    st.code(shopping)
    st.download_button(
        "장보기 리스트 .txt 저장",
        data=shopping.encode("utf-8"),
        file_name=f"{recipe_name}_장보기리스트.txt",
        mime="text/plain",
    )

st.divider()

# 탭: 만드는 순서 / 타이머 / 영상
make_tab, timer_tab, video_tab = st.tabs(["👩‍🍳 만드는 순서", "⏱️ 간단 타이머", "🎬 따라하기 영상"])

with make_tab:
    st.markdown(f"**난이도**: {recipe['level']}  ·  **예상 소요**: 약 {recipe['time_total_min']}분")
    for idx, step in enumerate(recipe["steps"], 1):
        st.checkbox(f"{idx}. {step}", key=f"step_{idx}")

with timer_tab:
    st.info("간단 타이머: 버튼을 누르면 해당 분수 뒤에 알림이 뜹니다(브라우저 탭 주의). 스트림릿 특성상 아주 정밀하진 않아요 😊")
    mins = st.slider("타이머(분)", 1, 60, 15)
    if st.button("타이머 시작"):
        st.session_state["timer_start"] = datetime.now()
        st.session_state["timer_end"] = st.session_state["timer_start"] + pd.to_timedelta(mins, unit="m")
        st.success(f"{mins}분 타이머 시작! 다른 탭을 보셔도 돼요")

    if "timer_end" in st.session_state:
        remaining = st.session_state["timer_end"] - datetime.now()
        if remaining.total_seconds() > 0:
            st.metric("남은 시간", f"{math.ceil(remaining.total_seconds()/60)} 분")
        else:
            st.warning("⏰ 타이머 종료! 반죽을 확인해주세요")

with video_tab:
    if videos:
        for url in videos:
            st.video(url)
    else:
        st.write("영상 URL을 사이드바에 붙여넣으면 여기서 바로 볼 수 있어요!")

st.divider()

with st.expander("치환/팁 보기"):
    st.markdown(
        """
        - 우유 → 물로 대체 가능(풍미 감소).
        - 인스턴트 드라이이스트 1g ≈ 생이스트 3g.
        - 반죽 온도는 24~26℃ 전후가 좋아요.
        - 굽는 온도/시간은 **반드시** 내 오븐에 맞춰 미세 조정해요.
        - 재료는 **그램(정확)** 계량을 추천해요.
        """
    )

st.caption("원하는 레시피를 더 넣고 싶다면 코드의 RECIPES 사전을 그대로 따라 하나 더 추가해 주세요 ✍️")

