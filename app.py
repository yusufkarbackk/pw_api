from fastapi import FastAPI
import mysql.connector
app_api = FastAPI()


def getMysqlConnection():
    return mysql.connector.connect(user='root', host='localhost', port=8889, password='root', database='perpustakaan')


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
        print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    print(result['results'])
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
        relasi.append({
            'id_genre': i,
        })
    result['results']['buku'] = buku
    result['results']['genre'] = genre
    result['results']['relasi'] = relasi
    return result


@app_api.get('/perpustakaan/api/show_genre/')
def show_genre():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from genre"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    for i in output_json:
        result['results'].append({
            'id_genre': i[0],
            'genre': i[1],
        })
    return result


@app_api.get('/perpustakaan/api/show_petugas/')
def show_petugas():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from petugas"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    for i in output_json:
        result['results'].append({
            'id_petugas': i[0],
            'nama': i[1],
            'jabatan': i[2],
            'telpon': i[3],
            'alamat': i[4]
        })
    return result


@app_api.get('/perpustakaan/api/show_rak/')
def show_rak():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from rak"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    for i in output_json:
        result['results'].append({
            'id_rak': i[0],
            'nama_rak': i[1],
            'lokasi': i[2],
            'id_buku': i[3],
        })
    return result


@app_api.get('/perpustakaan/api/show_peminjaman/')
def show_peminjaman():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from peminjaman"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    for i in output_json:
        result['results'].append({
            'id_peminjaman': i[0],
            'tgl_pinjam': i[1],
            'tgl_kembali': i[2],
            'id_buku': i[3],
            'id_anggota': i[4],
            'id_petugas': i[5],
        })
    return result
@app_api.get('/perpustakaan/api/show_pengembalian/')
def show_pengembalian():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from pengembalian"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        print(output_json)
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    for i in output_json:
        result['results'].append({
            'id_pengembalian': i[0],
            'tgl_pengembalian': i[1],
            'denda': i[2],
            'id_buku': i[3],
            'id_anggota': i[4],
            'id_petugas': i[5],
        })
    return result


if __name__ == '__main__':
    app_api.run(debug=True)
