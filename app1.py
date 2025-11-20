import streamlit as st

st.title("こんにちわ、吉村ゼミ")

name = st.text_input("座右の銘なんですか")

st.write(name)

camera_photo = st.camera_input("写真を撮影します！")
if camera:
  st.image(camera, caption="写真",use_column_width=True)
