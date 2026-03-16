import streamlit as st
import random

st.set_page_config(page_title="MBTI 궁합 & 포켓몬 추천 💘", page_icon="⚡")

st.title("💘 MBTI 궁합 & 포켓몬 추천 앱")
st.write("MBTI를 선택하면 **궁합 TOP3 + 어울리는 포켓몬**을 보여드립니다! ⚡")

mbti_types = [
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

# MBTI별 포켓몬
pokemon_map = {
"INTJ":("뮤츠","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png","전략적이고 지적인 성향이 강한 MBTI라 강력한 초능력과 높은 지능을 가진 뮤츠가 잘 어울립니다."),
"INTP":("팬텀","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png","호기심이 많고 독창적인 성향이 팬텀의 장난스럽고 창의적인 이미지와 비슷합니다."),
"ENTJ":("리자몽","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png","리더십과 강한 추진력을 가진 ENTJ는 강력한 카리스마의 리자몽과 잘 어울립니다."),
"ENTP":("피카츄","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png","에너지 넘치고 아이디어가 많은 ENTP는 활발하고 재치 있는 피카츄와 비슷합니다."),
"INFJ":("루기아","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png","신비롭고 통찰력이 강한 INFJ는 전설적이고 지혜로운 루기아와 잘 맞습니다."),
"INFP":("이브이","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png","따뜻하고 감성적인 성격이라 다양한 가능성을 가진 이브이와 어울립니다."),
"ENFJ":("가디안","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/282.png","타인을 보호하고 이끄는 성향이 강해 헌신적인 가디안과 비슷합니다."),
"ENFP":("피츄","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/172.png","밝고 에너지가 넘치는 ENFP는 귀엽고 활발한 피츄와 잘 어울립니다."),
"ISTJ":("거북왕","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png","책임감 있고 안정적인 성향이 강한 방어력의 거북왕과 비슷합니다."),
"ISFJ":("라프라스","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png","배려심이 많고 따뜻한 성격이라 온화한 라프라스와 잘 어울립니다."),
"ESTJ":("마기라스","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/248.png","강한 리더십과 조직력을 가진 ESTJ는 압도적인 힘의 마기라스와 비슷합니다."),
"ESFJ":("해피너스","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png","사람을 돌보는 것을 좋아하는 ESFJ는 치유 능력이 있는 해피너스와 잘 맞습니다."),
"ISTP":("핫삼","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/212.png","조용하지만 실력 있는 성향이 강한 전투형 포켓몬 핫삼과 어울립니다."),
"ISFP":("나인테일","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png","감성적이고 예술적인 이미지가 아름다운 나인테일과 비슷합니다."),
"ESTP":("갸라도스","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png","활동적이고 도전적인 ESTP는 강력하고 역동적인 갸라도스와 잘 어울립니다."),
"ESFP":("푸린","https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png","사람들과 어울리는 것을 좋아하는 ESFP는 귀엽고 인기 많은 푸린과 비슷합니다.")
}

compatibility = {

"INTJ":[("ENFP","창의적인 ENFP가 INTJ에게 새로운 시각을 제공합니다."),
("ENTP","두 유형 모두 지적인 토론을 좋아합니다."),
("INFJ","깊이 있는 대화와 가치관을 공유합니다.")],

"INTP":[("ENTJ","ENTJ의 실행력과 INTP의 분석력이 잘 맞습니다."),
("ENFJ","감정과 논리의 균형을 이룹니다."),
("INFJ","철학적인 대화를 즐기는 조합입니다.")],

"ENTJ":[("INFP","서로 부족한 부분을 보완합니다."),
("INTP","전략적 사고가 잘 맞습니다."),
("ENFP","아이디어와 실행력이 만나 좋은 결과를 만듭니다.")],

"ENTP":[("INFJ","아이디어와 통찰력이 잘 맞습니다."),
("INTJ","지적인 자극을 주는 관계입니다."),
("ENFP","활동적이고 재미있는 관계입니다.")],

"INFJ":[("ENFP","서로에게 영감을 주는 관계입니다."),
("ENTP","새로운 시각을 제공하는 파트너입니다."),
("INFP","감정적으로 깊이 공감합니다.")],

"INFP":[("ENFJ","감정을 잘 이해해주는 관계입니다."),
("ENTJ","목표와 의미를 함께 만들어갑니다."),
("INFJ","가치관이 잘 맞습니다.")],

"ENFJ":[("INFP","감정적으로 깊이 이해합니다."),
("ISFP","감성과 리더십이 균형을 이룹니다."),
("INTP","논리와 감정의 조합입니다.")],

"ENFP":[("INFJ","깊은 대화를 나누는 관계입니다."),
("INTJ","서로 다른 매력으로 균형을 이룹니다."),
("ENTP","에너지 넘치는 관계입니다.")],

"ISTJ":[("ESFP","활력을 더해주는 파트너입니다."),
("ESTP","현실적인 목표를 함께 추구합니다."),
("ISFJ","안정적인 관계입니다.")],

"ISFJ":[("ESFP","즐거움과 안정의 균형입니다."),
("ESTP","행동력과 배려심이 잘 맞습니다."),
("ISTJ","성실한 관계입니다.")],

"ESTJ":[("ISFP","감성과 현실의 균형입니다."),
("ISTP","실용적인 문제 해결 능력이 좋습니다."),
("ESFJ","안정적인 협력 관계입니다.")],

"ESFJ":[("ISFP","감성과 배려가 잘 맞습니다."),
("ISTP","서로 다른 매력이 있습니다."),
("INFP","감정적 공감이 깊습니다.")],

"ISTP":[("ESFJ","따뜻함과 실용성의 조합입니다."),
("ESTJ","현실적인 목표를 공유합니다."),
("ISFP","자유로운 관계입니다.")],

"ISFP":[("ESFJ","따뜻한 관계를 만듭니다."),
("ENFJ","재능을 이끌어 줍니다."),
("ISTP","편안한 관계입니다.")],

"ESTP":[("ISFJ","안정과 활력의 조합입니다."),
("ISTJ","현실적인 파트너입니다."),
("ESFP","활동적인 관계입니다.")],

"ESFP":[("ISFJ","안정과 즐거움의 조합입니다."),
("ISTJ","서로 다른 매력이 있습니다."),
("ESTP","에너지 넘치는 관계입니다.")]
}

selected = st.selectbox("🧠 당신의 MBTI를 선택하세요", mbti_types)

if st.button("💘 궁합 확인하기"):

    st.balloons()

    pokemon, img, reason = pokemon_map[selected]

    st.subheader(f"⚡ {selected}에게 어울리는 포켓몬")
    st.image(img, width=200)
    st.write(f"**{pokemon}**")
    st.write(reason)

    st.markdown("---")

    st.subheader("💖 궁합 TOP 3")

    matches = compatibility[selected]

    for i,(mbti,why) in enumerate(matches,1):
        st.markdown(f"### {i}위 💘 {mbti}")
        st.write(why)
        st.progress(random.randint(80,97))
        st.markdown("---")

st.caption("✨ 재미로 보는 MBTI 궁합입니다!")
