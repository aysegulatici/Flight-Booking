# Flight Booking System (OOP)

Bu proje, Nesne Yönelimli Programlama (OOP) prensipleri ve SOLID ilkeleri (özellikle Open/Closed ve Dependency Inversion) gözetilerek Python ile geliştirilmiş bir Uçuş Rezervasyon Sistemi simülasyonudur.

## Öne Çıkan Özellikler

* Uçuş Arama (FlightSearch): Kalkış, varış noktası ve tarihe göre dinamik uçuş sorgulama.
* Esnek Ödeme Altyapısı (Payment): Kredi Kartı, Havale/EFT ve Nakit ödeme yöntemlerinin polimorfizm (polymorphism) kullanılarak soyutlanması.
* Çoklu Bildirim Desteği (Notification): E-posta ve SMS gibi farklı kanallar üzerinden esnek bildirim gönderimi.
* Rezervasyon Yönetimi (Booking): Koltuk kapasite kontrolü, rezervasyon onaylama ve iptal süreçlerinin yönetimi.
* Merkezi Loglama (Logger): Sistem hareketlerinin zaman damgalı olarak takip edilmesi.

## Kullanılan Teknolojiler ve Prensipler

* Dil: Python 3.x
* Konseptler: OOP, Soyut Sınıflar (Abstract Classes), Polimorfizm (Polymorphism)
* Tasarım İlkeleri: SOLID (Open/Closed Principle, Dependency Inversion Principle)

## Nasıl Çalıştırılır?

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```bash
python main.py