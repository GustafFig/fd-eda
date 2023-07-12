"""
Inspired by
       - https://github.com/vinybrasil/fastapi_kafka/
       - https://github.com/pedrodeoliveira/fastapi-kafka-consumer
"""
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from balance.routes import router as balance_router
from database import Base, engine
from log import log
from balance.consumer import consume
from config import settings

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(cur_app):
    log.info("Lifespan started")
    task = asyncio.create_task(consume(settings))
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

app.include_router(balance_router)

@app.get("/")
async def root():
    return {"message": "Service Up and running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3303)
