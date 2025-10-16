import os, json, logging, time
import numpy as np

from typing import Union
from fastapi import FastAPI

from methods import matrix_math, m_rowoperations
from routes import main_routes


# Configure the logger
logging.basicConfig(filename='logs/error.log', level=logging.INFO, format="%(asctime)s - %(message)s")

def measure_response_time(start_time):
    print("Response time:", time.perf_counter() - start_time)


# """
# JSON Structure:

# {
#     "opname": <string>,
#     "matrices": [
#         [[1, 2], [3, 4]],
#         [[5, 6], [7, 8]]
#     ]
# }
# """

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