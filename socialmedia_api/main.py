"""
FAST API app for our project
"""

from fastapi import FastAPI
from socialmedia_api.routers.post import router as post_router

app = FastAPI()

# because we have routers, we can add prefixes: 'prefix=posts'
app.include_router(post_router)
