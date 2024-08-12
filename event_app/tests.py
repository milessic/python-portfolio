import pytest
from event_app import(
        set_event_name
        )

monkeypatch = pytest.MonkeyPatch()
def test_event_name_has_to_be_have_more_characters_than_3():
     # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr("builtins.input", lambda _: "Dw")
    short_name = set_event_name()
    assert short_name == None

