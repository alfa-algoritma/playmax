# Proyek PlayMax - Tugas 2 Pemrograman Berbasis Platform

Ini adalah implementasi proyek untuk Tugas 2, sebuah toko sepatu online bernama PlayMax.

**Nama**: Muhammad Alfa Mubarok
**NPM**: 2406431391
**Kelas**: PBP D

---

# Tautan Aplikasi PWS

Aplikasi dapat diakses melalui tautan berikut:
[https://muhammad-alfa41-playmax.pbp.cs.ui.ac.id/](https://muhammad-alfa41-playmax.pbp.cs.ui.ac.id/)

---

# Jawaban Pertanyaan

### 1. Jelaskan implementasi *checklist* tugas secara *step-by-step*.

Proyek `PlayMax` diimplementasikan dengan mengikuti alur arsitektur MVT pada Django:

1. **Inisialisasi Proyek dan Aplikasi**: Proyek `playmax` diinisialisasi menggunakan `django-admin startproject playmax`. Setelah itu, sebuah aplikasi `main` dibuat di dalamnya dengan `python manage.py startapp main` dan didaftarkan ke dalam `INSTALLED_APPS` di `playmax/settings.py`.

2. **Definisi Model**: Sesuai spesifikasi tugas, model `Product` dibuat di `main/models.py`. Model ini mendefinisikan struktur data produk dengan atribut wajib seperti `name` (CharField), `price` (IntegerField), `description` (TextField), dan lainnya.

3. **Migrasi Database**: Setelah model didefinisikan, perintah `python manage.py makemigrations` dijalankan untuk membuat skrip migrasi, diikuti `python manage.py migrate` untuk menerapkan skema model tersebut ke dalam database SQLite lokal.

4. **Pembuatan View dan Template**: Sebuah fungsi `show_main` dibuat di `main/views.py`. Fungsi ini bertindak sebagai lapisan **View (business logic)**. Awalnya, ia hanya mengirimkan *context* berisi data statis (nama, kelas, nama aplikasi) ke template. Template `main.html` kemudian dibuat sebagai lapisan **Template (presentation)** untuk menampilkan data dari *context* tersebut menggunakan *template tags* `{{ ... }}`.

5. **Konfigurasi Routing**: `main/urls.py` dibuat untuk memetakan URL root (`''`) ke fungsi `show_main`. Kemudian, `playmax/urls.py` (level proyek) dikonfigurasi untuk `include` semua URL dari aplikasi `main`, bertindak sebagai pintu gerbang utama untuk *request* yang masuk.

6. **Populasi Data**: Data produk pertama (sepatu Adidas Adizero) dimasukkan ke database melalui **Django Admin**. Ini dilakukan dengan membuat `superuser` via `python manage.py createsuperuser`, mendaftarkan model `Product` di `main/admin.py`, dan menginput data melalui antarmuka web di `/admin`.

7.  **Menampilkan Data Dinamis**: `main/views.py` diperbarui untuk mengambil semua objek produk dari database menggunakan `Product.objects.all()` dan menambahkannya ke *context*. `main.html` juga diperbarui dengan *loop* `{% for product in products %}` untuk menampilkan setiap data produk secara dinamis.

8.  **Deployment**: Semua perubahan kode di-*push* ke repositori PWS. Karena database produksi terpisah, `superuser` baru dibuat di server PWS melalui *console*, dan data produk dimasukkan kembali melalui halaman admin situs yang sudah *live*.

### 2. Bagan *request-response* dan kaitan MVT.
## Bagan 

```mermaid
graph TD
    A[Browser/Client] -->|HTTP Request| B[Django Server]
    B --> C[settings.py<br/>Konfigurasi]
    C --> D[urls.py<br/>URL Routing]
    D --> E[views.py<br/>Business Logic]
    E -->|Query Data| F[models.py<br/>ORM Layer]
    F -->|SQL Operations| G[(Database)]
    E -->|Context Data| H[templates/<br/>HTML Files]
    H --> I[Rendered<br/>Response]
    I --> B
    B -->|HTTP Response| A

    %% Styling
    classDef client fill:#e3f2fd,stroke:#1976d2,stroke-width:3px,color:#000
    classDef server fill:#ffe3e0,stroke:#f57c00,stroke-width:2px,color:#000
    classDef config fill:#e3f5f5,stroke:#7fb1a2,stroke-width:2px,color:#000
    classDef routing fill:#e8f5e8,stroke:#388e3c,stroke-width:2px,color:#000
    classDef logic fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#000
    classDef data fill:#fff1eb,stroke:#ffa000,stroke-width:2px,color:#000
    classDef database fill:#e0f2f1,stroke:#00796b,stroke-width:2px,color:#000
    classDef template fill:#fff8e9,stroke:#689f38,stroke-width:2px,color:#000
    classDef response fill:#ede7f6,stroke:#512da8,stroke-width:2px,color:#000

    class A client
    class B server
    class C config
    class D routing
    class E logic
    class F data
    class G database
    class H template
    class I response


Alur *request-response* pada Django mengikuti arsitektur Model-View-Template (MVT) yang memisahkan antara data, logika, dan tampilan.


Berikut penjelasannya berdasarkan bagan di atas:
1. **HTTP Request**: Pengguna mengakses sebuah URL, mengirimkan sebuah HTTP Request ke server.
2. **urls.py (Router)**: Django menerima *request* dan meneruskannya ke `urls.py`. Berkas ini bertindak seperti "peta jalan" yang mencocokkan pola URL dengan *view* yang sesuai untuk menanganinya.
3. **views.py (Business Logic Layer)**: Setelah menemukan kecocokan, `urls.py` akan memanggil fungsi yang sesuai di `views.py`. *View* adalah lapisan logika bisnis yang memproses *request*.
4. **models.py (Data Access Layer)**: Jika *view* membutuhkan data dari database (misalnya, daftar produk), ia akan berinteraksi dengan `models.py`. Model adalah lapisan akses data yang bertanggung jawab untuk membaca atau menulis data ke database.
5. **Template (Presentation Layer)**: Setelah *view* selesai memproses logika dan mendapatkan data dari model, ia akan meneruskan data tersebut ke sebuah *template* HTML.
6.  **HTTP Response (HTML)**: *Template engine* Django akan me-*render* berkas HTML, mengisi semua variabel dinamis (seperti `{{ product.name }}`) dengan data yang diterima dari *view*. Hasil akhirnya adalah sebuah halaman HTML utuh yang dikirim kembali ke browser pengguna sebagai HTTP Response.

### 3. Peran `settings.py` dalam proyek Django.

`settings.py` adalah file konfigurasi pusat untuk sebuah proyek Django. File ini berisi semua pengaturan penting yang menentukan bagaimana proyek berjalan, termasuk:
* **Konfigurasi Database**: Pengaturan untuk menghubungkan proyek dengan database (misalnya, SQLite, PostgreSQL).
* **Aplikasi Terinstal (`INSTALLED_APPS`)**: Daftar semua aplikasi yang aktif di dalam proyek, baik aplikasi bawaan Django maupun yang kita buat sendiri.
* **Konfigurasi Template**: Lokasi direktori tempat Django harus mencari file-file template HTML.
* **Secret Key**: Kunci unik untuk keamanan kriptografis.
* **Pengaturan Statis**: Konfigurasi untuk file statis seperti CSS dan JavaScript.
* **Middleware**: Daftar komponen yang memproses *request* dan *response* secara global.

Singkatnya, `settings.py` adalah "otak" dari konfigurasi proyek yang mengatur semua komponen untuk bekerja bersama.

### 4. Cara kerja migrasi database di Django.

Migrasi database di Django adalah proses dua langkah untuk menyinkronkan perubahan pada `models.py` dengan skema database yang sebenarnya.

1.  **`python manage.py makemigrations`**: Perintah ini akan membandingkan model Anda saat ini dengan versi terakhir yang disimpan dalam file migrasi. Jika ada perubahan (seperti menambah *field* atau model baru), Django akan membuat sebuah file Python baru di dalam folder `migrations/`. File ini berisi instruksi spesifik tentang bagaimana cara mengubah struktur database agar sesuai dengan model yang baru. Proses ini seperti membuat "cetak biru" atau *blueprint* perubahan.

2.  **`python manage.py migrate`**: Perintah ini membaca semua file "cetak biru" dari `makemigrations` yang belum diterapkan, lalu menerjemahkannya menjadi perintah SQL dan menjalankannya pada database. Proses inilah yang secara nyata mengubah struktur tabel di database, seperti membuat tabel baru atau menambahkan kolom.

Pemisahan ini memungkinkan developer untuk meninjau perubahan skema (cetak birunya) sebelum benar-benar menerapkannya ke database.

### 5. Mengapa Django dijadikan permulaan pembelajaran?

Menurut saya, Django adalah pilihan yang sangat baik untuk memulai pembelajaran pengembangan perangkat lunak karena beberapa alasan kuat:

* **Struktur yang Jelas (MVT)**: Arsitektur Model-View-Template memaksa pemula untuk mempraktikkan *Separation of Concerns*, yaitu memisahkan logika data (Model), logika bisnis (View), dan tampilan (Template). Ini membangun kebiasaan pengkodean yang baik dan terorganisir sejak awal.
* **"Batteries-Included" Philosophy**: Django hadir dengan banyak fitur bawaan yang sangat kuat, seperti ORM (Object-Relational Mapping) untuk berinteraksi dengan database tanpa perlu menulis SQL mentah, dan situs admin yang dibuat secara otomatis. Ini memungkinkan pemula untuk membuat aplikasi yang fungsional dengan cepat dan fokus pada logika aplikasi daripada membangun semuanya dari nol.
* **Keamanan Bawaan**: Django menangani banyak masalah keamanan umum (seperti SQL injection, XSS, CSRF) secara default, sehingga pemula dapat membangun aplikasi yang relatif aman tanpa harus menjadi ahli keamanan terlebih dahulu.
* **Ekosistem dan Dokumentasi yang Matang**: Django memiliki salah satu dokumentasi terbaik di dunia *open-source* dan didukung oleh komunitas yang besar. Ini memudahkan pemula untuk menemukan solusi, tutorial, dan bantuan saat menghadapi masalah.

### 6. Feedback untuk asisten dosen tutorial 1.

Untuk Feedback tersendiri saya cukup senang dengan kinerja para kakak-kakak asdos yang dimana sangat mau membantu adik tingkatnya yang mungkin kesusahan dalam memahami cara kerja Django, terima kasih kakak-kakak asdos dan semangat juga kuliahnya!