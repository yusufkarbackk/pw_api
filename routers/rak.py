from fastapi import APIRouter
from database import getMysqlConnection

router = APIRouter()


@router.get("/perpustakaan/api/rak")
async def read_rak():
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
