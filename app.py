import streamlit as st
import pandas as pd
import os

# 데이터 저장 함수
def save_data(data, file_name='data.csv'):
    # 만약 파일이 없으면 새로 생성하고, 있으면 데이터 추가
    if os.path.exists(file_name):
        existing_data = pd.read_csv(file_name)
        updated_data = pd.concat([existing_data, data], ignore_index=True)
        updated_data.to_csv(file_name, index=False)
    else:
        data.to_csv(file_name, index=False)

# 사용자 입력 받기
st.title("사용자 데이터 입력 및 저장")

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
gender = st.selectbox("성별을 선택하세요", ["남성", "여성", "기타"])

# 제출 버튼
if st.button("데이터 저장"):
    if name and age:  # 이름과 나이가 입력되었는지 확인
        # 입력된 데이터를 DataFrame으로 변환
        new_data = pd.DataFrame({
            "이름": [name],
            "나이": [age],
            "성별": [gender]
        })

        # 데이터 저장 함수 호출
        save_data(new_data)

        # 성공 메시지
        st.success("데이터가 성공적으로 저장되었습니다!")
    else:
        st.warning("이름과 나이를 입력해주세요.")
