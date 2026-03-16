import streamlit as st
import random

st.set_page_config(page_title="MBTI 궁합 추천 💘", page_icon="💖")

st.title("💘 MBTI 궁합 추천 앱")
st.write("당신의 MBTI를 선택하면 궁합이 잘 맞는 MBTI를 추천해드립니다! 😊")

mbti_types = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

# 간단한 궁합 데이터
compatibility = {
    "INTJ":["ENFP","ENTP"],
    "INTP":["ENTJ","ENFJ"],
    "ENTJ":["INTP","INFP"],
    "ENTP":["INFJ","INTJ"],
    "INFJ":["ENFP","ENTP"],
    "INFP":["ENFJ","ENTJ"],
    "ENFJ":["INFP","ISFP"],
    "ENFP":["INFJ","INTJ"],
    "ISTJ":["ESFP","ESTP"],
    "ISFJ":["ESFP","ESTP"],
    "ESTJ":["ISFP","ISTP"],
    "ESFJ":["ISFP","ISTP"],
    "ISTP":["ESFJ","ESTJ"],
    "ISFP":["ESFJ","ENFJ"],
    "ESTP":["ISFJ","ISTJ"],
    "ESFP":["ISFJ","ISTJ"]
}

selected = st.selectbox("🧠 당신의 MBTI를 선택하세요", mbti_types)

if st.button("💖 궁합 확인하기"):
    matches = compatibility[selected]
    best_match = random.choice(matches)

    st.balloons()

    st.success(f"🎉 {selected} 와(과) 가장 잘 맞는 MBTI는 **{best_match}** 입니다! 💕")

    st.write("✨ 이런 이유로 잘 맞아요!")
    
    reasons = [
        "서로의 성격을 잘 보완해줍니다 🤝",
        "대화가 잘 통하고 공감 능력이 좋습니다 💬",
        "서로 다른 매력이 있어서 관계가 즐겁습니다 🌈",
        "함께 있으면 에너지가 좋아집니다 ⚡"
    ]

    st.write(random.choice(reasons))

st.markdown("---")
st.caption("😎 MBTI 궁합은 재미로만 참고하세요!")
