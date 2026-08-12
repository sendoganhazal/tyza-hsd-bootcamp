"""
Amaç:
    - Müşteri ayrılma (churn) tahmini için temel makine öğrenmesi akışını uygulamak
    - Veri ön işleme, öznitelik türetme, train-validation-test ayrımı, model eğitimi ve değerlendirme adımlarını pratik etmek

Veri seti:
    - 150 örnek, müşteri özellikleri (yaş, gelir, abonelik süresi, destek talebi sayısı, şehir, üyelik tipi) ve hedef değişken (churn)

Plan/program:
    1. Veri setinin oluşturulması veya okunması
    2. Veri setinin incelenmesi (şekil, ilk satırlar, hedef değişken dağılımı)
    3. Eksik değer kontrolü ve doldurulması
    4. Yeni öznitelik türetilmesi (Feature Engineering)
    5. Kategorik değişkenlerin dönüştürülmesi (One-Hot Encoding)
    6. Sayısal değişkenlerin ölçeklenmesi (StandardScaler)
    7. Verinin train, validation ve test kümelerine ayrılması (Stratify ile)
    8. Modellerin eğitilmesi (Logistic Regression, KNN ve Decision Tree)
    9. Validation sonuçlarına göre modellerin karşılaştırılması
    10. Seçilen en iyi modelin test verisi üzerinde değerlendirilmesi
    11. Metriklerin ve Confusion Matrix'in yazdırılması
    12. Sonuç değerlendirmesi ve yorumlama

Kurulumlar:
pip install pandas numpy scikit-learn
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 1. Veri setinin oluşturulması
np.random.seed(42)
n_samples = 150

data = {
    'yas': np.random.randint(18, 65, size=n_samples),
    'gelir': np.random.randint(20000, 120000, size=n_samples),
    'abonelik_suresi': np.random.randint(1, 60, size=n_samples),
    'destek_talebi_sayisi': np.random.randint(0, 10, size=n_samples),
    'sehir': np.random.choice(['Istanbul', 'Ankara', 'Izmir', 'Bursa'], size=n_samples),
    'uyelik_tipi': np.random.choice(['Standard', 'Premium', 'VIP'], size=n_samples)
}

df = pd.DataFrame(data)

# Mantıklı bir churn (ayrılma) hedef değişkeni oluşturma (0 = Kalır, 1 = Ayrılır)
churn_prob = (df['destek_talebi_sayisi'] * 0.15) - (df['abonelik_suresi'] * 0.02) + np.random.normal(0, 0.2, n_samples)
df['churn'] = (churn_prob > 0).astype(int)

# 2. Veri setinin incelenmesi
print("--- Veri Seti İncelemesi ---")
print("Veri Seti Şekli (Satır, Sütun):", df.shape)
print("\nİlk 5 Satır:")
print(df.head())
print("\nHedef Değişken (Churn) Dağılımı:")
print(df['churn'].value_counts())

# 3. Eksik değer kontrolü ve doldurulması
# Örnek amaçlı birkaç eksik değer ekleyelim
df.loc[5, 'gelir'] = np.nan
df.loc[12, 'sehir'] = np.nan

print("\n--- Eksik Değer Kontrolü ---")
print(df.isnull().sum())

# Eksik değerleri medyan ve mod ile doldurma
df['gelir'] = df['gelir'].fillna(df['gelir'].median())
df['sehir'] = df['sehir'].fillna(df['sehir'].mode()[0])

# 4. Yeni öznitelik türetilmesi (Feature Engineering)
df['abonelik_yili'] = df['abonelik_suresi'] / 12
df['destek_talebi_var_mi'] = (df['destek_talebi_sayisi'] > 0).astype(int)

print("\nYeni eklenen öznitelikler:")
print(df[['abonelik_suresi', 'abonelik_yili', 'destek_talebi_sayisi', 'destek_talebi_var_mi']].head())

# 5. Kategorik değişkenlerin dönüştürülmesi (One-Hot Encoding)
kategorik_sutunlar = ['sehir', 'uyelik_tipi']
encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded_kategorik = encoder.fit_transform(df[kategorik_sutunlar])
encoded_df = pd.DataFrame(encoded_kategorik, columns=encoder.get_feature_names_out(kategorik_sutunlar))

# Eski kategorik sütunları çıkarıp yenilerini ekleme
df_processed = df.drop(columns=kategorik_sutunlar)
df_processed = pd.concat([df_processed, encoded_df], axis=1)

# Girdi (X) ve Hedef (y) ayrımı
X = df_processed.drop(columns=['churn'])
y = df_processed['churn']

# 6. Verinin train, validation ve test kümelerine ayrılması
# %60 Train, %20 Validation, %20 Test
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42, stratify=y_train_val
)

# 7. Sayısal değişkenlerin ölçeklenmesi
sayisal_sutunlar = ['yas', 'gelir', 'abonelik_suresi', 'destek_talebi_sayisi', 'abonelik_yili']

scaler = StandardScaler()
X_train[sayisal_sutunlar] = scaler.fit_transform(X_train[sayisal_sutunlar])
X_val[sayisal_sutunlar] = scaler.transform(X_val[sayisal_sutunlar])
X_test[sayisal_sutunlar] = scaler.transform(X_test[sayisal_sutunlar])

# 8. Modellerin tanımlanması ve eğitimi
log_reg = LogisticRegression(random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
dt = DecisionTreeClassifier(max_depth=4, random_state=42)

log_reg.fit(X_train, y_train)
knn.fit(X_train, y_train)
dt.fit(X_train, y_train)

# 9. Validation sonuçlarına göre modellerin karşılaştırılması
print("\n--- Validation Performansları ---")

val_preds_log = log_reg.predict(X_val)
val_preds_knn = knn.predict(X_val)
val_preds_dt = dt.predict(X_val)

f1_log = f1_score(y_val, val_preds_log)
f1_knn = f1_score(y_val, val_preds_knn)
f1_dt = f1_score(y_val, val_preds_dt)

print(f"Logistic Regression Validation F1-Score : {f1_log}")
print(f"KNN Validation F1-Score                 : {f1_knn}")
print(f"Decision Tree Validation F1-Score        : {f1_dt}")

# En iyi modeli belirleme
en_iyi_model = log_reg
en_iyi_model_adi = "Logistic Regression"

# 10 & 11. Seçilen en iyi modelin test verisi üzerinde değerlendirilmesi
test_preds = en_iyi_model.predict(X_test)

print(f"\n--- Seçilen En İyi Model ({en_iyi_model_adi}) Test Sonuçları ---")
print("Confusion Matrix:")
print(confusion_matrix(y_test, test_preds))
print(f"Accuracy  : {accuracy_score(y_test, test_preds)}")
print(f"Precision : {precision_score(y_test, test_preds)}")
print(f"Recall    : {recall_score(y_test, test_preds)}")
print(f"F1-Score  : {f1_score(y_test, test_preds)}")

# 12. Çıktılar ve Kod sonu değerlendirme yorumu

# Çıktı
"""
--- Veri Seti İncelemesi ---
Veri Seti Şekli (Satır, Sütun): (150, 7)

İlk 5 Satır:
   yas   gelir  abonelik_suresi  destek_talebi_sayisi     sehir uyelik_tipi  churn
0   56   38141               36                     9  Istanbul     Premium      1
1   46  100356               38                     5     Bursa         VIP      1
2   32   91910               40                     0     Bursa         VIP      0
3   60   76044               20                     3  Istanbul    Standard      1
4   25   87214               35                     9  Istanbul    Standard      1

Hedef Değişken (Churn) Dağılımı:
churn
1    81
0    69
Name: count, dtype: int64

--- Eksik Değer Kontrolü ---
yas                     0
gelir                   1
abonelik_suresi         0
destek_talebi_sayisi    0
sehir                   1
uyelik_tipi             0
churn                   0
dtype: int64

Yeni eklenen öznitelikler:
   abonelik_suresi  abonelik_yili  destek_talebi_sayisi  destek_talebi_var_mi
0               36       3.000000                     9                     1
1               38       3.166667                     5                     1
2               40       3.333333                     0                     0
3               20       1.666667                     3                     1
4               35       2.916667                     9                     1

--- Validation Performansları ---
Logistic Regression Validation F1-Score : 0.875
KNN Validation F1-Score                 : 0.8387096774193549
Decision Tree Validation F1-Score        : 0.8125

--- Seçilen En İyi Model (Logistic Regression) Test Sonuçları ---
Confusion Matrix:
[[10  4]
 [ 0 16]]
Accuracy  : 0.8666666666666667
Precision : 0.8
Recall    : 1.0
F1-Score  : 0.8888888888888888
"""

# Kod sonu değerlendirme yorumu
"""
Validation aşamasında en yüksek F1-Score değerini Logistic Regression modeli vermiştir.

Neden:
    1. Standartlaştırılmış verilerde doğrusal modeller daha dengeli sonuçlar vermektedir.
    2. KNN gibi komşuluk bazlı modeller küçük veri setlerinde gürültüden hızlı etkilenebilir.
    3. Karar ağaçları küçük veri setinde aşırı öğrenmeye (overfitting) meyilli olduğu için genel performansı düşebilir.
"""

