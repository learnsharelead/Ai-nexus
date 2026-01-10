"""
AI Nexus - Tutorial Data Tests
Unit tests for tutorial data functions
"""
import pytest
from data.final_tutorials import (
    get_all_tutorials,
    get_tutorials_by_category,
    get_tutorials_by_role,
    get_tutorials_by_difficulty,
    search_tutorials,
    get_popular_tutorials
)


class TestGetAllTutorials:
    """Tests for get_all_tutorials function"""
    
    def test_returns_list(self):
        """Should return a list"""
        result = get_all_tutorials()
        assert isinstance(result, list)
    
    def test_tutorials_have_required_fields(self):
        """Each tutorial should have required fields"""
        required_fields = ['id', 'title', 'category', 'duration', 'difficulty']
        tutorials = get_all_tutorials()
        
        for tutorial in tutorials:
            for field in required_fields:
                assert field in tutorial, f"Tutorial {tutorial.get('id')} missing field: {field}"
    
    def test_tutorial_ids_are_valid(self):
        """All tutorial IDs should start with valid prefixes"""
        valid_prefixes = ('qw-', 'dd-', 'mt-')
        tutorials = get_all_tutorials()
        
        for tutorial in tutorials:
            assert tutorial['id'].startswith(valid_prefixes), \
                f"Invalid tutorial ID prefix: {tutorial['id']}"
    
    def test_no_duplicate_ids(self):
        """Tutorial IDs should be unique"""
        tutorials = get_all_tutorials()
        ids = [t['id'] for t in tutorials]
        assert len(ids) == len(set(ids)), "Duplicate tutorial IDs found"


class TestSearchTutorials:
    """Tests for search_tutorials function"""
    
    def test_empty_query_returns_empty_list(self):
        """Empty query should return empty list"""
        result = search_tutorials("")
        assert result == []
    
    def test_none_query_returns_empty_list(self):
        """None query should return empty list"""
        result = search_tutorials(None)
        assert result == []
    
    def test_search_finds_matching_titles(self):
        """Should find tutorials with matching titles"""
        result = search_tutorials("RAG")
        assert len(result) > 0
        assert any("RAG" in t['title'] for t in result)
    
    def test_search_is_case_insensitive(self):
        """Search should be case insensitive"""
        result_lower = search_tutorials("rag")
        result_upper = search_tutorials("RAG")
        assert len(result_lower) == len(result_upper)


class TestGetTutorialsByCategory:
    """Tests for get_tutorials_by_category function"""
    
    def test_all_category_returns_all(self):
        """'All' category should return all tutorials"""
        result = get_tutorials_by_category("All")
        all_tutorials = get_all_tutorials()
        # Note: May differ due to filtering in get_all_tutorials
        assert len(result) >= len(all_tutorials)
    
    def test_filters_by_category(self):
        """Should filter by specified category"""
        result = get_tutorials_by_category("Generative AI")
        for tutorial in result:
            assert tutorial['category'].lower() == "generative ai"


class TestGetPopularTutorials:
    """Tests for get_popular_tutorials function"""
    
    def test_respects_limit(self):
        """Should return at most 'limit' tutorials"""
        result = get_popular_tutorials(3)
        assert len(result) <= 3
    
    def test_sorted_by_completions_desc(self):
        """Should be sorted by completions descending"""
        result = get_popular_tutorials(10)
        completions = [t.get('completions', 0) for t in result]
        assert completions == sorted(completions, reverse=True)
