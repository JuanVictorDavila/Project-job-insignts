from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    for job in read_brazilian_file("tests/mocks/brazilians_jobs.csv"):
        assert "salary" in job
        assert "title" in job
        assert "type" in job
    # pass
