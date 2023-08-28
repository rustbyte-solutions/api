from fastapi import FastAPI, HTTPException
import asyncpg
import config


app = FastAPI()
pool = None


@app.get("/avatars/{user_id}")
async def get_avatar(user_id: int):
    if not pool or not isinstance(pool, asyncpg.Pool):
        raise HTTPException(500, "Database connection pool is not initialized.")

    try:
        avatar = await pool.fetchval("SELECT avatar_url FROM AVATARS WHERE user_id = $1", user_id)
        if not avatar:
            raise HTTPException(404, "Avatar not found.")

        return {"user_id": user_id, "avatar_url": avatar}

    except asyncpg.exceptions.PostgresError:
        raise HTTPException(500, "Database error.")

@app.on_event("startup")
async def startup():
    global pool
    pool = await asyncpg.create_pool(config.DATABASE)

@app.on_event("shutdown")
async def shutdown():
    if pool:
        await pool.close()
