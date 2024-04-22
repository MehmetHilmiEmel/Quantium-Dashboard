import pytest
from app_task4 import app

@pytest.fixture


def test_header_exists( dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualizer"


def test_question_exists( dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h3").text == "The question is : Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"

def test_answer_exists( dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h3").text == "The answer is : Sales were higher after the Pink Morsel price increase on the 15th of January, 2021"
