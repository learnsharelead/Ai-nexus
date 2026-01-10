"""
AI Nexus - Prompt Data Tests
Unit tests for prompt data functions
"""
import pytest
from data.final_prompts import (
    get_all_prompts,
    get_prompts_by_category,
    get_prompts_by_difficulty,
    search_prompts,
    get_popular_prompts,
    get_prompt_by_id
)


class TestGetAllPrompts:
    """Tests for get_all_prompts function"""
    
    def test_returns_list(self):
        """Should return a list"""
        result = get_all_prompts()
        assert isinstance(result, list)
    
    def test_prompts_have_required_fields(self):
        """Each prompt should have required fields"""
        required_fields = ['id', 'title', 'category', 'prompt', 'difficulty']
        prompts = get_all_prompts()
        
        for prompt in prompts:
            for field in required_fields:
                assert field in prompt, f"Prompt {prompt.get('id')} missing field: {field}"
    
    def test_no_duplicate_ids(self):
        """Prompt IDs should be unique"""
        prompts = get_all_prompts()
        ids = [p['id'] for p in prompts]
        assert len(ids) == len(set(ids)), "Duplicate prompt IDs found"


class TestSearchPrompts:
    """Tests for search_prompts function"""
    
    def test_empty_query_returns_empty_list(self):
        """Empty query should return empty list"""
        result = search_prompts("")
        assert result == []
    
    def test_search_finds_matching_titles(self):
        """Should find prompts with matching titles"""
        result = search_prompts("SQL")
        assert len(result) > 0
    
    def test_search_finds_in_prompt_text(self):
        """Should find prompts with matching prompt text"""
        result = search_prompts("code")
        assert len(result) > 0


class TestGetPromptById:
    """Tests for get_prompt_by_id function"""
    
    def test_returns_prompt_for_valid_id(self):
        """Should return prompt for valid ID"""
        result = get_prompt_by_id("p-1")
        assert result is not None
        assert result['id'] == "p-1"
    
    def test_returns_none_for_invalid_id(self):
        """Should return None for invalid ID"""
        result = get_prompt_by_id("invalid-id")
        assert result is None


class TestGetPopularPrompts:
    """Tests for get_popular_prompts function"""
    
    def test_respects_limit(self):
        """Should return at most 'limit' prompts"""
        result = get_popular_prompts(5)
        assert len(result) <= 5
    
    def test_sorted_by_uses_desc(self):
        """Should be sorted by uses descending"""
        result = get_popular_prompts(10)
        uses = [p.get('uses', 0) for p in result]
        assert uses == sorted(uses, reverse=True)
