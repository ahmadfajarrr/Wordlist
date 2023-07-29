def replace_space_with_newline(sentence):
    # Mengganti spasi dengan \n
    return sentence.replace(' ', '\n')


def process_sentences(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Memproses kalimat dan mengganti spasi dengan \n
        processed_content = replace_space_with_newline(content)

        with open(filename, 'w') as file:
            file.write(processed_content)
        print("Pengolahan kalimat selesai.")
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat memproses file:", str(e))


if __name__ == "__main__":
    nama_file = "wordlist.txt"  # Ganti dengan nama file teks yang sesuai
    process_sentences(nama_file)
