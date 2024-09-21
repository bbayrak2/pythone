import sqlite3
db = sqlite3.connect("vt.splite")

im = db.cursor()

im.execute("""create table if not exists kullanicilar (kullanici_adi , parola)""")
veriler = [
    ("ahmet123","12345678"),
    ("mehmet321","87654321"),
    ("selin456","123123123")
]
for i in veriler:
    im.execute("""insert into kullanicilar values %s """ %(i,))
db.commit()

kull = input("lütfen kullanıcı adınızı giriniz : ")
par = input("lütfen parolanızı giriniz : ")

im.execute("""select * from kullanicilar where kullanici_adi = '%s' and parola = '%s' """ %(kull,par))
data = im.fetchone()

if data :
    print(f"programa hoş geldin {data[0]}")
else:
    print("hatalı giriş denemesi ")