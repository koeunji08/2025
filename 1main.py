import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="법 상식 퀴즈", page_icon="⚖️", layout="centered")
st.markdown("<h1 style='text-align:center; color:#2E86C1;'>⚖️ 법 상식 퀴즈</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- 문제 데이터 ---
basic_questions = [
    {"q": "대한민국의 최고 법은 헌법이다.", "a": "O"},
    {"q": "헌법상 대한민국의 주권은 국민에게 있다.", "a": "O"},
    {"q": "대통령 선거는 4년에 한 번씩 열린다.", "a": "X"},
    {"q": "대한민국은 민주공화국이다.", "a": "O"},
    {"q": "대한민국의 수도는 부산이다.", "a": "X"},
    {"q": "헌법 제1조는 국가의 정체를 규정한다.", "a": "O"},
    {"q": "대한민국은 다당제 국가이다.", "a": "O"},
    {"q": "국회의원 임기는 6년이다.", "a": "X"},
    {"q": "대법원장은 대통령이 임명한다.", "a": "O"},
    {"q": "국무총리는 국회의원만 될 수 있다.", "a": "X"},
    {"q": "지방자치단체장은 선거로 선출된다.", "a": "O"},
    {"q": "대한민국의 국기에는 빨간색, 파란색, 검은색, 흰색이 사용된다.", "a": "O"},
    {"q": "헌법은 법률보다 효력이 낮다.", "a": "X"},
    {"q": "대통령은 헌법상 국가원수이다.", "a": "O"},
    {"q": "대한민국의 법률 제정권은 행정부에 있다.", "a": "X"},
]

advanced_questions = [
    {"q": "형사재판에서 무죄가 선고되려면 '합리적 의심이 없는 증명'이 필요하다.", "a": "O"},
    {"q": "만 13세 미만의 청소년은 형사처벌을 받을 수 있다.", "a": "X"},
    {"q": "도로교통법상 보행자는 횡단보도에서 무조건 우선권이 있다.", "a": "O"},
    {"q": "헌법재판소는 법률의 위헌 여부를 판단할 수 있다.", "a": "O"},
    {"q": "대한민국 국회는 단원제로 구성되어 있다.", "a": "X"},
    {"q": "형법은 범죄와 형벌을 규정한다.", "a": "O"},
    {"q": "행정법은 공공기관과 개인 간의 관계를 다룬다.", "a": "O"},
    {"q": "민사재판에서는 피해자가 형사 책임을 추궁할 수 있다.", "a": "X"},
    {"q": "헌법재판소는 대통령 탄핵 심판을 한다.", "a": "O"},
    {"q": "법원은 모든 법률의 해석과 적용을 결정한다.", "a": "O"},
    {"q": "헌법상 기본권은 제한할 수 없다.", "a": "X"},
    {"q": "형사소송법은 피고인의 권리를 보장한다.", "a": "O"},
    {"q": "지방자치단체는 독자적으로 외교를 수행할 수 있다.", "a": "X"},
    {"q": "헌법상 국민투표는 필수적인 제도이다.", "a": "O"},
    {"q": "법률안은 대통령이 직접 발의할 수 있다.", "a": "X"},
]

# --- 세션 상태 초기화 ---
for key in ["questions", "user_answers", "current_idx", "level"]:
    if key not in st.session_state:
        if key == "questions":
            st.session_state[key] = []
        elif key == "user_answers":
            st.session_state[key] = []
        elif key == "current_idx":
            st.session_state[key] = 0
        else:
            st.session_state[key] = "기본"

# --- 난이도 선택 ---
level = st.radio("🔹 난이도를 선택하세요:", ["기본", "심화"], index=0)
st.session_state["level"] = level

if st.button("🚀 퀴즈 시작"):
    st.session_state["questions"] = random.sample(
        basic_questions if level == "기본" else advanced_questions,
        len(basic_questions if level == "기본" else advanced_questions)
    )
    st.session_state["user_answers"] = []
    st.session_state["current_idx"] = 0
    st.success("퀴즈가 시작되었습니다! 😎 문제를 풀어보세요.")

st.markdown("---")

# --- 퀴즈 진행 ---
if st.session_state["questions"] and st.session_state["current_idx"] < len(st.session_state["questions"]):
    current_q = st.session_state["questions"][st.session_state["current_idx"]]
    st.subheader(f"❓ 문제 {st.session_state['current_idx'] + 1}")
    st.markdown(f"<p style='font-size:18px'>{current_q['q']}</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    if col1.button("⭕ O"):
        st.session_state["user_answers"].append({"q": current_q['q'], "your": "O", "answer": current_q['a']})
        st.session_state["current_idx"] += 1
    if col2.button("❌ X"):
        st.session_state["user_answers"].append({"q": current_q['q'], "your": "X", "answer": current_q['a']})
        st.session_state["current_idx"] += 1

# --- 결과 요약 ---
if not st.session_state["questions"] and st.session_state["user_answers"]:
    st.markdown("---")
    st.subheader("📊 결과 요약")
    total = len(st.session_state["user_answers"])
    correct = sum(1 for a in st.session_state["user_answers"] if a['your'] == a['answer'])
    accuracy = correct / total * 100

    st.metric("정답 개수", f"{correct} / {total}")
    st.metric("정답률", f"{accuracy:.1f}%")

    if accuracy < 40:
        st.warning("📘 당신의 레벨: 법 상식 초보 – 차근차근 공부해보세요!")
    elif accuracy < 70:
        st.info("📗 당신의 레벨: 법 상식 보통 – 꽤 잘 알고 있네요!")
    else:
        st.success("📕 당신의 레벨: 법 상식 마스터 – 대단합니다! 👏")

    if st.checkbox("❌ 틀린 문제와 정답 보기"):
        for idx, a in enumerate(st.session_state["user_answers"], 1):
            st.write(f"{idx}. {a['q']}  |  내 답: {a['your']}  |  정답: {a['answer']}")

    if st.button("🔄 다시 시작"):
        st.session_state["questions"] = []
        st.session_state["user_answers"] = []
        st.session_state["current_idx"] = 0
        st.experimental_rerun()
