from fastapi import APIRouter, Response, status

router = APIRouter()

@router.get('/')
async def root() -> Response:
    """
    showing if app is run
    Returns:
        Response: code and text
    """
    return Response(status_code=status.HTTP_200_OK, content='write2me is running correctly')
