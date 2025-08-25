import streamlit as st

# 디저트 정보 딕셔너리
dessert_info = {
    "🥖 바게트": {
        "desc": "겉은 바삭하고 속은 쫄깃한 프랑스 전통 빵이에요.",
        "ingredients": [
            "- 강력분 250g",
            "- 물 170ml",
            "- 소금 5g",
            "- 드라이이스트 3g"
        ],
        "recipe": [
            "1️⃣ 밀가루, 물, 이스트, 소금을 넣고 반죽합니다.",
            "2️⃣ 반죽을 둥글게 만들어 1차 발효를 시킵니다.",
            "3️⃣ 길게 성형 후 2차 발효합니다.",
            "4️⃣ 오븐에서 220℃로 20분간 구워줍니다."
        ],
        "video": "https://www.youtube.com/watch?v=yeJ7kD9-O4k"
    },
    "🥯 베이글": {
        "desc": "쫄깃하고 담백한 뉴욕 스타일의 빵이에요.",
        "ingredients": [
            "- 강력분 250g",
            "- 물 140ml",
            "- 설탕 10g",
            "- 소금 5g",
            "- 드라이이스트 3g"
        ],
        "recipe": [
            "1️⃣ 모든 재료를 섞어 반죽합니다.",
            "2️⃣ 도넛 모양으로 성형 후 1차 발효합니다.",
            "3️⃣ 끓는 물에 살짝 데친 후 오븐에서 굽습니다."
        ],
        "video": "https://www.youtube.com/watch?v=EkGX9U5d4X0"
    },
    "🍪 마카롱": {
        "desc": "달콤하고 바삭한 프랑스 대표 디저트예요.",
        "ingredients": [
            "아몬드 가루: 100g",
            "슈가파우더: 100g",
            "달걀 흰자: 70g (상온)",
            "설탕: 30g",
            "무염버터: 50g",
            "바닐라 익스트랙: 약간"
        ],
        "recipe": [
            "1️⃣ 아몬드 가루와 슈가파우더를 체에 내립니다.",
            "2️⃣ 달걀 흰자에 설탕을 넣어 머랭을 만듭니다.",
            "3️⃣ 가루와 머랭을 섞어 리본처럼 흐르는 반죽을 만듭니다.",
            "4️⃣ 짤주머니에 넣고 팬에 짠 뒤 건조시킵니다.",
            "5️⃣ 150℃ 오븐에서 12~15분간 굽습니다.",
            "6️⃣ 버터크림을 만들어 샌드 후 숙성시킵니다."
        ],
        "video": "https://www.youtube.com/watch?v=yz8dm8dAP2c"
    }
}

# --- Streamlit UI ---
st.set_page_config(page_title="🍞 디저트 레시피북", page_icon="🍩")

st.markdown(
    """
    <div style='text-align: center; background-color:#d9a066; padding:30px; border-radius:25px;'>
        <h1 style='color:white;'>🥐 몽글몽글 빵&디저트 레시피북 🍪</h1>
        <p style='color:white;'>원하는 디저트를 선택해 보세요!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 선택 박스
dessert = st.selectbox("🍰 디저트를 골라주세요!", list(dessert_info.keys()))

if dessert:
    info = dessert_info[dessert]
    st.header(dessert)
    st.write(info["desc"])

    st.markdown("### 🧺 재료")
    for ing in info["ingredients"]:
        st.write(ing)

    st.markdown("### 👩‍🍳 만드는 법")
    for step in info["recipe"]:
        st.write(step)

    st.markdown("### 🎬 만드는 영상")
    st.video(info["video"])if dessert:
    st.subheader(f"{dessert} 🍰")
    st.write(dessert_info[dessert]["description"])
    
    st.markdown("### 🥣 필요한 재료")
    for ingredient in dessert_info[dessert]["ingredients"]:
        st.write(f"- {ingredient}")
    
    st.markdown("### 📝 만드는 방법")
    for step in dessert_info[dessert]["recipe"]:
        st.write(f"- {step}")
    
    st.markdown("### 🎬 만드는 영상")
    st.video(dessert_info[dessert]["video"])            "2️⃣ 반죽을 동그랗게 만들어 팬에 올립니다.",
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
    for ingredient in dessert_info[dessert]["ingredients"]:
        st.write(f"- {ingredient}")
    
    st.markdown("### 📝 만드는 방법")
    for step in dessert_info[dessert]["recipe"]:
        st.write(f"- {step}")
    
    st.markdown("### 🎬 만드는 영상")
    st.video(dessert_info[dessert]["video"])    df = pd.DataFrame(recipe["ingredients"])
    st.table(df)

    # 단계별 레시피
    st.subheader("🥣 만드는 법")
    for i, step in enumerate(recipe["steps"], 1):
        st.checkbox(f"{i}. {step}", key=f"{choice}_{i}")

    # 영상
    st.subheader("🎥 영상으로 배우기")
    for url in recipe["videos"]:
        st.video(url)
