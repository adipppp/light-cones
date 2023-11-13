### Apa perbedaan utama antara <i>stateless</i> dan <i>stateful widget</i> dalam konteks pengembangan aplikasi Flutter?

Stateless widget merupakan widget yang tidak akan berubah setelah di build, sedangkan stateful widget merupakan widget yang dapat berubah berdasarkan input yang diterima.

<br>

### Sebutkan seluruh <i>widget</i> yang kamu gunakan untuk menyelesaikan tugas ini dan jelaskan fungsinya masing-masing.

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

<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat sebuah program Flutter baru dengan tema inventory seperti tugas-tugas sebelumnya.

  1. Menjalankan `flutter create light_cones_mobile`
  2. Mengubah current working directory ke `light_cones_mobile`

- Membuat tombol sederhana dengan ikon dan teks untuk melihat daftar item

  1. Membuat class `MenuButton` dengan property `iconData` dan `text`
  2. Menambahkan `InkWell` yang mempunyai children `Icon` dan `Text` yang bertuliskan "Lihat Item" pada method build dari `MenuButton`

- Membuat tombol sederhana dengan ikon dan teks untuk menambah item

  1. Menambahkan `InkWell` yang mempunyai children `Icon` dan `Text` yang bertuliskan "Tambah Item" pada method build dari `MenuButton`

- Membuat tombol sederhana dengan ikon dan teks untuk logout

  1. Menambahkan `InkWell` yang mempunyai children `Icon` dan `Text` yang bertuliskan "Logout" pada method build dari `MenuButton`