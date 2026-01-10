"""
AI Nexus - Enums and Constants
Centralized enum definitions to replace magic strings throughout the codebase
"""
from enum import Enum


class TutorialType(str, Enum):
    """Tutorial category prefixes"""
    QUICK_WIN = "qw"
    DEEP_DIVE = "dd"
    MASTERY_TRACK = "mt"
    
    @classmethod
    def get_prefix(cls, tutorial_id: str) -> str:
        """Extract prefix from tutorial ID"""
        if '-' in tutorial_id:
            return tutorial_id.split('-')[0]
        return ''
    
    @classmethod
    def is_quick_win(cls, tutorial_id: str) -> bool:
        return tutorial_id.startswith(f"{cls.QUICK_WIN.value}-")
    
    @classmethod
    def is_deep_dive(cls, tutorial_id: str) -> bool:
        return tutorial_id.startswith(f"{cls.DEEP_DIVE.value}-")
    
    @classmethod
    def is_mastery_track(cls, tutorial_id: str) -> bool:
        return tutorial_id.startswith(f"{cls.MASTERY_TRACK.value}-")


class ActivityType(str, Enum):
    """User activity types for tracking"""
    TUTORIAL_VIEWED = "tutorial_viewed"
    TUTORIAL_COMPLETED = "tutorial_completed"
    PROMPT_SAVED = "prompt_saved"
    PROMPT_VIEWED = "prompt_viewed"
    TOOL_VIEWED = "tool_viewed"
    TOOL_FAVORITE = "tool_favorite"
    FAVORITE_ADDED = "favorite_added"
    FAVORITE_REMOVED = "favorite_removed"
    ASSESSMENT_STARTED = "assessment_started"
    ASSESSMENT_COMPLETED = "assessment_completed"
    PROFILE_UPDATED = "profile_updated"
    SEARCH_PERFORMED = "search_performed"


class ItemType(str, Enum):
    """Item types for favorites and activities"""
    TOOL = "tool"
    PROMPT = "prompt"
    TUTORIAL = "tutorial"


class DifficultyLevel(str, Enum):
    """Tutorial and prompt difficulty levels"""
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    COMPREHENSIVE = "Comprehensive"
    
    @classmethod
    def get_color(cls, difficulty: str) -> str:
        """Get color code for difficulty level"""
        colors = {
            cls.BEGINNER.value: "#10B981",
            cls.INTERMEDIATE.value: "#F59E0B",
            cls.ADVANCED.value: "#EF4444",
            cls.COMPREHENSIVE.value: "#6366F1"
        }
        return colors.get(difficulty, "#64748B")


class SkillLevel(str, Enum):
    """User skill levels"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"
    
    @classmethod
    def from_score(cls, score: int) -> 'SkillLevel':
        """Determine skill level from AI score"""
        if score >= 76:
            return cls.EXPERT
        elif score >= 51:
            return cls.ADVANCED
        elif score >= 26:
            return cls.INTERMEDIATE
        return cls.BEGINNER


class PromptCategory(str, Enum):
    """Prompt categories"""
    CODING = "coding"
    DEBUGGING = "debugging"
    TESTING = "testing"
    DOCUMENTATION = "documentation"
    ARCHITECTURE = "architecture"
    CODE_REVIEW = "code_review"
    REFACTORING = "refactoring"
    LEARNING = "learning"
    PRODUCTIVITY = "productivity"
    COMMUNICATION = "communication"
    DEVOPS_INFRA = "devops_infra"
    SECURITY = "security"
    CONTENT_CREATION = "content_creation"
    DATA_ANALYSIS = "data_analysis"


class ToolCategory(str, Enum):
    """AI tool categories"""
    CODE_GENERATION = "code_generation"
    TESTING_QA = "testing_qa"
    PROJECT_MANAGEMENT = "project_management"
    DOCUMENTATION = "documentation"
    DESIGN_PROTOTYPING = "design_prototyping"
    DATA_ANALYSIS = "data_analysis"
    COMMUNICATION = "communication"
    DEVOPS_INFRA = "devops_infra"
    SECURITY = "security"
    RESEARCH_LEARNING = "research_learning"
    PRODUCTIVITY = "productivity"
    CONTENT_CREATION = "content_creation"


class AssessmentCategory(str, Enum):
    """Assessment question categories"""
    CONCEPTS = "Concepts"
    ENGINEERING = "Engineering"
    PROMPTING = "Prompting"
    ARCHITECTURE = "Architecture"
    AGENTS = "Agents"
    SAFETY = "Safety"
    PARAMETERS = "Parameters"
    FUNDAMENTALS = "Fundamentals"
    SECURITY = "Security"
