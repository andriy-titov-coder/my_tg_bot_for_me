import pytest
from src.utils import load_message, load_prompt

def test_load_message_success():
    content = load_message("start")
    assert isinstance(content, str)
    assert len(content) > 0

def test_load_prompt_success():
    content = load_prompt("gpt")
    assert "Telegram" in content

def test_load_message_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_message("non_existent_file")