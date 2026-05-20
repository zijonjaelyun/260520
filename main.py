import streamlit as st
import time

# 1. 페이지 기본 설정 (웹 브라우저 탭부터 쌈뽕하게)
st.set_page_config(
    page_title="은택김의 유니버스",
    page_icon="👑",
    layout="wide"
)

# 2. 미친 세계 1위 수준의 커스텀 CSS (그라데이션 & 애니메이션 효과)
st.markdown("""
<style>
    .ssambbong-title {
        font-size: 60px;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #FFD93D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        animation: gradient 3s ease infinite;
        background-size: 200% 200%;
        margin-bottom: 20px;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #888;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 타이틀 렌더링
st.markdown('<div class="ssambbong-title">✨ 은택김의 웹앱 유니버스 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">안녕하새요╰(*°▽°*)╯ 우주 최강의 웹앱에 오신 것을 환영합니다!</div>', unsafe_allow_html=True)

st.write("---")

# 4. 레이아웃 분할로 세련미 추가
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.info('💡 현재 은택김의 폼이 미쳐 날뛰고 있습니다. 주의하세요!', icon="🔥")
    
    # 5. 시선을 사로잡는 인터랙티브 버튼
    if st.button('🚀 여기를 눌러서 쌈뽕함 충전하기', use_container_width=True):
        # 클릭 시 터지는 화려한 이펙트
        st.balloons()
        st.toast('폼 미쳤다! 쌈뽕함이 1000% 충전되었습니다.', icon='🎉')
        
        with st.spinner('세계 1위 서버와 연결 중...'):
            time.sleep(1)
        
        st.success("✨ 환영합니다! 당신의 눈을 사로잡을 준비가 완료되었습니다. 😎")

# 6. 추가 간지용 데이터 메트릭스 (있어 보이는 효과)
st.write("### 📊 현재 은택김 웹앱 상태")
m1, m2, m3 = st.columns(3)
m1.metric(label="멋짐 지수", value="9,999+", delta="우상향 중 🚀")
m2.metric(label="방문자 눈부심", value="100%", delta="선글라스 필수 😎")
m3.metric(label="세계 랭킹", value="1위", delta="유지 중 👑")
