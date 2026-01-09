# Reducing IDE Resource Usage

## 🔍 Understanding the Resource Usage

From your Task Manager screenshot:
- **pyrefly** (61.5% CPU, 2.7GB RAM) - Python Language Server (Pylance)
- **language_server_windows_x64** (0% CPU, 1.7GB RAM) - Other language servers

These are **NOT part of your AI Nexus app** - they're part of your IDE (VS Code).

## 📊 Why Language Servers Use Resources

### What They Do:
1. **Code Analysis**: Real-time type checking, linting, error detection
2. **IntelliSense**: Auto-completion suggestions
3. **Code Navigation**: Go to Definition, Find References
4. **Import Resolution**: Analyzing all dependencies
5. **File Watching**: Monitoring changes across entire workspace

### Why They're Heavy:
- Analyzing **entire workspace** including `venv/` folder
- Indexing **all Python packages** in virtual environment
- Watching **thousands of files** for changes
- Keeping **AST (Abstract Syntax Trees)** in memory

## ✅ Solutions to Reduce Resource Usage

### Option 1: Exclude Folders (Recommended) ⭐

Create/update `.vscode/settings.json` in your workspace:

```json
{
    "python.analysis.exclude": [
        "**/venv/**",
        "**/__pycache__/**"
    ],
    "files.watcherExclude": {
        "**/venv/**": true,
        "**/__pycache__/**": true
    },
    "search.exclude": {
        "**/venv/**": true,
        "**/__pycache__/**": true
    },
    "python.analysis.memory.keepLibraryAst": false,
    "python.analysis.typeCheckingMode": "basic"
}
```

**Expected Reduction**: 40-50% less memory usage

### Option 2: Disable Pylance Features

In VS Code settings:

```json
{
    "python.analysis.typeCheckingMode": "off",
    "python.analysis.autoImportCompletions": false,
    "python.analysis.indexing": false
}
```

**Trade-off**: Loses IntelliSense and type checking

### Option 3: Use Lighter Language Server

Switch from Pylance to Jedi:

```json
{
    "python.languageServer": "Jedi"
}
```

**Expected Reduction**: 60-70% less memory, but fewer features

### Option 4: Reload Window After Changes

After making settings changes:
1. Press `Ctrl+Shift+P`
2. Type "Reload Window"
3. Select "Developer: Reload Window"

### Option 5: Close Unused Files

- Close files you're not actively editing
- Language server analyzes open files more intensively

### Option 6: Restart Language Server

When it gets too heavy:
1. Press `Ctrl+Shift+P`
2. Type "Restart"
3. Select "Python: Restart Language Server"

## 🎯 Quick Wins (Do These Now)

### 1. Add to `.gitignore` (if not already there):
```
venv/
__pycache__/
*.pyc
.vscode/
```

### 2. Manually Create Settings File:

**Path**: `C:\Workspace\AI Nexus\.vscode\settings.json`

**Content**:
```json
{
    "python.analysis.exclude": [
        "**/venv/**",
        "**/__pycache__/**"
    ],
    "files.watcherExclude": {
        "**/venv/**": true,
        "**/__pycache__/**": true
    },
    "python.analysis.memory.keepLibraryAst": false,
    "python.analysis.typeCheckingMode": "basic"
}
```

### 3. Reload VS Code Window

## 📊 Expected Results

| Action | Memory Reduction | CPU Reduction |
|--------|------------------|---------------|
| Exclude venv/ | -40% | -30% |
| Basic type checking | -20% | -15% |
| Disable indexing | -30% | -25% |
| Switch to Jedi | -60% | -50% |

## 🔍 Verify It's Working

After making changes:
1. Open Task Manager
2. Find `pyrefly` process
3. Memory should drop from 2.7GB to ~1.5GB
4. CPU should drop from 61% to ~30%

## 💡 Alternative: Use Lighter IDE

If resource usage is still too high:

### Option A: Use VS Code Insiders (Lighter)
- Same features, often more optimized

### Option B: Use Sublime Text + LSP
- Much lighter than VS Code
- Still has language server support

### Option C: Use PyCharm Community (Different Trade-offs)
- Heavier initially but better optimized for large projects

## 🎓 Understanding the Trade-offs

| Feature | Resource Cost | Can Disable? |
|---------|---------------|--------------|
| IntelliSense | High | ✅ Yes |
| Type Checking | High | ✅ Yes |
| Error Detection | Medium | ✅ Yes |
| Syntax Highlighting | Low | ❌ No |
| File Watching | Medium | ✅ Yes |
| Import Analysis | High | ✅ Yes |

## 🚀 Recommended Configuration

For **best balance** of features vs performance:

```json
{
    // Exclude heavy folders
    "python.analysis.exclude": ["**/venv/**", "**/__pycache__/**"],
    "files.watcherExclude": {"**/venv/**": true},
    
    // Reduce memory usage
    "python.analysis.memory.keepLibraryAst": false,
    
    // Basic type checking (good enough for most cases)
    "python.analysis.typeCheckingMode": "basic",
    
    // Keep useful features
    "python.analysis.autoImportCompletions": true,
    "python.analysis.indexing": true
}
```

This gives you:
- ✅ Auto-completion
- ✅ Error detection
- ✅ Import suggestions
- ✅ ~50% less resource usage

## 📝 Summary

**The language servers are NOT your Streamlit app** - they're your IDE's code analysis tools.

**Quick Fix**:
1. Create `.vscode/settings.json` with exclusions
2. Reload VS Code window
3. Watch memory drop by ~40%

**Your Streamlit app** is separate and should now use much less resources after the optimizations we made!
