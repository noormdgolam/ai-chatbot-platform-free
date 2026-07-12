# AI Chatbot Platform Reviews - Static Site

This is the source code for the AI Chatbot Platform Reviews static website, designed for optimal SEO, Google AdSense monetization, and high performance (10,000+ daily visitors).

## 🚀 How to Build and Deploy
1. Ensure Python 3 is installed.
2. Run the build script:
   ```bash
   python build_site.py
   ```
3. The complete static site will be generated in the `public/` directory.
4. Upload the contents of the `public/` directory to any static hosting provider (e.g., GitHub Pages, Cloudflare Pages, Vercel, Netlify, AWS S3) or your preferred CDN.

## 📝 Adding New Articles
1. Open `build_site.py`.
2. Locate the `ARTICLES` list at the top of the file.
3. Add a new dictionary entry with your target keyword, slug, title, and category:
   ```python
   {"slug": "new-chatbot-review", "title": "Review of the New Chatbot", "category": "Reviews", "keyword": "New Chatbot"}
   ```
4. Run `python build_site.py`. The script will automatically:
   - Generate the new HTML page.
   - Update the client-side search index.
   - Update the category hub pages.
   - Update `sitemap.xml` and `rss.xml`.

## 💰 Inserting AdSense Code
The generated pages include placeholder `div`s where you should inject your Google AdSense units.
- **Auto Ads**: Replace the placeholder `client=ca-pub-XXXXXXXXXXXXXXXX` in the `<head>` of `build_site.py` with your actual AdSense Publisher ID.
- **Manual Ad Units**: Look for `<div class="ad-placeholder">...</div>` in `build_site.py` and replace these sections with the `<script>` and `<ins>` tags provided by your AdSense dashboard.

## 📧 Connecting the Newsletter
Currently, the newsletter form has a placeholder `onsubmit` action showing an alert. 
To connect it to a real provider (like Mailchimp, ConvertKit, etc.):
1. Open `build_site.py`.
2. Locate the newsletter HTML sections (one in the footer, one inline in the article).
3. Replace the `<form>` tag's `action` attribute with the endpoint provided by your email marketing tool.

## 🖼️ Missing Assets
Please ensure you add the following images to the `src_assets/images/` directory and update the build script to copy them, or upload them directly to `public/images/`:
- `icon-192.png`
- `icon-512.png`
- `logo.png`

## ⚙️ Updating Sitemap and RSS
You do not need to manually update the sitemap or RSS feed! The `build_site.py` script automatically regenerates `sitemap.xml` and `rss.xml` every time you build the site. Simply submit `https://ai-chatbot-platform-free.bongshai.com/sitemap.xml` to Google Search Console.
