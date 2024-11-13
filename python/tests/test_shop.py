import pytest
from shop import Shop, User


def test_happy_path(user_base):

    assert Shop.can_order(user_base)
    assert not Shop.must_pay_foreign_fee(user_base)


def test_minors_cannot_order_from_the_shop(user_minor):
    assert not Shop.can_order(user_minor)

# Ce test va échouer parce que le code qui implémente cette foncionnalité n'est pas cohérent
def test_cannot_order_if_not_verified(user_not_verified):
    assert not Shop.can_order(user_not_verified), f'La propriété Verified de User {user_not_verified} est False mais il arrive quand même à commander'


def test_foreigners_must_be_foreign_fee(user_foreign):
    assert Shop.must_pay_foreign_fee(user_foreign)
