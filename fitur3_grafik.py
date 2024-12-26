import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Kelas untuk simulasi biaya pendidikan
class SimulasiPendidikan:
    def __init__(self, biaya_tahunan, inflasi, tahun_masuk):
        self.biaya_tahunan = biaya_tahunan
        self.inflasi = inflasi
        self.tahun_masuk = tahun_masuk

    def grafik_estimasi(self):
        tahun = np.arange(2024, self.tahun_masuk + 1)
        biaya = self.biaya_tahunan * ((1 + self.inflasi) ** (tahun - 2024))
        return tahun, biaya

def tampilkan_grafik():
    if 'biaya_tahunan' in st.session_state and 'tahun_masuk' in st.session_state and 'inflasi' in st.session_state:
        # Mengambil data dari session state
        biaya_tahunan = st.session_state.biaya_tahunan
        tahun_masuk = st.session_state.tahun_masuk
        inflasi = st.session_state.inflasi
        
        # Membuat objek SimulasiPendidikan
        simulasi = SimulasiPendidikan(biaya_tahunan, inflasi, tahun_masuk)
        
        # Menghasilkan data untuk grafik
        tahun, biaya = simulasi.grafik_estimasi()
        
        # Membuat grafik
        plt.figure(figsize=(10,6))
        plt.plot(tahun, biaya, marker='o', color='b', label="Estimasi Biaya Pendidikan")
        plt.title('Estimasi Biaya Pendidikan Masa Depan')
        plt.xlabel('Tahun')
        plt.ylabel('Biaya (Rp)')
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)
    else:
        st.write("Harap masukkan informasi biaya pendidikan terlebih dahulu.")
