import fastapi

router = fastapi.APIRouter()

@router.get("/files/") #select * from files
def list_of_files():
    return [
        'file1',
        'file2',
        'file3'
    ]

@router.get('/files/{filename}/') #select * from files where filename
def get_file(filename: str):
    return {
        'filename': filename
    }

@router.delete('/files/{filename}/') #delete from files where delete
def delete_file(filename: str):
    return "deleted"

@router.put('/files/{filename}/') # update files where filename={filename} set .. FULL UPDATE
def full_update_file(filename: str):
    return "full update"

@router.patch('/files/{filename}/') # update files where filename={filename} set .. PARTIAL UPDATE (iba to co mu tam poslem)
def partial_update_file(filename: str):
    return "partial update"

@router.post('/files/') # insert into files values ()
def insert_file(filename: str):
    return "inserted"