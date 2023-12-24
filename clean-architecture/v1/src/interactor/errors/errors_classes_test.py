import pytest
from src.interactor.errors.errors_classes \
    import FieldValueNotPermittedException


def test_empty_field_exception():
    with pytest.raises(FieldValueNotPermittedException) as exception_info:
        raise FieldValueNotPermittedException("name", "Profession")
    assert str(exception_info.value) == "Name: Profession is not permitted"