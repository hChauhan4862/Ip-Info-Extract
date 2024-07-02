# FastApi
from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
import time
import os
import ipInfo_io
import shutil
from fastapi.staticfiles import StaticFiles


# Importing the routes
app = FastAPI()
app.mount("/tmp", StaticFiles(directory="/tmp"), name="static")


@app.get("/")
def read_root():
    return {"status": "ok"}
    
@app.get("/{ipAddress}")
def read_root(ipAddress: str = Path(..., title="The IP address to get the info of", regex='^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$')):
    res = ipInfo_io.get_ip_info(ipAddress)
    if "error" in res:
        return {'error': True, 'message': res['error']}
    
    IPNFO = res["data"]
    IPNFO["key"] = ipAddress
    IPNFO['time'] = time.time()
    return IPNFO

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)