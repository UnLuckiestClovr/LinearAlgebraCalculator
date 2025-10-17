from typing import Union
from fastapi import FastAPI

from routes import main_routes

if __name__ == "__main__":
    import uvicorn
    app = FastAPI(
        title="Linear Algebra Calculator API",
        description="An API for performing linear algebra operations such as matrix addition and solving systems of equations.",
        version="1.0.0"
    )

    app.include_router(router=main_routes.router)

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    uvicorn.run(app=app, host="0.0.0.0", port=10000)