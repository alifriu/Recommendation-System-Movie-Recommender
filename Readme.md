# Laporan Proyek Machine Learning - Muhammad Alif Alfattah Riu

## Project Overview

Pengembangan sistem rekomendasi semakin penting bagi platform streaming karena potensinya dalam meningkatkan kepuasan pengguna, keterlibatan, dan pendapatan platform. Dengan menyediakan konten yang dipersonalisasi, sistem ini memungkinkan pengguna menemukan film yang sesuai dengan preferensi mereka, sehingga memperbaiki pengalaman dan meningkatkan loyalitas terhadap platform. Sistem rekomendasi yang efektif tidak hanya mengurangi waktu pencarian konten, tetapi juga mendorong eksplorasi genre dan judul baru.

Platform seperti Netflix dan Spotify telah membuktikan bahwa mesin rekomendasi canggih mampu meningkatkan keterlibatan dan retensi pengguna. Misalnya, rekomendasi personal yang didasarkan pada preferensi pengguna meningkatkan durasi penggunaan dan kepuasan pelanggan. Strategi ini dilaporkan mampu mengurangi tingkat churn hingga 10% dan berkontribusi pada pertumbuhan pendapatan, terutama karena sistem ini juga dapat mempromosikan konten berbayar atau eksklusif dengan lebih efektif.

Sistem rekomendasi modern menggunakan pendekatan seperti Content-Based Filtering, Collaborative Filtering, dan metode hibrida, yang sering didukung oleh teknologi deep learning. Algoritme ini menganalisis data pengguna dan fitur item untuk memprediksi dan merekomendasikan konten yang paling relevan. Mengingat persaingan di industri streaming, mesin rekomendasi yang dirancang dengan baik tidak hanya menjadi alat personalisasi tetapi juga pendorong utama kesuksesan bisnis.

## Business Understanding

Bagian laporan ini mencakup:

### Problem Statements
1. Bagaimana cara merancang sistem rekomendasi yang memberikan saran film berdasarkan genre yang relevan dengan preferensi pengguna?
2. Bagaimana membangun sistem rekomendasi dengan pendekatan (Content-Based Filtering) menggunakan Cosine Similarity dan (Collaborative Filtering) berbasis Model Deep Learning?
3. Apa metode terbaik untuk mengevaluasi performa sistem rekomendasi yang dihasilkan?

### Goals

Untuk menjawab masalah yang telah dirumuskan, proyek ini bertujuan untuk:
1. Menghasilkan Top-N rekomendasi film berdasarkan genre yang sesuai dengan preferensi pengguna menggunakan pendekatan Content-Based Filtering.
2. Membangun sistem rekomendasi menggunakan dua pendekatan utama:
    - Content-Based Filtering dengan Cosine Similarity untuk memanfaatkan informasi genre dan fitur lain.
    - Collaborative Filtering berbasis Deep Learning untuk merekomendasikan film berdasarkan data rating yang diberikan pengguna.
3. Mengevaluasi performa sistem rekomendasi menggunakan metrik Precision dan Root Mean Squared Error (RMSE)

    ### Solution statements
    Untuk mencapai tujuan proyek, strategi yang akan dilakukan meliputi:

    1. Content-Based Filtering dengan Cosine Similarity
        - Pendekatan ini memanfaatkan fitur seperti genre untuk merekomendasikan film yang memiliki kemiripan tertinggi dengan film yang telah dinikmati pengguna.
         - Cosine Similarity digunakan untuk menghitung kemiripan antar film berdasarkan representasi vektor fitur.
    
    2. Collaborative Filtering berbasis Deep Learning
        - Data rating pengguna akan digunakan untuk melatih model rekomendasi berbasis Deep Learning.Model ini akan mengenali pola interaksi kompleks antara pengguna dan film untuk memberikan rekomendasi yang personal.

    3. Pengembangan dan Evaluasi Model
        - Dataset akan diproses untuk memilih fitur yang relevan seperti genre, judul, dan rating.
        - Dua pendekatan (Content-Based Filtering dan Collaborative Filtering) akan diimplementasikan dan diuji secara terpisah.
        - Evaluasi performa akan dilakukan menggunakan metrik Precision dan RMSE untuk mengukur relevansi dan akurasi rekomendasi.

## Data Understanding
Dataset yang digunakan merupakan dataset yang tersedia pada platform Kaggle [Movie Recommendation System](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system/data).Dataset Memiliki 2 file yang berbeda dengan deskripsi yang tertera dibawah ini.


### Informasi Dataset

| Jenis    | Keterangan                                                |
|----------|-----------------------------------------------------------|
| Title    | Movie Recommendation System                               |
| Source   |[Kaggle](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system/data)        |
| Owner    | [MANAS PARASHAR ](https://www.kaggle.com/parasharmanas)                                                  |
| License  | Database: Open Database, Contents: Database Contents      |
| Tags     | Arts and Entertainment, Movies and TV Shows               |
| Usability | 10.00                                                     |

### Variabel-variabel pada Dataset:
**movies.csv**
 - `movieId` : ID unik untuk setiap film.
 - `title` : Judul Tiap Film.
 - `genres` : Genre FIlm, dipisahkan dengan tanda "|".

**ratings.csv**
 - `userId` : ID unik untuk setiap User.
 - `movieId` : ID unik untuk setiap film.
 - `rating` : Penilaian yang diberikan oleh User untuk film yang telah ditonton.
 - `timestamp` : Waktu ketika User memberikan rating.
 

### Exploratory Data Analysis - Deskripsi Variabel
**movies.csv**
| No | Column       | Non-Null Count | Dtype  |
|----|--------------|----------------|--------|
| 1  | movieId      | 62423 non-null | int64  |
| 2  | title        | 62423 non-null | object |
| 3  | genres       | 62423 non-null | object |

**ratings.csv**
| No | Column       |   Non-Null Count  |   Dtype   |
|----|--------------|-------------------|-----------|
| 1  | movieId      | 25000095 non-null |   int64   |
| 2  | title        | 25000095 non-null |   int64   |
| 3  | genres       | 25000095 non-null |  flolat64 |
| 4  | genres       | 25000095 non-null |   object  |

### Exploratory Data Analysis - Cek Missing Value dan Duplicate Value
Pada tahap ini, kita akan mengecek apakah ada baris data yang terdapat missing value dan duplicate value
#### Null value
**movies.csv** 
| Column       | Null | 
|--------------|------|
| movieId      |  0   | 
| title        |  0   | 
| genres       |  0   | 

**ratings.csv** 
| Column       | Null | 
|--------------|------|
| userId       |  0   | 
| movieId      |  0   | 
| rating       |  0   |
| timestamp    |  0   |

#### Duplicated Value
| Dataset      | duplicate | 
|--------------|-----------|
| movies.csv   |     0     |
| ratings.csv  |     0     | 

setalah pengecekan, kedua file tidak ditemukan adanya missing value dan duplicate value

### Exploratory Data Analysis - Univariate Data Analysis
|       | nilai | 
|--------------|-----------|
| Jumlah Film yang tersedia  |     62325     |
| Jumlah user yang memberi rating  |     162541     | 

Berdasarkan data yang ada,jumlah film yang tersedia ada sebanyak __62.325__ film dan jumlah User yang memberikan rating sebanyak __162.541__.

Dari Keseluruhan Film yang ada, beberapa Film memiliki jumlah rata-rata Rating tertinggi.
<img src='gambar\top10moviesbyrating.png'></img>

Terlihat bahwa 10 film diatas,memiliki rata-rata sebesar 5.0


## Data Preparation
Teknik Data preparation yang dilakukan terdiri dari:
- Data Preprocessing
- TF-IDF Vectorizer Data Movies
- Encoding Data Ratings
- Membagi Data untuk Training dan Validasi

### Data Preprocessing

**Menghapus nilai beberapa nilai dan atribut yang tidak diperlukan**
|movieId|	title|	genres|
|-------|--------|---------|
|26497|	Another Country (1984)|	`Drama\|Romance`|
|137759|	Susie Q (1996)|	`Children\|Comedy\|Drama\|Mystery`|
|196627|	Malicious (2018)|`Horror\|Thriller`|
|172315|	Justin Time (2010)|`Action\|Adventure\|Children\|Fantasy\|Sci-Fi`|
|172675|	From 180 & Taller (2005)|`Comedy\|Romance`|
|592|	Batman (1989)|`Action\|Crime\|Thriller`|
|181949|	The Pelican and the Snipe (1944)|`Animation`|
|54833|	Brighton Rock (1947)|`Crime\|Drama\|Film-Noir`|
|155020|	Summers Downstairs (2015)|`(no genres listed)`|
|203290|	Check to the Queen (1969)|`Drama\|Romance`|

Pada data movies, terdapat beberapa baris yamg memiliki genre (no genres listed).

-|movieId|title|	genres|
-----|-------|-----|-------|
15881|	83773|	Away with Words (San tiao ren) (1999)|`(no genres listed)`|
16060|	84768|	Glitterbug (1994)|`(no genres listed)`|
16351|	86493|	Age of the Earth, The (A Idade da Terra) (1980)|`(no genres listed)`|
16491|	87061|	Trails (Veredas) (1978)|`(no genres listed)`|
17404|	91246|	Milky Way (Tejút) (2007)|`(no genres listed)`|
...|	...|	...|	...|
62400|	209101|	Hua yang de nian hua (2001)|`(no genres listed)`|
62401|	209103|	Tsar Ivan the Terrible (1991)|`(no genres listed)`|
62407|	209133|	The Riot and the Dance (2018)|`(no genres listed)`|
62415|	209151|	Mao Zedong 1949 (2019)|`(no genres listed)`|
62421|	209169|	A Girl Thing (2001)|`(no genres listed)`|

Karena Kita akan menggunakan sistem rekomendasi berbasis genre film, maka genre (not genres listed) akan kita hapus.

`movies = movies[movies['genres'] != '(no genres listed)']`

menampilkan data ratings
userId|	movieId|rating|timestamp|
------|--------|------|---------|
1	|296|	5.0	|1147880044
1	|306|	3.5	|1147868817
1	|307|	5.0	|1147868828
1	|665|	5.0	|1147878820
1	|899|	3.5	|1147868510

karena data ratings sangat banyak dan tidak sepadan dengan sumber daya yang saya miliki oleh karena itu kita akan mengambil beberap puluh ribu saja untuk dijadikan sample.
`ratings = ratings.sample(n=10000, random_state=42)`

Hapus fitur `timestamp` dari data ratings karena kita hanya menggunakan kolom `userId,movieId,rating` pada tahap pemodelan nanti.
userId|	movieId|rating|
------|--------|------|
1	|296|	5.0	|
1	|306|	3.5	|
1	|307|	5.0	|
1	|665|	5.0	|
1	|899|	3.5	|

**Mengapa tahapan Data Preprocessing diperlukan?**
- Data preprocessing adalah langkah penting untuk mempersiapkan data agar bersih dan relevan, termasuk menghapus atribut tidak penting serta nilai seperti `(no genres listed)` pada kolom Genre. Proses ini meningkatkan efisiensi analisis dan memastikan struktur data lebih terorganisir. Dengan data yang telah diproses, model machine learning dapat menghasilkan prediksi yang lebih akurat.

### TF-IDF VEctorizer Data Movies
Karena komputer hanya dapat memproses data numerik, oleh karena itu data genres perlu kita ubah menjadi numerik dengan menggunakan TFidfVectorizer sebelum di modelling menggunakan Cosine Similarity.

<img src='gambar\tfidf.png'></img>

**Mengapa tahap Mengubah data kedalam representasi numerik diperlukan?**
- Data perlu dikonversi ke dalam bentuk numerik karena sistem rekomendasi berbasis konten membutuhkan angka untuk merepresentasikan teks atau kategori, sehingga kemiripan antar-item dapat dihitung. Sebagai contoh, pada sistem rekomendasi film, kategori seperti "Adventure," "Comedy," atau "Drama" diterjemahkan ke dalam nilai angka agar dapat dibandingkan secara matematis. Representasi ini memungkinkan algoritma mengukur kesamaan dengan lebih akurat.

#### Encoding Data Ratings
|userId|movieId|rating|user|movie|
|------|-------|------|----|-----|
|15541|1240|4.0|5851|359|
|61719|44191|5.0|4469|1519|
|83787|26606|3.0|1701|1222|
|127634|2353|2.0|4522|604|
|54785|2019|5.0|4327|200|
|...|...|...|...|...|
|147810|2927|3.0|5390|2657|
|118865|2706|4.5|4924|318|
|71839|2320|2.5|633|2560|
|141460|1225|3.0|853|690|
|107286|1689|5.0|6740|3053|

**Mengapa tahap Encoding data diperlukan?**
- Proses encoding diperlukan untuk memastikan model Collaborative Filtering dapat memahami pola interaksi antara pengguna dan item. Transformasi data ke bentuk numerik penting agar model berbasis neural network mampu memproses dan menganalisis informasi tersebut secara efektif.

#### Membagi Data untuk Training dan Validasi
Setelah data diubah menjadi bentuk numerik, langkah berikutnya adalah membagi data menjadi set pelatihan dan validasi dengan perbandingan 80:20

**Mengapa tahap membagi Data untuk Training dan Validasi dibutuhkan?**
- Pembagian ini dilakukan untuk memastikan model dapat dilatih menggunakan sebagian besar data (80%) dan divalidasi dengan data yang terpisah (20%) untuk mengukur performa pada data baru.Proses ini penting untuk mencegah model overfitting, yaitu ketika model terlalu "menghafal" data pelatihan sehingga kinerjanya buruk pada data yang belum pernah dilihat sebelumnya. Pembagian dilakukan secara acak untuk memastikan distribusi data tetap representatif dalam kedua subset tersebut. 

## Modeling
Pada tahapan modeling, model yang digunakan terdiri dari:
- Content Based Filtering - Cosine Similarity
- Collaborative Filtering - RecomenderNet

### 1. Content Based Filtering - Cosine Similarity
Pendekatan ini merekomendasikan item berdasarkan kemiripan antara item yang sudah disukai pengguna dengan item lain yang tersedia. Dalam sistem rekomendasi berbasis konten, setiap item direpresentasikan oleh fitur-fitur tertentu (misalnya, genre, deskripsi, atau aktor dalam rekomendasi film).

Pada sistem rekomendasi berbasis konten, cosine simmilarity  sebagai algoritma untuk membuat sistem rekomendasi berdasarkan content-based filtering approach. Cosine Similarity digunakan untuk menghitung kemiripan antara dua item dengan mengukur sudut kosinus antara dua vektor fitur mereka. Semakin kecil sudutnya (atau semakin mendekati 1 nilai cosine similarity-nya), semakin mirip kedua item tersebut.Cosine similarity dirumuskan sebagai berikut.

$$Cos (\theta) = \frac{\sum_1^n a_ib_i}{\sqrt{\sum_1^n a_i^2}\sqrt{\sum_1^n b_i^2}}$$

Berikut adalah penjelasan dengan kelebihan dan kekurangan Content-Based Filtering

**Kelebihan:**
- __Personalisasi Tinggi__: Sistem memberikan rekomendasi spesifik berdasarkan preferensi unik setiap pengguna karena fokusnya pada fitur item yang sudah disukai.
- __Tidak Memerlukan Data Pengguna Lain__: Hanya menggunakan informasi item, sehingga efektif pada situasi dengan sedikit data pengguna (cold start untuk pengguna baru).
 
**Kekurangan:**
- __Kurang Variasi dalam Rekomendasi__: Sistem cenderung memberikan rekomendasi yang terlalu mirip dengan item sebelumnya, sehingga pengguna mungkin tidak menemukan item baru yang berbeda (sering disebut _serendipity problem_).
- __Ketergantungan pada Fitur Item__: Jika fitur yang tersedia tidak lengkap atau tidak relevan, sistem kesulitan memberikan rekomendasi yang akurat.

#### Hasil Top-N Rekomendasi Model Cosine Similiarity

Setelah dibentuk sistem rekomendasi, selanjutnya akan diuji sistem rekomendasi ini untuk menampilkan top 10 rekomendasi berdasarkan Movie yang ditonton/dipilih oleh user. Diperoleh hasil berikut.

__Pilihan User__:
|movieId|title|genres|
|-------|-----|------|
|157114	|Fatty Finn (1980)	|`Children\|Comedy\|Fantasy`|

__Top 10 rekomendasi film berdasarkan pilihan user__:
|title|	genres|
|-----|-------|
|I Downloaded a Ghost (2004)|	`Children\|Comedy\|Fantasy`|
|Nanny McPhee Returns (a.k.a. Nanny McPhee and ...|	`Children\|Comedy\|Fantasy`|
|Elf (2003)|`Children\|Comedy\|Fantasy`|
|Like Mike (2002)|`Children\|Comedy\|Fantasy`|
|Kazaam (1996)|`Children\|Comedy\|Fantasy`|
|Dr. Dolittle: Million Dollar Mutts (2009)|`Children\|Comedy\|Fantasy`|
|Dr. Dolittle: Tail to the Chief (2008)|`Children\|Comedy\|Fantasy`|
|That still Karloson! (2012)|`Children\|Comedy\|Fantasy`|
|Super Xuxa Contra o Baixo Astral (1988)|`Children\|Comedy\|Fantasy`|
|Pufnstuf (1970)|`Children\|Comedy\|Fantasy`|

### 2. Collaborative Filtering - RecomenderNet
Collaborative Filtering adalah pendekatan yang menganalisis pola interaksi antara pengguna dan item untuk menghasilkan rekomendasi. Metode ini bekerja dengan mencari kemiripan dalam perilaku pengguna, baik dalam bentuk penilaian (rating) maupun tindakan lain, seperti pembelian atau klik. Collaborative Filtering dapat dikategorikan menjadi dua jenis utama:
- __User-Based Collaborative Filtering:__
    Metode ini mencari pengguna dengan pola preferensi serupa. Rekomendasi diberikan berdasarkan item yang disukai oleh pengguna lain dengan preferensi mirip. Misalnya, jika dua pengguna menyukai genre film yang sama, film baru yang disukai oleh salah satu pengguna akan direkomendasikan kepada pengguna lainnya.

- __Item-Based Collaborative Filtering:__
    Metode ini menganalisis kemiripan antar-item berdasarkan penilaian atau interaksi pengguna. Item yang sering diberi rating tinggi oleh kelompok pengguna yang sama akan direkomendasikan kepada pengguna lain yang menyukai item tersebut.

Semakin banyak data interaksi yang tersedia, semakin akurat sistem rekomendasi, karena pola kesamaan antar-pengguna atau antar-item menjadi lebih jelas.

#### Cara Kerja RecomenderNet
Model yang akan digunakan pada metode ini bernama RecomenderNet.RecomenderNet adalah model deep learning yang digunakan untuk Collaborative Filtering berbasis neural network. Model ini dirancang untuk mempelajari pola kompleks dari data interaksi pengguna-item. Berikut adalah langkah kerja RecomenderNet:
1. __Input Data:__
    -  Input model terdiri dari pasangan data berupa UserId dan movieId.Kedua ID ini diubah menjadi representasi numerik menggunakan embedding layers, yang menciptakan vektor representasi untuk pengguna dan item.
2. __Embedding:__
    - Embedding layers memetakan setiap pengguna dan item ke dalam ruang vektor berdimensi rendah, di mana hubungan            antar-vektor menunjukkan kemiripan. Representasi ini memudahkan model untuk menangkap hubungan yang tidak linear antara pengguna dan item.
3. __Dense Layers (Fully Connected Layer):__
    - Setelah embedding, vektor pengguna dan item digabungkan lalu diteruskan ke beberapa lapisan fully connected.Lapisan ini belajar mengenali pola interaksi kompleks antara pengguna dan item.
4. __Output:__
    - Model menghasilkan skor prediksi, misalnya nilai rating yang menunjukkan seberapa besar kemungkinan seorang pengguna akan menyukai item tertentu.Skor ini digunakan untuk menyusun rekomendasi bagi pengguna.

Berikut adalah penjelasan dengan kelebihan dan kekurangan RecommenderNet

**Kelebihan:**
- __Efektif dalam Data berskala besar__: RecomenderNet sangat cocok untuk dataset besar, di mana pola preferensi pengguna lebih bervariasi. Dalam dataset besar, model dapat memanfaatkan kekuatan deep learning untuk memberikan rekomendasi yang sangat personal dan relevan.

**Kekurangan:**
- __Tantangan Cold Start__: RecomenderNet kesulitan memberikan rekomendasi untuk pengguna atau item baru yang belum memiliki interaksi sebelumnya. Tanpa data historis, model tidak dapat memprediksi preferensi dengan baik.
 

#### Hasil Top-N Rekomendasi RecommenderNet

=============================================

**Rekomendasi untuk pengguna: 140983**

=============================================

**Movie dengan rating tertinggi dari pengguna**

=============================================
|title|genres|
|-----|------|
|Exorcist, The (1973)  |`Horror\|Mystery`|
|Tropic Thunder (2008) | `Action\|Adventure\|Comedy\|War`|

===========================================================

**Rekomendasi Movies 10 Teratas**

===========================================================
|title|genres|
|-----|------|
|Gone with the Wind (1939)|`Drama\|Romance\|War`|
|39 Steps, The (1935) | `Drama\|Mystery\|Thriller`|
|Stalker (1979) | `Drama\|Mystery\|Sci-Fi`|
|Cool Hand Luke (1967) | `Drama`|
|High Noon (1952) |`Drama\|Western`|
|Joy Luck Club, The (1993) | `Drama\|Romance`|
|Rocky (1976) | `Drama`|
|Stepmom (1998) |`Drama`|
|Risky Business (1983) |`Comedy`|
|Last Unicorn, The (1982) |`Animation\|Children\|Fantasy`|

Berdasarkan hasil tabel di atas model RecommenderNet berhasil merekomendasikan anime dengan rating tertinggi dari pengguna dan merekomendasikan Top-N movies teratas pada Pengguna: 140983.

## Evaluation
Pada tiap metode sistem rekomendasi yang dikerjakan, proyek ini menggunakan 2 metrik evaluasi yaitu _Precision_ dan _RMSE_.Berikut penjabarannya pada tiap metrik evaluasi:
    
### Evaluasi Content Based Filtering - Cosine Simmilarity
Model ini hanya menggunakan metrik Precision untuk mengetahui seberapa baik perforam model tersebut. _Precision_ adalah metrik evaluasi yang digunakan untuk mengukur seberapa relevan item yang direkomendasikan oleh model dibandingkan dengan semua item yang direkomendasikan. Metrik ini dihitung sebagai rasio antara jumlah rekomendasi yang relevan (true positives) dengan total jumlah item yang direkomendasikan. Perhitungan rasio ini dijabarkan melalui rumus di bawah ini:

$$Precision = \frac{TP}{TP + FP}$$

Dimana:

- TP (*True Positive*), jumlah kejadian positif yang diprediksi dengan benar.
- FP (*False Positive*), jumlah kejadian positif yang diprediksi dengan salah.

Hasil dari  Hasil Top-10 Rekomendasi Model Cosine Similiarity untuk film:
|movieId|title|genres|
|-------|-----|------|
|157114	|Fatty Finn (1980)	|`Children\|Comedy\|Fantasy`|

Hasil Rekomendasi:
|title|	genres|
|-----|-------|
|I Downloaded a Ghost (2004)|	`Children\|Comedy\|Fantasy`|
|Nanny McPhee Returns (a.k.a. Nanny McPhee and ...|	`Children\|Comedy\|Fantasy`|
|Elf (2003)|`Children\|Comedy\|Fantasy`|
|Like Mike (2002)|`Children\|Comedy\|Fantasy`|
|Kazaam (1996)|`Children\|Comedy\|Fantasy`|
|Dr. Dolittle: Million Dollar Mutts (2009)|`Children\|Comedy\|Fantasy`|
|Dr. Dolittle: Tail to the Chief (2008)|`Children\|Comedy\|Fantasy`|
|That still Karloson! (2012)|`Children\|Comedy\|Fantasy`|
|Super Xuxa Contra o Baixo Astral (1988)|`Children\|Comedy\|Fantasy`|
|Pufnstuf (1970)|`Children\|Comedy\|Fantasy`|

Berdasarkan rekomendasi movie dengan genre serupa yaitu `Children|Comedy|Fantasy`, diketahui bahwa semua film yang direkomendasikan  memiliki genre serupa. Sehingga presisi sistem rekomendasi berbasis content-based filtering yang telah dibuat berhasil mencapai 10/10 atau 100%.


### Evaluasi Collaborative Filtering - RecommenderNet
Evaluasi metrik yang dapat digunakan untuk mengukur kinerja model ini adalah metrik _RMSE_ (*Root Mean Squared Error*). RMSE adalah metrik yang mengukur seberapa besar perbedaan antara prediksi model dengan nilai aktual dalam dataset. Metrik ini menghitung akar kuadrat dari rata-rata kuadrat kesalahan prediksi. RMSE cocok digunakan untuk mengevaluasi sistem rekomendasi berbasis rating, karena memberikan bobot lebih besar pada kesalahan besar, sehingga membantu mendeteksi apakah model menghasilkan prediksi yang terlalu jauh dari nilai sebenarnya. Nilai RMSE yang lebih rendah menunjukkan performa model yang lebih baik. RMSE dapat dijabarkan melalui pendekatan rumus berikut ini

$$RMSE =  \sqrt{\frac{\sum_{t=1}^{n}(A_t - F_t)^2}{n}}$$

Dimana:

- $A_t$ : Nilai aktual
- $F_t$ : Nilai hasil prediksi
- n: Banyak data

Collaborative Filtering dengan model RecommenderNet memberikan hasil training yang divisualisasikan melalui gambar di bawah ini:

<img src='gambar\evaluasi.png'></img>

Dengan epoch sebanyak 100, model ini memperoleh nilai error akhir sebesar sekitar 0.05 untuk training dan error pada data validasi sebesar 0.27. Nilai tersebut cukup bagus untuk sistem rekomendasi.

Berdasarkan hasil yang didapat pada tahap Model and Result untuk user dengan id 140983 model berhasil merekomendasikan Movie dengan rating tertinggi dari pengguna dan Rekomendasi Top-10 anime teratas untuk user 140983.

## Kesimpulan
Dari hasil evaluasi, penerapan sistem rekomendasi menggunakan Content-Based Filtering dengan Cosine Similarity dan Collaborative Filtering berbasis RecommenderNet telah memenuhi tujuan proyek. Pendekatan Content-Based Filtering berhasil merekomendasikan film secara relevan berdasarkan kesamaan fitur genre dengan tingkat _Precision_ yang tinggi, terutama dalam menyusun rekomendasi Top-10 sesuai kategori. Di sisi lain, pendekatan Collaborative Filtering dengan RecommenderNet menunjukkan performa yang baik dalam memprediksi preferensi pengguna berdasarkan pola rating, dengan tingkat kesalahan prediksi rendah (RMSE sebesar 0.05 pada data pelatihan dan 0.27 pada data validasi). Secara keseluruhan, kedua metode ini mampu memberikan rekomendasi yang akurat dan relevan, sesuai dengan tujuan utama, yaitu  memberikan saran film berdasarkan genre yang relevan dengan preferensi pengguna.