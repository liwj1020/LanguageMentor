import pytest
from unittest.mock import Mock
from src.agents.scenario_agent import ScenarioAgent
from langchain_core.messages import AIMessage

def test_scenario_agent_initialization():
    agent = ScenarioAgent("job_interview", "test_session")
    
    assert agent.name == "job_interview"
    assert agent.session_id == "test_session"
    assert len(agent.intro_messages) > 0

def test_start_new_session_with_empty_history(mocker):
    # Mock the session history
    mock_history = Mock()
    mock_history.messages = []
    mocker.patch('src.agents.scenario_agent.get_session_history', return_value=mock_history)
    
    agent = ScenarioAgent("job_interview", "test_session")
    initial_message = agent.start_new_session()
    
    assert initial_message in agent.intro_messages
    mock_history.add_message.assert_called_once()

def test_start_new_session_with_existing_history(mocker):
    # Mock the session history with existing messages
    last_message = "Previous message"
    mock_history = Mock()
    mock_history.messages = [AIMessage(content=last_message)]
    mocker.patch('src.agents.scenario_agent.get_session_history', return_value=mock_history)
    
    agent = ScenarioAgent("job_interview", "test_session")
    returned_message = agent.start_new_session()
    
    assert returned_message == last_message
    mock_history.add_message.assert_not_called() 