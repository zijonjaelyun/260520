import streamlit as st
import random
import time

# 1. 페이지 설정 및 쌈뽕한 CSS (이전 스타일 유지 + 게임용 UI 추가)
st.set_page_config(page_title="은택김의 협곡", page_icon="⚔️", layout="wide")

st.markdown("""
<style>
    .ssambbong-title {
        font-size: 50px; font-weight: 900; text-align: center; margin-bottom: 10px;
        background: -webkit-linear-gradient(45deg, #00C9FF, #92FE9D);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite; background-size: 200% 200%;
    }
    .hp-text { font-size: 20px; font-weight: bold; }
    .log-box { background-color: #1E1E1E; color: #00FF00; padding: 15px; border-radius: 10px; font-family: monospace; height: 200px; overflow-y: auto; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="ssambbong-title">⚔️ 은택김의 협곡 : 야스오 vs 티모 ⚔️</div>', unsafe_allow_html=True)
st.write("---")

# 2. 게임 상태(세션) 초기화 (스트림릿의 핵심!)
if 'player_hp' not in st.session_state:
    st.session_state.player_hp = 100
if 'enemy_hp' not in st.session_state:
    st.session_state.enemy_hp = 100
if 'logs' not in st.session_state:
    st.session_state.logs = ["📢 [시스템] 소환사의 협곡에 오신 것을 환영합니다.", "📢 [시스템] 야스오(당신) VS 악마 티모의 전투가 시작됩니다!"]
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# 3. 스킬 로직 함수
def use_skill(skill_name):
    if st.session_state.game_over:
        return

    # 플레이어(야스오)의 공격
    damage = 0
    if skill_name == "Q":
        damage = random.randint(10, 20)
        log = f"🗡️ 야스오가 [Q: 강철 폭풍]을(를) 사용! 티모에게 {damage}의 피해!"
    elif skill_name == "W":
        damage = 0
        log = f"💨 야스오가 [W: 바람 장막]을(를) 펼쳤습니다! 다음 공격을 방어할 준비를 합니다."
    elif skill_name == "R":
        damage = random.randint(30, 50)
        log = f"🌪️ 야스오가 [R: 최후의 숨결]을(를) 시전!! SORYE GE TON!!! 티모에게 {damage}의 치명타!"

    st.session_state.enemy_hp = max(0, st.session_state.enemy_hp - damage)
    st.session_state.logs.insert(0, log) # 최신 로그를 맨 위로

    # 적(티모) 처치 확인
    if st.session_state.enemy_hp <= 0:
        st.session_state.logs.insert(0, "🎉 [승리] 악마 티모를 처치했습니다! 폼 미쳤다!")
        st.session_state.game_over = True
        st.balloons()
        return

    # 적(티모)의 반격
    time.sleep(0.3) # 약간의 딜레이로 긴장감 조성
    if skill_name != "W": # W를 안 썼을 때만 맞음
        enemy_dmg = random.randint(15, 25)
        st.session_state.player_hp = max(0, st.session_state.player_hp - enemy_dmg)
        st.session_state.logs.insert(0, f"🍄 티모가 [맹독 다트]를 쏩니다! 윽... {enemy_dmg}의 피해를 입었습니다.")
    else:
        st.session_state.logs.insert(0, f"🛡️ 티모의 [맹독 다트]가 바람 장막에 막혔습니다! (피해 0)")

    # 플레이어 사망 확인
    if st.session_state.player_hp <= 0:
        st.session_state.logs.insert(0, "💀 [패배] 눈이 마주친 티모에게 당했습니다... 회색 화면을 감상하세요.")
        st.session_state.game_over = True


# 4. 게임 UI 레이아웃
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    st.subheader("🗡️ 야스오 (Player)")
    st.image("https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg", use_container_width=True)
    st.markdown(f'<div class="hp-text">HP: {st.session_state.player_hp} / 100</div>', unsafe_allow_html=True)
    st.progress(st.session_state.player_hp / 100)
    
    # 스킬 버튼들
    st.write("### 🎮 스킬 선택")
    btn1, btn2, btn3 = st.columns(3)
    if btn1.button("Q (강철폭풍)", disabled=st.session_state.game_over, use_container_width=True):
        use_skill("Q")
    if btn2.button("W (바람장막)", disabled=st.session_state.game_over, use_container_width=True):
        use_skill("W")
    if btn3.button("R (궁극기)", disabled=st.session_state.game_over, use_container_width=True):
        use_skill("R")

with col2:
    st.markdown("<h1 style='text-align: center; margin-top: 100px;'>VS</h1>", unsafe_allow_html=True)
    if st.session_state.game_over:
        if st.button("🔄 게임 다시하기", use_container_width=True):
            st.session_state.player_hp = 100
            st.session_state.enemy_hp = 100
            st.session_state.logs = ["📢 [시스템] 게임을 재시작합니다!"]
            st.session_state.game_over = False
            st.rerun()

with col3:
    st.subheader("🍄 티모 (AI)")
    st.image("https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_0.jpg", use_container_width=True)
    st.markdown(f'<div class="hp-text">HP: {st.session_state.enemy_hp} / 100</div>', unsafe_allow_html=True)
    st.progress(st.session_state.enemy_hp / 100)

# 5. 전투 로그창
st.write("---")
st.write("### 📜 전투 기록")
log_text = "<br>".join(st.session_state.logs)
st.markdown(f'<div class="log-box">{log_text}</div>', unsafe_allow_html=True)
