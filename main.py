from fastapi import FastAPI, Request, Header, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

from constants import ROOT_PATH
from utils import copy_files, MagnetLink, PartialTorrent, indicatorStyle, torrentClient

app = FastAPI(root_path=ROOT_PATH)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, hx_request: Optional[str] = Header(None)):
    torrents = torrentClient.get_torrents()
    context = {
        "request": request,
        "rootPath": ROOT_PATH,
        "torrents": torrents,
        "indicatorStyle": indicatorStyle,
    }
    return templates.TemplateResponse("index.html", context)


@app.post("/add")
async def add(magnetlink: MagnetLink):
    try:
        url = magnetlink.url
        res = torrentClient.add_torrent(url)
        return res.name
    except Exception as error:
        print(str(error))
        return str(error)


@app.delete("/delete/{id}")
async def delete(id):
    try:
        torrentClient.remove_torrent(id, delete_data=True)
    except Exception as error:
        print(str(error))
        return str(error)


@app.post("/copy/")
async def copy(torrent: PartialTorrent, background_tasks: BackgroundTasks):
    background_tasks.add_task(copy_files, torrent)
    return "Copying..."
