import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🌈 MBTI 직업 추천 💼", page_icon="🚀", layout="centered")

# 타이틀
st.markdown(
    """
    <h1 style="text-align:center; font-size:48px;">🌟 MBTI 기반 진로 추천 사이트 🌟</h1>
    <p style="text-align:center; font-size:20px;">✨ 당신의 MBTI를 선택하면 어울리는 직업을 알려드려요! ✨</p>
    """,
    unsafe_allow_html=True
)

# MBTI 리스트
mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI → 직업 추천 매핑
career_dict = {
    "ISTJ": ["📊 회계사", "🏛 행정직", "🪖 군인", "⚖️ 법률가"],
    "ISFJ": ["💉 간호사", "🤝 사회복지사", "📚 교사", "📝 비서"],
    "INFJ": ["🧠 심리상담가", "✍️ 작가", "📖 교사", "💡 컨설턴트"],
    "INTJ": ["🔬 과학자", "♟ 전략가", "📊 연구원", "💹 투자분석가"],
    "ISTP": ["🔧 엔지니어", "⚙️ 기술자", "🛩 파일럿", "🏋️ 운동선수"],
    "ISFP": ["🎨 예술가", "🎭 디자이너", "🎶 작곡가", "🌱 치유사"],
    "INFP": ["📖 작가", "💞 상담가", "🌍 인권운동가", "📚 교사"],
    "INTP": ["🎓 교수", "💻 프로그래머", "🔍 연구원", "📊 데이터 분석가"],
    "ESTP": ["🚀 기업가", "💼 세일즈 전문가", "⚽ 운동선수", "👮 경찰"],
    "ESFP": ["🎤 연예인", "🎉 이벤트 플래너", "📢 광고 전문가", "🎓 강사"],
    "ENFP": ["📢 마케터", "🚀 스타트업 창업가", "✍️ 작가", "📱 홍보 전문가"],
    "ENTP": ["💡 발명가", "🚀 기업가", "⚖️ 변호사", "🏛 정치가"],
    "ESTJ": ["👔 경영자", "🪖 군인", "📋 프로젝트 매니저", "🏛 행정가"],
    "ESFJ": ["💉 간호사", "📚 교사", "🤝 HR 전문가", "🌍 사회사업가"],
    "ENFJ": ["🎤 강사", "💞 상담가", "🌟 지도자", "📣 홍보 전문가"],
    "ENTJ": ["👑 CEO", "⚖️ 변호사", "📊 경영 컨설턴트", "📋 프로젝트 매니저"],
}

# 선택 UI
user_mbti = st.selectbox("🔎 당신의 MBTI는?", mbti_list, index=2)

# 결과 출력
if user_mbti in career_dict:
    st.markdown(f"<h2 style='text-align:center;'>🔮 {user_mbti} 유형 추천 직업 🔮</h2>", unsafe_allow_html=True)

    for job in career_dict[user_mbti]:
        st.markdown(
            f"""
            <div style="
                padding:20px;
                margin:12px 0;
                border-radius:20px;
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                color:#333;
                font-size:20px;
                text-align:center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                ">
                ✨ {job} ✨
            </div>
            """,
            unsafe_allow_html=True
        )

    st.balloons()
else:
    st.warning("😅 아직 이 MBTI는 준비되지 않았어요!")
