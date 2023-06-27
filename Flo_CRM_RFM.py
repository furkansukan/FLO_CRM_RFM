###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

# 1. İş Problemi (Business Problem)
# 2. Veriyi Anlama (Data Understanding)
# 3. Veri Hazırlama (Data Preparation)
# 4. RFM Metriklerinin Hesaplanması (Calculating RFM Metrics)
# 5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
# 6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
# 7. Tüm Sürecin Fonksiyonlaştırılması

###############################################################
# 1. İş Problemi (Business Problem)
###############################################################

# Değişkenler

# master_id Eşsiz müşteri numarası
# order_channel Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile)
# last_order_channel En son alışverişin yapıldığı kanal
# first_order_date Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online Müşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline Müşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


# Adım1: data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.
# Adım2: Veri setinde
# a. İlk 10 gözlem,
# b. Değişken isimleri,
# c. Betimsel istatistik,
# d. Boş değer,
# e. Değişken tipleri, incelemesi yapınız.
# Adım3: Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Her bir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.
# Adım4: Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
# Adım5: Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısının ve toplam harcamaların dağılımına bakınız.
# Adım6: En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
# Adım7: En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
# Adım8: Veri ön hazırlık sürecini fonksiyonlaştırınız.


###############################################################
# 2. Veriyi Anlama (Data Understanding)
###############################################################

import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Adım 1
df_ = pd.read_csv("datasets/flo_data_20k.csv")
df = df_.copy()
df.head()

# Adım 2
def check_df(dataframe):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(5))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)

df["master_id"].nunique()

# Adım 3

df["omni_order"] = df["order_num_total_ever_offline"] + df["order_num_total_ever_online"]
df["total_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
df.head()

# Adım 4

df.dtypes

df = df.astype({'first_order_date': 'datetime64[ns]',
           'last_order_date': 'datetime64[ns]',
           'last_order_date_online': 'datetime64[ns]',
           'last_order_date_offline': 'datetime64[ns]'})

# Adım 5

df.groupby("order_channel").agg({"omni_order": ["sum", "mean", "count"],
                                 "total_value": ["sum", "mean", "count"]

})

# Adım6: En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.head()
df.sort_values("total_value", ascending=False).head(10)

# Adım7: En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.sort_values("omni_order", ascending=False).head(10)

# Adım8: Veri ön hazırlık sürecini fonksiyonlaştırınız.


def data_preparation(dataframe):
    df["omni_order"] = df["order_num_total_ever_offline"] + df["order_num_total_ever_online"]
    df["total_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

    df = df.astype({'first_order_date': 'datetime64[ns]',
                    'last_order_date': 'datetime64[ns]',
                    'last_order_date_online': 'datetime64[ns]',
                    'last_order_date_offline': 'datetime64[ns]'})

    return dataframe



# RFM Metriklerinin Hesaplanması (Calculating RFM Metrics)

df["last_order_date"].max()
# 2021-05-30

today_date = dt.datetime(2021,6,1)



rfm = df.groupby("master_id").agg({"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
                                   "omni_order": lambda omni_order: omni_order,
                                   "total_value": lambda total_value: total_value

})

rfm.columns = ["Recency", "Frequency", "Monetary"]

rfm.describe().T

# RF Skorunun Hesaplanması

# Adım 1: Recency, Frequency ve Monetary metriklerini qcut yardımı ile
# 1-5 arasında skorlara çeviriniz.
# Adım 2: Bu skorları recency_score, frequency_score ve monetary_score olarak kaydediniz


rfm["recency_score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])

# Adım 3: recency_score ve frequency_score’u
# tek bir değişken olarak ifade ediniz ve RF_SCORE olarak kaydediniz.

rfm["RF_SCORE"] = rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str)

# RF Skorunun Segment Olarak Tanımlanması
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)

rfm.groupby("segment").agg({"Recency": "mean",
                            "Frequency": "mean",
                            "Monetary": "mean"

})

df["segment"] = rfm["segment"].values

adim1 = df[(df["segment"].isin(["champions", "loyal_customers"])) & (df["interested_in_categories_12"].str.contains("KADIN", na=False))]

adim1.to_csv("adim1.csv")

adim2 = df[(df["segment"].isin(["new_customers", "about_to_sleep", "cant_loose"])) & (df["interested_in_categories_12"].str.contains("ERKEK", na=False)) & (df["interested_in_categories_12"].str.contains("COCUK", na=False))]

adim2.to_csv("adim2.csv")