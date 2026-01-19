import requests
def calculate_risk(system_info):
    system_info = system_info.lower()
    high_risk_keywords = ["sql", "injection", "brute force", "xss", "open port", "port açık", "ftp", "ssh", "truva", "zayıf parola"]
    medium_risk_keywords = ["zayıf şifre", "ssl yok", "güncel değil"]

    for keyword in high_risk_keywords:
        if keyword in system_info:
            return "High Risk"

    for keyword in medium_risk_keywords:
        if keyword in system_info:
            return "Medium Risk"

    return "Low Risk"

def generate_emergency_actions(risk_level):
    if risk_level == "High Risk":
        return [
            "1. Açık portları acilen kapatın veya güvenli hale getirin.",
            "2. Şifreleme ve güvenlik protokollerini uygulayın (SSL, VPN vb.).",
            "3. Hızlı bir sızma testi (penetration test) yaptırın."
        ]
    elif risk_level == "Medium Risk":
        return [
            "1. Şifre politikalarını güçlendirin.",
            "2. SSL sertifikalarını kontrol edin.",
            "3. Sistem güncellemelerini uygulayın."
        ]
    else:
        return [
            "1. Mevcut güvenlik önlemlerini sürdürün.",
            "2. Periyodik güvenlik taramaları yapın.",
            "3. Çalışanlara temel siber güvenlik eğitimi verin."
        ]

def suggest_security_products(risk_level):
    if risk_level == "High Risk":
        return [
            "1. WAF (AWS WAF, Cloudflare)",
            "2. IDS/IPS (Snort, Suricata)",
            "3. Parola yöneticisi (Bitwarden, LastPass)",
            "4. MFA araçları"
        ]
    elif risk_level == "Medium Risk":
        return [
            "1. Antivirüs yazılımı (Kaspersky, ESET)",
            "2. Güncelleme yönetimi",
            "3. Şifre karma kontrol araçları"
        ]
    else:
        return [
            "1. Güvenlik farkındalık eğitimi",
            "2. Log takip yazılımları (ELK Stack)",
            "3. Güvenli yedekleme çözümleri"
        ]
