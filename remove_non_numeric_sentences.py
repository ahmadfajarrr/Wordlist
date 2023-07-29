def remove_non_numeric_sentences(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read()

        # Decode isi file sebagai UTF-8, mengabaikan karakter yang tidak valid
        content = content.decode('utf-8', errors='ignore')

        # Memisahkan kalimat menjadi kata-kata
        words = content.split()

        # Memfilter kata-kata untuk menyimpan hanya angka
        numeric_words = [word for word in words if word.isdigit()]

        # Menggabungkan kembali kata-kata menjadi kalimat
        processed_content = ' '.join(numeric_words)

        with open(filename, 'w') as file:
            file.write(processed_content)
        print("Penghapusan kalimat selain angka selesai.")
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memproses file:", str(e))


if __name__ == "__main__":
    nama_file = "wl.txt"  # Ganti dengan nama file teks yang sesuai
    remove_non_numeric_sentences(nama_file)
