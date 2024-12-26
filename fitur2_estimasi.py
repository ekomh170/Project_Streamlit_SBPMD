import streamlit as st

# Kelas untuk simulasi biaya pendidikan
class SimulasiPendidikan:
    def __init__(self, biaya_tahunan, inflasi, tahun_masuk):
        self.biaya_tahunan = biaya_tahunan
        self.inflasi = inflasi
        self.tahun_masuk = tahun_masuk

    def estimasi_biaya(self):
        tahun_selisih = self.tahun_masuk - 2024  # Mengasumsikan tahun ini 2024
        estimasi_biaya = self.biaya_tahunan * ((1 + self.inflasi) ** tahun_selisih)
        return estimasi_biaya

def tampilkan_estimasi():
    if 'biaya_tahunan' in st.session_state and 'tahun_masuk' in st.session_state and 'inflasi' in st.session_state:
        # Mengambil data dari session state
        biaya_tahunan = st.session_state.biaya_tahunan
        tahun_masuk = st.session_state.tahun_masuk
        inflasi = st.session_state.inflasi
        
        # Membuat objek SimulasiPendidikan
        simulasi = SimulasiPendidikan(biaya_tahunan, inflasi, tahun_masuk)
        
        # Menghitung estimasi biaya pendidikan
        estimasi = simulasi.estimasi_biaya()
        
        # Menampilkan hasil
        st.write(f"Estimasi biaya pendidikan pada tahun {tahun_masuk} adalah Rp {estimasi:,.2f}")
    else:
        st.write("Harap masukkan informasi biaya pendidikan terlebih dahulu.")
