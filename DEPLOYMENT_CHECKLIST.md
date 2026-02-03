# 🚀 Quick Deployment Checklist

Use this checklist to deploy Recipe AI to Streamlit Cloud in 10 minutes!

---

## ✅ Pre-Deployment (Already Done!)

- [x] Code pushed to GitHub: https://github.com/Rthomp61/Recipe-AI
- [x] requirements.txt created
- [x] .gitignore excludes secrets
- [x] Streamlit config added
- [x] Deployment guide created

---

## 📋 Deployment Steps (Do This Now!)

### Step 1: Create Account (2 min)
- [ ] Go to https://streamlit.io/cloud
- [ ] Click "Sign in with GitHub"
- [ ] Authorize Streamlit to access your GitHub

### Step 2: Create New App (1 min)
- [ ] Click "New app" button
- [ ] Fill in:
  - **Repository:** `Rthomp61/Recipe-AI`
  - **Branch:** `main`
  - **Main file:** `app.py`

### Step 3: Add API Key (1 min) ⚠️ CRITICAL!
- [ ] Click "Advanced settings"
- [ ] Find "Secrets" section
- [ ] Paste this EXACTLY:
```toml
GEMINI_API_KEY = "AIzaSyBZCdrlZ2-rwpPpL5h0KjvHB2aItqc-OxE"
```
- [ ] Click "Save"

### Step 4: Deploy (3 min)
- [ ] Click "Deploy!" button
- [ ] Wait for build to complete (watch the logs)
- [ ] App opens automatically when ready

### Step 5: Test (2 min)
- [ ] Add test ingredients: `chicken, tomatoes, rice, garlic`
- [ ] Click "Generate Recipe"
- [ ] Verify recipe appears
- [ ] Test download button

---

## 🎉 Post-Deployment

- [ ] Copy your app URL (looks like: `https://recipe-ai-xxx.streamlit.app`)
- [ ] Test from different device
- [ ] Share with 3 friends for feedback
- [ ] Add URL to GitHub README

---

## 📝 Your App URL

Once deployed, write your URL here:

**Live App:** ________________________________

---

## 🆘 Having Issues?

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed troubleshooting.

**Common fixes:**
- API key not working → Check secrets formatting (no extra quotes/spaces)
- App won't start → Check build logs for errors
- Slow generation → Normal! AI takes 10-20 seconds

---

## ⏱️ Total Time: ~10 minutes

You're ready to deploy! Follow the steps above and your app will be live! 🚀
