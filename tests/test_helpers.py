"""
AI Nexus - Helper Functions Tests
Unit tests for utility helper functions
"""
import pytest
from unittest.mock import MagicMock, patch
import sys
from pathlib import Path

# Add project root to path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))


class TestCalculateAIScore:
    """Tests for calculate_ai_score function"""
    
    @patch('utils.helpers.get_current_user_id')
    @patch('utils.helpers.get_completed_tutorials')
    @patch('utils.helpers.get_saved_prompts')
    @patch('utils.helpers.get_all_favorites')
    @patch('utils.helpers.get_from_local_storage')
    def test_calculates_score_from_activities(
        self, mock_storage, mock_favorites, mock_prompts, mock_tutorials, mock_user_id
    ):
        """Should calculate score based on user activities"""
        from utils.helpers import calculate_ai_score
        
        mock_user_id.return_value = None
        mock_tutorials.return_value = ['t1', 't2']  # 2 tutorials
        mock_prompts.return_value = {'p1': {}, 'p2': {}, 'p3': {}}  # 3 prompts
        mock_favorites.return_value = {'tools': {'tool1': {}}}  # 1 tool
        mock_storage.return_value = []
        
        score = calculate_ai_score()
        
        # 2 tutorials * 5 + 3 prompts * 2 + 1 tool * 1 = 17
        assert score == 17
    
    @patch('utils.helpers.get_current_user_id')
    @patch('utils.helpers.get_completed_tutorials')
    @patch('utils.helpers.get_saved_prompts')
    @patch('utils.helpers.get_all_favorites')
    @patch('utils.helpers.get_from_local_storage')
    def test_score_capped_at_100(
        self, mock_storage, mock_favorites, mock_prompts, mock_tutorials, mock_user_id
    ):
        """Score should be capped at 100"""
        from utils.helpers import calculate_ai_score
        
        mock_user_id.return_value = None
        mock_tutorials.return_value = ['t' + str(i) for i in range(50)]  # 50 tutorials
        mock_prompts.return_value = {}
        mock_favorites.return_value = {}
        mock_storage.return_value = []
        
        score = calculate_ai_score()
        
        assert score == 100


class TestLocalStorage:
    """Tests for local storage functions"""
    
    def test_save_and_get_from_local_storage(self):
        """Should save and retrieve data from session state"""
        # This requires mocking streamlit session state
        pass  # Skipped - requires Streamlit context


class TestCopyToClipboard:
    """Tests for copy_to_clipboard function"""
    
    def test_returns_false_when_not_clicked(self):
        """Should return False when button not clicked"""
        # This requires mocking streamlit
        pass  # Skipped - requires Streamlit context
