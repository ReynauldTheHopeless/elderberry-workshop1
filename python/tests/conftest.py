import pytest
from shop import Address, User


@pytest.fixture
def fsf_address():
    return Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")


@pytest.fixture
def paris_address():
    return Address("33 quai d'Orsay", "", "Paris", "75007", "France")


@pytest.fixture
def user_base(fsf_address):
    return User("Bob","bob@gmail.com",25,address=fsf_address,verified=True)

@pytest.fixture
def user_minor(user_base):
    user_base.age = 16
    return user_base

@pytest.fixture
def user_not_verified(user_base):
    user_base.verified = False
    return user_base

@pytest.fixture
def user_foreign(user_base,paris_address):
    user_base.address = paris_address

    return user_base




