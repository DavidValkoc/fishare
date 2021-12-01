import uvicorn
from fastapi import FastAPI
from fishare.fishare.api import files
from fishare.fishare.api import users
from fishare.fishare.views import homepage

app = FastAPI()
app.include_router(files.router, prefix='/api/v1')
app.include_router(users.router, prefix='/api/v1')
app.include_router(homepage.router)


# func na start priamo z pycharm nie cez prikazovy riadok
# reload=True, ak nieco zmenim v kode dam save tak hned to je aj v stranke
def main():
    uvicorn.run('main:app', port=8080, host='127.0.0.1', reload=True)


if __name__ == '__main__':
    main()
