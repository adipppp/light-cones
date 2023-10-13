### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Pada synchronous programming, program hanya menjalankan satu thread saja dalam satu waktu sehingga flow program berjalan secara linear. Hanya ada satu siklus input-proses-output saja dalam satu waktu.
<br><br>
Pada asynchronous programming, program menjalankan beberapa thread sekaligus dalam satu waktu. Thread yang dijalankan umumnya tidak bergantung kepada thread lain sehingga setiap thread dapat berjalan sebelum thread lainnya selesai dijalankan. Terdapat beberapa siklus input-proses-output dalam satu waktu.

<br>

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming merupakan sebuah paradigma dalam pemrograman yang bergantung kepada events. Program yang menerapkan paradigma ini menunggu events dikirimkan kepada program untuk kemudian diproses dan dikirimkan kembali sebagai respons terhadap input.
<br><br>
Pada event-driven programming, terdapat sebuah flow utama bernama event loop. Event loop berfungsi sebagai detektor events yang dikirimkan kepada program. Ketika sebuah event masuk, event loop akan menghandle event tersebut pada thread lain sehingga pemrosesan event tersebut tidak akan memblokir jalannya event loop. Dengan demikian, event loop dapat terus mendeteksi events yang masuk sambil memproses events sebelumnya.

<br>

### Jelaskan penerapan asynchronous programming pada AJAX.

Dengan AJAX, segala request yang dikirimkan menggunakan JavaScript tidak memblokir event loop pada sebuah website. Hal ini membuat JavaScript dapat terus menerima events dari input pengguna sehingga website terasa interaktif bagi pengguna.

<br>

### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Fetch API merupakan fitur native pada window yang tidak menggunakan XMLHttpRequest sehingga Fetch API akan lebih efisien dibandingkan dengan jQuery. Selain itu, Fetch API tidak menggunakan callback untuk menjalankan function setelah request tersebut selesai, tetapi menggunakan Promise sehingga fenomena "callback hell" dapat dihindari.

<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Ubahlah kode <i>cards</i> data item agar dapat mendukung AJAX GET.

  1. Membuat sebuah view baru bernama add_item_AJAX untuk menghandle request yang masuk menggunakan AJAX.
  2. Menambahkan beberapa function JavaScript ke `main.html` pada direktori main/templates/.
