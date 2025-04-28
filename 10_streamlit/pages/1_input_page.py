import streamlit as st

st.title('사용자 입력 받기')

col1, _, col2 = st.columns(3)

with col1:
    nickname = st.text_input("닉네임 입력")
    age = st.number_input("나이 입력: ", min_value=13, max_value=80)

    options = ["대학생", "고등학생", "중학생", "초등학생"]
    selected = st.selectbox("학교 입력", options)

    r_options = ["맛집 탐방", "영화 감상", "음악 감상", "사진찍기"]
    choice = st.radio("취미 입력", r_options)
    selected_many = st.multiselect("취미가 여러 개라면", r_options)

    checked = st.checkbox("개인정보 제공 동의")

with col2:
    if st.button('입력 완료!'):
        st.write(f"이름이 뭐야? {nickname}")
        st.write(f"몇 살이야? {age}")
        st.write(f"어디 다녀? {selected}")
        st.write(f"취미가 뭐야? {choice}")
        st.write(f"취미가 여러개야? {selected_many}")
        st.write(f"개인정보 제공 동의해? {checked}")
