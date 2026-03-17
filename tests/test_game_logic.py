import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import check_guess

def test_winning_guess():
    """Test that guessing the exact secret number returns Win."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high_returns_correct_outcome():
    """Test that guess > secret returns 'Too High' outcome."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_high_says_go_lower():
    """BUG FIX: When guess is too high, message should say 'Go LOWER!'"""
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_guess_too_low_returns_correct_outcome():
    """Test that guess < secret returns 'Too Low' outcome."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_low_says_go_higher():
    """BUG FIX: When guess is too low, message should say 'Go HIGHER!'"""
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_check_guess_with_integers_only():
    """BUG FIX: Ensure check_guess works with integers without string conversion."""
    # The old buggy code converted secret to string on even attempts
    # This test ensures we always compare integers
    outcome1, _ = check_guess(75, 50)
    outcome2, _ = check_guess(25, 50)
    assert outcome1 == "Too High"
    assert outcome2 == "Too Low"

def test_edge_case_guess_one_above():
    """Test guess exactly one above secret."""
    outcome, message = check_guess(51, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_edge_case_guess_one_below():
    """Test guess exactly one below secret."""
    outcome, message = check_guess(49, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
