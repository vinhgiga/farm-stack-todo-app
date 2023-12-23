from fastapi import APIRouter, Request, HTTPException, status

from fastapi.encoders import jsonable_encoder
from fastapi.params import Body
from todo.models import TaskModel, UpdateTaskModel
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/", response_description="Add a task")
async def create_task(request: Request, task: TaskModel):
    task = jsonable_encoder(task)
    new_task = await request.app.mongodb["tasks"].insert_one(task)
    create_task = await request.app.mongodb["tasks"].find_one(
        {"_id": new_task.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=create_task)


@router.get("/", response_description="List all tasks")
async def list_task(request: Request):
    cursor = request.app.mongodb["tasks"].find()
    tasks = []
    for doc in await cursor.to_list(length=100):
        tasks.append(doc)
    return tasks


@router.get("/{id}", response_description="Get a single task")
async def show_task(id: str, request: Request):
    task = await request.app.mongodb["tasks"].find_one({"_id": id})
    if task:
        return task
    return HTTPException(404, f"Task {id} not found")


@router.put("/{id}", response_description="Update a task")
async def update_task(id: str, request: Request, content: UpdateTaskModel = Body(...)):
    content = {k: v for k, v in content.dict().items() if v is not None}
    task = await request.app.mongodb["tasks"].find_one({"_id": id})
    if task:
        update_result = await request.app.mongodb["tasks"].update_one(
            {"_id": id}, {"$set": content}
        )
        updated_task = await request.app.mongodb["tasks"].find_one({"_id": id})
        return updated_task
    return HTTPException(404, f"Task {id} not found")


@router.delete("/{id}", response_description="Delete a task")
async def delete_task(id: str, request: Request):
    task = await request.app.mongodb["tasks"].find_one({"_id": id})
    if task:
        delete_result = await request.app.mongodb["tasks"].delete_one({"_id": id})
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": f"Task {id} deleted successfully"},
        )
    return HTTPException(404, f"Task {id} not found")
