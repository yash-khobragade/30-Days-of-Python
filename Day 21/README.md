📅 Day 21 – Web Scraping with requests, BeautifulSoup & Selenium

🗒️ Topics Covered  
🔹 requests – Fetch raw HTML from websites  
🔹 BeautifulSoup – Parse HTML to extract information  
🔹 Selenium – Automate browser to handle JavaScript-loaded content

🎯 Challenge  
🔧 Scrape headlines from a news site.

---

🧠 Web Scraping Approaches

✅ Method 1: Using requests + BeautifulSoup  
- Sends an HTTP request and parses the response HTML.  
- Works for static content.  
- ❌ Does **not** handle JavaScript-rendered content.

✅ Method 2: Using Selenium + BeautifulSoup  
- Automates a real browser, loads JavaScript-rendered content.  
- Can scrape all dynamic data.  
- ✅ Best choice for modern websites with dynamic content.

| Feature               | Method 1 (requests + BS) | Method 2 (Selenium + BS) |
|----------------------|---------------------------|----------------------------|
| JavaScript Handling  | ❌ No                     | ✅ Yes                     |
| Speed                | ⚡ Fast                   | 🐢 Slower                  |
| Setup                | ✅ Simple                 | ❗ Needs browser driver     |
| Best for             | Static pages              | Dynamic pages              |


📌 Progress  
Day 21 completed ✅  

#30DaysOfPython #IDC30DaysChallenge
