import streamlit as st

def tampilkan_input():
    st.header("Masukkan Informasi Biaya Pendidikan")
    
    # Input dari pengguna
    biaya_tahunan = st.number_input("Biaya Pendidikan Tahunan (Rp)", min_value=1000000, step=1000000)
    tahun_masuk = st.number_input("Tahun Masuk Sekolah", min_value=2024)
    inflasi = st.slider("Tingkat Inflasi Pendidikan (%)", min_value=1, max_value=15, value=5) / 100
    
    # Menyimpan nilai untuk digunakan di fitur lainnya
    st.session_state.biaya_tahunan = biaya_tahunan
    st.session_state.tahun_masuk = tahun_masuk
    st.session_state.inflasi = inflasi
