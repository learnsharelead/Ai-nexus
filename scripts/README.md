# AI Nexus - Content Management Scripts

## 📋 Available Scripts

### 1. Content Report Generator
Generates detailed statistics and recommendations for content updates.

```bash
python scripts/content_report.py
```

**Output:** `docs/CONTENT_REPORT.md`

**What it does:**
- Counts all content across tabs
- Breaks down by category, difficulty, pricing
- Shows trending topics
- Provides actionable recommendations

---

### 2. Content Validator
Validates all data files for completeness and correctness.

```bash
python scripts/validate_data.py
```

**What it checks:**
- Required fields present
- No duplicate IDs
- Data format correctness
- Missing values

**Exit codes:**
- `0` = All validations passed
- `1` = Some validations failed

---

### 3. Content Updater
Updates content and checks freshness.

```bash
python scripts/update_all.py
```

**What it does:**
- Refreshes AI news cache
- Checks content freshness
- Provides suggestions for new content
- Saves update timestamp

---

## 🔄 Recommended Workflow

### Before Adding Content:
```bash
# 1. Validate existing content
python scripts/validate_data.py

# 2. Generate current report
python scripts/content_report.py

# 3. Review recommendations in docs/CONTENT_REPORT.md
```

### After Adding Content:
```bash
# 1. Validate new content
python scripts/validate_data.py

# 2. Test locally
streamlit run app.py

# 3. Generate updated report
python scripts/content_report.py

# 4. Commit changes
git add -A
git commit -m "Content update: Added X tutorials, Y prompts"
```

---

## 📊 Current Content Status

Run `python scripts/content_report.py` to see latest stats.

**Last Report:**
- 📚 Tutorials: 25
- 💡 Prompts: 40
- 🛠️ Tools: 47
- 🔥 Hacks: 10
- 📰 News: Auto-updated (62 articles)

---

## 🎯 Content Goals

### Short-term (Next 2 weeks)
- [ ] 50 tutorials
- [ ] 60 prompts
- [ ] 60 tools
- [ ] 15 hacks

### Mid-term (Next month)
- [ ] 75 tutorials
- [ ] 100 prompts
- [ ] 75 tools
- [ ] 25 hacks

### Long-term (3 months)
- [ ] 100+ tutorials
- [ ] 200+ prompts
- [ ] 100+ tools
- [ ] 50+ hacks

---

## 📝 Content Templates

See `docs/CONTENT_UPDATE_GUIDE.md` for detailed templates and instructions.

---

## 🤖 Automation

### GitHub Actions (Recommended)
Create `.github/workflows/update-content.yml` for automated updates.

### Cron Job (Linux/Mac)
```bash
# Run every 6 hours
0 */6 * * * cd /path/to/AI-Nexus && python scripts/update_all.py
```

### Windows Task Scheduler
1. Open Task Scheduler
2. Create task to run `python scripts/update_all.py`
3. Set trigger: Daily, repeat every 6 hours

---

## 🔍 Troubleshooting

**Script fails with import error:**
```bash
# Make sure you're in the project root
cd "C:\Workspace\AI Nexus"
python scripts/script_name.py
```

**Validation fails:**
- Check error messages
- Fix data files
- Re-run validation

**News not updating:**
- Check internet connection
- Verify RSS feed URLs
- Clear cache: Delete `data/last_update.json`

---

## 📞 Need Help?

See `docs/CONTENT_UPDATE_GUIDE.md` for comprehensive documentation.
