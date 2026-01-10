"""
AI Nexus - Content Report Generator
Generates detailed reports about content status and metrics
"""
import sys
from pathlib import Path
from datetime import datetime

# Add root to path
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))


def generate_content_report():
    """Generate comprehensive content report"""
    
    try:
        from data.final_tutorials import get_all_tutorials
        from data.final_prompts import get_all_prompts
        from data.final_assets import get_all_tools
        from data.ai_hacks import get_all_hacks
        from data.ai_news import get_all_news, get_trending_topics
        
        tutorials = get_all_tutorials()
        prompts = get_all_prompts()
        tools = get_all_tools()
        hacks = get_all_hacks()
        news = get_all_news()
        trending = get_trending_topics()
        
        report = f"""
# AI Nexus Content Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 Content Overview

| Category | Count | Status |
|----------|-------|--------|
| 📚 Tutorials | {len(tutorials)} | {'✅ Good' if len(tutorials) >= 25 else '⚠️ Need more'} |
| 💡 Prompts | {len(prompts)} | {'✅ Good' if len(prompts) >= 40 else '⚠️ Need more'} |
| 🛠️ Tools | {len(tools)} | {'✅ Good' if len(tools) >= 45 else '⚠️ Need more'} |
| 🔥 Hacks | {len(hacks)} | {'✅ Good' if len(hacks) >= 10 else '⚠️ Need more'} |
| 📰 News | {len(news)} | ✅ Auto-updated |

---

## 📚 Tutorials Breakdown

"""
        
        # Tutorial categories
        tutorial_categories = {}
        for tut in tutorials:
            cat = tut.get('category', 'Unknown')
            tutorial_categories[cat] = tutorial_categories.get(cat, 0) + 1
        
        report += "### By Category\n"
        for cat, count in sorted(tutorial_categories.items(), key=lambda x: x[1], reverse=True):
            report += f"- {cat}: {count}\n"
        
        # Tutorial difficulties
        tutorial_difficulties = {}
        for tut in tutorials:
            diff = tut.get('difficulty', 'Unknown')
            tutorial_difficulties[diff] = tutorial_difficulties.get(diff, 0) + 1
        
        report += "\n### By Difficulty\n"
        for diff, count in sorted(tutorial_difficulties.items(), key=lambda x: x[1], reverse=True):
            report += f"- {diff}: {count}\n"
        
        # Prompts
        report += "\n---\n\n## 💡 Prompts Breakdown\n\n"
        
        prompt_categories = {}
        for prompt in prompts:
            cat = prompt.get('category', 'Unknown')
            prompt_categories[cat] = prompt_categories.get(cat, 0) + 1
        
        report += "### By Category\n"
        for cat, count in sorted(prompt_categories.items(), key=lambda x: x[1], reverse=True):
            report += f"- {cat}: {count}\n"
        
        # Tools
        report += "\n---\n\n## 🛠️ Tools Breakdown\n\n"
        
        tool_categories = {}
        for tool in tools:
            cat = tool.get('category', 'Unknown')
            tool_categories[cat] = tool_categories.get(cat, 0) + 1
        
        report += "### By Category\n"
        for cat, count in sorted(tool_categories.items(), key=lambda x: x[1], reverse=True):
            report += f"- {cat}: {count}\n"
        
        tool_pricing = {}
        for tool in tools:
            price = tool.get('pricing', 'Unknown')
            tool_pricing[price] = tool_pricing.get(price, 0) + 1
        
        report += "\n### By Pricing\n"
        for price, count in sorted(tool_pricing.items(), key=lambda x: x[1], reverse=True):
            report += f"- {price}: {count}\n"
        
        # Hacks
        report += "\n---\n\n## 🔥 Hacks Breakdown\n\n"
        
        hack_categories = {}
        for hack in hacks:
            cat = hack.get('category', 'Unknown')
            hack_categories[cat] = hack_categories.get(cat, 0) + 1
        
        report += "### By Category\n"
        for cat, count in sorted(hack_categories.items(), key=lambda x: x[1], reverse=True):
            report += f"- {cat}: {count}\n"
        
        hack_difficulties = {}
        for hack in hacks:
            diff = hack.get('difficulty', 'Unknown')
            hack_difficulties[diff] = hack_difficulties.get(diff, 0) + 1
        
        report += "\n### By Difficulty\n"
        for diff, count in sorted(hack_difficulties.items(), key=lambda x: x[1], reverse=True):
            report += f"- {diff}: {count}\n"
        
        hack_tools = {}
        for hack in hacks:
            tool = hack.get('tool', 'Unknown')
            hack_tools[tool] = hack_tools.get(tool, 0) + 1
        
        report += "\n### By Tool\n"
        for tool, count in sorted(hack_tools.items(), key=lambda x: x[1], reverse=True):
            report += f"- {tool}: {count}\n"
        
        # News
        report += "\n---\n\n## 📰 News Status\n\n"
        report += f"- Total articles: {len(news)}\n"
        report += f"- Trending topics: {len(trending)}\n"
        
        if trending:
            report += "\n### Top Trending Topics\n"
            for topic in trending[:5]:
                report += f"- {topic['topic']}: {topic['count']} mentions\n"
        
        # Recommendations
        report += "\n---\n\n## 💡 Recommendations\n\n"
        
        recommendations = []
        
        if len(tutorials) < 50:
            recommendations.append(f"- Add {50 - len(tutorials)} more tutorials to reach 50")
        
        if len(prompts) < 100:
            recommendations.append(f"- Add {100 - len(prompts)} more prompts to reach 100")
        
        if len(tools) < 75:
            recommendations.append(f"- Add {75 - len(tools)} more tools to reach 75")
        
        if len(hacks) < 25:
            recommendations.append(f"- Add {25 - len(hacks)} more hacks to reach 25")
        
        # Check for underrepresented categories
        if tutorial_categories:
            min_tut_cat = min(tutorial_categories.values())
            if min_tut_cat < 3:
                recommendations.append("- Balance tutorial categories (some have < 3 items)")
        
        if hack_tools:
            if len(hack_tools) < 8:
                recommendations.append("- Add hacks for more AI tools (currently covering " + str(len(hack_tools)) + " tools)")
        
        if recommendations:
            for rec in recommendations:
                report += rec + "\n"
        else:
            report += "✅ All content goals met!\n"
        
        report += "\n---\n\n"
        report += "**Next Update:** Add content following `docs/CONTENT_UPDATE_GUIDE.md`\n"
        
        return report
        
    except Exception as e:
        return f"❌ Error generating report: {e}"


def main():
    """Main report function"""
    print("📊 Generating Content Report...")
    
    report = generate_content_report()
    
    # Save to file
    report_file = ROOT_DIR / "docs" / "CONTENT_REPORT.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Report saved to: {report_file}")
    print("\n" + "=" * 50)
    print(report)
    print("=" * 50)


if __name__ == "__main__":
    main()
