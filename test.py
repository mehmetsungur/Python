import subprocess

def fake_terminal_command():
    commands = [
        "ls -la",         # Komut 1: Mevcut dizindeki dosyaları listele
        "mkdir test_dir", # Komut 2: "test_dir" adında bir dizin oluştur
        "cd test_dir",    # Komut 3: Oluşturulan dizine geç
        "touch test.txt", # Komut 4: "test.txt" adında bir dosya oluştur
        "cat test.txt"    # Komut 5: Dosyanın içeriğini göster
    ]

    for cmd in commands:
        print(f"Komut Çalıştırılıyor: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Komut Başarılı: \n{result.stdout}")
        else:
            print(f"Hata oluştu: \n{result.stderr}")

if __name__ == "__main__":
    fake_terminal_command()