import pytest
from src.agents.session_history import get_session_history, store
from langchain_core.chat_history import InMemoryChatMessageHistory

def test_get_session_history_new_session():
    # Clear the store before test
    store.clear()
    
    session_id = "test_session_1"
    history = get_session_history(session_id)
    
    assert isinstance(history, InMemoryChatMessageHistory)
    assert session_id in store
    assert store[session_id] == history

def test_get_session_history_existing_session():
    # Clear the store before test
    store.clear()
    
    session_id = "test_session_2"
    first_history = get_session_history(session_id)
    second_history = get_session_history(session_id)
    
    assert first_history == second_history 