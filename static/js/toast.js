function showToast(title, message, type = 'info') {
    // Warna berdasarkan tipe notifikasi
    const colors = {
        success: 'bg-green-500',
        error: 'bg-red-500',
        info: 'bg-blue-500'
    };

    // Buat elemen toast baru
    const toast = document.createElement('div');
    toast.className = `text-white px-6 py-4 border-0 rounded-md fixed top-4 right-4 shadow-lg z-50 ${colors[type]}`;
    toast.innerHTML = `<strong class="font-bold">${title}</strong><span class="block sm:inline ml-2">${message}</span>`;

    // Tambahkan toast ke halaman
    document.body.appendChild(toast);

    // Hapus toast setelah 3 detik
    setTimeout(() => {
        toast.remove();
    }, 3000);
}