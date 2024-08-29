# Quotes Scraper

A Scrapy project to scrape quotes from [Quotes to Scrape](http://quotes.toscrape.com) and store them in an SQLite database.

## Features

- Logs in to the website (if necessary)
- Scrapes quotes, authors, and tags
- Stores data in an SQLite database
- Dockerized for easy deployment

## Prerequisites

- Python 3.6+
- Docker (optional)

## Installation

### Local Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/quotes-scraper.git
   cd quotes-scraper
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the spider**

   ```bash
   scrapy crawl quotes
   ```

### Docker Setup

1. **Build the Docker image**

   ```bash
   docker build -t quotes-scraper .
   ```

2. **Run the Docker container**

   ```bash
   docker run -it --rm quotes-scraper
   ```

## Project Structure

- `quotes_scraper/`
  - `spiders/`
    - `quotes_spider.py`: Scrapy spider for scraping quotes.
  - `pipelines.py`: Pipeline for storing scraped data in SQLite.
- `Dockerfile`: Dockerfile for building the Docker image.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignore file.
- `README.md`: Project documentation.

## Usage

1. **Local Execution**: Run `scrapy crawl quotes` to start the spider and scrape quotes.
2. **Docker Execution**: Build and run the Docker container to execute the spider in an isolated environment.

## Configuration

- Update the `username` and `password` in `quotes_scraper/spiders/quotes_spider.py` with your login credentials if authentication is required.

## Database

- The scraped quotes are stored in an SQLite database named `quotes.db` in the project root directory.
- The database schema includes a table `quotes` with the following fields:
  - `id`: Primary key, auto-incremented integer.
  - `text`: The text of the quote.
  - `author`: The author of the quote.
  - `tags`: Comma-separated tags associated with the quote.
