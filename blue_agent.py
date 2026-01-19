from llama3_api import ask_ollama

def blue_team_defense(system_info, red_team_summary=None):
    prompt = f"""
    Sen bir Blue Team siber güvenlik uzmanısın.
    CEVAP VERİRKEN TÜRKÇE YAZ.
    Aşağıdaki sistem bilgilerini değerlendir ve bu sisteme yönelik olası saldırılara karşı alınması gereken savunma önlemlerini detaylandır.

    Sistem Bilgileri:
    {system_info}

    """
    if red_team_summary:
        prompt += f"\nAyrıca, Red Team'in önerdiği saldırı planı şu şekilde:\n{red_team_summary}\n\nBu plana karşı nasıl savunma yapılmalı?"

    prompt += "\n1. Güvenlik açıkları nasıl kapatılmalı?\n2. Hangi savunma araçları kullanılmalı?\n3. Loglama, IDS, firewall vb. konfigürasyonları ne olmalı?\n4. Sistem nasıl sağlamlaştırılır?"

    return ask_ollama(prompt, model="llama3")
