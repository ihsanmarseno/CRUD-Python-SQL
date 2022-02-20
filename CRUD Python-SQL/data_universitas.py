import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_university"
)

def insert_data(db):
    print("=== MASUKKAN DATA  ===")
    NIM                     = input("Masukkan NIM                 : ")
    NAMA                    = input("Masukkan Nama                : ")
    JURUSAN                 = input("Masukkan Jurusan             : ")
    SEX                     = input("Masukkan Jenis Kelamin [L/P] : ")
    val = (NIM, NAMA, JURUSAN, SEX)
    cursor = db.cursor()
    sql = "INSERT INTO mahasiswa (NIM, NAMA, JURUSAN, SEX) VALUES (%s,upper(%s),upper(%s), upper(%s))"
    cursor.execute (sql, val)

    db.commit()

    print("{} data berhasil disimpan" .format(cursor.rowcount))
    akhir = input("Ketik : 1. Tambahkan input mahasiswa || 2. Masuk ke menu  || 0. Keluar -> ")
    if akhir == "1":
      insert_data(db)
    elif akhir == "2":
      show_menu(db)
    else:
      exit()
    print("\n")

def show_data(db):
    cursor = db.cursor()
    show = input("Tulis jurusan yang ingin dipilih : ")
    print("=== DATA ===")
    sql = "SELECT * FROM mahasiswa WHERE jurusan = %s"
    val = (show,)
    cursor.execute(sql,val)
    result = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        for i in result:
            print(i)
    print("\n")
    akhir = input("Ketik : 1. Masuk ke menu  || 0. Keluar -> ")
    os.system('cls')
    print(" ")
    if akhir == "1":
      show_menu(db)
    else:
      exit()

def update_data(db):
    cursor = db.cursor()
    print("=== UPDATE DATA ===")
    NIM     = input("Tulis NIM anda -> ")
    print("Kolom ganti nama ")
    NAMA    = input("Nama baru anda                 : ")
    JURUSAN = input("Jurusan baru anda              : ")
    SEX     = input("Jenis Kelamin baru anda [L/P]  : ")

    sql = "UPDATE MAHASISWA SET NAMA=upper(%s), JURUSAN=upper(%s), SEX=upper(%s) where NIM=%s"
    val = (NAMA,JURUSAN, SEX,NIM)
    cursor.execute (sql,val)
    db.commit()

    print("{} data berhasil diubah" .format(cursor.rowcount))
    print("")
    akhir = input("Ketik : 1. Masuk ke menu  || 0. Keluar -> ")
    if akhir == "1":
      show_menu(db)
    else:
      exit()

def delete_data(db):
    cursor = db.cursor()
    print("=== HAPUS BARIS TABEL ===")
    delete = input("Hapus data berdasarkan NIM : ")
    sql = "DELETE FROM mahasiswa WHERE NIM = %s"
    val = (delete,)
    cursor.execute(sql,val)
    db.commit()

    print("{} baris telah terhapus" .format(cursor.rowcount))
    print("")
    akhir = input("Ketik : 1. Masuk ke menu  || 0. Keluar -> ")
    if akhir == "1":
      show_menu(db)
    else:
      exit()


def search_data(db):
    cursor = db.cursor()
    print("=== PENCARIAN DATA MAHASISWA ===")
    keyword= input("Kata kunci berdasarkan nama : ")
    sql = "SELECT * FROM mahasiswa where NAMA LIKE %s"
    val = ("%{}%" .format(keyword),)
    cursor.execute(sql,val)
    result = cursor.fetchall()

    if cursor.rowcount <= 0:
        print("Tidak ada data")
    else:
        for i in result:
            print(i)
    print("")
    akhir = input("Ketik : 1. Masuk ke menu  || 0. Keluar -> ")
    if akhir == "1":
      show_menu(db)
    else:
      exit()

def login(db):
    cursor = db.cursor()
    print("\n")
    print("== LOGIN DOSEN DAN MAHASISWA ==")
    id       = input("username : ")
    password = input("password : ")

    if id == "admin":
        if password == "admin":
          os.system('cls')
          show_menu(db)

        else:
            print("Input anda salah")
            login(db)
    else:
        ("Input anda salah")
        login(db)

def show_menu(db):
  print("")
  print("=== APLIKASI DATABASE MAHASISWA ===")
  print("[ 1 ] Insert Data")
  print("[ 2 ] Tampilkan Data")
  print("[ 3 ] Update Data")
  print("[ 4 ] Hapus Data")
  print("[ 5 ] Cari Data")
  print("[ 0 ] Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  os.system('cls')

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")

login(db)
