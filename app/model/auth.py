from sqlalchemy import Column, Integer, String, ForeignKey , Date , Text
from sqlalchemy.orm import relationship
from ..database import Base
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import relationship

class Contributor(Base):
    __tablename__ = 'contributors'

    contributorID = Column(Integer, primary_key=True)
    contributorLogin  = Column(Text)
    avatar_url = Column(Text)
    contributionsNumber = Column(Integer)
    contributorAccount =Column(Text)
    contributorEmail =Column(Text)

class ContributerCreate(Contributor):
    model_config = ConfigDict(from_attributes=True)


class Repository(Base):
    __tablename__ = 'repositories'

    repositoryID = Column(Integer, primary_key=True)
    repositoryName = Column(Text)
    repositoryFullName = Column(Text)
    stars = Column(Integer)
    forks = Column(Integer)
    lastUpdate = Column(Date)
    repo_size  = Column(Integer)
    topics = Column(Text)
    readmeURL = Column(Text)
    contributorsCount = Column(Integer)
    commitsCount = Column(Integer)
    descriptions = Column(Text)
    programming_language_1 = Column(String(200))
    summarize =Column(Text)
    vector=Column(Text)
    category=Column(Text)
    issue_count = Column(Integer)
# Define the junction table for the many-to-many relationship
class ContributorRepository(Base):
    __tablename__ = 'contributor_repository'
    contributorID = Column(Integer, ForeignKey('contributors.contributorID'), primary_key=True)
    repositoryID = Column(Integer, ForeignKey('repositories.repositoryID'), primary_key=True)
    repoRole  = Column(String(100))
    contributor = relationship("Contributor", backref="repositories")
    repository = relationship("Repository", backref="contributors")