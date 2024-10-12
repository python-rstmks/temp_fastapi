import time
from fastapi import FastAPI, Request, status
from routers import item, auth, category, subcategory, question
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination, paginate
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

# 例えば、リクエストの処理とレスポンスの生成にかかった秒数を含むカスタムヘッダー X-Process-Time を追加できます:
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(item.router)
app.include_router(auth.router)
app.include_router(category.router)
app.include_router(subcategory.router)
app.include_router(question.router)
add_pagination(app)
