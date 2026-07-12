import os
import json
import shutil
from datetime import datetime

# Configuration
SITE_URL = "https://ai-chatbot-platform-free.bongshai.com"
SITE_NAME = "AI Chatbot Platform Reviews"
OUTPUT_DIR = "public"
AUTHOR_NAME = "Alex Techwriter"
AUTHOR_BIO = "Alex is an experienced AI researcher and SaaS analyst with over 10 years of experience in conversational AI."
YEAR = datetime.now().year

# The 30+ Keywords/Topics
ARTICLES = [
    {"slug": "chatgpt-free-vs-plus", "title": "ChatGPT Free vs Plus: Is It Worth The Upgrade?", "category": "Comparisons", "keyword": "ChatGPT Free vs Plus"},
    {"slug": "claude-3-sonnet-vs-opus", "title": "Claude 3 Sonnet vs Opus: Which Anthropic Model is Best?", "category": "Comparisons", "keyword": "Claude 3 Sonnet vs Opus"},
    {"slug": "gemini-pro-vs-advanced", "title": "Google Gemini Pro vs Advanced: A Comprehensive Guide", "category": "Comparisons", "keyword": "Gemini Pro vs Advanced"},
    {"slug": "perplexity-free-vs-pro", "title": "Perplexity AI Free vs Pro: The Ultimate Search Chatbot?", "category": "Comparisons", "keyword": "Perplexity Free vs Pro"},
    {"slug": "microsoft-copilot-free-vs-pro", "title": "Microsoft Copilot Free vs Pro: Which One Do You Need?", "category": "Comparisons", "keyword": "Microsoft Copilot Free vs Pro"},
    {"slug": "best-free-ai-chatbots-small-business", "title": "Best Free AI Chatbots for Small Business in 2026", "category": "Business", "keyword": "best free AI chatbots for small business"},
    {"slug": "best-free-ai-chatbots-coding", "title": "Top 5 Free AI Chatbots for Coding and Programmers", "category": "Development", "keyword": "free AI chatbots for coding"},
    {"slug": "free-ai-chatbots-writers", "title": "Best Free AI Chatbots for Writers and Content Creators", "category": "Creative", "keyword": "free AI chatbots for writers"},
    {"slug": "free-ai-chatbots-students", "title": "Top Free AI Chatbots for Students and Homework Help", "category": "Education", "keyword": "free AI chatbots for students"},
    {"slug": "best-paid-ai-chatbots-enterprise", "title": "Best Paid AI Chatbots for Enterprise Level Businesses", "category": "Business", "keyword": "paid AI chatbots for enterprise"},
    {"slug": "chatgpt-plus-vs-claude-pro", "title": "ChatGPT Plus vs Claude Pro: The Battle of the Titans", "category": "Comparisons", "keyword": "ChatGPT Plus vs Claude Pro"},
    {"slug": "best-open-source-ai-chatbots", "title": "Best Open Source AI Chatbots You Can Use for Free", "category": "Development", "keyword": "best open source AI chatbots"},
    {"slug": "huggingchat-vs-chatgpt-free", "title": "HuggingChat vs ChatGPT Free: Which is Better?", "category": "Comparisons", "keyword": "HuggingChat vs ChatGPT Free"},
    {"slug": "mistral-le-chat-vs-chatgpt", "title": "Mistral Le Chat vs ChatGPT Free: The European Challenger", "category": "Comparisons", "keyword": "Mistral Le Chat vs ChatGPT Free"},
    {"slug": "meta-llama-3-free-chatbots", "title": "Where to Try Meta Llama 3 Free Chatbots Today", "category": "News", "keyword": "Meta Llama 3 free chatbots"},
    {"slug": "best-free-ai-chatbots-internet-access", "title": "Best Free AI Chatbots with Real-Time Internet Access", "category": "Features", "keyword": "free AI chatbots with internet access"},
    {"slug": "best-paid-ai-chatbots-file-uploads", "title": "Best Paid AI Chatbots for Large File Uploads & Analysis", "category": "Features", "keyword": "paid AI chatbots with file uploads"},
    {"slug": "best-ai-chatbots-customer-service", "title": "Best AI Chatbots for Customer Service Support", "category": "Business", "keyword": "best AI chatbots for customer service"},
    {"slug": "best-free-ai-chatbots-language-learning", "title": "Best Free AI Chatbots for Language Learning", "category": "Education", "keyword": "free AI chatbots for language learning"},
    {"slug": "best-free-ai-chatbots-data-analysis", "title": "Best Free AI Chatbots for Data Analysis and Spreadsheets", "category": "Features", "keyword": "free AI chatbots for data analysis"},
    {"slug": "best-paid-ai-chatbots-marketing", "title": "Top Paid AI Chatbots for Digital Marketing Teams", "category": "Business", "keyword": "paid AI chatbots for marketing"},
    {"slug": "jasper-ai-vs-chatgpt-plus", "title": "Jasper AI vs ChatGPT Plus: Which is Better for Writers?", "category": "Comparisons", "keyword": "Jasper AI vs ChatGPT Plus"},
    {"slug": "writesonic-vs-chatgpt-plus", "title": "Writesonic vs ChatGPT Plus: Content Creation Showdown", "category": "Comparisons", "keyword": "Writesonic vs ChatGPT Plus"},
    {"slug": "best-free-ai-image-generators-chatbots", "title": "Best Free AI Image Generators Included in Chatbots", "category": "Creative", "keyword": "free AI image generators in chatbots"},
    {"slug": "best-ai-chatbots-mac-users", "title": "Best Native AI Chatbot Apps for Mac Users", "category": "Platforms", "keyword": "best AI chatbots for Mac"},
    {"slug": "best-ai-chatbots-windows-users", "title": "Best Native AI Chatbot Apps for Windows PCs", "category": "Platforms", "keyword": "best AI chatbots for Windows"},
    {"slug": "best-ai-chatbots-ios-android", "title": "Top Mobile AI Chatbot Apps for iOS and Android", "category": "Platforms", "keyword": "best AI chatbots for iOS and Android"},
    {"slug": "free-vs-paid-ai-chatbots-upgrade-worth-it", "title": "Free vs Paid AI Chatbots: Is the Upgrade Actually Worth It?", "category": "Guide", "keyword": "free vs paid AI chatbots"},
    {"slug": "hidden-costs-free-ai-chatbots", "title": "Top 10 Hidden Costs of 'Free' AI Chatbots", "category": "Guide", "keyword": "hidden costs of free AI chatbots"},
    {"slug": "future-of-free-ai-chatbots", "title": "The Future of Free AI Chatbots: What to Expect in 2026", "category": "News", "keyword": "future of free AI chatbots"}
]

# Ensure Output Dir
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)
os.makedirs(os.path.join(OUTPUT_DIR, "assets"))
os.makedirs(os.path.join(OUTPUT_DIR, "images"))
os.makedirs(os.path.join(OUTPUT_DIR, "category"))

# Copy Assets
shutil.copy("src_assets/style.css", os.path.join(OUTPUT_DIR, "assets", "style.css"))
shutil.copy("src_assets/main.js", os.path.join(OUTPUT_DIR, "assets", "main.js"))
shutil.copy("src_assets/manifest.json", os.path.join(OUTPUT_DIR, "manifest.json"))
shutil.copy("src_assets/sw.js", os.path.join(OUTPUT_DIR, "sw.js"))
if os.path.exists("src_assets/images"):
    for file in os.listdir("src_assets/images"):
        shutil.copy(os.path.join("src_assets/images", file), os.path.join(OUTPUT_DIR, "images", file))

# Generate Search Index
search_index = [{"title": a["title"], "url": f"/{a['slug']}.html", "category": a["category"]} for a in ARTICLES]

HTML_BASE = """<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}">
    
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#1a1a2e">
    <link rel="stylesheet" href="/assets/style.css">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    
    {schema}
    
    <!-- Google Analytics 4 Placeholder -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>

    <!-- Google AdSense Placeholder -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
</head>
<body>
    <header class="glassmorphism">
        <div class="container nav-container">
            <a href="/" class="logo">{site_name}</a>
            <nav id="mobile-menu" class="nav-links">
                <a href="/">Home</a>
                <a href="/category/comparisons.html">Comparisons</a>
                <a href="/category/business.html">Business</a>
                <a href="/about.html">About Us</a>
            </nav>
            <div class="search-bar">
                <input type="text" id="searchInput" placeholder="Search..." aria-label="Search">
                <div id="searchResults" class="search-results"></div>
            </div>
            <button class="menu-toggle" aria-label="Toggle Menu">☰</button>
        </div>
    </header>

    <main class="container">
        {content}
    </main>

    <footer class="glassmorphism-footer">
        <div class="container footer-grid">
            <div class="footer-col">
                <h3>{site_name}</h3>
                <p>Helping you choose the perfect AI chatbot for your needs.</p>
            </div>
            <div class="footer-col">
                <h3>Links</h3>
                <a href="/about.html">About Us</a>
                <a href="/contact.html">Contact</a>
                <a href="/privacy-policy.html">Privacy Policy</a>
                <a href="/terms-of-service.html">Terms of Service</a>
                <a href="/disclaimer.html">Disclaimer</a>
            </div>
            <div class="footer-col newsletter-footer">
                <h3>Subscribe</h3>
                <p>Get the latest AI chatbot reviews and news.</p>
                <form onsubmit="event.preventDefault(); alert('Newsletter connected soon!');">
                    <input type="email" placeholder="Your email address" required>
                    <button class="btn btn-primary" type="submit">Subscribe</button>
                </form>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; {year} {site_name}. All rights reserved.</p>
        </div>
    </footer>

    <!-- Cookie Consent -->
    <div id="cookieBanner" class="cookie-banner">
        <p>We use cookies to personalize content and ads, to provide social media features and to analyze our traffic. See our <a href="/privacy-policy.html">Privacy Policy</a>.</p>
        <button id="acceptCookies" class="btn btn-primary">Accept</button>
    </div>

    <script src="/assets/main.js"></script>
    <script>
        const searchIndex = {search_json};
        // Service Worker Registration
        if ('serviceWorker' in navigator) {{
            window.addEventListener('load', () => {{
                navigator.serviceWorker.register('/sw.js');
            }});
        }}
    </script>
</body>
</html>
"""

def generate_schema(schema_type, data):
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'

# 1. Generate Articles
for article in ARTICLES:
    schema = generate_schema("Article", {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "author": {"@type": "Person", "name": AUTHOR_NAME},
        "datePublished": datetime.now().isoformat(),
        "publisher": {"@type": "Organization", "name": SITE_NAME, "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/images/logo.png"}}
    })

    content = f"""
    <article class="post">
        <!-- Breadcrumbs -->
        <nav class="breadcrumbs">
            <a href="/">Home</a> > <a href="/category/{article['category'].lower()}.html">{article['category']}</a> > <span>{article['title']}</span>
        </nav>
        
        <h1>{article['title']}</h1>
        <div class="author-meta">
            <span>By <a href="/about.html">{AUTHOR_NAME}</a></span> | <span>Last Updated: {datetime.now().strftime('%B %d, %Y')}</span>
        </div>

        <!-- AdSense Top -->
        <div class="ad-placeholder">AdSense Responsive Ad Unit (Top)</div>

        <div class="key-takeaways glassmorphism">
            <h2>Key Takeaways</h2>
            <ul>
                <li>Both free and paid AI chatbots offer immense value depending on your specific use case.</li>
                <li>Upgrading to a premium plan usually provides faster response times and priority access to new models.</li>
                <li>Consider your daily usage limits before committing to a paid subscription.</li>
            </ul>
        </div>

        <!-- Social Share Floating -->
        <div class="social-share">
            <button onclick="window.open('https://twitter.com/intent/tweet?text={article['title']}&url={SITE_URL}/{article['slug']}.html')">𝕏</button>
            <button onclick="window.open('https://www.facebook.com/sharer/sharer.php?u={SITE_URL}/{article['slug']}.html')">f</button>
            <button onclick="navigator.clipboard.writeText('{SITE_URL}/{article['slug']}.html'); alert('Copied!');">🔗</button>
        </div>

        <p class="intro">When comparing <strong>{article['keyword']}</strong>, the most common question users ask is whether the paid features justify the cost. In this comprehensive guide, we'll break down the pros, cons, and essential differences to help you make an informed decision.</p>
        
        <div class="toc">
            <h3>Table of Contents</h3>
            <ul>
                <li><a href="#overview">Overview</a></li>
                <li><a href="#features">Key Features</a></li>
                <li><a href="#pricing">Pricing & Value</a></li>
                <li><a href="#conclusion">Final Verdict</a></li>
            </ul>
        </div>

        <h2 id="overview">Overview of {article['keyword']}</h2>
        <p>The AI landscape is evolving rapidly. To understand which platform suits you best, we must first look at the foundational models powering these tools.</p>

        <!-- Newsletter Inline -->
        <div class="newsletter-inline glassmorphism">
            <h3>Don't Miss AI Updates!</h3>
            <p>Join our newsletter for the latest chatbot comparisons.</p>
            <form onsubmit="event.preventDefault(); alert('Subscribed!');">
                <input type="email" placeholder="Enter your email" required>
                <button class="btn btn-primary" type="submit">Subscribe</button>
            </form>
        </div>

        <h2 id="features">Key Features Comparison</h2>
        <p>Here is a detailed breakdown of what you get with each tier:</p>
        <div class="table-container">
            <table>
                <thead>
                    <tr><th>Feature</th><th>Free Tier</th><th>Paid Tier</th></tr>
                </thead>
                <tbody>
                    <tr><td>Model Access</td><td>Standard</td><td>Advanced / Latest</td></tr>
                    <tr><td>Response Speed</td><td>Normal</td><td>Fast / Priority</td></tr>
                    <tr><td>Usage Limits</td><td>Strict</td><td>High / Unlimited</td></tr>
                </tbody>
            </table>
        </div>

        <!-- AdSense Middle -->
        <div class="ad-placeholder">AdSense In-Article Ad Unit</div>

        <h2 id="pricing">Pricing & Value</h2>
        <p>Typically, paid AI chatbot subscriptions hover around $20/month. For heavy users, this is a negligible cost compared to the productivity gains. Casual users, however, may find the free tiers perfectly adequate.</p>

        <h2 id="conclusion">Final Verdict</h2>
        <p>If you rely on AI for your daily workflow, upgrading is usually a no-brainer. But if you just need occasional assistance, the free tools available today are more than capable.</p>

        <!-- AdSense Bottom -->
        <div class="ad-placeholder">AdSense Matched Content / Bottom Ad Unit</div>

        <hr>
        <div class="related-articles">
            <h3>Related Articles</h3>
            <ul>
                {"".join([f'<li><a href="/{a["slug"]}.html">{a["title"]}</a></li>' for a in ARTICLES[:3]])}
            </ul>
        </div>
    </article>
    """
    
    html = HTML_BASE.format(
        title=f"{article['title']} - {SITE_NAME}",
        description=f"Read our comprehensive comparison of {article['keyword']}. Find out which AI chatbot platform is right for you.",
        url=f"{SITE_URL}/{article['slug']}.html",
        schema=schema,
        site_name=SITE_NAME,
        year=YEAR,
        search_json=json.dumps(search_index),
        content=content
    )
    
    with open(os.path.join(OUTPUT_DIR, f"{article['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)

# 2. Generate Home Page
home_content = f"""
<div class="hero">
    <h1>Find the Perfect AI Chatbot</h1>
    <p>In-depth comparisons of Free vs Paid AI Chatbot Platforms to help you boost productivity and save money.</p>
</div>

<!-- AdSense Top -->
<div class="ad-placeholder">AdSense Responsive Ad Unit (Home Top)</div>

<div class="article-grid">
    {"".join([f'''
    <div class="card glassmorphism">
        <h2><a href="/{a["slug"]}.html">{a["title"]}</a></h2>
        <span class="badge">{a["category"]}</span>
    </div>
    ''' for a in ARTICLES[:12]])}
</div>
"""
home_html = HTML_BASE.format(
    title=f"Home - {SITE_NAME}",
    description="Compare the best free and paid AI chatbots. Unbiased reviews, feature breakdowns, and value assessments.",
    url=f"{SITE_URL}/",
    schema=generate_schema("WebSite", {"@context": "https://schema.org", "@type": "WebSite", "url": SITE_URL, "name": SITE_NAME}),
    site_name=SITE_NAME,
    year=YEAR,
    search_json=json.dumps(search_index),
    content=home_content
)
with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)

# 3. Generate Categories
categories = set(a["category"] for a in ARTICLES)
for cat in categories:
    cat_articles = [a for a in ARTICLES if a["category"] == cat]
    cat_content = f"<h1>{cat} AI Chatbots</h1><div class='article-grid'>"
    cat_content += "".join([f'<div class="card glassmorphism"><h2><a href="/{a["slug"]}.html">{a["title"]}</a></h2></div>' for a in cat_articles])
    cat_content += "</div>"
    
    cat_html = HTML_BASE.format(
        title=f"{cat} Chatbot Comparisons - {SITE_NAME}",
        description=f"Read all our reviews and comparisons for {cat} AI chatbots.",
        url=f"{SITE_URL}/category/{cat.lower()}.html",
        schema="",
        site_name=SITE_NAME,
        year=YEAR,
        search_json=json.dumps(search_index),
        content=cat_content
    )
    with open(os.path.join(OUTPUT_DIR, "category", f"{cat.lower()}.html"), "w", encoding="utf-8") as f:
        f.write(cat_html)

# 4. Generate Core Pages (About, Contact, Privacy, TOS, Disclaimer, 404)
core_pages = {
    "about": ("About Us", "Learn more about AI Chatbot Platform Reviews and our editorial process.", "<h1>About Us</h1><p>We are dedicated to providing unbiased reviews of AI chatbots...</p>"),
    "contact": ("Contact", "Get in touch with our team.", "<h1>Contact</h1><p>Email us at contact@ai-chatbot-platform-free.bongshai.com.</p>"),
    "privacy-policy": ("Privacy Policy", "Our privacy policy and cookie usage details.", "<h1>Privacy Policy</h1><p>We use Google AdSense which uses cookies to serve ads based on prior visits...</p>"),
    "terms-of-service": ("Terms of Service", "Terms of service for our website.", "<h1>Terms of Service</h1><p>By using this site, you agree to...</p>"),
    "disclaimer": ("Disclaimer", "Important disclaimers about our content.", "<h1>Disclaimer</h1><p>The information provided is for educational purposes. We are not responsible for decisions made based on our content.</p>"),
    "404": ("Page Not Found", "The page you are looking for does not exist.", "<h1>404 - Not Found</h1><p>Sorry, the page you requested could not be found. <a href='/'>Return to Home</a></p>")
}
for slug, (title, desc, content) in core_pages.items():
    page_html = HTML_BASE.format(
        title=f"{title} - {SITE_NAME}",
        description=desc,
        url=f"{SITE_URL}/{slug}.html",
        schema="",
        site_name=SITE_NAME,
        year=YEAR,
        search_json=json.dumps(search_index),
        content=content
    )
    with open(os.path.join(OUTPUT_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(page_html)

# 5. Generate Sitemap, RSS, robots.txt
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
rss_content = f'<?xml version="1.0" encoding="UTF-8" ?>\n<rss version="2.0">\n<channel>\n<title>{SITE_NAME}</title>\n<link>{SITE_URL}</link>\n<description>AI Chatbot Platform Comparisons</description>\n'

for a in ARTICLES:
    sitemap_content += f"  <url><loc>{SITE_URL}/{a['slug']}.html</loc></url>\n"
    rss_content += f"  <item><title>{a['title']}</title><link>{SITE_URL}/{a['slug']}.html</link><description>{a['title']} review</description></item>\n"

sitemap_content += "</urlset>"
rss_content += "</channel>\n</rss>"

with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)
with open(os.path.join(OUTPUT_DIR, "rss.xml"), "w", encoding="utf-8") as f:
    f.write(rss_content)
with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

print("Website generated successfully in public/ directory.")
