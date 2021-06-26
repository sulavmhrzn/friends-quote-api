from fastapi import APIRouter, status, Response
import utils

router = APIRouter(prefix="/quotes")


@router.get("/")
async def get_all_quotes():
    return utils.get_all_quotes()


@router.get("/random/")
async def get_random_quote():
    return utils.get_random_quote()


@router.get("/character")
async def get_quote_from_character(name: str, response: Response):
    quotes = utils.get_quote_from_character(name)
    if not quotes:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "status": "Not Found",
            "message": f"Character with name {name} not found.",
        }

    return quotes
