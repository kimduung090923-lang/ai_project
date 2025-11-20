# app.py
import streamlit as st

st.set_page_config(page_title="MBTI 친구/활동 추천 💫", page_icon="🧭", layout="centered")

st.title("MBTI 친구·활동 추천기 💬✨")
st.caption("16가지 MBTI 중 하나 고르면 센스있게 추천해줘요 — 친근한 말투 + 이모지 적용!")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 데이터: 각 유형별 추천(2가지) + 호환성(상위 리스트)
MBTI_INFO = {
    "ISTJ": {
        "recs": ["체계적인 프로젝트 맡기기 (체크리스트✔️ 좋아함)", "역사나 자료 정리하는 스터디"],
        "compat": ["ESTJ","ISFJ","INTJ","ESFJ"]
    },
    "ISFJ": {
        "recs": ["조용한 봉사활동이나 돌봄 역할 🫶", "감사 카드 만들기 같은 섬세한 작업"],
        "compat": ["ESFJ","ISTJ","INFP","ISFP"]
    },
    "INFJ": {
        "recs": ["심층 대화하기(마음 얘기) 💭", "창의적 글쓰기·상상력 발휘"],
        "compat": ["ENFP","ENFJ","INFP","INTJ"]
    },
    "INTJ": {
        "recs": ["전략 게임이나 장기 프로젝트 설계 ♟️", "심층 독서 모임"],
        "compat": ["ENTJ","INTP","INFJ","ISTJ"]
    },
    "ISTP": {
        "recs": ["실습형 활동(메이킹, 목공) 🛠️", "짧고 강한 액티비티 — 스포티브한 경험"],
        "compat": ["ESTP","ISFP","INTP","ISTJ"]
    },
    "ISFP": {
        "recs": ["아트워크·사진 찍기 🎨", "자연 속 소소한 산책과 감성 충전"],
        "compat": ["ESFP","INFP","ISTP","ISFJ"]
    },
    "INFP": {
        "recs": ["감성 글쓰기·일기 📝", "작은 창작 프로젝트(노래·시)"],
        "compat": ["ENFJ","INFJ","ISFP","ENFP"]
    },
    "INTP": {
        "recs": ["논리 퍼즐·토론 동아리 🧠", "혼자 깊이 파고드는 리서치"],
        "compat": ["ENTP","INTJ","ISTP","ENFP"]
    },
    "ESTP": {
        "recs": ["현장형 액티비티(스포츠·즉석 모험) 🏃‍♂️", "즉흥 공연·경쟁 게임"],
        "compat": ["ISTP","ESFP","ENTP","ESTJ"]
    },
    "ESFP": {
        "recs": ["파티·무대 활동 🎤", "즉흥 창작(댄스·노래)"],
        "compat": ["ISFP","ESTP","ENFP","ESFJ"]
    },
    "ENFP": {
        "recs": ["아이디어 브레인스토밍 🧩", "창의적 콜라보(프로젝트 팀)"],
        "compat": ["INFJ","INFP","ENFJ","ESFP"]
    },
    "ENTP": {
        "recs": ["토론·해커톤 참여 ⚡", "아이디어 실험과 창업 생각 나누기"],
        "compat": ["INTP","ENTJ","ESTP","ENFP"]
    },
    "ESTJ": {
        "recs": ["리더 역할 맡기기(조직 운영) 🗂️", "규칙 정리 + 실행 담당"],
        "compat": ["ISTJ","ESFJ","ENTJ","ESTP"]
    },
    "ESFJ": {
        "recs": ["모임 주최·케어 역할 🤝", "친구 챙기기·이벤트 기획"],
        "compat": ["ISFJ","ESTJ","ENFJ","ESFP"]
    },
    "ENFJ": {
        "recs": ["코칭·멘토링 역할 🌱", "협업 프로젝트에서 리더십 발휘"],
        "compat": ["INFP","INFJ","ESFJ","ENFP"]
    },
    "ENTJ": {
        "recs": ["전략적 프로젝트 리드하기 🏁", "토론·계획 수립 역할"],
        "compat": ["INTJ","ENTP","ESTJ","ENFP"]
    }
}

# helper: compatibility check between two types
def compatibility_message(a, b):
    if a == b:
        return "같은 유형이네요 — 서로 이해하는 부분이 많아요! 👯‍♂️"
    a_in_b = a in MBTI_INFO[b]["compat"]
    b_in_a = b in MBTI_INFO[a]["compat"]
    if a_in_b and b_in_a:
        return "서로 잘 맞는 편이에요 — 상호 보완 & 공감이 잘 일어날 가능성 높음! 🌟"
    if a_in_b or b_in_a:
        return "한쪽이 특히 잘 어울린다고 느낄 수 있어요 — 성향 보완 가능! 🤝"
    return "서로 다름이 클 수 있지만, 이해하려는 노력이 있으면 아주 좋은 케미가 될 수도 있어요. 🔄"

# Sidebar: 선택
st.sidebar.header("설정 ⚙️")
selected = st.sidebar.selectbox("👉 MBTI 하나 선택해주세요", MBTI_LIST, index=6)
compare_pair = st.sidebar.multiselect("🔁 두 유형 비교해볼래? (선택적으로 2개)", MBTI_LIST, default=[])

# 메인: 선택한 유형 정보 표시
st.markdown("---")
st.header(f"선택: {selected}  { '💡' }")
st.markdown(f"### {selected} 특징에 맞춘 추천 2가지")
for i, rec in enumerate(MBTI_INFO[selected]["recs"], 1):
    st.write(f"{i}. {rec}")

compat_list = MBTI_INFO[selected]["compat"]
st.markdown("**이 유형과 잘 어울리는 MBTI들 (추천)**")
st.write(", ".join(compat_list))

# 팁 문구 (친근한 말투)
st.info("팁: 유형은 성향을 보여주는 힌트일 뿐이에요. 상황과 사람에 따라 천차만별이니 부담 갖지 말고 편하게 참고해요! 😊")

# 비교 기능
st.markdown("---")
st.subheader("두 유형 케미 체크 💞")
if len(compare_pair) == 0:
    st.write("비교하려면 사이드바에서 MBTI 두 개를 골라줘요.")
elif len(compare_pair) == 1:
    st.warning("한 개만 골랐어요 — 두 개 선택하면 케미를 알려줄게요.")
else:
    a, b = compare_pair[0], compare_pair[1]
    st.write(f"**{a} ↔ {b}**")
    st.write(compatibility_message(a, b))
    # 상호 호환성 디테일
    st.write(f"- `{a}`가 `{b}`의 추천 목록에 있는가? {'✅' if a in MBTI_INFO[b]['compat'] else '❌'}")
    st.write(f"- `{b}`가 `{a}`의 추천 목록에 있는가? {'✅' if b in MBTI_INFO[a]['compat'] else '❌'}")

    # 추가: 서로 어울리는 활동 제안
    st.markdown("**같이 하면 좋은 활동 제안**")
    act1 = MBTI_INFO[a]["recs"][0]
    act2 = MBTI_INFO[b]["recs"][0]
    st.write(f"- 함께 해볼 만한 활동: `{act1}` + `{act2}` 조합을 시도해보자! 😄")

# 전체 요약 보기 토글
st.markdown("---")
if st.checkbox("전체 MBTI 요약표 보기"):
    st.write("각 유형과 추천 활동 / 상위 호환 MBTI")
    for t in MBTI_LIST:
        st.markdown(f"**{t}** — 추천: {MBTI_INFO[t]['recs'][0]} | {MBTI_INFO[t]['recs'][1]}  \n호환: {', '.join(MBTI_INFO[t]['compat'])}")

st.markdown("---")
st.caption("만들어준 사람: 너와 잘 맞는 활동·사람 찾기를 도와주는 작은 앱이에요. 결과는 참고용! 💖")
