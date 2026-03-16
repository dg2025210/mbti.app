import streamlit as st
import random

st.set_page_config(page_title="MBTI 궁합 추천 💘", page_icon="💖")

st.title("💘 MBTI 궁합 추천 앱")
st.write("당신의 MBTI를 선택하면 **궁합이 잘 맞는 MBTI TOP 3**를 추천해드립니다! 😆")

mbti_types = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP"
]

compatibility = {

"INTJ":[
("ENFP","자유로운 ENFP가 INTJ의 계획적인 성향에 새로운 아이디어와 활력을 불어넣어 서로에게 큰 자극이 됩니다."),
("ENTP","지적인 대화를 좋아하는 두 유형이라 토론과 아이디어 교환을 통해 서로 성장하기 좋습니다."),
("INFJ","둘 다 깊이 있는 사고를 좋아하며 미래지향적인 목표를 함께 세우는 관계입니다.")
],

"INTP":[
("ENTJ","ENTJ의 추진력과 INTP의 분석력이 만나면 강력한 팀워크가 만들어집니다."),
("ENFJ","ENFJ가 감정적인 부분을 채워주고 INTP는 논리적인 해결책을 제시합니다."),
("INFJ","서로 깊이 있는 생각을 공유하며 철학적인 대화를 즐길 수 있습니다.")
],

"ENTJ":[
("INFP","INFP의 따뜻함과 ENTJ의 리더십이 만나 서로 부족한 부분을 보완합니다."),
("INTP","논리적 사고가 비슷하여 문제 해결 능력이 뛰어난 조합입니다."),
("ENFP","ENFP의 창의성과 ENTJ의 실행력이 만나 새로운 도전을 만들어냅니다.")
],

"ENTP":[
("INFJ","ENTP의 아이디어와 INFJ의 통찰력이 만나 깊이 있는 관계가 됩니다."),
("INTJ","지적인 대화를 좋아하는 두 유형이라 서로에게 큰 자극이 됩니다."),
("ENFP","둘 다 에너지가 넘치고 새로운 것을 좋아해 즐거운 관계가 됩니다.")
],

"INFJ":[
("ENFP","ENFP의 밝은 에너지가 INFJ의 깊은 감성을 잘 끌어내 줍니다."),
("ENTP","ENTP의 창의적인 사고가 INFJ에게 새로운 시각을 제공합니다."),
("INFP","서로 감정적으로 깊이 공감할 수 있는 따뜻한 관계입니다.")
],

"INFP":[
("ENFJ","ENFJ가 INFP의 감정을 잘 이해하고 응원해주는 관계입니다."),
("ENTJ","ENTJ가 목표를 제시하고 INFP가 의미를 더해 균형을 만듭니다."),
("INFJ","둘 다 이상주의적이며 서로의 가치관을 존중합니다.")
],

"ENFJ":[
("INFP","서로 감정적으로 깊이 이해하고 배려하는 관계입니다."),
("ISFP","ISFP의 감성과 ENFJ의 따뜻한 리더십이 잘 어울립니다."),
("INTP","ENFJ가 감정을, INTP가 논리를 채워주는 균형 잡힌 관계입니다.")
],

"ENFP":[
("INFJ","서로에게 영감을 주는 관계로 깊은 대화를 즐깁니다."),
("INTJ","INTJ의 계획성과 ENFP의 자유로움이 좋은 균형을 만듭니다."),
("ENTP","둘 다 에너지가 넘치고 창의적인 활동을 좋아합니다.")
],

"ISTJ":[
("ESFP","ESFP의 활발함이 ISTJ의 일상에 즐거움을 더합니다."),
("ESTP","현실적인 사고를 공유하면서도 활동적인 관계가 됩니다."),
("ISFJ","책임감이 강한 두 유형이라 안정적인 관계를 만듭니다.")
],

"ISFJ":[
("ESFP","ESFP가 관계에 활력을 더하고 ISFJ는 안정감을 제공합니다."),
("ESTP","ESTP의 행동력과 ISFJ의 배려심이 잘 어울립니다."),
("ISTJ","성실하고 책임감 있는 공통점이 많습니다.")
],

"ESTJ":[
("ISFP","ISFP의 감성이 ESTJ에게 새로운 균형을 만들어 줍니다."),
("ISTP","현실적인 문제 해결 능력이 뛰어난 조합입니다."),
("ESFJ","책임감과 조직력이 강해 안정적인 관계입니다.")
],

"ESFJ":[
("ISFP","ISFP의 감성과 ESFJ의 따뜻함이 잘 어울립니다."),
("ISTP","서로 다른 매력이 있어 관계가 흥미롭습니다."),
("INFP","감정적으로 깊이 공감하는 관계입니다.")
],

"ISTP":[
("ESFJ","ESFJ가 관계를 따뜻하게 만들고 ISTP는 현실적인 해결책을 제시합니다."),
("ESTJ","둘 다 실용적인 성향이라 문제 해결 능력이 좋습니다."),
("ISFP","자유로운 분위기의 편안한 관계입니다.")
],

"ISFP":[
("ESFJ","ESFJ의 따뜻함과 ISFP의 감성이 잘 어울립니다."),
("ENFJ","ENFJ가 ISFP의 재능을 잘 이끌어 줍니다."),
("ISTP","서로 자유로운 성향이라 편안한 관계입니다.")
],

"ESTP":[
("ISFJ","ISFJ의 안정감과 ESTP의 활발함이 균형을 만듭니다."),
("ISTJ","현실적인 성향이 비슷해 함께 목표를 이루기 좋습니다."),
("ESFP","활동적인 성향이 같아 즐거운 관계입니다.")
],

"ESFP":[
("ISFJ","ISFJ가 안정감을 주고 ESFP는 즐거움을 제공합니다."),
("ISTJ","서로 다른 매력으로 균형 잡힌 관계가 됩니다."),
("ESTP","활동적이고 에너지가 넘치는 관계입니다.")
]

}

selected = st.selectbox("🧠 당신의 MBTI를 선택하세요", mbti_types)

if st.button("💘 궁합 확인하기"):
    
    st.balloons()

    st.subheader(f"✨ {selected}와 잘 맞는 MBTI TOP 3")

    matches = compatibility[selected]

    for i, (mbti, reason) in enumerate(matches,1):
        st.markdown(f"### {i}위 💖 {mbti}")
        st.write(reason)
        st.progress(random.randint(80,98))
        st.markdown("---")

st.caption("😆 MBTI 궁합은 재미로 참고하세요!")
