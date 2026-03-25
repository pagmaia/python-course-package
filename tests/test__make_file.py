import pytest


@pytest.fixture(scope="session")
def project():
    print("setup")
    yield 1
    print("Teardown")


def test__linting_passes(project):
    assert False


def test__tests_pass(): ...


def test__install_succeds(): ...
