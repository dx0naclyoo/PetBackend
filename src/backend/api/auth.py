from fastapi import APIRouter

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.get("/")
async def get_user():
    pass


@router.post("/login")
async def login():
    pass


@router.post("/register")
async def register():
    pass

