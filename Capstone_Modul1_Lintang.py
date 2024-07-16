# CRUD Program Data Pasien Rumah Sakit

# import module python
from tabulate import tabulate
from datetime import datetime

#data awal
data_pasien=[
    {
        'ID':'P0001',
        'Nama':'Budi Santoso',
        'Tanggal Lahir':'05/11/1978',
        'Jenis Kelamin':'L',
        'Alamat':'Jl. Thamrin No. 20',
        'No. Telepon':'081334455667',
        'Riwayat Penyakit' :'Demam Berdarah',  
        'Peserta BPJS' : 'Kelas 1'
    }
]

# tempat menyimpan data yang sudah dihapus
backup_data=[]

# menampilkan tabel data pasien
def display_data():
    print('Data Pasien Rumah Sakit')
    list_pasien=[]
    for i in range(len(data_pasien)):
        list_pasien.append([data_pasien[i]['ID'], data_pasien[i]['Nama'], data_pasien[i]['Tanggal Lahir'], data_pasien[i]['Jenis Kelamin'], data_pasien[i]['Alamat'], data_pasien[i]['No. Telepon'], data_pasien[i]['Riwayat Penyakit'], data_pasien[i]['Peserta BPJS']])

    print(tabulate(list_pasien,headers=['ID','Nama','Tanggal Lahir','Jenis Kelamin','Alamat','No. Telepon','Riwayat Penyakit','Peserta BPJS'],tablefmt='double_grid',numalign='left',stralign='center'))


#validasi input ID
def validasi_input_id():
    while True:
        id_pasien = input('Silakan masukkan ID pasien (Format: 1 karakter + 4 digit angka. Contoh : P0001): ').upper()
        if id_pasien.isalnum() and len(id_pasien) == 5:
            return id_pasien   
        else:
            print('Input tidak valid. \nMohon masukkan 1 karakter dan 4 digit angka sebagai ID pasien. \nContoh: P0001')
            
# validasi input nama
def validasi_input_nama():
    while True:
        input_nama = input('Masukkan nama pasien : ').title()
        if input_nama == '':
            print('Data harus diisi')
        elif not input_nama.replace(' ', '').isalpha():
            print('Input tidak valid. Nama hanya boleh mengandung huruf dan spasi.')
        else:
            return input_nama
            

# validasi imput tanggal lahir
def validasi_input_tanggal():
    while True:    
        input_tanggal_lahir = input('Masukkan data tanggal lahir pasien (DD/MM/YYYY): ')
        try:
            datetime.strptime(input_tanggal_lahir, '%d/%m/%Y')
            return input_tanggal_lahir
            
        except ValueError:
            print('Mohon masukkan tanggal lahir yang benar. Tanggal lahir harus dalam format DD-MM-YYYY')


# validasi input jenis kelamin
def validasi_input_gender():
    while True:
        input_jenis_kelamin = input('Masukkan data jenis kelamin pasien (L/P) : ').upper()
        if input_jenis_kelamin not in ['L', 'P']:
            print('Jenis kelamin harus diisi dengan L/P')
        else:
            return input_jenis_kelamin
        
            
# validasi input alamat
def validasi_alamat():
    while True:
        input_alamat = input('Masukkan alamat pasien : ').title()
        if input_alamat == '':
            print('Data harus diisi')
        else:
            return input_alamat
        
            
# validasi input no telepon
def validasi_no_hp():
    while True:
        input_no_telepon = input('Masukkan no.telepon pasien : ')
        if input_no_telepon.isdigit() and len(input_no_telepon) in range(10, 15):
            return input_no_telepon
        else:
            print('Nomor telepon harus berupa angka dan panjangnya antara 10 sampai 14 digit.')

            
#validasi input riwayat penyakit
def validasi_riwayat_penyakit():
    while True:
        input_riwayat = input('Masukkan riwayat penyakit pasien : ').title()
        if input_riwayat.replace(' ', '').isalpha():
            return input_riwayat
        else:
            print('Riwayat Penyakit hanya boleh mengandung huruf dan spasi.')

    
# validasi input status peserta bpjs
def validasi_input_bpjs():
    while True:
        input_bpjs = input('Masukkan status peserta BPJS pasien (Kelas 1/2/3/Tidak): ').capitalize()
        if input_bpjs not in ['Kelas 1', 'Kelas 2', 'Kelas 3','Tidak']:
            print('Input status peserta BPJS dapat diisi dengan : \nKelas 1 \nKelas 2 \nKelas 3 \nTidak.')
        else:
            return input_bpjs
        
            
# fungsi filter data peserta bpjs
def filter_bpjs(data_pasien):
    while True:
        bpjs_filter = input('Masukkan kelas BPJS yang ingin ditampilkan (Kelas 1/ Kelas 2/ Kelas 3/ Tidak): ').capitalize()        
        filtered_data = list(filter(lambda x: x['Peserta BPJS'] == bpjs_filter, data_pasien))

        if filtered_data:
            print(f'\nData Pasien dengan Kelas BPJS : {bpjs_filter}\n')
            table_data = [[i['ID'], i['Nama'], i['Tanggal Lahir'], i['Jenis Kelamin'], i['Alamat'], i['No. Telepon'], i['Riwayat Penyakit'], i['Peserta BPJS']] for i in filtered_data]
            print(tabulate(table_data, headers=['ID', 'Nama', 'Tanggal Lahir', 'Jenis Kelamin', 'Alamat', 'No. Telepon', 'Riwayat Penyakit', 'Peserta BPJS'], tablefmt='fancy_grid'))
            break
        else:
            print(f'Data dengan peserta BPJS {bpjs_filter} tidak ditemukan atau penulisan salah.')


# menu Read
def menu_read():
    while True:    
        print('''
        ============== VIEW DATA PASIEN ===============
            
        1. Menampilkan Seluruh Data Pasien
        2. Menampilkan Data Pasien Tertentu
        3. Filter Data Pasien Berdasarkan Kelas BPJS
        4. Kembali Ke Main Menu

        ===============================================    
        ''')
        try :
            submenu_read = int(input('\nSilakan masukkan pilihan menu yang ingin dijalankan (1-3): '))
        except ValueError:
            print('Input tidak valid. Silakan masukkan angka.')
            menu_read()

        if submenu_read == 1:
            if len(data_pasien) != 0:
                display_data()
            else :
                print('Data Pasien Kosong')
                menu_read()

        elif submenu_read == 2:
            if len(data_pasien) != 0:
                print('''
                    ======== MENAMPILKAN DATA PASIEN TERTENTU ========
                      
                    1. Menampilkan Data Pasien Berdasarkan Nama
                    2. Menampilkan Data Pasien Berdasarkan ID 
                    3. Kembali ke Menu
                      
                    ==================================================
                ''')
                try:
                    input_submenu_read=int(input('Silakan masukkan pilihan menu yang ingin dijalankan (1-3): '))
                except ValueError:
                    print('Input tidak valid. Silakan masukkan angka.')
                    continue

                if input_submenu_read == 1:
                    read_nama=validasi_input_nama()
                    
                    list_nama=[]
                    for j in range(len(data_pasien)):
                        list_nama.append(data_pasien[j]['Nama'])

                    if read_nama in list_nama:
                        tabel_by_nama=[
                            ['ID', data_pasien[list_nama.index(read_nama)]['ID']],
                            ['Nama', read_nama],
                            ['Tanggal Lahir', data_pasien[list_nama.index(read_nama)]['Tanggal Lahir']],
                            ['Jenis Kelamin', data_pasien[list_nama.index(read_nama)]['Jenis Kelamin']],
                            ['Alamat', data_pasien[list_nama.index(read_nama)]['Alamat']],
                            ['No. Telepon', data_pasien[list_nama.index(read_nama)]['No. Telepon']],
                            ['Riwayat Penyakit', data_pasien[list_nama.index(read_nama)]['Riwayat Penyakit']],
                            ['Peserta BPJS', data_pasien[list_nama.index(read_nama)]['Peserta BPJS']]
                        ]
                        print(f'\nData pasien dengan Nama : {read_nama}\n')
                        print(tabulate(tabel_by_nama, headers=['Keterangan', 'Data'], tablefmt='fancy_grid'))
                        
                    else:
                        print(f'Tidak ada Data Pasien dengan Nama : {read_nama}. \nMohon masukkan nama lengkap pasien')        
                
                elif input_submenu_read == 2:
                    read_id=validasi_input_id()

                    list_id=[]
                    for j in range(len(data_pasien)):
                        list_id.append(data_pasien[j]['ID'])
                    
                    if read_id in list_id:
                        tabel_by_id=[
                            ['ID', data_pasien[list_id.index(read_id)]['ID']],
                            ['Nama', read_id],
                            ['Tanggal Lahir', data_pasien[list_id.index(read_id)]['Tanggal Lahir']],
                            ['Jenis Kelamin', data_pasien[list_id.index(read_id)]['Jenis Kelamin']],
                            ['Alamat', data_pasien[list_id.index(read_id)]['Alamat']],
                            ['No. Telepon', data_pasien[list_id.index(read_id)]['No. Telepon']],
                            ['Riwayat Penyakit', data_pasien[list_id.index(read_id)]['Riwayat Penyakit']],
                            ['Peserta BPJS', data_pasien[list_id.index(read_id)]['Peserta BPJS']]
                        ]
                        print(f'\nData pasien dengan ID : {read_id}\n')
                        print(tabulate(tabel_by_id, headers=['Keterangan', 'Data'], tablefmt='fancy_grid'))
                    else:
                        print(f'Tidak ada Data Pasien dengan ID : {read_id}')

                elif input_submenu_read == 3:
                    menu_read()
                else:
                    print('Input tidak valid. silahkan coba lagi.')
                
            else:
                print('Data pasien tidak tersedia.')
                
        elif submenu_read == 3:
            filter_bpjs(data_pasien)
            
        elif submenu_read == 4:
            main_menu()
            break
        else:
            print('Input tidak valid. Silahkan coba lagi.')
                
# menu Create 
def menu_create():
    while True:
        print("""
        =========== MENAMBAH DATA PASIEN =============
        1. Menambahkan Data Pasien
        2. Kembali Ke Main Menu
        ===============================================
        
        """)
        
        try:
            input_create=int(input('Silahkan masukkan pilihan menu yang ingin dijalankan : '))
        except ValueError:
            print('Input tidak valid. Mohon masukkan angka.')
            menu_create()
            
        if input_create == 1:
            id_pasien = validasi_input_id()
            for i in range(len(data_pasien)):
                if id_pasien == data_pasien[i]['ID']:
                    print('Data Pasien sudah ada di database. \nSilahkan coba lagi.\nKembali ke Menu...')
                    menu_create()
                    
                else:
                    print('Isi data pasien baru :')
                    nama_pasien=validasi_input_nama()
                    tanggal_lahir=validasi_input_tanggal()
                    jenis_kelamin=validasi_input_gender()
                    alamat=validasi_alamat()
                    no_telepon=validasi_no_hp()
                    riwayat_penyakit=validasi_riwayat_penyakit()
                    tingkat_bpjs=validasi_input_bpjs()
                    
                    konfirmasi=input('Apakah data sudah benar? (Y/N) : ').upper()
                    if konfirmasi == 'Y':
                        data_baru={
                            'ID': id_pasien,
                            'Nama': nama_pasien,
                            'Tanggal Lahir': tanggal_lahir,
                            'Jenis Kelamin': jenis_kelamin,
                            'Alamat': alamat,
                            'No. Telepon': no_telepon,
                            'Riwayat Penyakit' : riwayat_penyakit,
                            'Peserta BPJS':tingkat_bpjs
                        }
                        data_pasien.append(data_baru)
                        list_pasien_baru = [
                                [data_baru['ID'], data_baru['Nama'], data_baru['Tanggal Lahir'], data_baru['Jenis Kelamin'], data_baru['Alamat'], data_baru['No. Telepon'], data_baru['Riwayat Penyakit'], data_baru['Peserta BPJS']]
                            ]
                        print(tabulate(list_pasien_baru, headers=['ID', 'Nama', 'Tanggal Lahir', 'Jenis Kelamin', 'Alamat', 'No. Telepon', 'Riwayat Penyakit', 'Peserta BPJS'], tablefmt='fancy_grid', stralign='center'))
                        print('Data pasien berhasil disimpan.')
                        menu_create()
                    
                    elif konfirmasi == 'N':
                        menu_create()
                    else:
                        print('Mohon hanya masukkan Y/N.')
                        menu_create()
         
        elif input_create == 2:
            main_menu()
            break
        else:
            print('Input tidak valid. Silahkan coba lagi.')
        break

# menu Update
def menu_update():
    while True:
        print('''
        ============ UPDATE DATA PASIEN ==============
            1. Mengupdate Data Pasien
            2. Kembali Ke Main Menu
        ==============================================
        ''')
        
        try:
            submenu_update = int(input('Masukkan pilihan sub menu : '))
        except ValueError:
            print('Input tidak valid. Mohon masukkan angka.')
            menu_update()
            return
    
        if submenu_update == 1:
            while True:
                id_input = validasi_input_id()
                found = False
    
                for i in range(len(data_pasien)):
                    if id_input == data_pasien[i]['ID']:
                        found = True
                        print('''
                            ========== MENGUPDATE DATA PASIEN ==========
                            Update data pasien berdasarkan :  
                                1. Nama
                                2. Tanggal Lahir
                                3. Jenis kelamin
                                4. Alamat
                                5. No. Telepon
                                6. Riwayat Penyakit
                                7. Peserta BPJS
                            ============================================
                            
                            ''')
                        try:
                            kolom_update = int(input('Masukkan pilihan kolom yang ingin diubah (1-7) : '))
                        except ValueError:
                            print('Input tidak valid. Mohon masukkan angka.')
                            continue
    
                        if kolom_update == 1:
                            input_nama = validasi_input_nama()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['Nama'] = input_nama
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue
    
                        elif kolom_update == 2:
                            input_tanggal_lahir = validasi_input_tanggal()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['Tanggal Lahir'] = input_tanggal_lahir
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue
    
                        elif kolom_update == 3:
                            input_jenis_kelamin = validasi_input_gender()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['Jenis Kelamin'] = input_jenis_kelamin
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue
    
                        elif kolom_update == 4:
                            input_alamat = validasi_alamat()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['Alamat'] = input_alamat
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue
    
                        elif kolom_update == 5:
                            input_no_telepon = validasi_no_hp()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['No. Telepon'] = input_no_telepon
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue

                        elif kolom_update == 6:
                            input_riwayat_penyakit = validasi_riwayat_penyakit()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['Riwayat Penyakit'] = input_riwayat_penyakit
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue
    
                        elif kolom_update == 7:
                            input_bpjs = validasi_input_bpjs()
                            konfirmasi_update = input('Apakah data jadi diubah? (Y/N) : ').upper()
                            if konfirmasi_update == 'Y':
                                data_pasien[i]['Peserta BPJS'] = input_bpjs
                                print('Data berhasil diupdate.')
                                menu_update()
                                return
                            elif konfirmasi_update == 'N':
                                print('Data tidak diupdate.')
                                continue
                            else:
                                print('Input tidak valid. Silakan coba lagi.')
                                continue
                        else:
                            print('Input tidak valid. Silakan coba lagi.')
                        
                if not found:
                    print('ID pasien tidak ditemukan. Silakan coba lagi.')
            
        elif submenu_update == 2:
            main_menu()
            break
            
        else:
            print('Input tidak valid. Silakan coba lagi.')

# menu Delete
def menu_delete():
    while True:
        print('''
            ============ DELETE DATA PASIEN ===============
            1. Menghapus Data Pasien
            2. Kembali Ke Main Menu
            ===============================================
            ''')
        try:
            submenu_delete=int(input('Masukkan pilihan angka menu :  '))
        except ValueError:
            print('Input tidak valid. Mohon masukkan angka.')
            menu_delete()
            
        if submenu_delete == 1:
            display_data()
            input_delete=validasi_input_id()
            
            for i in range(len(data_pasien)):
                if input_delete == data_pasien[i]['ID']:
                    konfirmasi_delete=input('Apakah yakin ingin dihapus ? (Y/N) : ').upper()
                    if konfirmasi_delete == 'Y':
                        backup_data.append(data_pasien[i])
                        del data_pasien[i]
                        display_data()
                        print('Data berhasil dihapus.')
                        menu_delete()
                        break
                    elif konfirmasi_delete == 'N':
                        print('Data gagal dihapus. Kembali ke menu...')
                        main_menu()
                        break
                    else:
                        print('Input tidak valid. Silahkan coba lagi.')
            else:
                print('ID pasien tidak ditemukan. Silahkan coba lagi.')
                menu_delete()
    
        elif submenu_delete == 2:
            main_menu()
            break
        else:
            print('Input tidak valid. Silahkan coba lagi.')
        break 

# menu restore
def menu_restore():
    while True:
        print('''
            ============ RESTORE DATA PASIEN ============
            1. Restore Data Pasien
            2. Kembali Ke Main Menu
            =============================================
            ''')
        try:
            submenu_restore = int(input('Masukkan pilihan angka menu :  '))
        except ValueError:
            print('Input tidak valid. Mohon masukkan angka.')
            continue
            
        if submenu_restore == 1:
            if not backup_data:
                print('Tidak ada data untuk direstore.')
                continue
            
            print('Data yang bisa direstore:\n')
            for i, value in enumerate(backup_data):
                print(f'{i+1}. ID: {value['ID']}, Nama: {value['Nama']}')
            
            try:
                restore_index = int(input('\nMasukkan nomor urutan data pasien yang ingin direstore: ')) - 1
                if 0 <= restore_index < len(backup_data):
                    data_pasien.append(backup_data.pop(restore_index))
                    display_data()
                    print('Data pasien berhasil direstore.')
                else:
                    print('Nomor tidak valid.')
            except ValueError:
                print('Input tidak valid. Silakan masukkan angka.')
                
        elif submenu_restore == 2:
            main_menu()
            break
        else:
            print('Input tidak valid. Silahkan coba lagi.')
            continue


# Main Menu
def main_menu():
    while True:
        print('''
            ======= DATABASE RUMAH SAKIT ======
            ========== MAIN MENU ==============
            
            1. View Data Pasien
            2. Add Data Pasien
            3. Update Data Pasien
            4. Delete Data Pasien
            5. Restore Data Pasien
            6. Exit Program
            
            ===================================
            ''')
            
        try :
            pilihan_menu = int(input('Masukkan pilihan menu yang ingin dijalankan (1-6): '))
        except ValueError:
            print('Input tidak valid. Silakan masukkan angka.')
            main_menu()
            
        if pilihan_menu == 1:
            menu_read()
        elif pilihan_menu == 2:
            menu_create()
        elif pilihan_menu == 3:
            menu_update()
        elif pilihan_menu == 4:
            menu_delete()
        elif pilihan_menu == 5:
            menu_restore()
        elif pilihan_menu == 6:
            print('\nAnda keluar dari program.\n') 
            break 
        else:
            print('Input tidak valid. Silahkan coba lagi.')
            main_menu()        
        break

# Menjalankan program
main_menu()

