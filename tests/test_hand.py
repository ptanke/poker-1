from rangeparser import Hand, Rank, InvalidHand
from pytest import raises


def test_first_and_second_are_instances_of_Rank():
    assert isinstance(Hand('22').first, Rank)
    assert Hand('22').first == Rank('2')
    assert isinstance(Hand('22').second, Rank)
    assert Hand('22').second == Rank('2')


def test_representations():
    assert str(Hand('22')) == '22'
    assert str(Hand('AKs')) == 'AKs'
    assert str(Hand('KJo')) == 'KJo'
    assert repr(Hand('22')) == "Hand('22')"


def test_ordering():
    assert Hand('AKo') > Hand('AQs')

    assert Hand('AKo') > Hand('KQo')
    assert Hand('AKs') > Hand('54o')
    assert Hand('AJo') > Hand('A2s')
    assert Hand('AJo') > Hand('A2o')
    assert Hand('KQo') > Hand('KJo')
    assert Hand('76s') > Hand('75s')
    assert Hand('76o') > Hand('75s')

    assert Hand('33') > Hand('22')
    assert Hand('22') > Hand('JTo')
    assert Hand('22') > Hand('A2o')
    assert Hand('22') > Hand('A3s')
    assert Hand('JJ') > Hand('JTs')
    assert Hand('JJ') > Hand('AJs')

    assert Hand('76s') > Hand('76o')


def test_ordering_reverse():
    assert Hand('AQs') < Hand('AKo')

    assert Hand('KQo') < Hand('AKo')
    assert Hand('54o') < Hand('AKs')
    assert Hand('A2s') < Hand('AJo')
    assert Hand('A2o') < Hand('AJo')
    assert Hand('KJo') < Hand('KQo')
    assert Hand('75s') < Hand('76s')
    assert Hand('75s') < Hand('76o')

    assert Hand('22') < Hand('33')
    assert Hand('JTo') < Hand('22')
    assert Hand('A2o') < Hand('22')
    assert Hand('A3s') < Hand('22')
    assert Hand('JTs') < Hand('JJ')
    assert Hand('AJs') < Hand('JJ')

    assert Hand('76o') < Hand('76s')


def test_only_same_suits_are_equal():
    assert Hand('AKo') == Hand('AKo')
    assert Hand('AKo') != Hand('AKs')


def test_case_insensitive():
    assert Hand('AKo') == Hand('akO')
    assert Hand('jks') == Hand('JKS')


def test_equality():
    assert Hand('AKs') != Hand('44')
    assert Hand('22') != Hand('33')
    assert Hand('22') == Hand('22')


def test_is_suited():
    assert Hand('AKs').is_suited() is True

    assert Hand('AKo').is_suited() is False
    assert Hand('22').is_suited() is False


def test_is_offsuit():
    assert Hand('AKs').is_offsuit() is False
    assert Hand('AKo').is_offsuit() is True
    assert Hand('22').is_offsuit() is False


def test_is_connector():
    assert Hand('76o').is_connector() is True
    assert Hand('AKo').is_connector() is True

    assert Hand('22').is_connector() is False
    assert Hand('85o').is_connector() is False


def test_is_one_gapper():
    assert Hand('86s').is_one_gapper() is True
    assert Hand('AQo').is_one_gapper() is True


def test_is_two_gapper():
    assert Hand('85s').is_two_gapper() is True
    assert Hand('AJo').is_two_gapper() is True

    assert Hand('86s').is_two_gapper() is False
    assert Hand('ATo').is_two_gapper() is False


def test_is_suited_connector():
    assert Hand('76s').is_suited_connector() is True
    assert Hand('45s').is_suited_connector() is True

    assert Hand('55').is_suited_connector() is False
    assert Hand('76o').is_suited_connector() is False


def test_is_broadway():
    assert Hand('AKo').is_broadway() is True
    assert Hand('J9o').is_broadway() is False
    assert Hand('99').is_broadway() is False


def test_is_pair():
    assert Hand('22').is_pair() is True
    assert Hand('86s').is_pair() is False


def test_invalid_suit():
    with raises(InvalidHand):
        Hand('32l')


def test_invalid_rank():
    with raises(InvalidHand):
        Hand('AMs')


def test_pair_with_suit():
    with raises(InvalidHand):
        Hand('22s')


def test_hand_without_suit():
    with raises(InvalidHand):
        Hand('AK')