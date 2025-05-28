from dishka import Provider, Scope, provide_all

from app.application.user.read_user import ReadUser
from app.application.user.sign_in import SignInUser
from app.application.user.sign_up import SignUpUser
from app.application.user.update import UpdateUser


class InteractorsProvider(Provider):
    scope = Scope.REQUEST

    provides = provide_all(
        SignUpUser,
        SignInUser,
        ReadUser,
        UpdateUser,
    )
