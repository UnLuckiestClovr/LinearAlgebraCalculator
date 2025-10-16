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


def perform_operation(op: dict):
    start_time = time.perf_counter()
    try:
        match op['opname']:
            case 'add':
                result = matrix_math.iterative_addition(op['matrices'])

                print(result)
            case 'solve':
                m_rowoperations.solve_matrix_values(np.array(op['matrices']))
            case _:
                return None # None is Python's version of 'null'
    except Exception as e:
        print("Error: ", e)
        # Log the exception along with additional information
        logging.info('An error occurred: %s', str(e))
    measure_response_time(start_time)



def handle_equations():
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)

            print(f'Data Loaded: {data} | {type(data)}')

            npArray = np.array(data)

            for operation in npArray:
                perform_operation(operation)

    except FileNotFoundError:
        print("input.json file not found. Please create the file and add your equations and arrays.")
    except Exception as e:
        print("Error: ", e)
        # Log the exception along with additional information
        logging.info('An error occurred: %s', str(e))

while(True):
    print("Enter Equations and Arrays into JSON file. Code will handle the rest.")
    user_input = input("Please enter your equations and arrays then press Enter (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break
    else:
        handle_equations()


"""
JSON Structure:

{
    "opname": <string>,
    "matrices": [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
}
"""

if __name__ == "__main__":
    import uvicorn
    app = FastAPI(
        title="Linear Algebra Calculator API",
        description="An API for performing linear algebra operations such as matrix addition and solving systems of equations.",
        version="1.0.0"
    )

    app.include_router(router=main_routes.router, prefix="/api")

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    uvicorn.run(app=app, host="0.0.0.0", port=10000)