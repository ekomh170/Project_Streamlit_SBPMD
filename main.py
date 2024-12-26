import streamlit as st
import fitur1_input
import fitur2_estimasi
import fitur3_grafik
import fitur4_informasi

# Judul aplikasi
st.title("Simulasi Biaya Pendidikan Masa Depan")

# Sidebar untuk navigasi
sidebar_options = {
    "Input Biaya Pendidikan": fitur1_input.tampilkan_input,
    "Estimasi Biaya Pendidikan": fitur2_estimasi.tampilkan_estimasi,
    "Grafik Estimasi Biaya": fitur3_grafik.tampilkan_grafik,
    "Informasi Aplikasi & Tim": fitur4_informasi.tampilkan_informasi
}

# Menambahkan link informasi aplikasi di sidebar
st.sidebar.header("Menu")
sidebar_pilihan = st.sidebar.radio("Pilih Fitur", list(sidebar_options.keys()), index=3)

# Menampilkan konten sesuai pilihan di sidebar
sidebar_options[sidebar_pilihan]()
