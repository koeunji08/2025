from pptx import Presentation
from pptx.util import Inches, Pt

# 새 프레젠테이션 생성
prs = Presentation()

# --- 슬라이드 함수 ---
def add_slide(title, content):
    slide_layout = prs.slide_layouts[1]  # 제목 + 내용
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = title
    text_box = slide.placeholders[1]
    text_box.text = content

# --- 슬라이드 내용 ---
slides = [
    ("🍞 오늘의 몽글몽글 디저트 앱 🍪",
     "Streamlit을 사용한 홈베이킹 레시피 앱\n사용자가 디저트를 선택하면 재료, 레시피, 팁, 영상 표시"),
    
    ("페이지 설정",
     "st.set_page_config(page_title='🍞 오늘의 디저트 추천 🍰', page_icon='🥐', layout='centered')\n- 앱 제목, 아이콘, 레이아웃 설정"),
    
    ("스타일 적용",
     "st.markdown(\"<style>body{background-color:#f5e0c3;color:black;}</style>\", unsafe_allow_html=True)\n- 글자색, 배경색, 폰트 스타일 적용"),
    
    ("타이틀과 안내문",
     "st.title('🍞🥐 오늘의 몽글몽글 디저트 🧁🍪')\nst.markdown('환영해요! 🥰 ...')\n- 제목과 안내 문구 표시"),
    
    ("디저트 선택",
     "dessert = st.selectbox('🍰 디저트를 선택해 주세요:', ['초코소라빵', '소금빵', '마카롱', '쿠키', '토스트', '케이크'])\n- 드롭다운 메뉴로 사용자 선택"),
    
    ("데이터 구조",
     "dessert_info = {\n '초코소라빵': {'description':'...', 'ingredients':[...], 'recipe':[...], 'tips':[...], 'video':'...'}, ...}\n- 딕셔너리 사용"),
    
    ("정보 출력",
     "info = dessert_info[dessert]\nst.write(info['description'])\nfor ing in info['ingredients']: st.write(f'- {ing}')\nst.video(info['video'])\n- 선택한 디저트 정보 출력"),
    
    ("핵심 코드 요약",
     "st.set_page_config(): 앱 제목, 아이콘, 레이아웃 설정\n"
     "st.markdown(): 글자색, 배경색, 폰트 디자인\n"
     "st.title()/st.markdown(): 제목과 안내문\n"
     "st.selectbox(): 사용자 선택 메뉴\n"
     "dict(딕셔너리): 디저트별 데이터 관리\n"
     "for문: 재료/레시피/팁 반복 출력\n"
     "st.video(): 영상 삽입")
]

# --- 슬라이드 추가 ---
for title, content in slides:
    add_slide(title, content)

# --- 파일 저장 ---
prs.save("Dessert_App_Code_Analysis.pptx")
print("PPT 생성 완료!")
