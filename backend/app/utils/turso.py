from fastapi import HTTPException
import httpx
from app.core.config import settings

def create_database(hash: str):
    try:
        url = f"https://api.turso.tech/v1/organizations/{settings.TURSO_ORG_NAME}/databases"
        headers = {"Authorization": f"Bearer {settings.TURS0_AUTH_TOKEN}"}
        json = {"name": hash, "group": "default"}
        httpx.post(url, headers=headers, json=json)
    except:
        raise HTTPException(status_code=500, detail="Error creating database")


def get(hash:str):
    url = f"libsql://{hash}-{settings.TURSO_ORG_NAME}.turso.io"
    return f"sqlite+{url}/?authToken={settings.GROUP_AUTH_TOKEN}&secure=true"

