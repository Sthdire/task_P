from resources.mass_mailing import Mass


def test_mailing_good():
    mass = Mass()
    assert mass.get(ml_name='ml_name') == {'if 200 all is ok': 200}
