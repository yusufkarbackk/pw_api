from fastapi import APIRouter
from database import getMysqlConnection

router = APIRouter()


@router.get('/perpustakaan/api/peminjaman/')
def show_peminjaman():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from peminjaman"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        #print(output_json)
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
