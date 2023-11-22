### Apakah bisa kita melakukan pengambilan data JSON tanpa membuat model terlebih dahulu? Jika iya, apakah hal tersebut lebih baik daripada membuat model sebelum melakukan pengambilan data JSON?

Ya, tetapi data yang diambil masih belum dikelompokkan menjadi satu kesatuan.

<br>

### Jelaskan fungsi dari CookieRequest dan jelaskan mengapa <i>instance</i> CookieRequest perlu untuk dibagikan ke semua komponen di aplikasi Flutter.

CookieRequest merupakan sebuah class yang instancenya merepresentasikan cookies yang digunakan client selama app tersebut berjalan. Dengan membagikan sebuah instance CookieRequest kepada komponen-komponen pada sebuah app Flutter, sebuah app dapat melihat dan mengakses cookies secara real-time.

<br>

### Jelaskan mekanisme pengambilan data dari JSON hingga dapat ditampilkan pada Flutter.

1. Aplikasi Flutter melakukan fetch endpoint JSON menggunakan `http.get()`
2. HTTP response yang diterima di-`decode` menggunakan function `jsonDecode()`
3. Melakukan konversi data dari bentuk JSON ke bentuk object Item
4. Data dapat ditampilkan

<br>

### Jelaskan mekanisme autentikasi dari input data akun pada Flutter ke Django hingga selesainya proses autentikasi oleh Django dan tampilnya menu pada Flutter.

1. Melakukan login menggunakan method `login()` pada instance dari `CookieRequest` menggunakan username dan password yang didapatkan dari input pengguna
2. Mengecek apakah login berhasil dengan cara melihat nilai dari property `request.loggedIn`
3. Jika berhasil, lakukan `pushReplacement()` dan navigasi ke home page
4. Jika gagal, tampilkan `AlertDialog` yang menjelaskan bahwa user gagal login

### Sebutkan seluruh widget yang kamu pakai pada tugas ini dan jelaskan fungsinya masing-masing.

`StatelessWidget` - Widget yang cocok digunakan jika komposisi dari widget tersebut tidak pernah berubah jika diberikan input pengguna.

`Material` - Widget yang berfungsi menampung widget lain dengan tujuan menerapkan material design system dalam menyusun UI.

`MaterialApp` - Widget yang berfungsi sebagai starting point sebuah app Flutter. Seperti Material, MaterialApp juga menerapkan material design system.

`Scaffold` - Widget yang memiliki fungsi serupa dengan Material, dengan perbedaan Scaffold biasanya digunakan sebagai top-level container sebuah page pada Flutter.

`AppBar` - Widget yang merepresentasikan sebuah app bar pada page yang umumnya diletakkan pada Scaffold. AppBar berfungsi sebagai template yang dapat menampung widget-widget lain dengan layout yang sudah ditentukan.

`Container` - Widget yang berfungsi menampung widget lain dan menyediakan berbagai fitur layout seperti menambahkan padding dan margin pada widget tersebut.

`GridView` - Sebuah widget yang menampung widget-widget lain dan menyusunnya dengan layout grid.

`InkWell` - Widget berbentuk persegi panjang yang merespons terhadap touch event.

`Column` - Widget yang digunakan untuk menampung widget-widget lain dan menyusunnya sebagai sebuah kolom.

`Icon` - Widget yang merepresentasikan sebuah icon. Widget ini menyediakan berbagai icon bawaan yang tersedia pada Flutter untuk ditampilkan.

`Text` - Widget yang berfungsi menampilkan sebuah teks.

`ScaffoldMessenger` - Widget yang berfungsi mengatur SnackBar dan MaterialBanner.

`SnackBar` - Sebuah banner yang dapat dimunculkan pada bagian bawah layar.

`Provider` - Widget yang mengekspos sebuah instance ke semua komponen pada sebuah aplikasi flutter.

`TextButton` - Widget yang merepresentasikan sebuah button dengan teks diatasnya

`ElevatedButton` - Widget yang merepresentasikan sebuah button yang berada pada sebuah Material dan jika ditekan, Material.elevation dari Material tersebut bertambah

`AlertDialog` - Widget yang merepresentasikan sebuah pop-up

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step! (bukan hanya sekadar mengikuti tutorial).

  - Menambahkan app `authentication` pada Django project yang berfungsi untuk menghandle login dan logout pada aplikasi Flutter

  - Melakukan integrasi fungsionalitas autentikasi Django pada Flutter

  - Membuat model Item berdasarkan JSON response dari endpoint `/main/json`

  - Menerapkan fetch request pada Flutter dengan package `http`

  - Menambahkan endpoint Django baru bernama `/main/create-product-flutter` untuk menghandle tambah produk melalui Flutter
