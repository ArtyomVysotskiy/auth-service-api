from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.application.data_model.token_data import TokenResponse
from app.application.data_model.user import UserData
from app.application.user.read_user import ReadUser
from app.application.user.sign_in import SignInUser, SignInUserRequest
from app.application.user.sign_up import SignUpUser, SignUpUserRequest
from app.application.user.update import UpdateUser, UpdateUserRequest
from app.presentation.http_endpoints.error_model import ErrorModel

router = APIRouter(
    route_class=DishkaRoute,
    tags=["Пользователи"],
    prefix="/users",
)

security = HTTPBearer(auto_error=False)


@router.post(
    "/sign_up",
    description="Авторизация пользователя",
    responses={
        200: {"model": TokenResponse, "description": "Успешная авторизация пользователя"},
        409: {"model": ErrorModel, "description": "Пользователь с таким name уже существует"},
    },
)
async def sign_up_user(
    schema: SignUpUserRequest,
    interactor: FromDishka[SignUpUser],
) -> TokenResponse:
    return await interactor.execute(schema)


@router.post(
    "/sign_in",
    description="Регистрация пользователя",
    responses={
        200: {
            "model": TokenResponse,
            "description": "Успешная регистрация пользователя",
        },
    },
)
async def sign_in_user(
    schema: SignInUserRequest,
    interactor: FromDishka[SignInUser],
) -> TokenResponse:
    return await interactor.execute(schema)


@router.patch(
    "/",
    description="Обновление данных пользователя",
    responses={
        200: {"description": "Успешное обновление данных"},
        401: {
            "model": ErrorModel,
            "description": "Пользователь не авторизирован",
        },
    },
)
async def update_user(
    schema: UpdateUserRequest,
    interactor: FromDishka[UpdateUser],
    _token: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> None:
    return await interactor.execute(schema)


@router.get(
    "/me",
    description="Получение данных о себе",
    responses={
        200: {"model": UserData, "description": "Успешное получение данных"},
        401: {
            "model": ErrorModel,
            "description": "Пользователь не авторизирован",
        },
    },
)
async def read_user(
    command: FromDishka[ReadUser],
    _token: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> UserData:
    return await command.execute()
