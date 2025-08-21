import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(
    page_title="🍞귀여운 빵 디저트 만들기🍰",
    page_icon="🥐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- CSS 스타일 ---
st.markdown("""
<style>
body {
    background-color: #fff0f5; /* 연한 분홍 배경 */
}
h1, h2, h3 {
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #ff69b4;
}
.stButton>button {
    background-color: #ffb6c1;
    color: white;
    font-weight: bold;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# --- 타이틀 ---
st.title("🥐 귀여운 빵 디저트 만들기 🥰")
st.markdown("나만의 빵 디저트를 만들어보세요! 재료 선택, 랜덤 레시피, 그리고 귀여운 그림까지 😋")

# --- 재료 선택 ---
st.header("🍞 재료 선택하기")
breads = st.multiselect(
    "기본 빵을 선택해주세요",
    ["식빵", "바게트", "머핀", "크루아상", "도넛"]
)
toppings = st.multiselect(
    "토핑을 골라주세요",
    ["초콜릿", "딸기잼", "치즈", "아몬드", "크림"]
)

if breads or toppings:
    st.markdown("### 🥰 내가 선택한 디저트")
    st.write("빵:", ", ".join(breads) if breads else "없음")
    st.write("토핑:", ", ".join(toppings) if toppings else "없음")

# --- 랜덤 레시피 ---
st.header("🎲 랜덤 디저트 레시피")
if st.button("레시피 뽑기!"):
    base = random.choice(["식빵", "머핀", "바게트", "크루아상", "도넛"])
    top = random.choice(["초콜릿", "딸기잼", "치즈", "아몬드", "크림"])
    st.success(f"오늘의 디저트는 **{base} + {top}** 😋")

    # --- 귀여운 이미지 보여주기 ---
    # 이미지 URL 예시 (인터넷에서 귀여운 빵 이미지 사용)
    cute_images = [
        "https://i.ibb.co/9V2Ff2v/cute-bread1.png",
        "https://i.ibb.co/1v3tCvx/cute-bread2.png",
        "https://i.ibb.co/3Y7fCwJ/cute-bread3.png"
    ]
    img_url = random.choice(cute_images)
    st.image(img_url, width=300, caption=f"{base} + {top} 완성!")

# --- 마무리 ---
st.markdown("💖 재료와 레시피를 조합하며 나만의 귀여운 디저트를 만들어보세요!")
