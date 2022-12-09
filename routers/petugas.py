from fastapi import APIRouter
from database import getMysqlConnection

router = APIRouter()

@router.get('/perpustakaan/api/petugas/')
def show_petugas():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from petugas"
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
            'id_petugas': i[0],
            'nama': i[1],
            'jabatan': i[2],
            'telpon': i[3],
            'alamat': i[4]
        })
    return result