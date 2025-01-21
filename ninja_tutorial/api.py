from ninja import NinjaAPI, Schema

api = NinjaAPI()

class HelloSchema(Schema):
    name: str = "world"

@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"

@api.get("/hello")
def hello(request, name: str = "world"):
    return f"Hello {name}"

@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None
    first_name: str = None
    last_name: str = None

class Error(Schema):
    message: str

@api.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user
