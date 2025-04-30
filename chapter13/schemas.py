"""Pydantic schemas"""
from pydantic import BaseModel

# Defines the input values that users will send to get prediction from the model
class FantasAcquisitionFeatures(BaseModel):
    waiver_value_tier: int
    fantasy_regular_season_weeks_remaining: int
    league_budget_pct_remainin: int

# The output that will be returned from the model
class PredictionOutput(BaseModel):
    winning_bid_10th_percentile: float
    winning_bid_50th_percentile: float
    winning_bid_90th_percentile: float
