from fastapi import APIRouter
from database import getMysqlConnection

router = APIRouter()


@router.get('/perpustakaan/api/anggota/')
def show_anggota():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from anggota"
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
            'id_anggota': i[0],
            'kode_anggota': i[1],
            'nama_anggota': i[2],
            'password': i[3],
            'jk_anggota': i[4],
            'jurusan_anggota': i[5],
            'no_telepon_anggota': i[6],
            'alamat_anggota': i[7],
        })
    return result
