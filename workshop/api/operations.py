from fastapi import APIRouter
from typing import List
from ..models.operations import Operation
from ..database import get_session
from .. import tables
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/operations'
)


@router.get("/", response_model=List[Operation])
def get_operations(session: Session = Depends(get_session)):
    session = Session()
    operations = (
        session
        .query(tables.Operation)
        .all()
    )
    return operations