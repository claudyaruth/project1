# Nama : Claudya Ruth Fransisca
# Capstone Project Modul 1 - Data Nilai Siswa
# CRUD (Create, Read, Update, Delete)
# Kelas : JCDSOL - 012 (C)
# Teacher : Khumaeni
# 22 November 2023


students = [
    {
        'nomor_absen': '1',
        'nama_siswa': 'Ayu',
        'nilai_tugas': '85',
        'nilai_uts': '85',
        'nilai_uas': '88',
        'nilai_raport': '86'
    },
     {
        'nomor_absen': '2',
        'nama_siswa': 'Budi',
        'nilai_tugas': '90',
        'nilai_uts': '88',
        'nilai_uas': '86',
        'nilai_raport': '88'
    },
    {
        'nomor_absen': '3',
        'nama_siswa': 'Cantika',
        'nilai_tugas': '88',
        'nilai_uts': '85',
        'nilai_uas': '91',
        'nilai_raport': '88'
    },
    {
        'nomor_absen': '4',
        'nama_siswa': 'Dewi',
        'nilai_tugas': '95',
        'nilai_uts': '88',
        'nilai_uas': '90',
        'nilai_raport': '91'
    },
    {
        'nomor_absen': '5',
        'nama_siswa': 'Elang',
        'nilai_tugas': '92',
        'nilai_uts': '90',
        'nilai_uas': '88',
        'nilai_raport': '90'
    }
]

def show_menu():
    print("=== Data Nilai Raport Siswa SMA Cahaya  ===")
    print("Menu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")

def validate_input(prompt, is_numeric=False):
    while True:
        value = input(prompt)
        if is_numeric:
            if value.isdigit():
                return int(value)
            else:
                print("Input harus berupa angka. Coba lagi!")
        else:
            return value

def add_data():
    while True:
        nomor_absen = validate_input("Masukkan Nomor Absen: ", is_numeric=True)

        # Validasi nomor absen
        if any(student['nomor_absen'] == str(nomor_absen) for student in students):
            print("Nomor Absen sudah ada. Silahkan gunakan nomor absen lain.")
            continue

        nama_siswa = validate_input("Masukkan Nama Siswa: ")
        nilai_tugas = validate_input("Masukkan Nilai Tugas: ", is_numeric=True)
        nilai_uts = validate_input("Masukkan Nilai UTS: ", is_numeric=True)
        nilai_uas = validate_input("Masukkan Nilai UAS: ", is_numeric=True)
        nilai_raport = validate_input("Masukkan Nilai Raport: ", is_numeric=True)

        students.append({
            'nomor_absen': str(nomor_absen),
            'nama_siswa': nama_siswa,
            'nilai_tugas': nilai_tugas,
            'nilai_uts': nilai_uts,
            'nilai_uas': nilai_uas,
            'nilai_raport': nilai_raport
        })
        print("Data berhasil ditambahkan.")
        input("Tekan Enter untuk kembali ke menu utama.")
        break

def show_data():
    while True:
        if not students:
            print("Belum ada data.")
        else:
            print("=== Pilihan Tampilkan Data ===")
            print("1. Tampilkan Seluruh Data")
            print("2. Tampilkan Data Tertentu")
            print("3. Kembali ke Menu Utama")
            choice = validate_input("Masukkan pilihan (1-3): ", is_numeric=True)

            if choice == 1:
                show_all_data()
            elif choice == 2:
                show_specific_data()
            elif choice == 3:
                break
            else:
                print("Pilihan tidak valid.")

def show_all_data():
    # Mengatur jarak judul agar ke tengah
    column_width = 15  
    title = "            === Data Nilai Raport Siswa SMA Cahaya ===           "
    print(" ")
    title_padding = (column_width * 6 - len(title)) // 2
    print("{:^{width}}".format(title, width=title_padding + len(title)))
    print("|{:^10} | {:^11} | {:^11} | {:^9} | {:^9} | {:^10} |".format("No Absen", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Nilai Raport"))
    print("|" + "-" * 11 + "|" + "-" * 13 + "|" + "-" * 13 + "|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 14 + "|")

    for student in students:
        print("| {:^9} | {:^11} | {:^11} | {:^9} | {:^9} | {:^12} |".format(student['nomor_absen'], student['nama_siswa'], student['nilai_tugas'], student['nilai_uts'], student['nilai_uas'], student['nilai_raport']))
    print(" ")    
def show_specific_data():
    print("=== Tampilkan Data Tertentu ===")
    print("1. Berdasarkan Nomor Absen")
    print("2. Berdasarkan Nama Siswa")
    print("3. Kembali ke Menu Utama")
    choice = validate_input("Masukkan pilihan (1-3): ", is_numeric=True)
    print(" ")

    if choice == 1:
        nomor_absen = validate_input("Masukkan Nomor Absen: ", is_numeric=True)
        show_data_by_nomor_absen(nomor_absen)
    elif choice == 2:
        nama_siswa = validate_input("Masukkan Nama Siswa: ")
        show_data_by_nama_siswa(nama_siswa)
    elif choice == 3:
        return
    else:
        print("Pilihan tidak valid.")

def show_data_by_nomor_absen(nomor_absen):
    for student in students:
        if student["nomor_absen"] == str(nomor_absen):
            column_width = 15  
            title = "            === Data Nilai Raport Siswa SMA Cahaya ===           "
            print(" ")
            title_padding = (column_width * 6 - len(title)) // 2
            print("{:^{width}}".format(title, width=title_padding + len(title)))
            print("|{:^10} | {:^11} | {:^11} | {:^9} | {:^9} | {:^10} |".format("No Absen", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Nilai Raport"))
            print("|" + "-" * 11 + "|" + "-" * 13 + "|" + "-" * 13 + "|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 14 + "|")
            print("| {:^9} | {:^11} | {:^11} | {:^9} | {:^9} | {:^12} |".format(student['nomor_absen'], student['nama_siswa'], student['nilai_tugas'], student['nilai_uts'], student['nilai_uas'], student['nilai_raport']))
            return
    print("Nomor Absen tidak ditemukan.")

def show_data_by_nama_siswa(nama_siswa):
    found = False
    column_width = 15  
    title = "            === Data Nilai Raport Siswa SMA Cahaya ===           "
    print(" ")
    title_padding = (column_width * 6 - len(title)) // 2
    print("{:^{width}}".format(title, width=title_padding + len(title)))
    print("|{:^10} | {:^11} | {:^11} | {:^9} | {:^9} | {:^10} |".format("No Absen", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Nilai Raport"))
    print("|" + "-" * 11 + "|" + "-" * 13 + "|" + "-" * 13 + "|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 14 + "|")
    for student in students:
        if student["nama_siswa"].lower() == nama_siswa.lower():
            found = True
            print("| {:^9} | {:^11} | {:^11} | {:^9} | {:^9} | {:^12} |".format(student['nomor_absen'], student['nama_siswa'], student['nilai_tugas'], student['nilai_uts'], student['nilai_uas'], student['nilai_raport']))
    if not found:
        print("Nama Siswa tidak ditemukan.")

def update_data():
    while True:
        print("=== Pilihan Update Data ===")
        print("1. Update Nomor Absen")
        print("2. Update Nama Siswa")
        print("3. Update Nilai Tugas")
        print("4. Update Nilai UTS")
        print("5. Update Nilai UAS")
        print("6. Update Nilai Raport")
        print("7. Kembali ke Menu Utama")
        choice = validate_input("Masukkan pilihan (1-7): ", is_numeric=True)

        if choice == 7:
            break

        nomor_absen = validate_input("Masukkan Nomor Absen yang akan diubah: ", is_numeric=True)

        # Validasi nomor absen yang diubah tidak boleh sama dengan yang sudah ada
        if any(student['nomor_absen'] == str(nomor_absen) for student in students):
            for student in students:
                if student["nomor_absen"] == str(nomor_absen):
                    if choice == 1:
                        new_value = validate_input("Masukkan Nomor Absen Baru: ", is_numeric=True)

                        # Validasi nomor absen baru
                        if any(s['nomor_absen'] == str(new_value) for s in students):
                            print("Nomor Absen baru sudah ada. Gunakan nomor absen lain.")
                            continue
                        student["nomor_absen"] = str(new_value)
                    elif choice == 2:
                        new_value = validate_input("Masukkan Nama Siswa Baru: ")
                        student["nama_siswa"] = new_value
                    elif choice == 3:
                        new_value = validate_input("Masukkan Nilai Tugas Baru: ", is_numeric=True)
                        student["nilai_tugas"] = new_value
                    elif choice == 4:
                        new_value = validate_input("Masukkan Nilai UTS Baru: ", is_numeric=True)
                        student["nilai_uts"] = new_value
                    elif choice == 5:
                        new_value = validate_input("Masukkan Nilai UAS Baru: ", is_numeric=True)
                        student["nilai_uas"] = new_value
                    elif choice == 6:
                        new_value = validate_input("Masukkan Nilai Raport Baru: ", is_numeric=True)
                        student["nilai_raport"] = new_value

                    print("Data berhasil diubah.")
                    show_data()  # Menampilkan data setelah diubah
                
                    input("Tekan Enter untuk kembali ke menu utama.")
                    return
            else:
                print("Nomor Absen tidak ditemukan.")
        else:
            print("Nomor Absen tidak ditemukan.")

def delete_data():
    while True:
        nomor_absen = validate_input("Masukkan Nomor Absen yang akan dihapus: ", is_numeric=True)

        # Validasi nomor absen yang akan dihapus
        for student in students:
            if student["nomor_absen"] == str(nomor_absen):
                column_width = 15  
                title = "            === Data Nilai Raport Siswa SMA Cahaya ===           "
                print(" ")
                title_padding = (column_width * 6 - len(title)) // 2
                print("{:^{width}}".format(title, width=title_padding + len(title)))
                print("|{:^10} | {:^11} | {:^11} | {:^9} | {:^9} | {:^10} |".format("No Absen", "Nama Siswa", "Nilai Tugas", "Nilai UTS", "Nilai UAS", "Nilai Raport"))
                print("|" + "-" * 11 + "|" + "-" * 13 + "|" + "-" * 13 + "|" + "-" * 11 + "|" + "-" * 11 + "|" + "-" * 14 + "|")
                print("| {:^9} | {:^11} | {:^11} | {:^9} | {:^9} | {:^12} |".format(student['nomor_absen'], student['nama_siswa'], student['nilai_tugas'], student['nilai_uts'], student['nilai_uas'], student['nilai_raport']))
                
                confirm_delete = input("Apakah Anda yakin ingin menghapus data siswa ini? (y/n): ")
                if confirm_delete.lower() == 'y':
                    # Simpan salinan data yang akan dihapus
                    deleted_student = student.copy()

                    students.remove(student)
                    print("Data berhasil dihapus.")
                    
                    # Tambahkan opsi undo
                    undo_option = input("Apakah Anda ingin melakukan undo? (y/n): ")
                    if undo_option.lower() == 'y':
                        students.append(deleted_student)
                        print("Undo berhasil. Data telah dikembalikan.")
                    
                    return
                elif confirm_delete.lower() == 'n':
                    print("Penghapusan data dibatalkan.")
                    return
                else:
                    print("Pilihan tidak valid. Penghapusan data dibatalkan.")
                    return

        else:
            print("Nomor Absen tidak ditemukan.")



# Program Utama
while True:
    show_menu()
    choice = validate_input("Masukkan pilihan (1-5): ", is_numeric=True)

    if choice == 1:
        add_data()
    elif choice == 2:
        show_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        print("Terima kasih telah mengakses database Nilai Raport SMA Cahaya. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")