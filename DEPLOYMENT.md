# Deployment Guide - Recipe AI

This guide walks you through deploying Recipe AI to Streamlit Community Cloud in under 10 minutes.

---

## Prerequisites

- [x] GitHub repository (already created: https://github.com/Rthomp61/Recipe-AI)
- [x] Google Gemini API key
- [ ] Streamlit Community Cloud account (free)

---

## Step-by-Step Deployment

### Step 1: Create Streamlit Cloud Account

1. Go to https://streamlit.io/cloud
2. Click **"Sign up"** or **"Sign in with GitHub"**
3. Authorize Streamlit to access your GitHub account
4. Complete the account setup

**Time:** 2 minutes

---

### Step 2: Deploy Your App

1. Once logged in, click the **"New app"** button
2. You'll see three fields to fill:

   **Repository:** `Rthomp61/Recipe-AI`

   **Branch:** `main`

   **Main file path:** `app.py`

3. Click **"Advanced settings"** (optional but recommended)

**Time:** 1 minute

---

### Step 3: Configure Secrets (IMPORTANT!)

This is the most critical step - your app won't work without the API key!

1. In the "Advanced settings" section, find **"Secrets"**
2. In the secrets text box, add:

```toml
GEMINI_API_KEY = "AIzaSyBZCdrlZ2-rwpPpL5h0KjvHB2aItqc-OxE"
```

3. Make sure there are no extra spaces or quotes issues
4. Click **"Save"**

**Time:** 1 minute

---

### Step 4: Launch!

1. Click the **"Deploy!"** button
2. Wait 2-3 minutes while Streamlit:
   - Pulls your code from GitHub
   - Installs dependencies from `requirements.txt`
   - Starts your app
3. You'll see a build log showing progress
4. Once complete, your app will automatically open

**Time:** 3 minutes

---

### Step 5: Test Your Deployed App

1. Try adding ingredients: `chicken, tomatoes, garlic, rice`
2. Select dietary restrictions (optional)
3. Click **"Generate Recipe"**
4. Verify the AI generates a recipe successfully
5. Test the download button

**Time:** 2 minutes

---

## Your App is Live! 🎉

Once deployed, you'll receive a URL like:
```
https://recipe-ai-[random-string].streamlit.app
```

### What to Do Next

- [ ] Copy your app URL
- [ ] Update README.md with the live link
- [ ] Share with friends and family
- [ ] Monitor usage in Streamlit Cloud dashboard
- [ ] Gather feedback

---

## Updating Your App

Streamlit Cloud automatically redeploys when you push to GitHub:

```bash
# Make changes to your code
git add .
git commit -m "Updated recipe generation prompt"
git push

# Your app will automatically redeploy in 2-3 minutes!
```

---

## Troubleshooting

### Issue: App shows "Error generating recipe"

**Solution:** Check that your API key is correctly set in Streamlit secrets:
1. Go to your app dashboard
2. Click the menu (⋮) → "Settings"
3. Navigate to "Secrets"
4. Verify `GEMINI_API_KEY` is set correctly

### Issue: App won't start / Shows dependency errors

**Solution:** Check your `requirements.txt`:
- Ensure all dependencies are listed
- Try pinning specific versions if needed
- Check the build logs for specific error messages

### Issue: App is slow or timing out

**Solution:** Streamlit free tier has resource limits:
- Recipe generation typically takes 10-20 seconds
- If consistently slow, consider upgrading or optimizing prompts
- Check Gemini API quota limits

### Issue: Can't find my app in dashboard

**Solution:**
- Make sure you're logged into the correct GitHub account
- Check that the repository is public (or Streamlit has access)
- Try refreshing the Streamlit Cloud dashboard

---

## App Management

### Viewing Logs
1. Go to your app in Streamlit Cloud dashboard
2. Click the menu (⋮) → "Logs"
3. View real-time logs and errors

### Restarting Your App
1. Go to your app dashboard
2. Click the menu (⋮) → "Reboot app"
3. Wait 1-2 minutes for restart

### Deleting Your App
1. Go to your app dashboard
2. Click the menu (⋮) → "Settings"
3. Scroll to bottom → "Delete app"

---

## Resource Limits (Free Tier)

- **Memory:** 1 GB RAM
- **CPU:** Shared CPU resources
- **Storage:** Limited to repository size
- **Bandwidth:** Generous (suitable for demos)
- **Concurrent Users:** ~100 (more than enough for MVP)

---

## Security Best Practices

✅ **DO:**
- Use Streamlit secrets for API keys
- Keep `.env` and `secrets.toml` in `.gitignore`
- Monitor API usage regularly
- Rotate API keys periodically

❌ **DON'T:**
- Commit API keys to Git
- Share your secrets publicly
- Hardcode sensitive data in code
- Share your Streamlit app credentials

---

## Cost Monitoring

### Streamlit Cloud
- **Cost:** FREE for public apps
- **Limits:** 1 app on free tier, unlimited viewers

### Google Gemini API
- **Free tier:** 15 requests/minute, 1,500 requests/day
- **Monitor usage:** https://console.cloud.google.com
- **Set up alerts:** Configure budget alerts in Google Cloud Console

---

## Support Resources

- **Streamlit Docs:** https://docs.streamlit.io/streamlit-community-cloud
- **Community Forum:** https://discuss.streamlit.io
- **Status Page:** https://streamlit.statuspage.io
- **GitHub Issues:** https://github.com/Rthomp61/Recipe-AI/issues

---

## Deployment Checklist

Use this checklist when deploying:

### Pre-Deployment
- [x] Code pushed to GitHub
- [x] `requirements.txt` is up to date
- [x] `.gitignore` excludes secrets
- [x] App runs locally without errors
- [x] API key is valid and working

### During Deployment
- [ ] Created Streamlit Cloud account
- [ ] Connected GitHub repository
- [ ] Set main file to `app.py`
- [ ] Added `GEMINI_API_KEY` to secrets
- [ ] Clicked "Deploy"

### Post-Deployment
- [ ] App successfully loaded
- [ ] Tested recipe generation
- [ ] All features work correctly
- [ ] Updated README with live URL
- [ ] Shared with testers
- [ ] Monitored for errors

---

## Advanced Configuration

### Custom Domain (Paid Plans Only)
Streamlit Cloud paid plans allow custom domains:
- Purchase domain from registrar
- Configure DNS CNAME record
- Add domain in Streamlit settings

### Analytics Integration
Add Google Analytics to track usage:
```python
# Add to app.py
import streamlit.components.v1 as components

# Embed Google Analytics
components.html("""
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
""")
```

### Environment-Specific Configs
Use Streamlit secrets for environment variables:
```toml
# In Streamlit Cloud secrets
ENVIRONMENT = "production"
DEBUG_MODE = false
```

---

## Next Steps After Deployment

1. **Share your app:**
   - Post on social media
   - Share with friends/family
   - Add to your portfolio

2. **Gather feedback:**
   - Add feedback form in app
   - Monitor user behavior
   - Iterate based on insights

3. **Monitor performance:**
   - Check Streamlit analytics
   - Monitor API usage
   - Track error rates

4. **Plan enhancements:**
   - Review PRD for next features
   - Prioritize based on feedback
   - Iterate and improve

---

**Questions?** Open an issue on GitHub or contact the maintainer.

**Happy Deploying! 🚀**
