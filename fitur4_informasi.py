import streamlit as st

def tampilkan_informasi():
    # Menampilkan judul informasi
    st.header("Informasi Aplikasi & Tim")

    # Menjelaskan sistem perhitungan
    st.subheader("Sistem Perhitungan Biaya Pendidikan Masa Depan")

    st.write("""
    Aplikasi **Simulasi Biaya Pendidikan Masa Depan** dirancang untuk membantu Anda memperkirakan biaya pendidikan yang akan dikeluarkan di masa depan, 
    dengan mempertimbangkan faktor inflasi dan jumlah tahun yang diinginkan.
    Berikut adalah penjelasan tentang sistem perhitungan yang digunakan dalam aplikasi ini:

    ### 1. Input Data
    - **Biaya Pendidikan Saat Ini**: Biaya yang Anda bayarkan saat ini atau biaya yang diperkirakan akan dibayarkan saat ini (misalnya biaya kuliah tahunan).
    - **Tingkat Inflasi Pendidikan**: Persentase inflasi pendidikan tahunan yang digunakan untuk memperkirakan kenaikan biaya pendidikan.
    - **Jumlah Tahun**: Berapa tahun ke depan Anda ingin memperkirakan biaya pendidikan (misalnya 5 tahun ke depan).

    ### 2. Proses Perhitungan
    Rumus yang digunakan untuk menghitung biaya pendidikan masa depan adalah:
    
    Biaya Masa Depan = Biaya Saat Ini * (1 + Inflasi) ^ Jumlah Tahun
    
    Dimana:
    - **Biaya Pendidikan Saat Ini** adalah nilai yang Anda masukkan pada input.
    - **Inflasi** adalah tingkat inflasi yang Anda tentukan dalam bentuk desimal (misalnya 5% = 0.05).
    - **Jumlah Tahun** adalah jumlah tahun yang Anda pilih.

    ### 3. Hasil Perhitungan
    Setelah melakukan perhitungan berdasarkan rumus di atas, aplikasi akan menampilkan:
    - Estimasi biaya pendidikan tahunan di masa depan.
    - Total biaya pendidikan yang diperkirakan untuk jumlah tahun yang Anda tentukan.

    ### 4. Grafik Estimasi
    Aplikasi juga menampilkan grafik yang menggambarkan bagaimana biaya pendidikan akan berkembang dari tahun ke tahun berdasarkan estimasi inflasi yang Anda masukkan.
    """)

    # Menampilkan informasi tentang tim pengembang
    st.subheader("Tim Pengembang")
    st.write("""
    - **Ketua Tim**: Eko Muchamad Haryono
    - **Anggota Tim**: [Anggota lainnya, jika ada]
    """)
