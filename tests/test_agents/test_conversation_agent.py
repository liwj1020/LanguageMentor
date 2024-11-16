import pytest
from src.agents.conversation_agent import ConversationAgent

def test_conversation_agent_initialization():
    agent = ConversationAgent("test_session")
    
    assert agent.name == "conversation"
    assert agent.session_id == "test_session" 