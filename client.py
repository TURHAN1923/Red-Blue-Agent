import requests
import datetime
import os
from risk_planı import calculate_risk, generate_emergency_actions, suggest_security_products

BASE_URL = "http://localhost:5000"

def send_to_red_agent(system_info):
    try:
        response = requests.post(
            f"{BASE_URL}/red",
            json={"system_info": system_info}
        )
        response.raise_for_status()
        return response.json().get("red_team_plan", "")
    except Exception as e:
        print("Red Agent Hatası:", response.text)
        print("Hata Detayı:", e)
        return None

def send_to_blue_agent(system_info, red_plan):
    try:
        response = requests.post(
            f"{BASE_URL}/blue",
            json={
                "system_info": system_info,
                "red_team_plan": red_plan
            }
        )
        response.raise_for_status()
        return response.json().get("blue_team_response", "")
    except Exception as e:
        print(" Blue Agent Hatası:", response.text)
        print(" Hata Detayı:", e)
        return None

def save_report(system_info, risk_label, actions, products, red_response, blue_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_safe_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = "agent_reports"
    os.makedirs(folder, exist_ok=True)

    # === TXT RAPOR ===
    txt_path = os.path.join(folder, f"report_{file_safe_time}.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("=== Red & Blue Agent Güvenlik Raporu ===\n\n")
        f.write(f"Tarih/Saat: {timestamp}\n")
        f.write(f"Sistem Bilgisi: {system_info}\n")
        f.write(f"Risk Seviyesi: {risk_label}\n\n")

        f.write("🚨 Önerilen Acil Eylemler:\n")
        for a in actions:
            f.write(f"- {a}\n")
        f.write("\n Önerilen Güvenlik Ürünleri:\n")
        for p in products:
            f.write(f"- {p}\n")
        f.write("\n Red Agent Planı:\n")
        f.write(red_response + "\n\n")

        if blue_response:
            f.write(" Blue Agent Yanıtı:\n")
            f.write(blue_response + "\n")

    # === HTML RAPOR ===
    html_path = os.path.join(folder, f"report_{file_safe_time}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""<html><head><meta charset="UTF-8"><title>Red & Blue Agent Raporu</title></head><body style="font-family:Arial;">
<h1>Red & Blue Agent Güvenlik Raporu</h1>
<p><b>Tarih:</b> {timestamp}</p>
<p><b>Sistem Bilgisi:</b> {system_info}</p>
<p><b>Risk Seviyesi:</b> {risk_label}</p>

<h2> Önerilen Acil Eylemler</h2>
<ul>""" + "".join(f"<li>{a}</li>" for a in actions) + "</ul>"

+ f"""<h2> Önerilen Güvenlik Ürünleri</h2>
<ul>""" + "".join(f"<li>{p}</li>" for p in products) + "</ul>"

+ f"""<h2> Red Agent Planı</h2>
<pre>{red_response}</pre>"""

+ (f"""<h2> Blue Agent Yanıtı</h2><pre>{blue_response}</pre>""" if blue_response else "")

+ "</body></html>")

    print(f"\n Raporlar kaydedildi: {txt_path}, {html_path}")

if __name__ == "__main__":
    print(" Red & Blue Agent Client\n")

    system_info = input("Sistem bilgilerini girin (örnek: Apache 2.4.49, Ubuntu 18.04, port 80 açık):\n> ")

    risk_label = calculate_risk(system_info)
    print(f"\n [Risk Seviyesi]: {risk_label}")

    actions = generate_emergency_actions(risk_label)
    print("\n [Önerilen Acil Eylemler]:")
    for action in actions:
        print(action)

    products = suggest_security_products(risk_label)
    print("\n [Önerilen Güvenlik Ürünleri]:")
    for product in products:
        print(product)

    print("\n Red Agent'a gönderiliyor...")
    red_response = send_to_red_agent(system_info)

    blue_response = None
    if red_response:
        print("\n Red Agent Planı:\n")
        print(red_response)

        proceed = input("\nBu saldırı planını Blue Agent'a iletmek ister misiniz? (e/h): ").strip().lower()
        if proceed == "e":
            print("\n Blue Agent'a gönderiliyor...")
            blue_response = send_to_blue_agent(system_info, red_response)

            if blue_response:
                print("\n Blue Agent Yanıtı:\n")
                print(blue_response)
            else:
                print("Blue Agent yanıt vermedi.")
        else:
            print("Blue Agent çağrılmadı.")
    else:
        print("Red Agent başarısız oldu.")


    if red_response:
        save_report(system_info, risk_label, actions, products, red_response, blue_response)
