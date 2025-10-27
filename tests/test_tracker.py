"""
Integration tests for the SupplyChainTracker class.
"""

import pytest
from src.blockchain.tracker import SupplyChainTracker

@pytest.fixture
def tracker():
    """Fixture for SupplyChainTracker instance."""
    return SupplyChainTracker()

def test_start_tracking(tracker):
    """Test starting the tracker."""
    assert tracker.start_tracking()

def test_log_event(tracker):
    """Test logging an event."""
    tracker.start_tracking()
    tx_hash = tracker.log_event(1, "Test Event", "Test Location")
    assert tx_hash is not None

def test_query_history(tracker):
    """Test querying history."""
    tracker.start_tracking()
    history = tracker.query_history(1)
    assert history is not None