from enum import Enum


class Endpoints(Enum):
    login = "/oauth/issueToken"
    job_titles = "/api/jobTitles"
    job_categories = "/api/jobCategories"
