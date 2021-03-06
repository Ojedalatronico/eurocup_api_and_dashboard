from fastapi import APIRouter
from ..data.mongo import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/matches")
def all_matches():
    q={}
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1,"team_home_score":1,
        "possession_home":1,"total_shots_home":1,"shots_on_target_home":1,"duels_won_home":1
        ,"yellow_cards_home":1,"red_cards_home":1,"team_away_score":1,"possession_away":1,
        "total_shots_away":1,"shots_on_target_away":1,"duels_won_away":1,"yellow_cards_away":1,"red_cards_away":1}
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/matche/teams")
def all_matches_teams(stage):
    q={"stage":stage}
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1}
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/matche/rival")
def team_rival(stage,team_name_home):
    q={"stage":stage,
        "team_name_home":team_name_home}
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1}
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/home/stats")
def home_stats(stage,team_name_home):
    q={"stage":stage,
        "team_name_home": team_name_home}
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1,"pens":1,"team_home_score":1, "pens_home_score":1,
        "pen_away_score":1,"possession_home":1,"total_shots_home":1,"shots_on_target_home":1,"duels_won_home":1
        ,"yellow_cards_home":1,"red_cards_home":1}
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/away/stats")
def away_stats(stage,team_name_home):
    q={"stage":stage,
        "team_name_home": team_name_home
        }
    p={"_id":0,"team_name_home":1,"team_name_away":1,"stage":1,"pens":1,"team_away_score":1,
        "pen_away_score":1,"possession_away":1,
        "total_shots_away":1,"shots_on_target_away":1,"duels_won_away":1,"yellow_cards_away":1,"red_cards_away":1
        }
    results = list(db["UEFA"].find(q,p))
    return loads(json_util.dumps(results))

@router.get("/events")
def all_events(stage,team_name_home):
    q={"stage":stage,
        "team_name_home": team_name_home}
    results = list(db["UEFA"].find(q,{"_id":0,"team_name_home":1,"team_name_away":1,"stage":1,"events_list":1}))
    return loads(json_util.dumps(results))
    