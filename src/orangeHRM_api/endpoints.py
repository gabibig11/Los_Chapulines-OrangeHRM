from enum import Enum


class Endpoints(Enum):
    delete_nationalit = None
    login = "/oauth/issueToken"
    job_titles = "/api/jobTitles"
    nationality_list = "/api/nationality"
    getusers_id = "/api/systemUsers/"
    getusers_filter = "/api/systemUsers"
    job_categories = "/api/jobCategories"
    location = "/api/locations"
    employment_status = "/api/employmentStatus"
    subunits = "/api/subunits"

    postvacancy = '/api/recruitment/vacancies'
    postcustormer = '/api/customers'
    patchusers = '/api/systemUsers/'
    deletenationality = '/api/nationality?='
