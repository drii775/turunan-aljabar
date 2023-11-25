import streamlit as st
from sympy import symbols, diff, simplify
from streamlit_option_menu import option_menu

with open('WARNA.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# navigasi sidebar
with st.sidebar :
    selected = option_menu('Menu',
    ['Home','Panduan Program','Rumus'],
    default_index=0)

# halaman panduan program
if (selected == 'Home') :
    st.markdown('<h1 class="serif-title">KALKULUS I', unsafe_allow_html=True) 
    st.write('Turunan Aljabar')
    # Nama-nama kelompok
    st.write('Anggota Kelompok : \n'
        '- Ririn Rahma Arifa_237006171_Kelas F \n'
        '- Tia Amelia_237006162_Kelas E \n'
        '- Rheyna Louisa Pratiwi_237006169_Kelas F \n'
        '')

# Fungsi untuk mengganti operator pangkat
def ganti_operator_pangkat(ekspresi):
    ekspresi = ekspresi.replace('^', '**')
    return ekspresi

# halaman panduan program
if (selected == 'Panduan Program') :
    st.markdown('<h1 class="serif-title">PANDUAN PROGRAM</h1>', unsafe_allow_html=True)
    #panduan
    st.write('**PANDUAN SIDEBAR :** \n'
        '1. Home, menampilkan menu utama \n'
        '2. Panduan Program, menampilkan petunjuk untuk menggunakan program \n'
        '3. Rumus, menampilkan kalkultor turunan aljabar \n'
        '')
    st.write('**PANDUAN MENU RUMUS :** \n'
        '1. Nilai dapat diisi dengan nilai positif dan negatif \n'
        '2. Nilai dapat diisi dengan negatif tak hingga sampai positif tak hingga \n'
        '3. Untuk menambahkan variabel "X" gunakan symbol bintang (*) \n'
        '4. Untuk menambahkan pangkat gunakan symbol sirkumfleks (^) \n'
        '5. Tombol hitung digunakan untuk menampilkan hasil turunan \n'
        '6. Tombol enter pada keyboard dapat digunakan untuk menghapus seluruh hasil turunan \n'
        '')
    st.write('Catatan : Program kalkulator ini hanya dapat digunakan untuk operasi yang sederhana, seperti jenis turunan dengan operasi tambah, kurang dan kali saja')

# halaman rumus
if (selected == 'Rumus') :
    def kalkulator_turunan(ekspresi):
        # Membuat simbol variabel
        x = symbols('x')

        try:
            # Mengevaluasi ekspresi dan menghitung turunan pertama
            fungsi = simplify(ekspresi)
            # Turunan pertama
            turunan_pertama = diff(fungsi, x)

            # Turunan kedua
            turunan_kedua = diff(turunan_pertama, x)

            # Turunan ketiga
            turunan_ketiga = diff(turunan_kedua, x)

            # Menampilkan fungsi asli
            st.write("Fungsi asli f(x) =", fungsi)

            # Menampilkan turunan 
            st.write("y ' =", turunan_pertama)
            st.write("y '' =", turunan_kedua)
            st.write("y ''' =", turunan_ketiga)
            #st.success(f"Turunannya adalah = {turunan_pertama}")

        except Exception as e:
            st.write("Terjadi kesalahan:", e)

    def main():
        st.markdown('<h1 class="serif-title">Kalkulator Turunan Aljabar', unsafe_allow_html=True)

        # Menerima ekspresi dari pengguna
        ekspresi = st.text_input("Masukkan ekspresi turunanan aljabar")

        # Memanggil kalkulator_turunan jika pengguna menekan tombol "Hitung"
        if st.button("Hitung"):
            kalkulator_turunan(ekspresi)

            

    if __name__ == "__main__":
        main()
