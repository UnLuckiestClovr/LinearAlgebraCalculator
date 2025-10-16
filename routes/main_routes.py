import numpy as np        

from fastapi import APIRouter, Depends, HTTPException, Path

from models.api_models import Operation
from models.matrix import Matrix

router = APIRouter(
    prefix="/operation",
    tags=["Matrix Operations"],
    responses={404 : {"description":"Not Found"}}
)


@router.post("/add")
async def matrix_addition(operation: Operation):
    if (operation.matrixB is None or operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for addition.")

    try:
        if isinstance(operation.matrixB, float):
            return {"result": Matrix(operation.matrixA).add_number(operation.matrixB).return_matrix().tolist()}
        elif isinstance(operation.matrixB, list):
            return {"result": Matrix(operation.matrixA).add(operation.matrixB).return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/subtract")
async def matrix_subtraction(operation: Operation):
    if (operation.matrixB is None or operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for subtraction.")

    try:
        if isinstance(operation.matrixB, float):
            return {"result": Matrix(operation.matrixA).subtract_number(operation.matrixB).return_matrix().tolist()}
        elif isinstance(operation.matrixB, list):
            return {"result": Matrix(operation.matrixA).subtract(operation.matrixB).return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/multiply")
async def matrix_multiplication(operation: Operation):
    if (operation.matrixB is None or operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for multiplication.")

    try:
        if isinstance(operation.matrixB, float):
            return {"result": Matrix(operation.matrixA).multiply_scalar(operation.matrixB).return_matrix().tolist()}
        elif isinstance(operation.matrixB, list):
            return {"result": Matrix(operation.matrixA).multiply(operation.matrixB).return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/solve")
async def matrix_solver(operation: Operation):
    if (operation.matrixB is None or operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for solving.")

    try:
        return {"result": Matrix(operation.matrixA).solve_variables(np.array(operation.matrixB))}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/determinant")
async def matrix_determinant(operation: Operation):
    if (operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Input matrix is required for determinant calculation.")

    try:
        return {"result": Matrix(operation.matrixA).determinant()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/transpose")
async def matrix_transpose(operation: Operation):
    if (operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Input matrix is required for transposition.")

    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/inverse")
async def matrix_inverse(operation: Operation):
    if (operation.matrixA is None):
        raise HTTPException(status_code=400, detail="Input matrix is required for inversion.")

    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))