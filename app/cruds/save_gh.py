import csv
from datetime import datetime
from sqlalchemy.orm import Session
from ..model.auth import Contributor, ContributorRepository, Repository

def store_repo_info(db: Session):
    file_path = r'D:\GoOpenSource\GoOpenSource\back\app\repo.csv'
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create a Contributor object
            contributor = Contributor(
                contributorLogin=row['contributorsName'],  
                avatar_url=row['contributorsPhoto'],
                contributionsNumber=1,
                contributorAccount=row['contributorsAccount']  # Added new field
            )
            db.add(contributor)
            db.commit()  # Commit after adding contributor

            # Create a Repository object
            repository = Repository(
                repositoryName=row['repositoryName'],
                repositoryFullName=row['repositoryFullName'],
                stars=int(row['stars']), 
                forks=int(row['forks']), 
                lastUpdate=datetime.strptime(row['lastUpdate'], '%Y-%m-%dT%H:%M:%SZ'),
                repo_size=int(row['size']),  # Updated field name
                topics=row['Topics'],
                readmeURL=row['Readme URL modified'],
                contributorsCount=0,
                commitsCount=0,
                descriptions=row['descriptions'],
                programming_language_1='python',  
                summarize="hohoh",  # Added new field
                vector="123",
                category=0,
                issue_count=0 
            )
            db.add(repository)
            db.commit()  # Commit after adding repository

            # Create a ContributorRepository object
            contributor_repository = ContributorRepository(
                contributorID=contributor.contributorID,
                repositoryID=repository.repositoryID,
                repoRole=row['contributorsRole']  # Updated field name
            )
            db.add(contributor_repository)
            db.commit()  # Commit after adding contributor_repository


def extract_contributor_and_emails():
    contributor_list = []
    email_list = []
    file_path = r'D:\GoOpenSource\GoOpenSource\back\app\repo.csv'
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extracting contributor information
            contributor_name = row['contributorsName']
            contributor_email = row['emails']  
            contributor_list.append(contributor_name)
            if contributor_email and contributor_email.endswith('@gmail.com'):
                email_list.append(contributor_email)
    
    return contributor_list, email_list
