# GitHub Secrets Configuration for Qodo Merge

## Setup required secrets:

1. **OPENAI_KEY** (required)
   - Get from: https://platform.openai.com/api-keys
   - Select: `gpt-4` or `gpt-3.5-turbo` models
   - Steps:
     ```
     a) Go to https://platform.openai.com
     b) Navigate to API keys
     c) Create new secret key
     d) Copy the key
     ```

2. **GITHUB_TOKEN** (auto-provided by GitHub)
   - This is automatically available in GitHub Actions
   - No manual setup needed

## How to set secrets:

1. Go to repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Add:
   - Name: `OPENAI_KEY`
   - Value: [your OpenAI API key]
4. Click "Add secret"

## Test the workflow:

1. Create a test branch:
   ```bash
   git checkout -b test/qodo-review
   ```

2. Make some code changes (file with issues already exists)

3. Commit and push:
   ```bash
   git add .
   git commit -m "test: changes for qodo review"
   git push -u origin test/qodo-review
   ```

4. Create PR on GitHub
5. Watch Qodo Merge review the PR automatically!

## Expected Qodo Review output:

✅ PR Summary - tóm tắt thay đổi
🔍 Code Review - comment trên các issues
💡 Suggestions - gợi ý improvements
🐛 Bug Detection - phát hiện potential bugs
📋 File-by-file Analysis - phân tích chi tiết
