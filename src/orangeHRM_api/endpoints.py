from enum import Enum


class Endpoints(Enum):
    login = "/oauth/issueToken"
    job_titles = "/api/jobTitles"
    nacionality_list = "/api/nationality"
    getusers_id="/api/systemUsers/"
    job_categories = "/api/jobCategories"
    location = "/api/locations"