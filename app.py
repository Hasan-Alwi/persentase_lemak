import streamlit as st
import pandas as pd 
import numpy as np

def calculate_body_fat(weight, height, gender, waist, wrist, hip, forearm):
    if gender == "Pria":
        f1 = (weight * 1.082) + 94.42
        f2 = wrist / 3.14
        f3 = waist * 4.15
        f4 = hip * 0.082
        f5 = forearm * 0.434
        lean_body_mass = f1 - f2 + f3 - f4 + f5
    else:
        f1 = (weight * 0.732) + 8.987
        f2 = wrist / 3.14
        f3 = waist * 0.157
        f4 = hip * 0.249
        f5 = forearm * 0.434
        lean_body_mass = f1 + f2 - f3 - f4 + f5

    persentase_lemak = (weight - lean_body_mass) / weight * 100
    return persentase_lemak

st.title("Alat Pengukur Persentase Lemak")

weight = st.number_input("berat badan (kg)")
height = st.number_input("tinggi badan (cm)")
gender = st.selectbox("jenis kelamin", ("Pria", "Wanita"))
waist = st.number_input("lingkar pinggang (cm)")
wrist = st.number_input("lingkar pergelangan tangan (cm)")
hip = st.number_input("lingkar pinggul (cm)")
forearm = st.number_input("lingkar lengan bawah (cm)")

if st.button("Hitung"):
    persentase_lemak = calculate_body_fat(weight, height, gender, waist, wrist, hip, forearm)
    st.write("Persentase lemak tubuh:", round(persentase_lemak, 2), "%")
