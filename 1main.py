import React, { useState } from "react"; import { Card, CardContent } from "@/components/ui/card"; import { Button } from "@/components/ui/button";

const recipes = { "초코소라빵": { ingredients: [ "강력분 250g", "설탕 30g", "소금 3g", "드라이이스트 4g", "코코아 파우더 20g", "버터 30g", "우유 150ml" ], recipe: [ "재료 섞어 반죽 후 1차 발효", "소라 모양으로 성형", "초코크림 넣기", "180℃에서 15분 굽기" ], video: "https://www.youtube.com/embed/8g_2zL8iFfg" }, "소금빵": { ingredients: [ "강력분 250g", "소금 5g", "설탕 20g", "버터 40g", "드라이이스트 4g", "우유 140ml" ], recipe: [ "재료 섞어 반죽 후 발효", "길쭉하게 밀어 소라모양 성형", "버터 얹고 소금 살짝 뿌리기", "180℃에서 1515분 굽기", "버터크림 넣고 샌드" ], video: "https://www.youtube.com/embed/CkDMsMK2qD4" }, "쿠키": { ingredients: [ "박력분 200g", "설탕 100g", "버터 100g", "계란 1개", "초코칩 50g" ], recipe: [ "버터+설탕 크림화", "계란 섞고 밀가루 넣기", "초코칩 섞어 동그랗게 성형", "170℃에서 12~15분 굽기" ], video: "https://www.youtube.com/embed/6lxdGfkEPgY" } };

export default function App() { const [selected, setSelected] = useState(null);

return ( <div className="min-h-screen bg-gradient-to-b from-amber-200 to-orange-100 flex flex-col items-center p-6"> <h1 className="text-3xl font-bold mb-6 text-brown-700">🥐🍞 빵이랑 디저트 레시피 🍪🍰</h1>

{!selected && (
    <div className="grid grid-cols-2 gap-4">
      {Object.keys(recipes).map((name) => (
        <Button
          key={name}
          className="text-lg p-6 rounded-2xl shadow-md bg-amber-300 hover:bg-amber-400"
          onClick={() => setSelected(name)}
        >
          {name} 🍩
        </Button>
      ))}
    </div>
  )}

  {selected && (
    <Card className="w-full max-w-xl bg-amber-50 shadow-lg rounded-2xl p-4">
      <CardContent>
        <h2 className="text-2xl font-bold mb-4">{selected} 레시피 🍴</h2>

        <h3 className="text-xl font-semibold">📋 재료</h3>
        <ul className="list-disc list-inside mb-4">
          {recipes[selected].ingredients.map((item, i) => (
            <li key={i}>{item}</li>
          ))}
        </ul>

        <h3 className="text-xl font-semibold">👩‍🍳 만드는 법</h3>
        <ol className="list-decimal list-inside mb-4">
          {recipes[selected].recipe.map((step, i) => (
            <li key={i}>{step}</li>
          ))}
        </ol>

        <div className="aspect-w-16 aspect-h-9 mb-4">
          <iframe
            width="100%"
            height="315"
            src={recipes[selected].video}
            title="YouTube video player"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          ></iframe>
        </div>

        <Button
          className="bg-orange-300 hover:bg-orange-400 rounded-xl"
          onClick={() => setSelected(null)}
        >
          ⬅️ 처음으로 돌아가기
        </Button>
      </CardContent>
    </Card>
  )}
</div>

); }

# 귀여운 테마 CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF9E6; /* 파스텔 옐로우 */
        color: #5C4033; /* 브라운 글씨 */
        font-family: "Comic Sans MS", "Arial Rounded MT Bold", cursive;
    }
    .recipe-card {
        background-color: #FFEFD5;
        padding: 15px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 2px 2px 10px #e5c9a8;
        margin: 10px;
    }
    .recipe-card:hover {
        background-color: #FFE2B7;
        transform: scale(1.02);
        transition: 0.2s;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 메인 타이틀
st.title("🍞 아기자기한 빵 레시피 도우미 🥐")
st.markdown("**따뜻한 파스텔 옐로우 × 브라운 톤으로 준비했어요 ✨**")

# 첫 화면 빵 카드 보여주기
st.subheader("오늘 어떤 빵을 만들어볼까요? 🥰")
cols = st.columns(4)
for i, (name, data) in enumerate(RECIPES.items()):
    with cols[i % 4]:
        if st.button(f"{data['emoji']} {name}", key=name):
            st.session_state["selected"] = name

# 선택된 빵 레시피 보여주기
if "selected" in st.session_state:
    choice = st.session_state["selected"]
    recipe = RECIPES[choice]

    st.header(f"{recipe['emoji']} {choice} 레시피")
    st.write(recipe["yield_text"])

    # 재료표
    st.subheader("📝 재료")
    df = pd.DataFrame(recipe["ingredients"])
    st.table(df)

    # 단계별 레시피
    st.subheader("🥣 만드는 법")
    for i, step in enumerate(recipe["steps"], 1):
        st.checkbox(f"{i}. {step}", key=f"{choice}_{i}")

    # 영상
    st.subheader("🎥 영상으로 배우기")
    for url in recipe["videos"]:
        st.video(url)
