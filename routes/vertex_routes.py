import logging, traceback
import numpy as np        

from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from fractions import Fraction

from models.api_models import InputData, InputData_Singular
from models.matrix import Matrix

# Configure the logger
logging.basicConfig(filename='logs/error.log', level=logging.INFO, format="%(asctime)s - %(message)s")

def log_exception(message: Exception):
    logging.error(traceback.format_exc())


router = APIRouter(
    prefix="/vertex",
    tags=["Vertex Operations"],
    responses={404 : {"description":"Not Found"}}
)