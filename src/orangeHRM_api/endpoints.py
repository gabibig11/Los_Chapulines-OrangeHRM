from enum import Enum


class Endpoints(Enum):
    login = "/oauth/issueToken"
    job_titles = "/api/jobTitles"
    getusers_id="/api/systemUsers/"
    job_categories = "/api/jobCategories"
    location = "/api/locations"
