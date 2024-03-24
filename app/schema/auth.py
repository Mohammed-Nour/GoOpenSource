from pydantic import BaseModel, ConfigDict



class ContributorBase(BaseModel):
    contributorName: str
    contributorEmail: str
    avatar_url: str
    contributionsNumber: int
    model_config = ConfigDict(from_attributes=True)