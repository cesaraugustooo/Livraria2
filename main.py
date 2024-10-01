from fastapi import FastAPI
from routers.livros_router import router as livros_router
from config.database import conect,end_database
app = FastAPI()

app.add_event_handler("startup", func=conect)
app.add_event_handler(event_type='shutdown',func=end_database)


app.include_router(livros_router, tags=['Livros'])