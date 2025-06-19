# Web Scraper for News Headlines

This project features a small Python script designed to **automate the scraping of headlines and their corresponding links** from selected German news websites. Currently, it supports **BILD** and **Spiegel**. The script allows users to configure the scraping interval and the total number of requests, with all collected data automatically written to a CSV file.

---

## 🚀 Project Overview

This application serves as a **personal exercise in web scraping**, focusing on foundational techniques using Python and the `BeautifulSoup` library. It's an ongoing learning project, and I plan to expand its functionalities and the range of supported websites incrementally. This project is intended to demonstrate basic scraping capabilities rather than to be a robust, production-ready tool.

---

## ✨ Key Features

* **Targeted Scraping:** Extracts headlines and links from BILD and Spiegel.
* **Configurable Operation:** Set the interval between requests and the total number of repetitions.
* **CSV Output:** Automatically saves scraped data (website, timestamp, headline, link) to a `headlines.csv` file.
* **Progress Tracking:** Displays remaining time until program completion.

---

## ⚙️ Technologies Used

* **Python:** The core programming language.
* **`requests`:** For making HTTP requests to retrieve webpage content.
* **`BeautifulSoup4` (bs4):** For parsing HTML and extracting data.
* **`csv` module:** For writing data to CSV files.
* **`datetime` module:** For timestamping scraped data.

---

## ⚠️ Legal Disclaimer

**Important:** When using this script or any web scraping tool, it's **CRUCIAL to comply with the Terms and Conditions (AGB) of the respective website operators** regarding the permissibility of automated data retrieval. Scraping websites without explicit permission or in violation of their terms may lead to legal consequences. This script is provided for educational and personal learning purposes only, and I am not responsible for its misuse. **Users are solely responsible for ensuring their use of this script adheres to all applicable laws and website policies.**

---

## 🏃 Getting Started

To run this web scraper locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file if you haven't already: `pip freeze > requirements.txt`)
4.  **Configure scraping settings (optional):**
    Open `main.py` and adjust the `INTERVALL`, `REPETITIONS`, and `PAGE` variables as needed.
    ```python
    INTERVALL = 30  # time between two requests in seconds
    REPETITIONS = 10  # total number of requests
    PAGE = "BILD"  # either "Spiegel" or "BILD" atm
    ```
5.  **Run the script:**
    ```bash
    python main.py
    ```
    The scraped headlines will be saved in `headlines.csv` in the project root directory.

---

## 🔮 Future Enhancements

I plan to progressively expand this project by:

* Adding support for **more news websites** and different content types (e.g., article bodies, authors).
* Implementing **more robust error handling** for network issues or website structure changes.
* Considering **data storage options** beyond CSV, such as databases.
* Potentially developing a **user interface** for easier configuration and monitoring.