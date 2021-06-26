from fastapi import APIRouter
import utils

router = APIRouter(prefix="/quotes")


@router.get("/")
async def get_all_quotes():
    return utils.get_all_quotes()


@router.get("/random/")
async def get_random_quote():
    return utils.get_random_quote()


@router.get("/character/{character}")
async def get_quote_from_character(character: str):
    quotes = utils.get_quote_from_character(character)
    return quotes or {
        "status": "Not Found",
        "message": f"Character with name {character} not found.",
    }
