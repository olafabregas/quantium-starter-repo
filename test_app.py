import pytest
from dash import Dash
from app import app as dash_app

@pytest.fixture
def app():
    return dash_app

import pytest
from dash import Dash
from app import app as dash_app

@pytest.fixture
def app():
    return dash_app

def test_header_present(dash_duo, app):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.text

def test_visualisation_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-radio")
    assert radio is not None