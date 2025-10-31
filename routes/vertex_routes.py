import logging, traceback
import numpy as np        

from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from fractions import Fraction

from models.api_models import InputData, InputData_Singular
from models.vector import Vector

# Configure the logger
logging.basicConfig(filename='logs/error.log', level=logging.INFO, format="%(asctime)s - %(message)s")

def log_exception(message: Exception):
    logging.error(traceback.format_exc())


router = APIRouter(
    prefix="/vertex",
    tags=["Vertex Operations"],
    responses={404 : {"description":"Not Found"}}
)


def float_to_frac_str(x: float, max_denominator: int = 10**6) -> str:
    """
    Convert a single float to a Fraction string.
    Uses limit_denominator to produce a human-friendly rational approximation.
    """
    if np.isnan(x):
        return "nan"
    if np.isinf(x):
        return "inf" if x > 0 else "-inf"

    frac = Fraction(x).limit_denominator(max_denominator)
    if frac.denominator == 1:
        return str(frac.numerator)
    else:
        return f"{frac.numerator}/{frac.denominator}"


def matrix_floats_to_fraction_strings(mat: np.ndarray, max_denominator: int = 10**6) -> List[List[str]]:
    """
    Convert a matrix (numpy ndarray or nested list) of floats 
    to a nested list of fraction strings.
    """
    arr = np.asarray(mat, dtype=float)
    out = []
    for row in arr:
        out_row = [
            float_to_frac_str(float(x), max_denominator=max_denominator) for x in row
        ]
        out.append(out_row)
    return out


@router.post("/magnitude")
def vector_magnitude(operation: InputData_Singular):
    try:
        vectorA = operation.inputA
        vecA = Vector(vectorA)

        magnitude = vecA.magnitude()

        return {
            "magnitude": float_to_frac_str(magnitude)
        }

    except Exception as e:
        log_exception(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/unit-vector")
def vector_unit_vector(operation: InputData_Singular):
    try:
        vectorA = operation.inputA
        vecA = Vector(vectorA)

        unit_vec = vecA.unit_vector()

        return {
            "unit_vector": matrix_floats_to_fraction_strings(unit_vec.data.reshape(1, -1))[0]
        }

    except Exception as e:
        log_exception(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/addition")
def vector_addition(operation: InputData):
    try:
        vecA = Vector(operation.inputA)
        vecB = Vector(operation.inputB)

        result = vecA.addition(vecB)

        return {
            "result": matrix_floats_to_fraction_strings(result.data.reshape(1, -1))[0]
        }

    except Exception as e:
        log_exception(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/subtraction")
def vector_subtraction(operation: InputData):
    try:
        vecA = Vector(operation.inputA)
        vecB = Vector(operation.inputB)

        result = vecA.subtraction(vecB)

        return {
            "result": matrix_floats_to_fraction_strings(result.data.reshape(1, -1))[0]
        }

    except Exception as e:
        log_exception(e)
        raise HTTPException(status_code=500, detail=str(e))