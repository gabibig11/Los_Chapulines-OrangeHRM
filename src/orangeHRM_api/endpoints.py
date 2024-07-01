from enum import Enum


class Endpoints(Enum):
    login = "/oauth/issueToken"
    job_titles = "/api/jobTitles"
    employment_status = "/api/employmentStatus"
