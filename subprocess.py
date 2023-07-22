import subprocess

def run_terminal_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Komut Başarılı:")
            print(result.stdout)
        else:
            print("Hata oluştu:")
            print(result.stderr)
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    command = input("Terminalde çalıştırmak istediğiniz komutu girin: ")
    run_terminal_command(command)