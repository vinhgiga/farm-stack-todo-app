import uvicorn
from config import settings
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from todo.routers import router as todo_router

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(todo_router, prefix="/task", tags=["tasks"])
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG_MODE,
        reload=settings.RELOAD_MODE,
    )
