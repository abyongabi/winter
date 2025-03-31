from model import LoginRequest, LoginResponse

def main(request: LoginRequest) -> LoginResponse:
    if request.user_name == "abyongabi" and request.password == "winter":
        return LoginResponse(result="Success")
    return LoginResponse(result="Failed")