from santag.convertor import convert
from santag.domain_model.rules import Rules


def test_empty() -> None:
    assert list(convert([], Rules(substitutions=[]))) == []
