from fastapi import APIRouter
from typing import List , Optional
from ..models.operations import Operation, OperationKind
from fastapi import Depends
from ..services.operations import OperationsService



router = APIRouter(
    prefix='/operations'
)


@router.get("/", response_model=List[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationsService = Depends(),
):
    return service.get_list(kind=kind)
