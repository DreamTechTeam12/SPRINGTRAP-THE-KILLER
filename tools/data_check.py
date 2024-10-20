import os
import time
import sys
from tqdm import tqdm

def clear_console():
    """Ekranı temizler. Windows veya Linux için uygun komutu kullanır."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_data_leak(directory, keywords, file_extensions):
    leaked_files = []
    error_logs = []
    total_files = 0
    start_time = time.time()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                total_files += 1

    for root, dirs, files in os.walk(directory):
        for file in tqdm(files, desc="Tarama İşlemi", unit="dosya", total=total_files):
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        found_keywords = [keyword for keyword in keywords if keyword.lower() in content.lower()]
                        if found_keywords:
                            leaked_files.append((file_path, found_keywords))
                except Exception as e:
                    error_logs.append(f"Hata: {file_path} okunurken hata: {e}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    return leaked_files, error_logs, total_files, elapsed_time

def generate_report(leaked_files, error_logs, total_files, elapsed_time):
    with open('leak_report.txt', 'w') as report:
        report.write("Veri Sızıntısı Raporu\n")
        report.write("====================\n\n")
        report.write(f"Tarama Süresi: {elapsed_time:.2f} saniye\n")
        report.write(f"Toplam Dosya Sayısı: {total_files}\n\n")

        if leaked_files:
            report.write("Sızdırılan Dosyalar:\n")
            for leak, found_keywords in leaked_files:
                report.write(f"{leak} - Bulunan Anahtar Kelimeler: {', '.join(found_keywords)}\n")
        else:
            report.write("Sızdırılan dosya bulunamadı.\n")
        
        report.write("\nHata Kayıtları:\n")
        if error_logs:
            for error in error_logs:
                report.write(f"{error}\n")
        else:
            report.write("Hiçbir hata kaydı yok.\n")

def validate_input(directory, keywords):
    if not os.path.isdir(directory):
        raise ValueError("Geçersiz dizin: " + directory)
    if not keywords:
        raise ValueError("Anahtar kelimeler boş olamaz.")

if __name__ == "__main__":
    clear_console()

    print("""
  _____        _           _____ _               _             
 |  __ \      | |         / ____| |             | |            
 | |  | | __ _| |_ __ _  | |    | |__   ___  ___| | _____ _ __ 
 | |  | |/ _` | __/ _` | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| | (_| | || (_| | | |____| | | |  __/ (__|   <  __/ |   
 |_____/ \__,_|\__\__,_|  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                               
                                       By dreamtech.dev                        
    """)

    while True:
        dir_to_check = input("Sızdırılma kontrolü yapılacak dizin: ")
        keywords_to_check = input("Anahtar kelimeleri virgülle ayırarak girin: ").split(',')
        file_extensions_to_check = input("Kontrol edilecek dosya uzantılarını virgülle ayırarak girin (örn. .txt,.log): ").split(',')

        try:
            validate_input(dir_to_check, keywords_to_check)
            
            keywords_to_check = [keyword.strip() for keyword in keywords_to_check]
            file_extensions_to_check = [ext.strip() for ext in file_extensions_to_check]
            
            leaks, errors, total_files, elapsed_time = check_data_leak(dir_to_check, keywords_to_check, file_extensions_to_check)

            if leaks:
                print("Sızdırılan dosyalar bulundu:")
                for leak, found_keywords in leaks:
                    print(f"{leak} - Bulunan Anahtar Kelimeler: {', '.join(found_keywords)}")
            else:
                print("Sızdırılan dosya bulunamadı.")
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            generate_report(leaks, errors, total_files, elapsed_time)
            print("Rapor 'leak_report.txt' dosyasına kaydedildi.")

            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            retry = input("Başka bir dizin taramak ister misiniz? (E/H): ")
            if retry.lower() != 'e':
                break
            if retry.lower() != 'h':
                os.system("start.bat")
    
        except ValueError as e:
            print(e)
