import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Phan tich du lieu diem so hoc sinh")

uploaded_file = st.file_uploader("Chon file", type=["xlsx"])

#tinh diem trung binh
def calculate_avg(scores):
  return sum(scores) / len(scores)

#phan loai theo diem so
def percentage_dist(scores):
  bins = {'90-100': 0,'80-89': 0,'70-79': 0,'60-69': 0,'<60': 0,}
  for score in scores:
    if scores >= 90:
      bins['90-100'] += 1
    elif scores >= 80:
      bins['80-89'] += 1
    elif scores >= 70:
      bins['70-79'] += 1
    elif scores >= 60:
      bins['60-69'] += 1
    else:
      bins['<60'] += 1
  return bins

#Check neu co file uploaded
if uploaded_file: 
  df = pd.read_excel(uploaded_file)
  #lấy giá trị của cột điểm số, loại bỏ ô trống, lưu thành định dạng float và đưa vàp list
  scores = df["Diem so"].dropna().astype(float).tolist()
  st.write("Tong so hoc sinh la:", len(scores))
  st.write("Diem trung binh la:", round(calculate_avg(scores), 2))
  st.write("Phan loai theo diem so:")
