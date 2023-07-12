"""
Inspired by
       - https://github.com/vinybrasil/fastapi_kafka/
       - https://github.com/pedrodeoliveira/fastapi-kafka-consumer
"""
import asyncio
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
import uvicorn

from balance.consumer import consume
from config import settings

from balance.routes import router as balance_router
from database import Base, SessionLocal, engine


Base.metadata.create_all(bind=engine)

# initialize logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(cur_app: FastAPI):
    log.info(f'Initializing API ...')
    task = asyncio.create_task(consume(settings))
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

app.include_router(balance_router)

@app.get("balances/{balance_id}")
def get_balance(balance_id: str):
    return 


@app.get("/")
async def root():
    return {"message": "Service Up and running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3303)
