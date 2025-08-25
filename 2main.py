import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="🍞 디저트 PPT용 미리보기",
    page_icon="🥐",
    layout="centered"
)

# --- 스타일 ---
st.markdown("""
<style>
body {
    background-color: #f5e0c3;
    color: black;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.slide {
    background-color: #fff5e6;
    padding: 20px;
    margin: 20px 0;
    border-radius: 15px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
}
h2 {
    text-align: center;
    color: #d2691e;
}
</style>
""", unsafe_allow_html=True)

# --- 디저트 데이터 ---
desserts = {
    "초코소라빵 🍫": {
        "description": "촉촉한 초코 시트와 달콤한 필링이 조화된 홈베이킹 대표 메뉴입니다.",
        "ingredients": [
            "강력분 200~250g", "설탕 25~30g", "소금 3g", "인스턴트 이스트 3~4g",
            "우유 120~150ml", "계란 1개", "녹인 버터 10~30g", "코코아 가루 20g",
            "무염버터 50g", "슈가파우더 50g", "코코아 가루 10g", "우유 20ml"
        ],
        "recipe": [
            "반죽 준비 → 1차 발효",
            "필링 준비",
            "반죽 성형 후 2차 발효",
            "굽기 180℃ 15~20분"
        ]
    },
    "소금빵 🧂": {
        "description": "일본에서 유래한 버터 풍미의 발효빵, 겉바속촉과 짭조름한 맛이 특징입니다.",
        "ingredients": [
            "강력분 200g", "박력분 100g", "설탕 25g", "소금 6g", "드라이이스트 6g",
            "물 170ml", "버터 25g", "추가 버터 60g", "펄솔트 약간"
        ],
        "recipe": [
            "반죽 → 1차 발효 1시간",
            "버터 넣고 성형 → 2차 발효 50분",
            "굽기 200℃ 20분"
        ]
    },
    "마카롱 🌈": {
        "description": "꼬끄와 필링으로 구성된 프랑스 디저트.",
        "ingredients": [
            "아몬드가루 82~92g", "슈가파우더 75~92g", "달걀흰자 63~65g",
            "설탕 20~60g", "코코아파우더 5~7g", "생크림 100g",
            "다크초콜릿 100g", "버터 10g", "물엿 15g"
        ],
        "recipe": [
            "꼬끄 준비 → 머랭 만들기 → 가루와 섞기",
            "팬닝 3.5cm → 표면 건조 30분~1시간",
            "굽기 150~170℃ 13~14분 → 필링 샌드"
        ]
    }
}

st.title("🍞 디저트 PPT용 미리보기")

# --- HTML로 슬라이드처럼 표시 ---
html_content = ""
for name, info in desserts.items():
    html_content += f"<div class='slide'><h2>{name}</h2>"
    html_content += f"<p><b>설명:</b> {info['description']}</p>"
    html_content += "<p><b>재료:</b></p><ul>"
    for ing in info['ingredients']:
        html_content += f"<li>{ing}</li>"
    html_content += "</ul>"
    html_content += "<p><b>만드는 방법:</b></p><ol>"
    for step in info['recipe']:
        html_content += f"<li>{step}</li>"
    html_content += "</ol></div>"

st.markdown(html_content, unsafe_allow_html=True)

st.info("브라우저에서 'Print' → 'Save as PDF'로 저장하면 PPT처럼 사용할 수 있습니다. 🖨️")
