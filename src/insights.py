from src.jobs import read


def get_unique_job_types(path):
    job_types = read(path)
    jobs_unique = set()

    for row in job_types:
        jobs_unique.add(row["job_type"])

    return jobs_unique
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """


def filter_by_job_type(jobs, job_type):
    filter_job_type = []

    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)

    return filter_job_type
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # return []


def get_unique_industries(path):
    job_industries = read(path)
    industries_unique = set()

    for row in job_industries:
        if row["industry"] != '':
            industries_unique.add(row["industry"])

    return industries_unique
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """


def filter_by_industry(jobs, industry):
    filter_industry = []

    for job in jobs:
        if job["industry"] == industry:
            filter_industry.append(job)

    return filter_industry
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # return []


def get_max_salary(path):
    job_max_salary = read(path)
    salary_max = []

    for row in job_max_salary:
        if row["max_salary"] != '' and row["max_salary"].isdigit():
            salary_max.append(int(row["max_salary"]))

    return max(salary_max)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # pass


def get_min_salary(path):
    job_min_salary = read(path)
    salary_min = []

    for row in job_min_salary:
        if row["min_salary"] != '' and row["min_salary"].isdigit():
            salary_min.append(int(row["min_salary"]))

    return min(salary_min)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # pass


def matches_salary_range(job, salary):
    errorMessage = "Busca n??o encontrada"
# Usei Raise para lan??ar erro
    if ("min_salary" or "max_salary") not in job:
        raise ValueError(errorMessage)
    elif type(job["min_salary"] or job["max_salary"] or salary) != int:
        raise ValueError(errorMessage)
    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError(errorMessage)
    elif (job["min_salary"] <= salary <= job["max_salary"]):
        return True

    return False
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # pass


def filter_by_salary_range(jobs, salary):
    salary_range = []

    for job in jobs:
        try:
            if isinstance(salary, int) and matches_salary_range(job, salary):
                salary_range.append(job)
        except ValueError:
            print("Ocorreu um erro, tente novamente")

    return salary_range
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # return []
