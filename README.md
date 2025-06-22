# Xarvis 🧠⚙️  
**Your Automated Twitter Assistant via GitHub Actions**

Xarvis is a lightweight automation system that posts scheduled tweets to X (formerly Twitter) using GitHub Actions. Built for developers, creators, and marketers, Xarvis enables seamless tweet automation directly from your GitHub repository—no need for external servers or paid scheduling tools.

---

## ✨ Features

- 🚀 **Automated Tweet Posting**  
  Schedule and post tweets using GitHub Actions at defined intervals (daily, weekly, custom CRON).

- 📝 **Fully Customizable Tweets**  
  Store your tweets in a `.txt` file, post them in order or randomly, and even include hashtags and emojis.

- 🧠 **No Server Required**  
  Powered by GitHub’s free infrastructure. Deploy once and let it run forever.

- 🔐 **Secure API Integration**  
  Uses encrypted GitHub Secrets to safely store and access your X API keys and tokens.

---

## 🔧 How It Works

1. **Prepare Your Tweet File**  
   Create a file named `tweets.txt` in the root of your repo. Each line represents a new tweet.

2. **Configure GitHub Secrets**  
   Store the following keys in your repo’s `Settings > Secrets and Variables > Actions`:
   - `X_API_KEY`
   - `X_API_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_SECRET`

3. **GitHub Actions Workflow**  
   The `.github/workflows/tweet.yml` workflow reads the `tweets.txt` file and posts tweets based on your schedule.

---

## 🗂️ Folder Structure

📦Xarvis/
┣ 📜 tweets.txt # Your tweet content
┣ 📜 tweet.py # The script that posts to X
┣ 📂 .github/workflows/
┃ ┗ 📜 tweet.yml # GitHub Actions workflow
┗ 📜 README.md # Project documentation


---

## 🛠 Setup Instructions

1. **Fork or Clone this Repository**
   ```bash
   git clone https://github.com/QuantumAlchemist03/Xarvis.git
   cd Xarvis

2. **Add Your Tweets**
Edit `tweets.txt` to include your tweet lines.

3. **Add Secrets**
Go to your GitHub repo settings and add your API credentials.

4. **Customize the Workflow (Optional)**
Change the CRON schedule in `.github/workflows/tweet.yml` to control tweet timing.

5. **Push and Watch it Tweet!**
Once the workflow is live, Xarvis will begin tweeting automatically at the set intervals.

🔄 Example Tweet Schedule (CRON)
```bash
# Every day at 12:00 PM UTC
schedule:
  - cron: '0 12 * * *'
Use crontab.guru to generate your desired CRON syntax.
```

## 📌 Notes
* Tweets are posted in order from top to bottom. You can randomize them in the script if you wish.

* Ensure your X Developer account is approved and has write permissions for the API.

## 📈 Future Plans
* Support for media/image uploads 🖼️

* Threaded tweets support 🧵

* Integration with OpenAI or RSS feeds for dynamic content

* Analytics and logging of tweet status

## 🤖 Built With
* Python 🐍

* GitHub Actions ⚙️

* Twitter/X Developer API 🐦  

## 👨‍💻 Author
QuantumAlchemist03
Twitter: @AlifSathar
GitHub: QuantumAlchemist03

## 📜 License
This project is licensed under the MIT License.

