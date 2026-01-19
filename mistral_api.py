import requests

def ask_ollama(prompt, model="mistral"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        data = response.json()

        if "response" not in data or not data["response"].strip():
            return "❗ LLM yanıtı boş döndü. Lütfen daha açıklayıcı bir prompt deneyin."

        return data["response"]

    except requests.exceptions.ConnectionError:
        return "AAAAAA Ollama sunucusuna bağlanılamadı. `ollama run mistral` komutu ile modeli başlatın."
    except requests.exceptions.HTTPError as http_err:
        return f"AAAAAA HTTP hatası oluştu: {http_err}"
    except Exception as e:
        return f"AAAAAA Beklenmeyen hata: {str(e)}"
