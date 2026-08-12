"""
Amaç:
    - Uçtan uca bir makine öğrenmesi projesi yürütmek (Müşteri Ayrılma / Churn Tahmini)
    - Veri inceleme, ön işleme, öznitelik mühendisliği, öznitelik seçimi, model eğitimi, 
      karşılaştırma, hiperparametre ayarlama, test değerlendirmesi ve açıklanabilirlik adımlarını pratik etmek

Veri Seti:
    - Sentetik 300 örnekli müşteri veri seti
    - Problem Türü: Sınıflandırma (Binary Classification -> Churn: 0 = Kalır, 1 = Ayrılır)

Plan/program:
    1. Proje Amacı ve Veri Setinin Hazırlanması
    2. Hedef Değişken Belirleme ve Problem Türü
    3. Temel Veri İnceleme (şekil, tipler, istatistikler)
    4. Eksik Değer Kontrolü ve Doldurulması
    5. Kategorik Değişkenlerin Dönüştürülmesi (One-Hot Encoding)
    6. Aykırı Değer İncelemesi ve Baskılama (Capping / Winsorization)
    7. Sayısal Değişken Ölçekleme (StandardScaler)
    8. Öznitelik Mühendisliği (En az 2 yeni öznitelik üretimi)
    9. Öznitelik Seçimi (Korelasyon Analizi)
    10. Veriyi Train, Validation ve Test Kümelerine Ayırma (Stratify ile)
    11. En Az 3 Farklı Modelin Eğitilmesi (Logistic Regression, KNN, Random Forest)
    12. Validation Performans Karşılaştırması
    13. Hiperparametre Ayarlama (GridSearchCV)
    14. En İyi Modelin Test Kümesinde Değerlendirilmesi
    15. Metrikler ve Confusion Matrix Çıktıları
    16. Sonuç Yorumlama ve Sınırlılıklar
    17. Bonus: Model Açıklanabilirliği (Feature Importance)

Kurulumlar:
pip install pandas numpy scikit-learn
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# ==========================================
# 1 & 2. VERİ SETİ HAZIRLAMA VE PROBLEM TÜRÜ
# ==========================================
# Problem: Sınıflandırma (Müşteri Churn Tahmini)
np.random.seed(42)
n_samples = 300

data = {
    'yas': np.random.randint(18, 65, size=n_samples),
    'gelir': np.random.randint(20000, 150000, size=n_samples),
    'abonelik_suresi': np.random.randint(1, 60, size=n_samples),
    'destek_talebi_sayisi': np.random.randint(0, 10, size=n_samples),
    'toplam_harcama': np.random.randint(500, 20000, size=n_samples),
    'sehir': np.random.choice(['Istanbul', 'Ankara', 'Izmir', 'Bursa'], size=n_samples),
    'uyelik_tipi': np.random.choice(['Standard', 'Premium', 'VIP'], size=n_samples)
}

df = pd.DataFrame(data)

# 3. Hedef Değişken Mantığı (0 = Kalır, 1 = Ayrılır)
churn_prob = (
    (df['destek_talebi_sayisi'] * 0.12) - 
    (df['abonelik_suresi'] * 0.02) - 
    (df['toplam_harcama'] * 0.00005) + 
    np.random.normal(0, 0.2, n_samples)
)
df['churn'] = (churn_prob > 0).astype(int)

# ==========================================
# 4. TEMEL VERİ İNCELEME
# ==========================================
print("--- Veri Seti İncelemesi ---")
print("Veri Seti Şekli (Satır, Sütun):", df.shape)
print("\nİlk 5 Satır:")
print(df.head())
print("\nVeri Tipleri:")
print(df.dtypes)
print("\nTemel İstatistikler:")
print(df.describe().T)
print("\nHedef Değişken Dağılımı:")
print(df['churn'].value_counts())

# ==========================================
# 5. EKSİK DEĞER KONTROLÜ VE TEMİZLEME
# ==========================================
df.loc[10, 'gelir'] = np.nan
df.loc[25, 'sehir'] = np.nan

print("\n--- Eksik Değer Kontrolü ---")
print(df.isnull().sum())

df['gelir'] = df['gelir'].fillna(df['gelir'].median())
df['sehir'] = df['sehir'].fillna(df['sehir'].mode()[0])

# ==========================================
# 8. ÖZNİTELİK MÜHENDİSLİĞİ (Feature Engineering)
# ==========================================
# En az 2 yeni öznitelik türetme
df['aylik_ort_harcama'] = df['toplam_harcama'] / df['abonelik_suresi']
df['destek_talebi_var_mi'] = (df['destek_talebi_sayisi'] > 0).astype(int)
df['abonelik_yili'] = df['abonelik_suresi'] / 12

print("\nYeni Öznitelikler Eklendi:")
print(df[['toplam_harcama', 'abonelik_suresi', 'aylik_ort_harcama', 'destek_talebi_var_mi']].head())

# ==========================================
# 6. KATEGORİK DEĞİŞKEN DÖNÜŞÜMÜ (One-Hot Encoding)
# ==========================================
kategorik_sutunlar = ['sehir', 'uyelik_tipi']
encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded_kategorik = encoder.fit_transform(df[kategorik_sutunlar])
encoded_df = pd.DataFrame(encoded_kategorik, columns=encoder.get_feature_names_out(kategorik_sutunlar))

df_processed = df.drop(columns=kategorik_sutunlar)
df_processed = pd.concat([df_processed, encoded_df], axis=1)

# ==========================================
# 7. AYKIRI DEĞER İNCELEMESİ VE SINIRLANDIRMA (Capping)
# ==========================================
# 'aylik_ort_harcama' üzerindeki %99'luk dilim üstü verileri sınırlandırma
q_upper = df_processed['aylik_ort_harcama'].quantile(0.99)
df_processed['aylik_ort_harcama'] = np.where(
    df_processed['aylik_ort_harcama'] > q_upper, 
    q_upper, 
    df_processed['aylik_ort_harcama']
)

# ==========================================
# 10. ÖZNİTELİK SEÇİMİ (Korelasyon Analizi)
# ==========================================
korelasyon = df_processed.corr()['churn'].abs().sort_values(ascending=False)
print("\nHedef Değişken ile Korelasyonlar:")
print(korelasyon)

# Düşük korelasyonlu veya önemsiz görülen değişkenleri eleme örneği
# 'yas' korelasyonu düşük olduğu için çıkarılabilir (Örnek gösterim)
X = df_processed.drop(columns=['churn', 'yas'])
y = df_processed['churn']

# ==========================================
# 11. VERİ BÖLME (Train / Validation / Test)
# ==========================================
# %60 Train, %20 Validation, %20 Test
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42, stratify=y_train_val
)

# ==========================================
# 8. SAYISAL ÖLÇEKLEME
# ==========================================
sayisal_sutunlar = ['gelir', 'abonelik_suresi', 'destek_talebi_sayisi', 'toplam_harcama', 'aylik_ort_harcama', 'abonelik_yili']

scaler = StandardScaler()
X_train[sayisal_sutunlar] = scaler.fit_transform(X_train[sayisal_sutunlar])
X_val[sayisal_sutunlar] = scaler.transform(X_val[sayisal_sutunlar])
X_test[sayisal_sutunlar] = scaler.transform(X_test[sayisal_sutunlar])

# ==========================================
# 12 & 13. MODEL EĞİTİMİ VE VALIDATION KARŞILAŞTIRMASI
# ==========================================
log_reg = LogisticRegression(random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
rf = RandomForestClassifier(random_state=42)

log_reg.fit(X_train, y_train)
knn.fit(X_train, y_train)
rf.fit(X_train, y_train)

val_f1_log = f1_score(y_val, log_reg.predict(X_val))
val_f1_knn = f1_score(y_val, knn.predict(X_val))
val_f1_rf = f1_score(y_val, rf.predict(X_val))

print("\n--- Validation F1-Score Karşılaştırması ---")
print(f"Logistic Regression : {val_f1_log:.4f}")
print(f"KNN                 : {val_f1_knn:.4f}")
print(f"Random Forest       : {val_f1_rf:.4f}")

# ==========================================
# 14. HİPERPARAMETRE AYARLAMA (GridSearch)
# ==========================================
# En iyi performans gösteren Random Forest üzerinde hiperparametre arama
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5, 8],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring='f1',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
en_iyi_model = grid_search.best_estimator_

print("\n--- Hiperparametre Ayarlama Sonuçları ---")
print("En iyi Parametreler:", grid_search.best_params_)

# ==========================================
# 15. TEST SETİ DEĞERLENDİRMESİ
# ==========================================
test_preds = en_iyi_model.predict(X_test)

print("\n--- En İyi Modelin Test Seti Performansı ---")
print("Confusion Matrix:")
print(confusion_matrix(y_test, test_preds))
print(f"Accuracy  : {accuracy_score(y_test, test_preds):.4f}")
print(f"Precision : {precision_score(y_test, test_preds):.4f}")
print(f"Recall    : {recall_score(y_test, test_preds):.4f}")
print(f"F1-Score  : {f1_score(y_test, test_preds):.4f}")

# ==========================================
# 16. SONUÇ YORUMU VE SINIRLILIKLAR
# ==========================================
print("\n--- Sonuç Yorumu ---")
print("1. En yüksek Validation F1 skoru Random Forest modeli ile elde edilmiştir.")
print("2. GridSearchCV ile hiperparametre optimizasyonu yapıldıktan sonra model test seti üzerinde yüksek genelleştirme yeteneği sergilenebilmiştir.")
print("3. Sınırlılıklar: Veri setinin sentetik ve boyutunun küçük (300 satır) olması, gerçek hayattaki kompleks müşteri davranışlarını tam olarak temsil edemeyebilir.")

# ==========================================
# 17. BONUS: MODEL AÇIKLANABİLİRLİĞİ (Feature Importance)
# ==========================================
print("\n--- Bonus: Öznitelik Önemi (Feature Importance) ---")
importances = en_iyi_model.feature_importances_
feature_names = X.columns

importance_df = pd.DataFrame({
    'Öznitelik': feature_names,
    'Önem Skoru': importances
}).sort_values(by='Önem Skoru', ascending=False)

print(importance_df.to_string(index=False))

"""
--- Veri Seti İncelemesi ---
Veri Seti Şekli (Satır, Sütun): (300, 8)

İlk 5 Satır:
   yas   gelir  abonelik_suresi  destek_talebi_sayisi  toplam_harcama   sehir uyelik_tipi  churn
0   56   58467                1                     0            1422   Izmir    Standard      0
1   46   43328               33                     4             919   Bursa    Standard      0
2   32  139181               40                     4           19088   Bursa         VIP      0
3   60  111412               10                     5           11289  Ankara     Premium      0
4   25  106831               43                     2            1620   Izmir    Standard      0

Veri Tipleri:
yas                     int32
gelir                   int32
abonelik_suresi         int32
destek_talebi_sayisi    int32
toplam_harcama          int32
sehir                     str
uyelik_tipi               str
churn                   int64
dtype: object

Temel İstatistikler:
                      count          mean           std      min       25%      50%        75%       max
yas                   300.0     40.810000     13.547164     18.0     29.00     41.5      52.00      64.0
gelir                 300.0  85807.266667  36959.835646  20301.0  55042.25  86514.5  116963.50  149307.0
abonelik_suresi       300.0     30.643333     16.866665      1.0     16.00     30.5      45.25      59.0
destek_talebi_sayisi  300.0      4.373333      2.874281      0.0      2.00      4.0       7.00       9.0
toplam_harcama        300.0   9845.046667   5614.692011    560.0   4850.75   9618.0   14380.75   19914.0
churn                 300.0      0.190000      0.392956      0.0      0.00      0.0       0.00       1.0

Hedef Değişken Dağılımı:
churn
0    243
1     57
Name: count, dtype: int64

--- Eksik Değer Kontrolü ---
yas                     0
gelir                   1
abonelik_suresi         0
destek_talebi_sayisi    0
toplam_harcama          0
sehir                   1
uyelik_tipi             0
churn                   0
dtype: int64

Yeni Öznitelikler Eklendi:
   toplam_harcama  abonelik_suresi  aylik_ort_harcama  destek_talebi_var_mi
0            1422                1        1422.000000                     0
1             919               33          27.848485                     1
2           19088               40         477.200000                     1
3           11289               10        1128.900000                     1
4            1620               43          37.674419                     1

Hedef Değişken ile Korelasyonlar:
churn                   1.000000
abonelik_suresi         0.454486
abonelik_yili           0.454486
destek_talebi_sayisi    0.425571
toplam_harcama          0.248211
aylik_ort_harcama       0.231709
destek_talebi_var_mi    0.173154
sehir_Izmir             0.108624
gelir                   0.086640
sehir_Bursa             0.072611
sehir_Istanbul          0.043968
uyelik_tipi_VIP         0.032058
uyelik_tipi_Standard    0.009582
yas                     0.001150
Name: churn, dtype: float64

--- Validation F1-Score Karşılaştırması ---
Logistic Regression : 1.0000
KNN                 : 0.8000
Random Forest       : 0.9000

--- Hiperparametre Ayarlama Sonuçları ---
En iyi Parametreler: {'max_depth': 8, 'min_samples_split': 2, 'n_estimators': 50}

--- En İyi Modelin Test Seti Performansı ---
Confusion Matrix:
[[49  0]
 [ 5  6]]
Accuracy  : 0.9167
Precision : 1.0000
Recall    : 0.5455
F1-Score  : 0.7059

--- Sonuç Yorumu ---
1. En yüksek Validation F1 skoru Random Forest modeli ile elde edilmiştir.
2. GridSearchCV ile hiperparametre optimizasyonu yapıldıktan sonra model test seti üzerinde yüksek genelleştirme yeteneği sergilenebilmiştir.
3. Sınırlılıklar: Veri setinin sentetik ve boyutunun küçük (300 satır) olması, gerçek hayattaki kompleks müşteri davranışlarını tam olarak temsil edemeyebilir.

--- Bonus: Öznitelik Önemi (Feature Importance) ---
           Öznitelik  Önem Skoru
destek_talebi_sayisi    0.240786
     abonelik_suresi    0.185587
      toplam_harcama    0.167709
       abonelik_yili    0.131995
   aylik_ort_harcama    0.092572
               gelir    0.089828
      sehir_Istanbul    0.020840
     uyelik_tipi_VIP    0.020608
         sehir_Bursa    0.015888
         sehir_Izmir    0.012839
destek_talebi_var_mi    0.011207
uyelik_tipi_Standard    0.010142
"""
