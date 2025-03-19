import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will executed last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Rahul", "shetty"), ("firefox", "Shetty"), ("IE", "SS")])
def crossBrowser(request):
    return request.param