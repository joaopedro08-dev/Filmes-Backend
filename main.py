from fastapi import FastAPI
from config.cors import setup_cors  
from controller.filmController import router as film_router
import uvicorn

# Start FastAPI
app = FastAPI()

# Cors
setup_cors(app)

# Controller Routes
app.include_router(film_router)

# Start the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)