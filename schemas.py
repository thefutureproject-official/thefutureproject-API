from pydantic import BaseModel
from typing import List, Optional


class Contest_Ranking(BaseModel):
    contestants_ids: List[str]


class Contest_Ranking_Out(BaseModel):
    username: str
    rank: int
    finish_time: str
    A_st: Optional[str]
    A_flc: Optional[int]
    B_st: Optional[str]
    B_flc: Optional[int]
    C_st: Optional[str]
    C_flc: Optional[int]
    D_st: Optional[str]
    D_flc: Optional[int]

    class Config:
        from_attributes = True


class Stock_Market_Ticker(BaseModel):
    tickers: List[str]


class Stock_Market_Ticker_Out(BaseModel):
    ticker: str
    last_quote: float

    class Config:
        from_attributes = True


class Contest_Info_In(BaseModel):
    contest_name: str


class Contest_Info_Out(BaseModel):
    contest_name: str
    contest_link: str
    problems: dict

    class Config:
        from_attributes = True


class Image_Out(BaseModel):
    text: str
    language: str

    class Config:
        from_attributes = True


class Image_Url_In(BaseModel):
    url: str
    language: Optional[str] = "eng"


class Ip_Info_In(BaseModel):
    ip: str


class Problem_Info_In(BaseModel):
    title_slug: str


class Problem_Info_Out(BaseModel):
    question_id: int
    title: str
    difficulty: str
    category: str
    tags: List[str]
    description: str

    class Config:
        from_attributes = True
