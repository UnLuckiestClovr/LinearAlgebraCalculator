from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

class Operation(BaseModel):
    matrixA: List[List[float]] = Field(..., description="A list of matrices involved in the operation.")
    matrixB: Optional[List[List[float]] | float] = Field(..., description="A second matrix or scalar involved in the operation, if applicable.")