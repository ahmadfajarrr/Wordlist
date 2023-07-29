def remove_words_with_characters(filename, characters_to_remove):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                # Menghapus kata yang mengandung karakter yang ada dalam characters_to_remove
                words = line.split()
                filtered_words = [word for word in words if not any(char in word for char in characters_to_remove)]
                new_line = ' '.join(filtered_words) + '\n'
                file.write(new_line)
        print("Penghapusan kata dengan karakter tertentu selesai.")
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memproses file:", str(e))


if __name__ == "__main__":
    nama_file = "wordlist.txt"  # Ganti dengan nama file teks sumber yang sesuai
    characters_to_remove = "!@#%&*()_-=<>?{}/[]\|"  # Karakter yang ingin dihapus dari kata-kata

    remove_words_with_characters(nama_file, characters_to_remove)
