# FLO_CRM_RFM
Customer_Segmentation_with_RFM

![image](https://github.com/furkansukan/FLO_CRM_RFM/assets/115731123/deb95a72-3ae5-4e28-bf4b-3819b2fbb567)


###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

1. İş Problemi (Business Problem)
2. Veriyi Anlama (Data Understanding)
3. Veri Hazırlama (Data Preparation)
4. RFM Metriklerinin Hesaplanması (Calculating RFM Metrics)
5. RFM Skorlarının Hesaplanması (Calculating RFM Scores)
6. RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments)
7. Tüm Sürecin Fonksiyonlaştırılması

###############################################################
# 1. İş Problemi (Business Problem)
###############################################################

# Değişkenler

master_id Eşsiz müşteri numarası

order_channel Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile)

last_order_channel En son alışverişin yapıldığı kanal

first_order_date Müşterinin yaptığı ilk alışveriş tarihi

last_order_date Müşterinin yaptığı son alışveriş tarihi

last_order_date_online Müşterinin online platformda yaptığı son alışveriş tarihi

last_order_date_offline Müşterinin offline platformda yaptığı son alışveriş tarihi

order_num_total_ever_online Müşterinin online platformda yaptığı toplam alışveriş sayısı

order_num_total_ever_offline Müşterinin offline'da yaptığı toplam alışveriş sayısı

customer_value_total_ever_offline Müşterinin offline alışverişlerinde ödediği toplam ücret

customer_value_total_ever_online Müşterinin online alışverişlerinde ödediği toplam ücret

interested_in_categories_12 Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


Adım1: data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.

Adım2: Veri setinde

a. İlk 10 gözlem,
b. Değişken isimleri,
c. Betimsel istatistik,
d. Boş değer,
e. Değişken tipleri, incelemesi yapınız.

Adım3: Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Her bir müşterinin toplam
alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

Adım4: Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

Adım5: Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısının ve toplam harcamaların dağılımına bakınız.

Adım6: En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

Adım7: En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

Adım8: Veri ön hazırlık sürecini fonksiyonlaştırınız.
