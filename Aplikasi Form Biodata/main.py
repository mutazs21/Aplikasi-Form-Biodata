import streamlit as st
import pandas as pd
import datetime

st.title("Aplikasi Form Biodata")

# Gunakan Form agar tidak terjadi refresh otomatis saat submit
with st.form("biodata_form"):
    st.subheader('Isi Biodata')

    name = st.text_input(label='Nama Lengkap', value='')
    berat_badan = st.number_input(label="Berat badan", min_value=1)
    date = st.date_input(label='Tanggal Lahir', min_value=datetime.date(1900, 1, 1))

    # Hitung Umur
    today = datetime.date.today()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))

    feedback = st.text_area('Feedback')

    # Tombol submit
    submit_biodata = st.form_submit_button("Simpan Biodata")

# Menampilkan hasil input jika tombol ditekan
if submit_biodata:
    if name:
        st.write("### Hasil Biodata")
        st.write(f'**Nama** : {name}')
        st.write(f'**Berat Badan** : {berat_badan} Kg')
        st.write(f'**Tanggal Lahir** : {date}')
        st.write(f'**Umur** : {age} tahun')
        st.write(f'**Feedback** : {feedback}')
    else:
        st.warning("⚠️ Silakan isi Nama Lengkap!")

# **File Upload**
st.subheader("Upload File")

upload_file = st.file_uploader('Pilih file CSV (maks: 10MB)')
picture = st.camera_input('Ambil Foto')

if upload_file:
    st.write("### Dataset:")
    df = pd.read_csv(upload_file)
    st.dataframe(df)

if picture:
    st.write("### Gambar:")
    st.image(picture)

# **Pilihan Cita-Cita**
st.subheader("Pilih Cita-Cita")
future = st.radio(
    label="Apa cita-citamu?",
    options=('Presiden', 'Polisi', 'Tentara', 'Yang Lain'),
    horizontal=False
)

if future == 'Yang Lain':
    other_future = st.text_input("Silakan tulis cita-citamu:")
else:
    other_future = future

# **Jurusan**
st.subheader("Pilih Jurusan")

jurusan = st.selectbox(
    label="Pilih Jurusan",
    options=('Desain Komunikasi Visual', 'Perhotelan', 'Akuntansi', 'Perkantoran')
)

jurusan2 = st.multiselect(
    label="Jurusan yang kamu tertarik",
    options=('Desain Komunikasi Visual', 'Perhotelan', 'Akuntansi', 'Perkantoran')
)

st.write(f'**Cita-Cita**: {other_future}')
st.write(f'**Jurusan Pilihan**: {jurusan}')
st.write(f'**Jurusan Tertarik**: {", ".join(jurusan2) if jurusan2 else "Belum memilih"}')

# **Slider**
values = st.slider(
    label='Pilih Rentang Nilai',
    min_value=0, max_value=100, value=(10, 90)
)
st.write('**Rentang Nilai**:', values)

# **Checkbox & Verifikasi Robot**
agree = st.checkbox('Saya setuju dengan ini semua')

if st.button('Verifikasi Robot'):
    if agree:
        st.success('✅ Anda adalah manusia!')
    else:
        st.warning('⚠️ Harap setujui pernyataan di atas!')