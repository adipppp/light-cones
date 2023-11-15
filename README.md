### Jelaskan perbedaan antara `Navigator.push()` dan `Navigator.pushReplacement()`, disertai dengan contoh mengenai penggunaan kedua metode tersebut yang tepat!

`Navigator.push()` melakukan navigasi ke sebuah page dan memasukkan page tersebut ke dalam navigation stack. Contoh penggunaan `Navigator.push()` yaitu navigasi dari home page.

`Navigator.pushReplacement()` melakukan navigasi ke sebuah page, mengeluarkan page sebelumnya dari navigation stack, dan memasukkan current page ke dalam navigation stack. Contoh penggunaan `Navigator.pushReplacement()` adalah navigasi dari halaman register akun pengguna.

<br>

### Jelaskan masing-masing <i>layout</i> widget pada Flutter dan konteks penggunaannya masing-masing!

`GridView` - Berfungsi untuk menyusun elemen UI sebagai grid/table.
`ListView` - Layout yang mirip dengan GridView, bedanya ListView hanya memiliki 1 column saja. ListTile umumnya digunakan sebagai children dari ListView.
`Align` - Layout widget yang berfungsi untuk menerapkan align pada child relatif terhadap widget Align tersebut.
`Center` - Mirip dengan widget Align, dengan perbedaan alignment nya selalu ke tengah.
`SizedBox` - Layout widget yang berfungsi untuk mengatur size pada child widgetnya.

<br>

### Sebutkan apa saja elemen input pada form yang kamu pakai pada tugas kali ini dan jelaskan mengapa kamu menggunakan elemen input tersebut!

`Form` - Sebagai parent untuk `TextFormField`
`TextFormField` - Agar input yang diterima dalam bentuk string sehingga input string tersebut dapat diproses lebih lanjut sesuai yang diinginkan.
`FormPageState` - berfungsi untuk melakukan validasi input

<br>

### Bagaimana penerapan <i>clean architecture</i> pada aplikasi Flutter?

Mengelompokkan Widget-Widget yang memiliki fungsionalitas sama ke dalam file yang sama serta file-file yang memiliki kesamaan fungsi ke dalam direktori yang sama

### Jelaskan bagaimana cara kamu mengimplementasikan <i>checklist</i> di atas <i>secara step-by-step!</i> (bukan hanya sekadar mengikuti tutorial)

- Membuat minimal satu halaman baru pada aplikasi, yaitu halaman formulir tambah item baru.

  1. Membuat sebuah file baru bernama form.dart yang berisi `StatefulWidget` berupa `FormPage` beserta `State`-nya, yaitu `FormPageState`
  2. Menambahkan lima elemen input berupa `name`, `amount`, `description`, `rarity`, dan `path` ke dalam widget `Form` menggunakan `TextFormField` sebagai children
  3. Menambahkan button yang berfungsi menunjukkan data pada elemen-elemen input sebagai pop-up menggunakan `ElevatedButton`
  4. Melakukan validasi input dengan memanggil method `validate()` di dalam button tersebut

- Mengarahkan pengguna ke halaman form tambah item baru ketika menekan tombol `Tambah Item` pada halaman utama.

  1. Memanggil `Navigator.push()` pada widget `MenuButton` yang bertuliskan "Tambah Item" di menu.dart

- Memunculkan data sesuai isi dari formulir yang diisi dalam sebuah `pop-up` setelah menekan tombol `Save` pada halaman formulir tambah item baru.

  1. Memanggil method `showDialog()` pada handler onPressed `ElevatedButton` yang berisi data dari input pengguna pada widget `Form` di file form.dart

- Membuat sebuah drawer pada aplikasi

  1. Membuat file baru bernama `left_drawer.dart` yang berisi `StatelesWidget` bernama `LeftDrawer` dengan method build dengan return value widget `Drawer`
  2. Menambahkan `DrawerHeader` dan `ListTile` pada drawer dengan `ListTile` pertama mengarahkan ke home page dan `ListTile` kedua yang mengarahkan pengguna ke page Tambah Item
  3. Menambahkan drawer pada `MainMenu`