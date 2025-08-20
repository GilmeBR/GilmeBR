from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from nba_api.stats.endpoints import leagueleaders
from nba_api.stats.library.parameters import Season

app = FastAPI(title="NBA Historical Stats API")

FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def serve_index():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/api/players/league-leaders")
def get_league_leaders(season: str = Season.default, stat: str = "PTS"):
    """Return league leaders for a given season and stat category."""
    try:
        leaders = leagueleaders.LeagueLeaders(season=season, stat_category=stat)
        df = leaders.get_data_frames()[0]
        top = df[["PLAYER", "TEAM", stat]]
        return top.to_dict(orient="records")
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
