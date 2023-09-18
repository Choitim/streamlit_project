import streamlit as st

# 사용자 이름과 비밀번호 설정
correct_username = "myuser"
correct_password = "mypassword"

# 사용자 이름과 비밀번호 입력
username = st.text_input("사용자 이름:")
password = st.text_input("비밀번호:", type="password")

# 로그인 버튼
if st.button("로그인"):
    if username == correct_username and password == correct_password:
        st.success("로그인 성공")
        # 여기에 로그인 후에 보여줄 내용을 추가할 수 있습니다.
    else:
        st.error("로그인 실패. 사용자 이름 또는 비밀번호가 잘못되었습니다.")
