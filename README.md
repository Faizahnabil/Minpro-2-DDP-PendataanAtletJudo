Nama : Faizah Nabil
NIM : 2609116007
Tema : Pendataan Atlet Judo

A. Penjelasan Program
<img width="954" height="317" alt="Screenshot 2026-10-05 202831" src="https://github.com/user-attachments/assets/26f95b5b-057b-4ba6-8f95-17f48501657f" />

Bagian ini digunakan untuk menyimpan username, password, dan role pengguna menggunakan Dictionary. Dictionary akun menyimpan data pengguna. Setiap pengguna memiliki password dan role. Role digunakan untuk menentukan menu yang dapat diakses.

<img width="693" height="424" alt="Screenshot 2026-10-05 203807" src="https://github.com/user-attachments/assets/d82dcf79-b725-49c8-97c0-cf9170f78be7" />
Penggunaan conditional statement ada pada kode tersebut. Admin memiliki akses penuh untuk mengelola data atlet.

<img width="992" height="414" alt="Screenshot 2026-10-05 204008" src="https://github.com/user-attachments/assets/28d6c768-8056-49b6-bdae-b43f836353c1" />
Program utama menggunakan perulangan. Program akan terus berjalan dan kembali ke halaman login setelah pengguna melakukan logout. Program berhenti jika percobaan login sudah habis.

<img width="744" height="141" alt="Screenshot 2026-10-05 203051" src="https://github.com/user-attachments/assets/8bcf86ec-6180-4826-87f2-d4c2904384e1" />
<img width="286" height="49" alt="Screenshot 2026-10-05 204335" src="https://github.com/user-attachments/assets/1f3fe710-d066-49dc-a1a8-58b1660f13e9" />
<img width="418" height="57" alt="Screenshot 2026-10-05 204417" src="https://github.com/user-attachments/assets/5efc1a19-0a02-4f56-a071-3dbc038fb5c4" />
<img width="418" height="57" alt="Screenshot 2026-10-05 204417" src="https://github.com/user-attachments/assets/5acce5fe-abc3-4350-8b2e-703be5391908" />
<img width="408" height="42" alt="Screenshot 2026-10-05 204459" src="https://github.com/user-attachments/assets/3c426194-63a7-4ec5-8bf7-52d0da54e2c4" />
<img width="407" height="44" alt="Screenshot 2026-10-05 204513" src="https://github.com/user-attachments/assets/d2658622-c086-4199-b7f5-0dc598c000fc" />
<img width="357" height="46" alt="Screenshot 2026-10-05 204525" src="https://github.com/user-attachments/assets/e98c1477-4f43-4486-be4d-63026c638e24" />
<img width="345" height="34" alt="Screenshot 2026-10-05 204537" src="https://github.com/user-attachments/assets/c00d9e5f-bb1e-4e7e-9973-6c01e47abef2" />
<img width="345" height="54" alt="Screenshot 2026-10-05 204552" src="https://github.com/user-attachments/assets/295edcb7-a877-4d60-87b1-881b65bf1465" />
<img width="339" height="59" alt="Screenshot 2026-10-05 204606" src="https://github.com/user-attachments/assets/c1e7fc46-fe22-476e-9434-58e8b5a0fc6a" />

Semua kode diatas menggunakan Function. Pada program Sistem Pendataan Atlet Judo, function digunakan untuk membagi program menjadi beberapa bagian agar lebih terstruktur dan mudah digunakan kembali, seperti function login() untuk proses login, tambah_data() untuk menambahkan atlet, dan tampilkan_data() untuk menampilkan data atlet.




B. Penjelasan Output

<img width="1359" height="528" alt="Screenshot 2026-10-05 194322" src="https://github.com/user-attachments/assets/bf368de0-d2e3-42fe-9d53-1b273bfab7b4" />
Terdapat 2 role pengguna yaitu admin dan user. Di output ini role saya adalah user, login menggunakan username dan password. User hanya dapat melihat data atlet yang sudah tersimpan saja tidak dapat melakukan apapun selain hal itu.

<img width="1575" height="391" alt="Screenshot 2026-10-05 192002" src="https://github.com/user-attachments/assets/8d5e640a-e448-489c-a554-956c76208814" />
Login tetap menggunakan username dan password. Di output ini role saya adalah admin, admin dapat menambah data, melihat data, mengubah data dan menghapus data.

<img width="1582" height="630" alt="Screenshot 2026-10-05 192032" src="https://github.com/user-attachments/assets/cec6480a-2e4b-40f4-b407-0fb0f17b1850" />
Setelah login saya langsung memilih menu ke-1 untuk menambah data atlet yang saya inginkan.

<img width="1549" height="773" alt="Screenshot 2026-10-05 192130" src="https://github.com/user-attachments/assets/8a24be9b-1d3a-46c1-baca-e8c56100ba84" />
Jika memilih menu ke-2 tampilan output nya akan seperti ini, menampilkan seluruh data atlet yang telah diinput sebelumnya.

<img width="1544" height="908" alt="Screenshot 2026-10-05 192323" src="https://github.com/user-attachments/assets/77146575-622b-4cb2-a217-a7e3648424f9" />
Menu ke-3 untuk mengubah data atlet, hanya perlu menginput data yang baru lalu data atlet yang salah sebelumnya akan berubah.

<img width="1542" height="902" alt="Screenshot 2026-10-05 192434" src="https://github.com/user-attachments/assets/866359d6-d7fa-44cd-8a3c-9aa3a83bb84b" />
Menu ke-4 untuk menghapus data atlet, ada pilihan ingin menghapus data atau tidak. Jika yakin ingin menghapus data ketik Y (Yes).

<img width="1029" height="419" alt="Screenshot 2026-10-05 192514" src="https://github.com/user-attachments/assets/533ee87e-335b-4cb9-a4e8-98c0ca76b4fd" />
Dan menu yang terakhir adalah Logout, Program selesai.

C. Penjelasan Flowchart

Flowchart ini menggambarkan alur Sistem Pendataan Atlet Judo yang dimulai dari proses login menggunakan username dan password. Sistem memberikan tiga kesempatan login. Setelah login berhasil, sistem mengecek role pengguna. Jika pengguna merupakan admin, maka dapat menambah, melihat, mengubah, dan menghapus data atlet. Sedangkan user hanya dapat melihat data atlet. Setiap proses input memiliki validasi untuk memastikan data yang dimasukkan sesuai. Setelah selesai menggunakan sistem, pengguna dapat melakukan logout dan kembali ke halaman login.
