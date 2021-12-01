import fastapi

router = fastapi.APIRouter()

@router.get("/")
def hello():
    return "hello world"

@router.get("/api/v1/{name}")
def homepage(name: str):
    return {"Ahoj": name}