"""
AI Nexus - Content Validation Script
Validates all data files for completeness and correctness
"""
import sys
from pathlib import Path

# Add root to path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))


def validate_tutorials():
    """Validate tutorial data"""
    print("📚 Validating Tutorials...")
    
    try:
        from data.final_tutorials import get_all_tutorials
        tutorials = get_all_tutorials()
        
        required_fields = ['id', 'title', 'category', 'duration', 'difficulty', 'role', 'rating', 'icon', 'description']
        errors = []
        
        for tut in tutorials:
            for field in required_fields:
                if field not in tut or not tut[field]:
                    errors.append(f"  ❌ Tutorial '{tut.get('id', 'UNKNOWN')}' missing field: {field}")
        
        if errors:
            print(f"  Found {len(errors)} errors:")
            for error in errors[:10]:  # Show first 10
                print(error)
        else:
            print(f"  ✅ All {len(tutorials)} tutorials valid")
        
        return len(errors) == 0
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def validate_prompts():
    """Validate prompt data"""
    print("\n💡 Validating Prompts...")
    
    try:
        from data.final_prompts import get_all_prompts
        prompts = get_all_prompts()
        
        required_fields = ['id', 'title', 'category', 'description', 'prompt', 'use_case', 'tags']
        errors = []
        
        for prompt in prompts:
            for field in required_fields:
                if field not in prompt or not prompt[field]:
                    errors.append(f"  ❌ Prompt '{prompt.get('id', 'UNKNOWN')}' missing field: {field}")
        
        if errors:
            print(f"  Found {len(errors)} errors:")
            for error in errors[:10]:
                print(error)
        else:
            print(f"  ✅ All {len(prompts)} prompts valid")
        
        return len(errors) == 0
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def validate_tools():
    """Validate tool data"""
    print("\n🛠️  Validating Tools...")
    
    try:
        from data.final_assets import get_all_tools
        tools = get_all_tools()
        
        required_fields = ['id', 'name', 'category', 'description', 'icon', 'rating', 'pricing']
        errors = []
        
        for tool in tools:
            for field in required_fields:
                if field not in tool or not tool[field]:
                    errors.append(f"  ❌ Tool '{tool.get('id', 'UNKNOWN')}' missing field: {field}")
        
        if errors:
            print(f"  Found {len(errors)} errors:")
            for error in errors[:10]:
                print(error)
        else:
            print(f"  ✅ All {len(tools)} tools valid")
        
        return len(errors) == 0
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def validate_hacks():
    """Validate hack data"""
    print("\n🔥 Validating Hacks...")
    
    try:
        from data.ai_hacks import get_all_hacks
        hacks = get_all_hacks()
        
        required_fields = ['id', 'title', 'category', 'difficulty', 'tool', 'icon', 'description', 'hack', 'tags', 'time_saved']
        errors = []
        
        for hack in hacks:
            for field in required_fields:
                if field not in hack or not hack[field]:
                    errors.append(f"  ❌ Hack '{hack.get('id', 'UNKNOWN')}' missing field: {field}")
        
        if errors:
            print(f"  Found {len(errors)} errors:")
            for error in errors[:10]:
                print(error)
        else:
            print(f"  ✅ All {len(hacks)} hacks valid")
        
        return len(errors) == 0
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def check_duplicate_ids():
    """Check for duplicate IDs across all content"""
    print("\n🔍 Checking for Duplicate IDs...")
    
    try:
        from data.final_tutorials import get_all_tutorials
        from data.final_prompts import get_all_prompts
        from data.final_assets import get_all_tools
        from data.ai_hacks import get_all_hacks
        
        all_ids = []
        
        # Collect all IDs
        all_ids.extend([t['id'] for t in get_all_tutorials()])
        all_ids.extend([p['id'] for p in get_all_prompts()])
        all_ids.extend([t['id'] for t in get_all_tools()])
        all_ids.extend([h['id'] for h in get_all_hacks()])
        
        # Find duplicates
        seen = set()
        duplicates = []
        for id in all_ids:
            if id in seen:
                duplicates.append(id)
            seen.add(id)
        
        if duplicates:
            print(f"  ❌ Found {len(duplicates)} duplicate IDs:")
            for dup in duplicates:
                print(f"    - {dup}")
            return False
        else:
            print(f"  ✅ No duplicate IDs found ({len(all_ids)} total)")
            return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Main validation function"""
    print("🔍 AI Nexus Content Validation")
    print("=" * 50)
    
    results = {
        "tutorials": validate_tutorials(),
        "prompts": validate_prompts(),
        "tools": validate_tools(),
        "hacks": validate_hacks(),
        "duplicates": check_duplicate_ids()
    }
    
    print("\n" + "=" * 50)
    print("📊 Validation Summary")
    print("=" * 50)
    
    for name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name.title()}")
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n✅ All validations passed!")
        return 0
    else:
        print("\n❌ Some validations failed. Please fix errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
