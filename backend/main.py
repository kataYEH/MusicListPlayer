from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000" ,
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

media_dir = Path("media")
media_dir.mkdir(parents=True, exist_ok=True)

reactPath = "../frontend/build/"
# Mount the "media" directory as a static file directory
app.mount("/media", StaticFiles(directory=str(media_dir)), name="media")
app.mount("/static", StaticFiles(directory=reactPath+"static/"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return FileResponse(reactPath+"index.html")


@app.get("/audio_files")
async def get_audio_files():
    audio_dir = Path("media")
    audio_files = [str(file.name) for file in audio_dir.glob("*.mp3")]  # Adjust the file extension as needed

    sorted_audio_files = sorted(audio_files, key=lambda x: int(x.split("-")[0]))
    print(sorted_audio_files)

    return {"audio_files": sorted_audio_files}

@app.get("/play_audio/{file_name}")
async def play_audio(file_name: str):
    file_path = Path("media") / file_name
    return FileResponse(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
