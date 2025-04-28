from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Team(BaseModel):
    name: str = Field(..., description="Nome do time")
    slug: str = Field(..., description="Slug do time (usado na URL)")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Match(BaseModel):
    match_id: str = Field(..., description="ID único da partida")
    home_team: str = Field(..., description="Nome do time da casa")
    away_team: str = Field(..., description="Nome do time visitante")
    home_score: Optional[int] = Field(None, description="Placar do time da casa")
    away_score: Optional[int] = Field(None, description="Placar do time visitante")
    link: str = Field(..., description="Link para a página da partida")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class TeamResponse(BaseModel):
    status: str = Field(..., description="Status da resposta")
    data: List[Team] = Field(..., description="Lista de times")
    count: int = Field(..., description="Quantidade de times")

class MatchResponse(BaseModel):
    status: str = Field(..., description="Status da resposta")
    data: List[Match] = Field(..., description="Lista de partidas")
    count: int = Field(..., description="Quantidade de partidas") 