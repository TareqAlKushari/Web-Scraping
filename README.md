# Web-Scraping: YallaKora Match Results Extractor

This project is a simple yet powerful Python script that performs **web scraping** to extract football match data from [YallaKora](https://www.yallakora.com/) based on a user-specified date. It demonstrates the use of key Python libraries such as `requests`, `BeautifulSoup`, and `csv`.

## 📌 Project Overview

The script allows users to input a date in the format `MM/DD/YYYY` and scrapes all the football match details available on that date from the YallaKora Match Center.

### ✅ Features
- Scrapes live and historical football match data
- User-friendly date input
- Fetches data directly from YallaKora's public match-center
- Stores the extracted data into a `.csv` file for easy access and analysis

## 📂 Technologies Used

- **Python 3**
- [`requests`](https://docs.python-requests.org/en/latest/): for HTTP requests
- [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/): for HTML parsing
- [`csv`](https://docs.python.org/3/library/csv.html): for saving data

## 🖥 How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TareqAlKushari/Web-Scraping.git
   cd Web-Scraping
   ```

2. **Install dependencies** (if not already installed):

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the script**:

   ```bash
   python main.py
   ```

4. **Enter the date** in the required format when prompted:

   ```
   please enter a date in the following format MM/DD/YYYY: 06/15/2025
   ```

5. **Output**: The script will create a CSV file with the scraped match data.

## 📦 Output Example

A sample output CSV (`matches.csv`) might look like:

| League         | Match Time | Team A | Team B | Result |
| -------------- | ---------- | ------ | ------ | ------ |
| Premier League | 18:00      | Team A | Team B | 2 - 1  |
| Serie A        | 20:00      | Team C | Team D | 1 - 1  |

## ⚠️ Note

* This script depends on the current structure of the YallaKora website. Any major changes to their frontend may break the parser.
* Ensure you use it responsibly and avoid sending too many requests in a short time.

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Tareq Al Kushari**
Computer and Control Engineer
🔗 [GitHub Profile](https://github.com/TareqAlKushari)

---
