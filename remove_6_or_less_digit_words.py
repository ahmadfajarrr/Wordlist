def remove_6_or_less_digit_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                # Mencari kata berisi 6 digit huruf atau kurang dan menghapusnya
                words = line.split()
                filtered_words = [word for word in words if not word.isalpha() or len(word) > 6]
                new_line = ' '.join(filtered_words) + '\n'
                file.write(new_line)
        print("Penghapusan kata dengan 6 digit huruf atau kurang selesai.")
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memproses file:", str(e))


if __name__ == "__main__":
    nama_file = "wordlist.txt"  # Ganti dengan nama file teks yang sesuai
    remove_6_or_less_digit_words(nama_file)
