from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pages.messages import router as message_router


app = FastAPI()


origins = [
    'http://web:80'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(message_router, tags=['messages'], prefix='/api/v1')


