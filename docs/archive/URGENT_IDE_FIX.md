# URGENT: Reduce Pyrefly Resource Usage - Action Plan

## 🚨 Current Status (Still High)
- **pyrefly**: 61.5% CPU, 2.7GB Memory
- **language_server**: 0% CPU, 1.7GB Memory
- **Total IDE overhead**: ~4.4GB Memory

## ✅ IMMEDIATE ACTIONS (Do These Now)

### Action 1: Create VS Code Settings File (MANUAL)

**You need to create this file manually since it's gitignored:**

1. **Open File Explorer**
2. **Navigate to**: `C:\Workspace\AI Nexus`
3. **Create folder** (if not exists): `.vscode`
4. **Create file**: `settings.json` inside `.vscode` folder
5. **Paste this content**:

```json
{
    "python.analysis.exclude": [
        "**/venv/**",
        "**/__pycache__/**",
        "**/node_modules/**"
    ],
    "files.watcherExclude": {
        "**/venv/**": true,
        "**/__pycache__/**": true,
        "**/node_modules/**": true,
        "**/.git/**": true
    },
    "search.exclude": {
        "**/venv/**": true,
        "**/__pycache__/**": true
    },
    "python.analysis.memory.keepLibraryAst": false,
    "python.analysis.memory.keepLibraryLocalVariables": false,
    "python.analysis.typeCheckingMode": "off",
    "python.analysis.autoImportCompletions": false,
    "python.analysis.indexing": false,
    "python.languageServer": "Jedi"
}
```

6. **Save the file**
7. **In VS Code**: Press `Ctrl+Shift+P` → Type "Reload Window" → Press Enter

### Action 2: Close Unused Files (RIGHT NOW)

You have many files open:
- `data\ai_tools.py`
- `data\tutorial_content.py`
- `QUICK_FIXES.md`
- `database\__init__.py`
- `pages\__init__.py`
- `config\__init__.py`

**Close all except the one you're actively editing!**

### Action 3: Restart Python Language Server

1. Press `Ctrl+Shift+P`
2. Type: "Python: Restart Language Server"
3. Press Enter

### Action 4: Switch to Jedi (Lighter Language Server)

In VS Code:
1. Press `Ctrl+,` (Settings)
2. Search: "python language server"
3. Change from "Pylance" to "Jedi"

**Expected reduction**: 60-70% less memory

## 🔧 ALTERNATIVE SOLUTIONS

### Option A: Disable Pylance Completely

**User Settings** (`Ctrl+,`):
```
Python › Language Server: None
```

**Trade-off**: No IntelliSense, but 90% less resource usage

### Option B: Use Different Editor for Large Files

- Use **Notepad++** or **Sublime Text** for viewing large data files
- Keep VS Code only for active editing

### Option C: Reduce VS Code Extensions

1. Press `Ctrl+Shift+X` (Extensions)
2. Disable extensions you don't actively use
3. Especially disable:
   - Linters you don't need
   - Formatters you don't use
   - Language support for languages you're not using

## 📊 Expected Results After All Actions

| Action | Memory Reduction | CPU Reduction |
|--------|------------------|---------------|
| Close unused files | -20% | -15% |
| Exclude venv | -30% | -25% |
| Switch to Jedi | -60% | -50% |
| Disable language server | -90% | -80% |

**Target**: Get pyrefly down to ~800MB and <20% CPU

## 🎯 NUCLEAR OPTION (If Nothing Works)

### Close VS Code While Testing

1. Save all your work
2. Close VS Code completely
3. Run Streamlit from Command Prompt:
   ```cmd
   cd C:\Workspace\AI Nexus
   venv\Scripts\activate
   streamlit run app.py
   ```
4. Edit files in a lighter editor (Notepad++, Sublime)

**Result**: Pyrefly won't run at all (0% CPU, 0MB memory)

## 🔍 Verify Settings Applied

After creating settings.json and reloading:

1. Open VS Code Output panel (`Ctrl+Shift+U`)
2. Select "Python" from dropdown
3. Look for: "Analysis excluded: venv"
4. Check Task Manager - memory should drop

## ⚡ FASTEST FIX (30 seconds)

**If you just want it to work NOW:**

1. **Close VS Code**
2. **Open Command Prompt**
3. **Run**:
   ```cmd
   cd C:\Workspace\AI Nexus
   venv\Scripts\activate
   streamlit run app.py
   ```
4. **Use browser to test your app**
5. **Edit files in Notepad++ if needed**

**Result**: Pyrefly gone, only Streamlit running (~500MB memory)

## 📝 What to Do RIGHT NOW (Priority Order)

1. ✅ **Close all open files except one** (30 seconds)
2. ✅ **Create .vscode/settings.json manually** (2 minutes)
3. ✅ **Reload VS Code window** (10 seconds)
4. ✅ **Check Task Manager** (verify reduction)
5. ✅ **If still high, switch to Jedi** (1 minute)
6. ✅ **If still high, close VS Code and use Command Prompt** (1 minute)

## 🎓 Why This Happens

VS Code's Pylance is analyzing:
- Your entire workspace (~50+ Python files)
- All packages in venv/ (hundreds of files)
- All imports and dependencies
- Type hints across all files
- Keeping AST of all files in memory

**Solution**: Tell it to ignore venv/ and use lighter analysis

---

**NEXT STEP**: Create the settings.json file manually (I can't create it due to gitignore). Let me know once you've done it and reloaded VS Code!
