from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import BaseAppExceptions
from app.routers.router_order import router_order
from app.routers.router_tenant import router_tenant


app = FastAPI(title="crm-tenant-api", version="1.0.0")


@app.exception_handler(BaseAppExceptions)
async def app_exceptions_handler(request: Request, exc: BaseAppExceptions):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


app.include_router(router_order)
app.include_router(router_tenant)

