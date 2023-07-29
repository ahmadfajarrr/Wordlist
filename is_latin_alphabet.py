def is_latin_alphabet(word):
    # Fungsi ini akan memeriksa apakah kata hanya mengandung karakter alfabet Latin
    return all(65 <= ord(char) <= 122 for char in word)


def remove_non_latin_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                # Membagi kalimat menjadi kata-kata
                words = line.split()
                filtered_words = [word for word in words if is_latin_alphabet(word)]
                new_line = ' '.join(filtered_words) + '\n'
                file.write(new_line)
        print("Penghapusan kata dengan karakter non-alfabet Latin selesai.")
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memproses file:", str(e))


if __name__ == "__main__":
    nama_file = "wordlist.txt"  # Ganti dengan nama file teks yang sesuai
    remove_non_latin_words(nama_file)
