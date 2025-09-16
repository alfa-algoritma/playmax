# Proyek PlayMax - Tugas 3 Pemrograman Berbasis Platform

Ini adalah implementasi proyek untuk Tugas 3, sebuah toko sepatu online bernama PlayMax, yang kini dilengkapi dengan fitur form dan data delivery (XML/JSON).

**Nama**: Muhammad Alfa Mubarok
**NPM**: 2406431391
**Kelas**: PBP D

---

# Tautan Aplikasi PWS

Aplikasi dapat diakses melalui tautan berikut:
[https://muhammad-alfa41-playmax.pbp.cs.ui.ac.id/](https://muhammad-alfa41-playmax.pbp.cs.ui.ac.id/)

---

# Jawaban Pertanyaan Tugas 3

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Kita memerlukan **data delivery** karena platform modern seringkali terdiri dari berbagai komponen atau *stack* yang terpisah (misalnya, backend dan frontend) yang perlu berkomunikasi satu sama lain.  Data delivery berfungsi sebagai jembatan yang memungkinkan pengiriman dan pertukaran data antar komponen tersebut.

Sebagai contoh, backend (server) perlu mengirimkan data ke frontend (browser) untuk ditampilkan kepada pengguna. Format data seperti **HTML**, **XML**, atau **JSON** digunakan untuk membungkus data agar terstruktur dan dapat dibaca oleh komponen yang menerimanya. Tanpa mekanisme data delivery yang standar, integrasi antar sistem menjadi sangat sulit dan tidak efisien.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Untuk sebagian besar aplikasi web modern, **JSON dianggap lebih baik** dan lebih populer karena beberapa alasan:

* **Lebih Ringkas dan Cepat**: JSON memiliki sintaks yang lebih sedikit (*less verbose*) dibandingkan XML. JSON tidak memerlukan tag penutup, sehingga ukuran datanya lebih kecil dan lebih cepat untuk diproses (di-*parsing*).
* **Mudah Dibaca**: Struktur `key-value` pada JSON seringkali lebih mudah dibaca dan dipahami oleh manusia dibandingkan struktur tag pada XML.
* **Integrasi dengan JavaScript**: Sintaks JSON identik dengan cara membuat objek JavaScript. Hal ini membuatnya sangat mudah digunakan dalam pengembangan web, di mana JavaScript adalah bahasa dominan di sisi klien. Mengubah data JSON menjadi objek JavaScript hanya memerlukan satu baris fungsi, yaitu `JSON.parse()`.

Karena alasan-alasan inilah, terutama kemudahan dan efisiensinya dalam ekosistem web berbasis JavaScript, JSON menjadi jauh lebih populer daripada XML.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi `is_valid()` pada form Django adalah sebuah *method* yang bertugas untuk **menjalankan validasi data** yang dikirim oleh pengguna melalui form. Method ini akan memeriksa apakah data yang diinput sesuai dengan aturan yang telah didefinisikan pada model atau form (misalnya, tipe data, panjang maksimal, apakah wajib diisi, dll.).

Kita sangat membutuhkan `is_valid()` karena:
1.  **Keamanan**: Mencegah data yang tidak valid atau berbahaya masuk ke dalam database.
2.  **Integritas Data**: Memastikan data yang tersimpan di database bersih, konsisten, dan sesuai dengan skema yang diharapkan.
3.  **User Experience**: Memberikan umpan balik yang jelas kepada pengguna jika ada kesalahan input, sehingga mereka bisa memperbaikinya.

Dalam kode, data hanya akan disimpan (`form.save()`) jika `is_valid()` mengembalikan nilai `True`, yang berarti semua data sudah lolos proses validasi.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkannya?

`{% csrf_token %}` adalah *template tag* Django yang berfungsi untuk **mencegah serangan Cross-Site Request Forgery (CSRF)**. CSRF adalah jenis serangan di mana situs web jahat menipu browser pengguna untuk melakukan permintaan (misalnya, mengirimkan data form) ke situs web lain tempat pengguna sedang login, tanpa sepengetahuan pengguna.

**Apa yang terjadi jika tidak ada `csrf_token`?**
Jika kita tidak menyertakan `csrf_token`, aplikasi kita menjadi rentan terhadap serangan CSRF. Penyerang dapat membuat halaman web palsu yang berisi form tersembunyi. Form ini akan otomatis mengirimkan data ke aplikasi kita (misalnya, menghapus data atau mengubah password) saat pengguna yang sedang login di aplikasi kita mengunjungi halaman palsu tersebut. Karena permintaan datang dari browser pengguna, server akan menganggapnya sebagai permintaan yang sah.

`csrf_token` mencegah ini dengan cara menghasilkan sebuah token unik di sisi server untuk setiap sesi pengguna dan menyisipkannya di dalam form. Ketika form dikirim, Django akan memverifikasi apakah token yang dikirim kembali oleh browser cocok dengan yang ada di server. Jika tidak, permintaan akan ditolak.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

Berikut adalah langkah-langkah implementasi yang saya lakukan untuk Tugas 3:

1. **Membuat Form**: Pertama, saya membuat file `main/forms.py` dan mendefinisikan `ProductForm` menggunakan `ModelForm` untuk terhubung langsung dengan model `Product`. Saya tentukan *field-field* yang akan ditampilkan di form.
2. **Membuat Views untuk Form dan Data Display**: Di `main/views.py`, saya membuat fungsi `create_product` untuk menangani logika form. Selain itu, saya memperbarui `show_main` untuk mengambil semua objek produk dari database (`Product.objects.all()`) dan mengirimkannya ke template.
3. **Membuat Template Form dan Memperbarui Halaman Utama**: Saya membuat file `main/templates/create_product.html` untuk halaman form. Kemudian, saya memodifikasi `main.html` untuk menampilkan semua produk dalam bentuk kartu dan menambahkan tombol "Add New Product" yang mengarah ke halaman form.
4. **Membuat Data Delivery Endpoints (XML & JSON)**: Di `views.py`, saya menambahkan empat fungsi: `show_xml` dan `show_json` untuk semua data, serta `show_xml_by_id` dan `show_json_by_id` untuk data spesifik. Fungsi-fungsi ini menggunakan `serializers.serialize()` dari Django untuk mengubah *queryset* model menjadi format XML atau JSON dan mengembalikannya sebagai `HttpResponse`.
5. **Menambahkan URL Routing**: Terakhir, saya mendaftarkan semua path URL untuk setiap view yang telah dibuat di `main/urls.py`, memberikan nama untuk setiap path agar mudah dipanggil dari template.

### Screenshot Akses URL Menggunakan Postman

**Contoh Akses `.../json/`:**
![Contoh JSON](URL_JSON)

**Contoh Akses `.../xml/`:**
![Contoh XML](URL_XML)

**Contoh Akses `.../json/1/`:**
![Contoh JSON by ID](URL_JSON_BY_ID)

**Contoh Akses `.../xml/1/`:**
![Contoh XML by ID](URL_XML_BY_ID)


### Feedback untuk Asisten Dosen Tutorial 2

Untuk Feedback tersendiri saya sangat senang dengan kinerja para kakak-kakak asdos yang dimana mau membantu adik tingkatnya yang mungkin kesusahan dalam memahami cara kerja Django dan juga mungkin mau ditanya-tanya beberapa hal diluar tugas yang menambah wawasan baru saya dalam perkuliahan, terima kasih kakak-kakak asdos dan semangat juga kuliahnya!