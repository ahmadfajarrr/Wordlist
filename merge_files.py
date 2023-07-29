def merge_files(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'a') as destination:
            destination.write(content)
        
        print("Merge isi file selesai.")
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat menggabungkan file:", str(e))


if __name__ == "__main__":
    file_sumber = "wl.txt"  # Nama file sumber yang akan digabungkan
    file_tujuan = "wordlist.txt"  # Nama file tujuan yang akan diisi dengan isi dari file sumber

    merge_files(file_sumber, file_tujuan)
