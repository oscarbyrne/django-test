from core.services import ion_test


@ion_test
def test_smelliness(butt):
    assert butt.is_smelly()
