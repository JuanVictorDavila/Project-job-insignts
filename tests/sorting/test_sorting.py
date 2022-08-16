from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"date_posted": "2020-05-08", "max_salary": 1000, "min_salary": 10},
        {"date_posted": "2020-08-08", "max_salary": 10000, "min_salary": 2},
        {"date_posted": "2020-01-08", "max_salary": 8000, "min_salary": 5},
        {"date_posted": "2020-03-08", "max_salary": 2000, "min_salary": 7},
        {"date_posted": "2020-09-08", "max_salary": 4000, "min_salary": 3},
        {"date_posted": "2020-12-08", "max_salary": 6000, "min_salary": 4},
    ]

    salary_to_sort = [
        {"date_posted": "2020-08-08", "max_salary": 10000, "min_salary": 2},
        {"date_posted": "2020-09-08", "max_salary": 4000, "min_salary": 3},
        {"date_posted": "2020-12-08", "max_salary": 6000, "min_salary": 4},
        {"date_posted": "2020-01-08", "max_salary": 8000, "min_salary": 5},
        {"date_posted": "2020-03-08", "max_salary": 2000, "min_salary": 7},
        {"date_posted": "2020-05-08", "max_salary": 1000, "min_salary": 10},
    ]
    # pass

    sort_by(jobs, "min_salary")
    assert jobs == salary_to_sort
