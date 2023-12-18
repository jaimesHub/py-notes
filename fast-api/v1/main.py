from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     """
#     Path Parameters & Path Parameters with Types
#     Same with the syntax used by Python format strings
#     The value of the path parameter 'item_id' will be passed to you function as the argument 'item_id'
#     Test 1: http://localhost:8000/items/foo
#     Test 2: http://localhost:8000/items/1
#     Output: {"item_id": "foo"}
#     """
#     print(type(item_id))
#     return {"item_id": item_id}

# @app.get("/users/{user_id}")
# async def read_user(user_id):
#     """
#     Should not define this before the /users/me
#     """
#     return {
#         "user_id": user_id
#     }

@app.get("/users/me")
async def read_user_me():
    """
    The fixed path with path operations should be declared before dynamic
    If not ?
    """
    return {
        "user_id": "the current user"
    }

@app.get("/users/{user_id}")
async def read_user(user_id):
    """
    The dynamic path with path operations should be declared after the fixed one
    """
    return {
        "user_id": user_id
    }

class ModelName(str, Enum):
    """Predefined values"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """Predefined values"""
    # Compare enumeration member
    if model_name is ModelName.alexnet:
        return {
            "model_name": model_name,
            "message": "Deep Learning FTW!"
        }
    
    # Get the enumeration value
    # model_name.value
    # ModelName.lenet.value
    if model_name.value == "lenet":
        return {
            "model_name": model_name,
            "message": "LeCNN al the images"
        }
    
    # You can return enum members from your path operation, even nested in a JSON body (e.g. a `dict`)
    return {
        "model_name": model_name,
        "message": "Have some residuals"
    }

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """Path parameters containing paths"""
    print(file_path)
    return {"file_path": file_path}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """Query Parameters - Default value
    skip and limit are not part of the path parameters
    skip and limit called query parameter
    Test: http://127.0.0.1:8000/items/?skip=0&limit=10
    Test default value: http://127.0.0.1:8000/items/?skip=10
    """
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """Query Parameters - Optional parameters 
    Test: http://127.0.0.1:8000/items/1
    """
    print(q)
    if q:
        return {
            "item_id": item_id,
            "q": q
        }
    return {"item_id": item_id}
