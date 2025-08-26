import streamlit as st
from pptx import Presentation
from pptx.util import Inches, Pt

# --- 앱 제목 ---
st.title("🍞 디저트 앱 발표 자료 만들기 🍰")

# --- PPT 생성 함수 ---
def create_ppt():
    prs = Presentation()

    # 슬라이드 1: 제목
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "🍞 오늘의 디저트 앱"
    slide.placeholders[1].text = "스트림릿으로 만든 디저트 추천 앱 발표 자료"

    # 슬라이드 2: 페이지 설정
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "1️⃣ 페이지 설정"
    slide.placeholders[1].text = (
        "앱 제목, 아이콘, 레이아웃을 설정\n\n"
        "코드 예시:\n"
        "st.set_page_config(page_title='🍞 오늘의 디저트 추천 🍰', page_icon='🥐', layout='centered')"
    )

    # 슬라이드 3: CSS 스타일
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "2️⃣ CSS 스타일"
    slide.placeholders[1].text = (
        "앱 배경색, 글씨 색, 제목 정렬 등 디자인 적용\n\n"
        "코드 예시:\n"
        "st.markdown('<style>body {background-color:#f5e0c3;color:black;}</style>', unsafe_allow_html=True)"
    )

    # 슬라이드 4: 디저트 선택 & 정보 표시
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "3️⃣ 디저트 선택 & 정보 표시"
    slide.placeholders[1].text = (
        "- st.selectbox()로 디저트 선택\n"
        "- 딕셔너리에 재료, 레시피, 팁, 영상 링크 저장\n"
        "- for문으로 재료/레시피/팁 출력\n"
        "- st.video()로 유튜브 영상 표시"
    )

    # 슬라이드 5: 주요 코드 포인트
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "4️⃣ 주요 코드 포인트"
    slide.placeholders[1].text = (
        "1. 스트림릿 기본 함수 사용 (st.title, st.markdown, st.selectbox, st.write, st.video)\n"
        "2. 딕셔너리로 레시피 데이터 구조화\n"
        "3. for문 반복 처리로 정보 출력\n"
        "4. CSS로 디자인 커스터마이징"
    )

    return prs

# --- PPT 다운로드 버튼 ---
if st.button("📥 발표용 PPT 만들기"):
    prs = create_ppt()
    prs.save("디저트_앱_발표.pptx")
    st.success("✅ PPT 파일이 생성되었습니다! 다운로드 버튼 사용 가능")
    st.markdown("[다운로드 PPT](디저트_앱_발표.pptx)")
