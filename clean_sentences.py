def clean_sentences(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Mengganti multiple newlines menjadi satu newline
        cleaned_content = "\n".join(line.strip() for line in content.splitlines() if line.strip())

        with open(filename, 'w') as file:
            file.write(cleaned_content)
        print("Pengolahan kalimat selesai.")
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memproses file:", str(e))


if __name__ == "__main__":
    nama_file = "wordlist.txt"  # Ganti dengan nama file teks yang sesuai
    clean_sentences(nama_file)
