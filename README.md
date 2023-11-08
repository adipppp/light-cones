### Apa perbedaan utama antara <i>stateless</i> dan <i>stateful widget</i> dalam konteks pengembangan aplikasi Flutter?

Stateless widget merupakan widget yang tidak akan berubah setelah di build, sedangkan stateful widget merupakan widget yang dapat berubah berdasarkan input yang diterima.

<br>

### Sebutkan seluruh <i>widget</i> yang kamu gunakan untuk menyelesaikan tugas ini dan jelaskan fungsinya masing-masing.

`StatelessWidget` - Widget yang tidak akan berubah setelah di build
`MaterialApp`
`Scaffold`
`AppBar`
`Container`
`GridView`
`InkWell`
`Column`
`Icon`
`Text`
`ScaffoldMessenger`
`SnackBar`

<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Ubahlah kode <i>cards</i> data item agar dapat mendukung AJAX GET.
  1. Membuat sebuah view baru bernama `get_item_json` untuk menghandle GET request yang masuk dan mengirimkan JSON
  sebagai response
  2. Menambahkan function `displayLightCones` ke dalam main.html pada direktori main/templates
  3. Mengganti fitur for loop Django pada main.html menjadi sebuah table kosong dengan id `display-table`

- Lakukan pengambilan task menggunakan AJAX GET
  1. Memanggil `displayLightCones` setiap halaman di-load

- Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
  1. Menambahkan kode HTML modal ke dalam `main.html` pada direktori main/templates
  2. Menambahkan button yang berfungsi untuk menampilkan modal pada `main.html`

- Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
  1. Membuat sebuah function bernama `add_item_ajax` pada views.py untuk menghandle POST request yang masuk menggunakan AJAX

- Buatlah path `/create-ajax/` yang mengarah ke fungsi view yang baru kamu buat.
  1. Menambahkan route url baru berupa `/main/add_light_cone_ajax/` pada urls.py yang berfungsi memanggil view `add_item_ajax`

- Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`.
  1. Menambahkan beberapa function JavaScript ke dalam `main.html` pada direktori main/templates/
  2. Menambahkan click listener pada button untuk mengumpulkan hasil modal dengan function `addLightConeAJAX` melalui POST request

- Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.
  1. Memanggil function `displayLightCones` untuk mengupdate table yang berisi list light cone yang ada setelah memanggil function `addLightConeAJAX`

- Melakukan perintah collectstatic.
  1. Membuat sebuah direktori baru pada root direktori bernama `static/`
  2. Menambahkan line `STATIC_ROOT = os.path.join(BASE_DIR, 'static')` pada settings.py