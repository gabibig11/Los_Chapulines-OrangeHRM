from enum import Enum


class Endpoints(Enum):
    login = "/oauth/issueToken"
    job_titles = "/api/jobTitles"
    nacionality_list = "/api/nationality"
    getusers_id="/api/systemUsers/"
    getusers_filter="/api/systemUsers"
    job_categories = "/api/jobCategories"
    location = "/api/locations"
    employment_status = "/api/employmentStatus"

