# -*- coding: utf-8 -*-
"""Indonesia-Death-Cause-Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LpdPj0Re6Rc30NrjWIladIeZ5O3CMgcx

# **Analisis data penyebab kematian yang ada di Indonesia**
"""

df2 = pd.DataFrame(
{
"NAMA" : [ "Rezki Fauzi FIrmansyah","Egy Maretiano","AFRIANDI", "Galang MAulana", "I Wayan Bayu Arya Wiguna"],
"NIM" : ["21.11.3974", "21.11.4009", "21.11.4018", "21.11.4019", "21.11.4092"],
}
)

df2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error, mean_absolute_error
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/content/sample_data/Penyebab Kematian di Indonesia yang Dilaporkan - Raw.csv", header = 0, index_col = 0)
df.info()

"""# **EDA dan Visualisasi Data**"""

df.head()

top_causes = df.groupby("Cause")["Total Deaths"].sum().nlargest(10)
print(top_causes)

df.describe()

df.isnull().sum()

#Mencari penyebab kematian yg masih ada di 2021
cause_23 = data.query("Year==2021")
print(cause_23['Cause'])

# Menampilkan distribusi frekuensi menggunakan histogram
plt.figure(figsize=(10, 6))
df["Total Deaths"].plot(kind="hist", bins=10, edgecolor="black")
plt.xlabel("Total Deaths")
plt.ylabel("Frequency")
plt.title("Distribution of Total Deaths")
plt.show()

# Menampilkan grafik batang untuk 10 penyebab kematian teratas
plt.figure(figsize=(12, 6))
top_causes.plot(kind="bar")
plt.xlabel("Cause")
plt.ylabel("Total Deaths")
plt.title("Top 10 Causes of Death in Indonesia")
plt.xticks(rotation=45)
plt.show()

# Menampilkan korelasi antara variabel numerik menggunakan heatmap
numeric_columns = ['Total Deaths', 'Year']
correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

#Analisis tren kematian akibat gempa bumi
earth_quake = data.query("Cause=='Gempa Bumi'")
earth_quake

cause_counts = data['Cause'].value_counts()
top_causes = cause_counts.head(10)

plt.figure(figsize=(10, 6))
plt.pie(top_causes , labels=top_causes.index, autopct='%1.1f%%')
plt.title('Top 10 Causes of Death in Indonesia')
plt.show()

# Menampilkan boxplot penyebab kematian
plt.figure(figsize=(25, 6))
sns.boxplot(data=data, x='Cause', y='Total Deaths')
plt.title('Boxplot of Total Deaths by Cause')
plt.xlabel('Cause')
plt.ylabel('Total Deaths')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

X = df[['Total Deaths']]
Y = df[['Year']]

# Membuat scatter plot
plt.scatter(X, Y)

# Memberikan label sumbu x dan y
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Memberikan judul plot
plt.title('Scatter Plot')

# Menampilkan plot
plt.show()

"""# **Korelasi Data**"""

# Memilih subset kolom yang akan digunakan untuk korelasi
selected_columns = ['Total Deaths', 'Cause']

# Membuat subset DataFrame dengan kolom yang dipilih
subset_df = data[selected_columns]

# Menghitung matriks korelasi
correlation_matrix = subset_df.corr()

# Menampilkan heatmap korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Korelasi Heatmap')
plt.show()

# Menampilkan scatter plot untuk memvisualisasikan korelasi
sns.pairplot(subset_df)
plt.show()

# Menghitung rata-rata Total Kematian
mean_Total_Kematian = data['Total Deaths'].mean()
# Menghitung rata-rata Pengeluaran

mean_Data_Redundancy = data['Year'].mean()

print("Rata-rata Total_Kematian:", mean_Total_Kematian)

print("Rata-rata Data_Redundancy:", mean_Data_Redundancy)

corr, _= pearsonr(data['Total Deaths'],data ['Year'])
corr

# Mengambil 5 korelasi teratas
top_5_correlations = correlation_matrix.unstack().sort_values(ascending=False)[:5]

# Menampilkan 5 korelasi teratas
print(top_5_correlations)

correlation2 = df["Total Deaths"].corr(df["Year"])
print("Korelasi antara Total Deaths dan Year:", correlation2)

correlation7 = df["Year"].corr(df["Total Deaths"])
print("Korelasi antara Year dan Total Deaths:", correlation7)



"""# **Visualisasi hasil prediksi model Regresi**"""

X = df[['Total Deaths']]
Y = df[['Year']]

# splitting the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# checking the shapes
print('Shape of x_train:', x_train.shape)
print('Shape of y_train:', y_train.shape)
print('Shape of x_test:', x_test.shape)
print('Shape of y_test:', y_test.shape)

# import regressor from sklearn
from sklearn.linear_model import LinearRegression

# call the regressor
reg = LinearRegression()

# fit the regression to the training data
reg = reg.fit(x_train, y_train)

# fit the regression to the training data
y_pred = reg.predict(x_test)

x_test[:2]

df.corr()

"""# **Evaluasi model dengan menggunakan RMSE & MSE**"""

#melakukan evaluasi model regresi dengan MSE dan RMSE, serta melakukan visualisasi perbandingan antara nilai sebenarnya dan nilai prediksi pada data pengujian.
mse = mean_squared_error(y_test, y_pred)
print('Mean absolute error of testing set:', mse)
rmse = np.sqrt(mse)
print('Mean absolute error of testing set:', rmse)

plt.scatter(x_test, y_test, c = 'green')
plt.scatter(x_test, y_pred, c = 'red')
plt.xlabel('nilai x')
plt.xlabel('nilai y')
plt.title("true value vs prediced value : Linear Regresson")
plt.show()

"""# **Model Regresi linier**"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Contoh data sintetis
data = {
    'tahun': np.arange(2000, 2021),
    'kematian': [50, 60, 70, 80, 90, 110, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Variabel independen (fitur)
x = df['tahun'].values.reshape(-1, 1)

# Variabel dependen (target)
y = df['kematian'].values

# Membagi data menjadi data pelatihan dan data pengujian
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Membangun model regresi linier
model = LinearRegression()
model.fit(x_train, y_train)

# Prediksi nilai berdasarkan model
y_pred = model.predict(x_test)

# Evaluasi model menggunakan MSE dan R-squared
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

# Menampilkan hasil evaluasi
print("Mean Squared Error (MSE):", mse)
print("R-squared:", r_squared)

# Visualisasi data dan model regresi linier
plt.scatter(x, y, c='blue', label='Data')
plt.plot(x_test, y_pred, c='red', label='Model Regresi Linier')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Kematian')
plt.title('Model Regresi Linier Penyebab Kematian di Indonesia')
plt.legend()
plt.show()

"""# **Mengevaluasi model regresi linear pada data penyebab kematian di Indonesia**"""

# Variabel independen (fitur)
x = df['tahun'].values.reshape(-1, 1)

# Variabel dependen (target)
y = df['kematian'].values

# Membagi data menjadi data pelatihan dan data pengujian (opsional)
# Jika menggunakan seluruh data sebagai pelatihan, lewati langkah ini
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Membangun model regresi linier
model = LinearRegression()
model.fit(x_train, y_train)

# Prediksi nilai berdasarkan model
y_pred = model.predict(x_test)

# Evaluasi model menggunakan MSE dan R-squared
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r_squared = r2_score(y_test, y_pred)

# Menampilkan hasil evaluasi
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared:", r_squared)