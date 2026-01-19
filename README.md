![](assets/a.png)

🔴🔵 Red Agent – Blue Agent
LLM Tabanlı Otomatik Siber Güvenlik Analiz Sistemi

Bu proje, Red Team ve Blue Team yaklaşımını temel alan, yapay zeka tabanlı otomatik bir siber güvenlik analiz sistemi geliştirmeyi amaçlamaktadır.

Sistem; kullanıcıdan alınan sistem bilgilerine dayanarak:

Red Agent ile olası saldırı yollarını analiz eder,

Blue Agent ile savunma stratejileri üretir,

Sonuçları .txt ve .html formatlarında detaylı raporlar halinde sunar.

Tüm karar ve analiz süreçleri, Mistral 7B Instruct ve LLaMA 3 Instruct büyük dil modelleri kullanılarak gerçekleştirilir.

🎯 Proje Amacı

Yapay zeka destekli otomatik siber güvenlik analiz sistemi geliştirmek

Red Agent ile saldırı vektörleri ve sızma planlarını üretmek

Blue Agent ile savunma önlemleri ve güvenlik stratejileri oluşturmak

Risk seviyesini otomatik belirleyerek uygun acil eylem adımları önermek

Analiz sonuçlarını .txt ve .html formatlarında raporlamak

🧩 Sistem Tasarımı

Sistem, istemci–sunucu mimarisiyle yapılandırılmıştır ve tüm işlemler yerel olarak yürütülür.

Temel Bileşenler

İstemci (CLI):
Kullanıcıdan sistem bilgisi alır, analiz sürecini adım adım gösterir ve raporları kaydeder.

Sunucu (Flask):
Red Agent ve Blue Agent için ayrı endpoint’ler üzerinden istekleri yönetir.

Red Agent (Mistral 7B):
Saldırı planı ve zafiyet analizleri üretir.

Blue Agent (LLaMA 3):
Savunma stratejileri ve önleyici tedbirler oluşturur.

Raporlama Modülü:
Tüm çıktıları .txt ve .html formatında saklar.

🔴 Red Agent (Saldırgan)

Amaç:

Sistemdeki zafiyetleri belirlemek

Kullanılabilecek saldırı tekniklerini listelemek

Adım adım sızma planı oluşturmak

Kullanılan Model:

Mistral 7B Instruct

Hızlı ve hafif yapı

Teknik analizlerde yüksek performans

Prompta saldırgan rolü verilmiştir

🔵 Blue Agent (Savunmacı)

Amaç:

Sistemdeki zayıflıklara karşı savunma önlemleri önermek

Kritik yapıların korunması için araçlar ve politikalar sunmak

Kullanılan Model:

LLaMA 3 8B Instruct

Güçlü bağlam anlama yeteneği

Detaylı çözüm ve strateji üretimi

Prompta güvenlik danışmanı rolü verilmiştir

🧠 Kullanılan Modeller
Model	Kullanım Amacı
Mistral-7B-Instruct	Red Agent – saldırı analizi
LLaMA 3 8B Instruct	Blue Agent – savunma stratejileri

Modeller Ollama üzerinden yerel olarak çalıştırılmıştır.

⚙️ Kullanılan Teknolojiler

Python 3.10+

Flask (sunucu altyapısı)

Ollama (yerel LLM çalıştırma)

HTML & TXT (rapor formatları)

requests, json, datetime, os

🧪 Raporlama Sistemi

Sistem, analiz sonucunda iki ayrı formatta çıktı üretir:

.txt raporu

.html raporu

Her rapor şu bilgileri içerir:

Sistem bilgisi

Risk seviyesi

Acil eylem planı

Önerilen güvenlik ürünleri

Red Agent ve Blue Agent çıktıları

## 📁 Proje Klasör Yapısı

```text
Red-Blue-Agent/
├── agents/
│   ├── red_agent.py
│   └── blue_agent.py
│
├── server/
│   └── app.py
│
├── reports/
│   ├── report.txt
│   └── report.html
│
├── assets/
│   ├── system_design.png
│   └── sample_report.png
│
├── requirements.txt
└── README.md
```



🚀 Geliştirme Süreci

Gereksinim analizi ve sistem tasarımı yapıldı

Flask tabanlı sunucu geliştirildi

Red Agent ve Blue Agent için ayrı prompt yapıları oluşturuldu

LLM çıktıları raporlama sistemine entegre edildi

Senaryo bazlı testlerle sistem doğrulandı
