from fastapi import APIRouter
from database import getMysqlConnection
from pydantic import BaseModel

router = APIRouter()


class Genre(BaseModel):
    genre: str


@router.get('/perpustakaan/api/genre/')
def show_genre():
    db = getMysqlConnection()
    result = {}
    result['results'] = []
    try:
        sqlstr = f"SELECT * from genre"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
        # print(output_json)
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


@router.post('/perpustakaan/api/genre/')
async def tambah_genre(genre: Genre):
    db = getMysqlConnection()
    try:
        cur = db.cursor()
        sqlstr = f"INSERT INTO genre (genre) VALUES('{genre.genre}')"
        cur.execute(sqlstr)
        db.commit()
        cur.close()
        print('sukses')
        # output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    # print(genre)
    return {
        "message": "sukses"
    }
