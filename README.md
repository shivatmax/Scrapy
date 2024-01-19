# Scrapy JobScraper

This is a job scraping project using Scrapy, a powerful open-source web crawling framework.

## Project Structure

The project is organized into two main directories:

- `jobs/`: This directory contains the logic for processing and analyzing job data. Notable functions include [`num_urgent_words`](MyJobScrapper/jobs/__init__.py) which counts the number of urgent words in a job description.

- `scrapers/`: This directory contains the web scrapers for different job sites. Each job site has its own subdirectory (e.g., `indeed/`, `linkedin/`, `glassdoor/`, `ziprecruiter/`). Notable functions include [`create_session`](MyJobScrapper/scrapers/utils.py) which creates a new web scraping session, and [`find_mosaic_script`](MyJobScrapper/scrapers/indeed/__init__.py) which finds a specific script on Indeed job listings.

The main entry point of the application is [`scrapy.py`](scrapy.py).

## How to Run

To run the project, execute the `scrapy.py` script. Make sure you have Scrapy installed in your Python environment.

```sh
streamlit run scrapy.py
