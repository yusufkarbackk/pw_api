from fastapi import FastAPI
from database import getMysqlConnection
from routers import rak, genre, petugas, anggota, peminjaman, pengembalian

app_api = FastAPI()

app_api.include_router(rak.router)
app_api.include_router(genre.router)
app_api.include_router(petugas.router)
app_api.include_router(anggota.router)
app_api.include_router(peminjaman.router)
app_api.include_router(pengembalian.router)


@app_api.get('/perpustakaan/api/show_buku/')
def show_buku():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = "SELECT buku.kode_buku, buku.judul_buku, genre.genre, buku.penulis_buku, buku.penerbit_buku, buku.tahun_penerbit, buku.stok FROM buku INNER JOIN relasi_buku_genre ON relasi_buku_genre.kode_buku=buku.kode_buku INNER JOIN genre on genre.id_genre=relasi_buku_genre.id_genre"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        # print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    # print(result['results'])
    for i in output_json:
        result['results'].append({
            'kd_buku': i[0],
            'judul': i[1],
            'genre': i[2],
            'penulis': i[3],
            'penerbit': i[4],
            'tahun_terbit': i[5],
            'stok': i[6]

        })
    print(result['results'])
    return result


@app_api.get('/perpustakaan/api/update_buku/{kd_buku}')
def update_buku(kd_buku: int):
    db = getMysqlConnection()
    result = {}
    result['results'] = {}
    genre = []
    relasi = []
    try:
        sqlstr = f"SELECT * from buku where kode_buku={kd_buku}"
        cur = db.cursor()
        cur.execute(sqlstr)
        old_data = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    try:
        sqlstr = f"SELECT * from genre"
        cur = db.cursor()
        cur.execute(sqlstr)
        genres = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)

    try:
        sqlstr = f"SELECT id_genre from relasi_buku_genre where kode_buku={kd_buku}"
        cur = db.cursor()
        cur.execute(sqlstr)
        genre_relation = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    joined_genre_relation = []  # [(1,), (2,)]
    for i in genre_relation:
        joined_genre_relation.append(i[0])
    print(joined_genre_relation)

    for i in old_data:
        buku = {
            'id_buku': i[0],
            'kode_buku': i[1],
            'judul_buku': i[2],
            'penulis': i[3],
            'penerbit': i[4],
            'tahun_terbit': i[5],
            'stok': i[6]
        }

    for i in genres:
        genre.append({
            'id_genre': i[0],
            'genre': i[1],
        })

    for i in joined_genre_relation:
        relasi.append(i)
    result['results']['buku'] = buku
    result['results']['genre'] = genre
    result['results']['relasi'] = relasi
    return result


if __name__ == '__main__':
    app_api.run(debug=True)
