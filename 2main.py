import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt
from io import BytesIO

# --- 디저트 정보 ---
dessert_info = {
    "초코소라빵 🍫": {
        "description": "촉촉한 초코 시트와 달콤한 필링이 조화된 홈베이킹 대표 메뉴입니다.",
        "ingredients": [
            "강력분 200~250g", "설탕 25~30g", "소금 3g", "인스턴트 이스트 3~4g",
            "우유 120~150ml", "계란 1개", "녹인 버터 10~30g", "코코아 가루 20g",
            "무염버터 50g", "슈가파우더 50g", "코코아 가루 10g", "우유 20ml"
        ],
        "recipe": [
            "반죽: 강력분, 설탕, 소금 섞은 후 따뜻한 우유에 이스트 풀고 5분 둡니다.",
            "계란과 녹인 버터 추가 후 코코아 가루 넣고 10분 치댐. 1시간 1차 발효.",
            "필링: 버터+슈가파우더+코코아+우유 섞어 준비.",
            "성형: 반죽 5mm 두께로 펴 필링 발라 돌돌 말기. 1시간 2차 발효.",
            "굽기: 180℃ 오븐에서 15~20분 굽고 코코아 가루 뿌리기."
        ],
        "video": "https://youtu.be/FaSJFZsYzEM?si=gtqDUZeEDd4emRms"
    },
    "소금빵 🧂": {
        "description": "일본 유래 버터 풍미 발효빵, 겉바속촉 짭조름한 맛.",
        "ingredients": [
            "강력분 200g", "박력분 100g", "설탕 25g", "소금 6g", "드라이이스트 6g",
            "물 170ml", "버터 25g", "추가 버터 60g", "펄솔트 약간"
        ],
        "recipe": [
            "반죽: 가루류에 이스트 녹인 따뜻한 물 넣고 15분 치대기.",
            "1차 발효: 1시간 따뜻한 곳 (40℃ 유지).",
            "성형: 6등분 후 버터 넣고 돌돌 말아 크로아상 형태.",
            "2차 발효: 50분 따뜻한 곳.",
            "굽기: 200℃ 오븐 20분, 펄솔트 토핑."
        ],
        "video": "https://youtu.be/OoKzyOJLygo?si=uSNS7NHAKL_y43pV"
    },
    "마카롱 🌈": {
        "description": "꼬끄와 필링으로 구성, 초보자도 도전 가능.",
        "ingredients": [
            "아몬드가루 82~92g", "슈가파우더 75~92g", "달걀흰자 63~65g",
            "설탕 20~60g", "코코아파우더 5~7g (선택)",
            "생크림 100g", "다크초콜릿 100g", "버터 10g", "물엿 15g"
        ],
        "recipe": [
            "꼬끄 준비: 아몬드+슈가 체에 내려 달걀흰자+설탕 3회 넣어 머랭 만들기.",
            "팬닝: 짤주머니에 담아 3.5cm 팬에 짜고 30분~1시간 실온 말리기.",
            "굽기: 150~170℃ 오븐 13~14분, 식힌 후 필링 넣어 샌드."
        ],
        "video": "https://youtu.be/XzC1aN6jpsI?si=oxLXEEkmxqL96ZWM"
    },
    "쿠키 🍪": {
        "description": "초콜릿 칩 쿠키, 겉바속촉 또는 쫀득한 식감.",
        "ingredients": [
            "무염버터 100g", "설탕 50g", "황설탕 50g", "계란 1개", "바닐라 익스트랙 1작은술",
            "박력분 160g", "베이킹소다 1/3작은술", "소금 한 꼬집",
            "초코칩 80g", "견과류 (선택)"
        ],
        "recipe": [
            "버터+설탕 크림화: 실온 버터와 설탕 섞기.",
            "계란+바닐라 추가.",
            "가루류 혼합: 박력분, 베이킹소다, 소금.",
            "초코칩+견과류 넣고 냉장 30분 휴지.",
            "170℃ 오븐 12~15분 굽기, 식힘망에 식힘."
        ],
        "video": "https://youtu.be/00hLM-CftNg?si=aV3yY_JVqkE6oGt9"
    },
    "토스트 🍞": {
        "description": "햄&치즈 에그 토스트, 매콤/달콤 소스로 즐기기.",
        "ingredients": [
            "식빵", "계란", "햄", "치즈", "버터", "소스 (마요+스리라차/연유)"
        ],
        "recipe": [
            "계란물에 야채 섞어 팬에 굽기.",
            "빵 위에 햄, 치즈, 달걀 올리기.",
            "취향 소스 발라 완성."
        ],
        "video": "https://youtu.be/SwYuaK3Bqac?si=3o9szJtaLppGou4D"
    },
    "케이크 🎂": {
        "description": "부드럽고 촉촉한 케이크, 초보자도 쉽게 가능.",
        "ingredients": [
            "박력분 150g", "설탕 100g", "버터 100g", "계란 2개",
            "우유 50ml", "베이킹파우더 1작은술", "바닐라 익스트랙 1작은술"
        ],
        "recipe": [
            "오븐 170℃ 예열",
            "버터+설탕 크림화",
            "계란 한 개씩 넣고 섞기",
            "박력분+베이킹파우더 체에 내려 혼합",
            "우유+바닐라 넣고 가볍게 섞기",
            "틀에 붓고 25~30분 굽기. 꼬치 테스트"
        ],
        "video": "https://youtu.be/WBll_pmvY78?si=4SK-cAG4ovcRbjD7"
    }
}

# --- Streamlit UI ---
st.title("🍞 디저트 PPT 생성기 🍰")
dessert_selected = st.multiselect("PPT에 넣을 디저트를 선택하세요", list(dessert_info.keys()))

if st.button("PPT 생성 및 다운로드"):
    prs = Presentation()
    
    for name in dessert_selected:
        info = dessert_info[name]
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = name
        
        content = f"{info['description']}\n\n"
        content += "재료:\n" + "\n".join(info['ingredients']) + "\n\n"
        content += "만드는 법:\n" + "\n".join(info['recipe']) + "\n\n"
        content += f"영상: {info['video']}"
        
        textbox = slide.shapes.placeholders[1]
        textbox.text = content

    # PPT 저장
    ppt_io = BytesIO()
    prs.save(ppt_io)
    ppt_io.seek(0)
    
    st.download_button(
        label="PPT 다운로드",
        data=ppt_io,
        file_name="dessert_recipes.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
