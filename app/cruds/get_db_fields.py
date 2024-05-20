from sqlalchemy.orm import Session
from ..model.auth import Repository, Contributor, ContributorRepository

from datetime import date

def get_repository_fields(db: Session):
    repositories = db.query(Repository).all()
    repository_fields = []
    for repo in repositories:
            repo_dict = {
                'repositoryID': repo.repositoryID,
                'repositoryName': repo.repositoryName,
                'repositoryFullName': repo.repositoryFullName,
                'stars': repo.stars,
                'forks': repo.forks,
                # 'lastUpdate': repo.lastUpdate.isoformat(),  # Convert date to ISO 8601 string
                'repoSize': repo.repo_size,
                'topics': repo.topics,
                'readmeURL': repo.readmeURL,
                'contributorsCount': repo.contributorsCount,
                'commitsCount': repo.commitsCount,
                'descriptions': repo.descriptions,
                'programmingLanguages1': repo.programming_language_1,
                'summarize': repo.summarize,
                # 'vector': repo.vector,
                'category': repo.category,
                'issue_count': repo.issue_count
            }
            repository_fields.append(repo_dict)  
    return repository_fields






def get_contributor_fields(db: Session):
    contributors = db.query(Contributor).all()
    contributor_fields = []
    for contributor in contributors:
        contributor_dict = {
            'contributorID': contributor.contributorID,
            'contributorLogin': contributor.contributorLogin,
            'avatarURL': contributor.avatar_url,
            'contributionsNumber': contributor.contributionsNumber,
            'contributorAccount': contributor.contributorAccount
        }
        contributor_fields.append(contributor_dict) 
    return contributor_fields

def get_contributor_repository_fields(db: Session):
    contributor_repositories = db.query(ContributorRepository).all()
    contributor_repository_fields = []
    for cr in contributor_repositories:
        cr_dict = {
            'contributorID': cr.contributorID,
            'repositoryID': cr.repositoryID,
            'repoRole': cr.repoRole
        }
        contributor_repository_fields.append(cr_dict)
    return contributor_repository_fields

