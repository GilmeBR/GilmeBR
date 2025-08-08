import pandas as pd
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class DummyLeader:
    def get_data_frames(self):
        return [pd.DataFrame([{"PLAYER": "Test Player", "TEAM": "TST", "PTS": 30}])]


def test_league_leaders_endpoint(monkeypatch):
    monkeypatch.setattr(
        "app.main.leagueleaders.LeagueLeaders",
        lambda season, stat_category: DummyLeader(),
    )
    response = client.get("/api/players/league-leaders?season=2023-24&stat=PTS")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["PLAYER"] == "Test Player"
