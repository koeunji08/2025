import streamlit as st
import random

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
]

advanced_questions = [
    {"q": "형사재판에서 무죄가 선고되려면 '합리적 의심이 없는 증명'이 필요하다.", "a": "O"},
    {"q": "만 13세 미만의 청소년은 형사처벌을 받을 수 있다.", "a": "X"},
    {"q": "도로교통법상 보행자는 횡단보도에서 무조건 우선권이 있다.", "a": "O"},
    {"q": "헌법재판소는 법률의 위헌 여부를 판단할 수 있다.", "a": "O"},
    {"q": "대한민국 국회는 단원제로 구성되어 있다.", "a": "X"},
]

# --- 세션 초기화 ---
for key in ["questions", "current_idx", "user_answers", "level"]:
    if key not in st.session_state:
        if key == "questions":
            st.session_state[key] = []
        elif key == "current_idx":
            st.session_state[key] = 0
        elif key == "user_answers":
            st.session_state[key] = []
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
if st.session_state["current_idx"] < len(st.session_state["questions"]):
    current_q = st.session_state["questions"][st.session_state["current_idx"]]
    st.subheader(f"❓ 문제 {st.session_state['current_idx'] + 1}")
    st.markdown(f"<p style='font-size:18px'>{current_q['q']}</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    if col1.button("⭕ O"):
        st.session_state["user_answers"].append({"q": current_q['q'], "your": "O", "answer": current_q['a']})
        st.session_state["current_idx"] += 1
        st.experimental_rerun()  # 문제 이동을 위해 리렌더링
    if col2.button("❌ X"):
        st.session_state["user_answers"].append({"q": current_q['q'], "your": "X", "answer": current_q['a']})
        st.session_state["current_idx"] += 1
        st.experimental_rerun()  # 문제 이동을 위해 리렌더링

# --- 결과 요약 ---
if st.session_state["current_idx"] >= len(st.session_state["questions"]) and st.session_state["user_answers"]:
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

    st.markdown("### 📝 문제와 정답 확인")
    for idx, a in enumerate(st.session_state["user_answers"], 1):
        st.write(f"{idx}. {a['q']}  |  내 답: {a['your']}  |  정답: {a['answer']}")

    if st.button("🔄 다시 시작"):
        st.session_state["questions"] = []
        st.session_state["user_answers"] = []
        st.session_state["current_idx"] = 0
        st.experimental_rerun()
