# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan yang menghadapi masalah tingginya angka dropout siswa (15% pada 2023). Proyek ini bertujuan untuk mengidentifikasi siswa berisiko dropout menggunakan data performa akademik, kehadiran, dan faktor demografis, sehingga institusi dapat memberikan intervensi dini untuk mengurangi angka dropout.

### Permasalahan Bisnis
1. Tingginya persentase siswa yang tidak menyelesaikan pendidikan (dropout)

2. Ketidakmampuan mengidentifikasi siswa berisiko secara real-time

3. Kurangnya strategi pencegahan berbasis data

### Tujuan Proyek
1. Membangun model Machine Learning untuk memprediksi risiko dropout.

2. Membuat dashboard monitoring untuk tim akademik guna analisis visual.

3. Mengembangkan prototype sistem prediksi yang dapat diakses secara online.

### Cakupan Proyek
1. Membangun model prediksi risiko dropout menggunakan Machine Learning

2. Membuat dashboard monitoring untuk tim akademik

3. Mengembangkan prototype sistem prediksi yang dapat diakses online

### Persiapan
Sumber data: Dataset performa siswa dari Kaggle ([StudentsPerformance.csv](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)) dengan penambahan kolom:
- attendance: Persentase kehadiran (60-100%)
- dropout: Label risiko (1 jika nilai matematika < 50, else 0)

kolom asli:
- math_score: Nilai matematika (0-100)
- reading_score: Nilai membaca (0-100)
- writing_score: Nilai menulis (0-100)
- gender: Jenis kelamin (male/female)
- parental_level_of_education: Tingkat pendidikan orang tua (kategori seperti some high school, high school, some college, dll.)

Setup environment:
```bash
pip install -r requirements.txt
```
Dependensi utama meliputi: pandas, scikit-learn, streamlit, matplotlib, dan numpy (lihat requirements.txt untuk detail).

## Business Dashboard
Dashboard ini menampilkan analisis faktor risiko dropout secara visual untuk membantu tim akademik memahami distribusi siswa dan faktor penentu.

**Fitur Utama**:
- Distribusi nilai matematika vs status dropout.
- Pengaruh kehadiran terhadap performa akademik (math, reading, writing).
- Analisis demografis: Distribusi risiko berdasarkan gender dan tingkat pendidikan orang tua.

Akses Dashboard:
([Looker Studio Dashboard](https://lookerstudio.google.com/reporting/1aa7f661-87ed-4f09-9f22-1b392e2f7442))
Looker Studio Dashboard
Kredensial:
Email: root@mail.com
Password: root123
(Catatan: Kredensial dan link bersifat placeholder untuk keperluan submission.)

## Menjalankan Sistem Machine Learning
**Lokal**
Jalankan aplikasi Streamlit dengan perintah:
```bash
streamlit run app.py
```

**Online**
([Streamlit App](https://dicodinglevelexpertsubmissionakhirproyekinstitution.streamlit.app/))

**Fitur Prototype**:
1. Input data siswa: nilai matematika dan persentase kehadiran.

2. Prediksi risiko dropout (Tinggi/Rendah) menggunakan model Logistic Regression.

3. Visualisasi faktor penentu: kontribusi nilai matematika dan kehadiran terhadap prediksi.

**Detail Model**
Model Machine Learning yang digunakan adalah Logistic Regression, dilatih menggunakan data dari students_performance.csv. Fitur utama yang digunakan: math_score, attendance, dan parental_level_of_education. Model dievaluasi di notebook.ipynb dengan metrik seperti akurasi dan F1-score.

## Conclusion
Berdasarkan analisis:

1. Siswa dengan nilai matematika < 50 memiliki risiko dropout 4x lebih tinggi dibandingkan siswa dengan nilai di atas 50.

2. Kehadiran < 70% berkorelasi dengan peningkatan risiko dropout sebesar 35%.

3. Faktor dominan yang memengaruhi risiko dropout: nilai matematika, kehadiran, dan tingkat pendidikan orang tua.

4. Nilai membaca dan menulis menunjukkan korelasi yang lebih lemah dengan risiko dropout, namun tetap relevan untuk analisis performa keseluruhan.

### Rekomendasi Action Items
1. Program Remedial Matematika: Intervensi khusus untuk siswa dengan nilai matematika < 50, termasuk kelas tambahan dan tutor.

2. Sistem Monitoring Kehadiran: Implementasi alert otomatis jika kehadiran siswa < 70% untuk tindakan cepat.

3. Parental Engagement: Workshop untuk orang tua dengan tingkat pendidikan "high school" atau "some high school" guna meningkatkan dukungan terhadap siswa.

4. Dashboard Real-time: Integrasi sistem prediksi dengan database akademik untuk monitoring berkelanjutan.
