import streamlit as st
from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt

# --- Streamlit 페이지 설정 ---
st.set_page_config(
    page_title="🍞 디저트 앱 발표용 PPT 🍰",
    page_icon="🥐",
    layout="centered"
)

st.title("🍞🥐 디저트 앱 발표용 PPT 만들기 🧁🍪")
st.markdown("아래 버튼을 클릭하면 앱 소개 PPT 파일을 다운로드할 수 있습니다!")

# --- PPT 생성 함수 ---
def create_ppt():
    prs = Presentation()

    slides = [
        ("🍞 오늘의 몽글몽글 디저트 앱", "Streamlit으로 만든 디저트 레시피 앱\n선택한 디저트의 레시피와 영상 제공"),
        ("앱 기능", "디저트 선택 가능\n레시피, 재료, 팁, 영상 제공\n직관적 UI + 귀여운 디자인"),
        ("Streamlit 기본", "import streamlit as st\nst.set_page_config(...)"),
        ("CSS 스타일 적용", "st.markdown('''<style>...''', unsafe_allow_html=True)"),
        ("타이틀 & 안내문", "st.title(...)\nst.markdown(...)"),
        ("디저트 선택", "dessert = st.selectbox(..., [디저트 목록])"),
        ("디저트 정보 저장", "딕셔너리로 레시피, 재료, 영상 저장"),
        ("선택한 디저트 정보 표시", "st.subheader(dessert)\nst.write(info['description'])\nfor ing in info['ingredients']:\n    st.write(f'- {ing}')\nst.video(info['video'])"),
        ("발표 포인트", "Streamlit으로 인터랙티브 앱 제작\nCSS로 디자인 커스터마이징\n딕셔너리로 데이터 구조화\nfor문으로 리스트 반복 출력")
    ]

    for title, content in slides:
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = title
        slide.placeholders[1].text = content

    ppt_bytes = BytesIO()
    prs.save(ppt_bytes)
    ppt_bytes.seek(0)
    return ppt_bytes

# --- 다운로드 버튼 ---
ppt_file = create_ppt()
st.download_button(
    label="📥 PPT 다운로드",
    data=ppt_file,
    file_name="디저트앱_발표.pptx",
    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
)
