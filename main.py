import time
from fastapi import FastAPI, Request
from routers import item, auth, category, subcategory, question
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
# app.include_router(question.router)
