import numpy as np        

from fastapi import APIRouter, Depends, HTTPException, Path

from models.api_models import InputData, InputData_Singular
from models.matrix import Matrix

router = APIRouter(
    prefix="/operation",
    tags=["Matrix Operations"],
    responses={404 : {"description":"Not Found"}}
)


@router.post("/add")
async def matrix_addition(operation: InputData):
    if (operation.inputB is None or operation.inputA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for addition.")

    try:
        if isinstance(operation.inputB, float):
            return {"result": Matrix(operation.inputA).add_number(operation.inputB).return_matrix().tolist()}
        elif isinstance(operation.inputB, list):
            return {"result": Matrix(operation.inputA).add(operation.inputB).return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/subtract")
async def matrix_subtraction(operation: InputData):
    if (operation.inputB is None or operation.inputA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for subtraction.")

    try:
        if isinstance(operation.inputB, float):
            return {"result": Matrix(operation.inputA).subtract_number(operation.inputB).return_matrix().tolist()}
        elif isinstance(operation.inputB, list):
            return {"result": Matrix(operation.inputA).subtract(operation.inputB).return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/multiply")
async def matrix_multiplication(operation: InputData):
    if (operation.inputB is None or operation.inputA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for multiplication.")

    try:
        if isinstance(operation.inputB, float):
            return {"result": Matrix(operation.inputA).multiply_scalar(operation.inputB).return_matrix().tolist()}
        elif isinstance(operation.inputB, list):
            return {"result": Matrix(operation.inputA).multiply(operation.inputB).return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/solve")
async def matrix_solver(operation: InputData):
    if (operation.inputB is None or operation.inputA is None):
        raise HTTPException(status_code=400, detail="Both inputs are required for solving.")

    try:
        return {"result": Matrix(operation.inputA).solve_variables(np.array(operation.inputB))}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/determinant")
async def matrix_determinant(operation: InputData_Singular):
    if (operation.inputA is None):
        raise HTTPException(status_code=400, detail="Input matrix is required for determinant calculation.")

    try:
        return {"result": Matrix(operation.inputA).determinant()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/transpose")
async def matrix_transpose(operation: InputData_Singular):
    if (operation.inputA is None):
        raise HTTPException(status_code=400, detail="Input matrix is required for transposition.")

    try:
        matrix = Matrix(operation.inputA)
        matrix.transpose()
        return {"result": matrix.return_matrix().tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/inverse")
async def matrix_inverse(operation: InputData_Singular):
    if (operation.inputA is None):
        raise HTTPException(status_code=400, detail="Input matrix is required for inversion.")

    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))