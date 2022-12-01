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
def show_genre():
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


if __name__ == '__main__':
    app_api.run(debug=True)
