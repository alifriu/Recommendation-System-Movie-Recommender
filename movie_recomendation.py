# -*- coding: utf-8 -*-
"""Movie Recomendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mudXCyk_bT9669KCIHRLO5lwo9xX0acE

# 1. Import Packages
Pada tahap ini, kita mengimpor seluruh library yang diperlukan, seperti numpy, pandas, matplotlib, seaborn.
"""

import kagglehub
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# 2. Data Loading

Dataset yang akan kita gunakan berasal dari kaggle,jadi kita perlu terlebih dahulu mengunduh datasetnya
"""

# Download latest version
path = kagglehub.dataset_download("parasharmanas/movie-recommendation-system")

print("Path to dataset files:", path)

"""file yang sudah kita unduh akan terdiri dari 2 file data yang ada yaitu file movies dan file rating.

Kita perlu baca file yang telah diunduh lalu simpan ke dalam variabel movies dan ratings.
"""

movies = pd.read_csv(path + "/movies.csv")
ratings = pd.read_csv(path + "/ratings.csv")

"""# 3. Data Understanding
Tahap ini merupakan proses analisis data yang bertujuan untuk memahami dataset secara mendalam sebelum melakukan analisis lebih lanjut.

| Jenis    | Keterangan                                                |
|----------|-----------------------------------------------------------|
| Title    | Movie Recommendation System                               |
| Source   |[Kaggle](https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system/data)        |
| Owner    | [MANAS PARASHAR ](https://www.kaggle.com/parasharmanas)                                                  |
| License  | Database: Open Database, Contents: Database Contents      |
| Tags     | Arts and Entertainment, Movies and TV Shows               |
| Usability | 10.00                                                     |

**movies.csv**
 - movieId : ID unik untuk setiap film.
 - title : Judul Tiap Film.
 - genres : Genre FIlm, dipisahkan dengan tanda "|".
"""

movies.head()

"""**ratings.csv**
 - userId : ID unik untuk setiap User.
 - movieId : ID unik untuk setiap film.
 - rating : Penilaian yang diberikan oleh User untuk film yang telah ditonton.
 - timestamp : Waktu ketika User memberikan rating.
"""

ratings.head()

"""## Exploratory Data Analysis

### Deskripsi Variabel
"""

movies.info()

movies.shape

movies.describe().T

ratings.info()

ratings.shape

ratings.describe().T

"""### Cek Missing Value dan Duplicate Value
Pada tahap ini, kita akan mengecek apakah ada baris data yang terdapat missing value dan duplicate value
"""

movies.isnull().sum()

ratings.isnull().sum()

movies.duplicated().sum()

ratings.duplicated().sum()

"""setalah pengecekan, kedua file tidak ditemukan adanya missing value dan duplicate value

### Univariate Analysis
"""

print(f"Jumlah Film yang ada: {movies['title'].nunique()}")
print(f"Jumlah User yang memberi rating: {ratings.userId.nunique()}")

"""Menggabungkan data movies dan data ratings untuk di analisis"""

merged_data = pd.merge(ratings, movies, on='movieId')

# Top 10 movies by average rating
top_movies = merged_data.groupby('title')['rating'].mean().sort_values(ascending=False).head(10)

# Convert to DataFrame for compatibility with Seaborn
top_movies_df = top_movies.reset_index()
top_movies_df.columns = ['Movie Title', 'Average Rating']

# Set Seaborn style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 4))

# Plot horizontal bar chart with Set2 palette
sns.barplot(
    x='Average Rating',
    y='Movie Title',
    data=top_movies_df,
    palette='Set2',  # Use Set2 color palette
    edgecolor='black'
)

# Add title and labels
plt.title('Top 10 Movies by Average Rating', fontsize=14, weight='bold')
plt.xlabel('Average Rating', fontsize=12)
plt.ylabel('Movie Title', fontsize=12)

# Add value labels to each bar
for index, value in enumerate(top_movies_df['Average Rating']):
    plt.text(value + 0.05, index, f'{value:.2f}', va='center', fontsize=10)

# Adjust layout and show plot
plt.tight_layout()
plt.show()

"""Terlihat bahwa 10 film diatas,memiliki rata-rata sebesar 5.0

# Data Preparation

Teknik Data preparation yang dilakukan terdiri dari:
- Data Preprocessing
- TF-IDF Vectorizer Data Movies
- Encoding Data Ratings
- Membagi Data untuk Training dan Validasi

## Data Preprocessing
"""

movies.sample(10)

"""Pada data movies, terdapat beberapa baris yamg memiliki genre `(no genres listed)`."""

movies[movies['genres'] == '(no genres listed)']

"""Karena Kita akan menggunakan sistem rekomendasi berbasis genre film, maka genre `(not genres listed)` akan kita hapus."""

movies = movies[movies['genres'] != '(no genres listed)']

"""Menyamakan genre film"""

final_movies = movies.sort_values('movieId', ascending=True)
final_movies

"""karena data `ratings` sangat banyak dan tidak sepadan dengan sumber daya yang saya miliki oleh karena itu kita akan mengambil beberap puluh ribu saja untuk dijadikan sample."""

ratings = ratings.sample(n=10000, random_state=42)

example_rating = ratings.copy()
example_rating.head()

"""Hapus fitur `timestamp` dari data ratings karena kita hanya menggunakan kolom `userId,movieId,rating` pada tahap pemodelan nanti."""

final_ratings = ratings.drop(columns=['timestamp'])
final_ratings.head()

"""## TF-IDF Vectorizer Data Movies

Karena komputer hanya dapat memproses data numerik, oleh karena itu data genres perlu kita ubah menjadi numerik dengan menggunakan TFidfVectorizer
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada kolom `genres`
tf.fit(final_movies['genres'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()

"""selanjutnya kita lakukan fit dan transform ke dalam bentuk matriks"""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(final_movies['genres'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""matriks yang kita miliki berukuran (57361, 21). Nilai 57361 merupakan ukuran data dan 21 merupakan genres film.

Untuk menghasilkan vektor tf-idf dalam bentuk matriks, kita menggunakan fungsi todense().
"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

"""melihat matriks tf-idf untuk beberapa film dan genrenya"""

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis genre
# Baris diisi dengan title movie

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=final_movies.title
).sample(21, axis=1).sample(10, axis=0)

"""## Encoding Data Ratings

melakukan prosesn encode pada kolom `userId` dan `movieId`
"""

# Mengubah userId menjadi list tanpa nilai yang sama
user_ids = final_ratings['userId'].unique().tolist()

# Melakukan encoding userId
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}

# Melakukan proses encoding angka ke ke userID
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

# Mengubah movieId menjadi list tanpa nilai yang sama
movie_ids = final_ratings['movieId'].unique().tolist()

# Melakukan proses encoding movieId
movie_to_movie_encoded = {x: i for i, x in enumerate(movie_ids)}

# Melakukan proses encoding angka ke movieId
movie_encoded_to_movie = {i: x for i, x in enumerate(movie_ids)}

# Mapping userId ke dataframe user
final_ratings['user'] = final_ratings['userId'].map(user_to_user_encoded)

# Mapping movieId ke dataframe movie
final_ratings['movie'] = final_ratings['movieId'].map(movie_to_movie_encoded)

"""melihat beberapa hal seperti jumlah user,jumlah movie"""

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah movie
num_movie = len(movie_to_movie_encoded)
print(num_movie)

# Mengubah rating menjadi nilai float
final_ratings['rating'] = final_ratings['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(final_ratings['rating'])

# Nilai maksimal rating
max_rating = max(final_ratings['rating'])

print('Number of User: {}, Number of movie: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_movie, min_rating, max_rating
))

"""## Membagi Data untuk Training dan Validasi"""

final_ratings = final_ratings.sample(frac=1, random_state=42)
final_ratings

""" Memerakan data user dan movie lalu melakukan proses scaling dari 0 - 1 untuk mempermudah proses training dan membagi data train dan validasi menjadi 80:20"""

# Membuat variabel x untuk mencocokkan data user dan movie menjadi satu value
x = final_ratings[['user', 'movie']].values

# Membuat variabel y untuk membuat rating dari hasil
y = final_ratings['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * final_ratings.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

"""# Modeling and Result

Pada tahapan model yang digunakan terdiri dari:

- Cosine Similarity
- recomenderNet

## Content Based Filtering - Cosine Similarity

selanjutnya menghitung derajat kesamaan (similarity degree) antar anime dengan teknik cosine similarity. Di sini, kita menggunakan fungsi cosine_similarity dari library sklearn dengan kode berikut.
"""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

"""Pada tahap ini, kita akan menghitung tingkat kesamaan antar film menggunakan matriks *TF-IDF* yang telah dibuat sebelumnya. Dengan satu baris kode, kita dapat memanfaatkan fungsi *cosine similarity* dari pustaka sklearn. Proses ini menghasilkan sebuah matriks kesamaan dalam bentuk array, yang menggambarkan hubungan atau kemiripan antar film berdasarkan fitur yang telah diolah."""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama movie
cosine_sim_df = pd.DataFrame(cosine_sim, index=final_movies['title'], columns=final_movies['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap movie
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Dengan cosine similarity, kita berhasil mengidentifikasi kesamaan antara satu movie dengan movie lainnya.

### Mendapatkan rekomendasi
"""

def movie_recommendations(movie, similarity_data=cosine_sim_df, items=final_movies[['title', 'genres']], k=10):


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,movie].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop movie agar movie yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(movie, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

"""Pada kode tersebut, dengan memanfaatkan fungsi *argpartition*, kita mengambil sejumlah nilai *k* tertinggi dari data kesamaan (dalam hal ini: dataframe `cosine_sim_df`). Selanjutnya, data kesamaan ini diurutkan dari bobot tertinggi ke terendah dan disimpan dalam variabel `closest`. Setelah itu, untuk memastikan hasil rekomendasi tidak menampilkan movie yang sama dengan movie yang dicari, kita menghapus nama movie tersebut dari daftar rekomendasi. Misalnya, jika kita mencari film yang mirip dengan *Fatty Finn (1980)*, maka nama film *Fatty Finn (1980)* akan dihapus dari hasil rekomendasi agar tidak muncul kembali."""

final_movies.sample(1)

"""Kita akan melakukan rekomendasi film yang berjudul *Fatty Finn (1980)* dengan genre `	Children|Comedy|Fantasy`.Tentu kita berharap rekomendasi yang diberikan adalah movie dengan genre yang mirip. Sekarang, kita akan dapatkan  rekomendasi movie dengan memanggil fungsi yang telah kita definisikan sebelumnya:"""

movie_recommendations('Fatty Finn (1980)')

"""Sistem akan memberikan movie dengan genre `Children|Comedy|Fantasy`

## Collaborative Filtering - RecomenderNet

Model ini menghitung skor kecocokan antara pengguna dan film dengan menggunakan teknik *embedding*. Proses ini mencakup pembuatan representasi *embedding* untuk data user dan movie, kemudian melakukan operasi perkalian (*dot product*) antara kedua embedding tersebut. Selain itu, bias untuk setiap pengguna dan film juga dapat ditambahkan ke dalam perhitungan. Skor kecocokan dihasilkan dalam rentang [0,1] dengan memanfaatkan fungsi aktivasi *sigmoid*.

Untuk implementasinya, sebuah kelas bernama `RecommenderNet` dibuat dengan mewarisi kelas Model dari pustaka Keras. Struktur kode kelas ini terinspirasi dari tutorial pada situs resmi Keras, dengan beberapa penyesuaian yang disesuaikan dengan kebutuhan kasus sistem rekomendasi film. Berikut merupakan penerapkan kodenya:
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_movie, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_movie = num_movie
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.movie_embedding = layers.Embedding( # layer embeddings movie
        num_movie,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.movie_bias = layers.Embedding(num_movie, 1) # layer embedding movie bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    movie_vector = self.movie_embedding(inputs[:, 1]) # memanggil layer embedding 3
    movie_bias = self.movie_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_movie = tf.tensordot(user_vector, movie_vector, 2)

    x = dot_user_movie + user_bias + movie_bias

    return tf.nn.sigmoid(x) # activation sigmoid

"""lalu lakukan compile terhadap model dengan *loss function __BinaryCrossentropy__,optimer __Adam__ dan metrik evaluasi __RMSE__*"""

model = RecommenderNet(num_users, num_movie, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""lalukan proses training dengan epoch sebesar 100"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 32,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""**Hasil Top-N Rekomendasi RecommenderNet**

Untuk mendapatkan rekomendasi *movie*, kita akan mengambil sampel pengguna secara acak dan mendefinisikan variabel `movies_not_visited`, yaitu daftar *movie* yang belum pernah ditonton oleh pengguna tersebut. Daftar ini menjadi basis dari rekomendasi yang akan diberikan kepada pengguna.

Sebelumnya, pengguna telah memberikan penilaian pada beberapa *movie* yang pernah mereka tonton. Penilaian ini digunakan untuk membuat rekomendasi *movie* yang sesuai dengan preferensi mereka. Karena rekomendasi hanya akan diberikan untuk *movie* yang belum ditonton, kita perlu membuat variabel `movies_not_visited` sebagai daftar *movie* yang belum pernah diakses oleh pengguna.

Variabel `movies_not_visited` diperoleh dengan menggunakan operator bitwise `~` pada variabel `movies_visited_by_user`. Operator ini membantu kita menentukan *movie* mana yang belum ada dalam daftar *visited*. Berikut adalah kode yang dapat digunakan untuk mengimplementasikan proses ini.
"""

movies_df = final_movies
df = example_rating

# Mengambil sample user
user_id = df.userId.sample(1).iloc[0]
movies_visited_by_user = df[df.userId == user_id]

# Operator bitwise (~), bisa diketahui di sini https://docs.python.org/3/reference/expressions.html
movies_not_visited = movies_df[~movies_df['movieId'].isin(movies_visited_by_user.movieId.values)]['movieId']
movies_not_visited = list(
    set(movies_not_visited)
    .intersection(set(movie_to_movie_encoded.keys()))
)

movies_not_visited = [[movie_to_movie_encoded.get(x)] for x in movies_not_visited]
user_encoder = user_to_user_encoded.get(user_id)
user_movies_array = np.hstack(
    ([[user_encoder]] * len(movies_not_visited), movies_not_visited)
)

ratings = model.predict(user_movies_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_movies_ids = [
    movie_encoded_to_movie.get(movies_not_visited[x][0]) for x in top_ratings_indices
]

print('Rekomendasi untuk pengguna: {}'.format(user_id))
print('===' * 15)
print('Movie dengan rating tertinggi dari pengguna')
print('----' * 15)

top_movies_user = (
    movies_visited_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(5)
    .movieId.values
)

movies_df_rows = movies_df[movies_df['movieId'].isin(top_movies_user)]
for row in movies_df_rows.itertuples():
    print(row.title, ':', row.genres)

print('----' * 15)
print('Rekomendasi Movies 10 Teratas')
print('----' * 15)

recommended_movies = movies_df[movies_df['movieId'].isin(recommended_movies_ids)]
for row in recommended_movies.itertuples():
    print(row.title, ':', row.genres)

"""Berdasarkan hasil di atas adalah rekomendasi untuk user dengan id 140983. Dari output tersebut, kita dapat membandingkan antara movie dengan rating tertinggi dari pengguna dan Rekomendasi 10 movie teratas untuk user.

# Evaluasi Model

## Evaluasi Content Based Filtering - Cosine Simmilarity

Model ini hanya menggunakan metrik Precision untuk mengetahui seberapa baik perforam model tersebut. _Precision_ adalah metrik evaluasi yang digunakan untuk mengukur seberapa relevan item yang direkomendasikan oleh model dibandingkan dengan semua item yang direkomendasikan. Metrik ini dihitung sebagai rasio antara jumlah rekomendasi yang relevan (true positives) dengan total jumlah item yang direkomendasikan. Perhitungan rasio ini dijabarkan melalui rumus di bawah ini:

$$Precision = \frac{TP}{TP + FP}$$

Dimana:

- TP (*True Positive*), jumlah kejadian positif yang diprediksi dengan benar.
- FP (*False Positive*), jumlah kejadian positif yang diprediksi dengan salah.

Berdasarkan rekomendasi movie dengan genre serupa yaitu `Children|Comedy|Fantasy`, diketahui bahwa semua film yang direkomendasikan  memiliki genre serupa. Sehingga presisi sistem rekomendasi berbasis content-based filtering yang telah dibuat berhasil mencapai 10/10 atau 100%.

## Evaluasi Collaborative Filtering - RecommenderNet

Evaluasi metrik yang dapat digunakan untuk mengukur kinerja model ini adalah metrik _RMSE_ (*Root Mean Squared Error*). RMSE adalah metrik yang mengukur seberapa besar perbedaan antara prediksi model dengan nilai aktual dalam dataset. Metrik ini menghitung akar kuadrat dari rata-rata kuadrat kesalahan prediksi. RMSE cocok digunakan untuk mengevaluasi sistem rekomendasi berbasis rating, karena memberikan bobot lebih besar pada kesalahan besar, sehingga membantu mendeteksi apakah model menghasilkan prediksi yang terlalu jauh dari nilai sebenarnya. Nilai RMSE yang lebih rendah menunjukkan performa model yang lebih baik. RMSE dapat dijabarkan melalui pendekatan rumus berikut ini

$$RMSE =  \sqrt{\frac{\sum_{t=1}^{n}(A_t - F_t)^2}{n}}$$
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""Dengan epoch sebanyak 100, model ini memperoleh nilai error akhir sebesar sekitar 0.05 untuk training dan error pada data validasi sebesar 0.27. Nilai tersebut cukup bagus untuk sistem rekomendasi.

Berdasarkan hasil yang didapat pada tahap Model and Result untuk user dengan id 140983 model berhasil merekomendasikan Movie dengan rating tertinggi dari pengguna dan Rekomendasi Top-10 anime teratas untuk user 140983.

# Kesimpulan

Dari hasil evaluasi, penerapan sistem rekomendasi menggunakan Content-Based Filtering dengan Cosine Similarity dan Collaborative Filtering berbasis RecommenderNet telah memenuhi tujuan proyek. Pendekatan Content-Based Filtering berhasil merekomendasikan film secara relevan berdasarkan kesamaan fitur genre dengan tingkat Precision yang tinggi, terutama dalam menyusun rekomendasi Top-10 sesuai genre. Di sisi lain, pendekatan Collaborative Filtering dengan RecommenderNet menunjukkan performa yang baik dalam memprediksi preferensi pengguna berdasarkan pola rating, dengan tingkat kesalahan prediksi rendah (RMSE sebesar 0.05 pada data pelatihan dan 0.27 pada data validasi). Secara keseluruhan, kedua metode ini mampu memberikan rekomendasi yang akurat dan relevan, sesuai dengan tujuan utama, yaitu memberikan saran film berdasarkan genre yang relevan dengan preferensi pengguna.
"""

