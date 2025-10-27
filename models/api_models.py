from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

class InputData(BaseModel):
    inputA: List[List[float]] | List[float] = Field(..., description="A list of matrices involved in the operation.")
    inputB: Optional[List[List[float]] | float] | Optional[List[float]] = Field(..., description="A second matrix or scalar involved in the operation, if applicable.")

class InputData_Singular(BaseModel):
    inputA: List[List[float]] | List[float] = Field(..., description="A list of matrices involved in the operation.")