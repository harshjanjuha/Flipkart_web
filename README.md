# Web Scraping and Review Aggregation Application
This repository contains a Flask web application for web scraping product reviews from Flipkart and storing them in a MongoDB database. The application allows users to enter a search string, which is used to fetch product reviews from Flipkart. The scraped reviews are then stored in a MongoDB database for further analysis.

## Features
- User-friendly web interface for entering search queries and viewing scraped reviews.
- Scrapes product reviews from Flipkart using BeautifulSoup and requests libraries.
- Stores scraped reviews in a MongoDB database using pymongo library.
- Logs application activities into a scrapper.log file for debugging and monitoring.
- Utilizes Flask for routing and rendering HTML templates.
- Implements CORS (Cross-Origin Resource Sharing) to handle cross-origin requests.

## Prerequisites
### Before running the application, make sure you have the following:

- Python 3.x installed on your system.
- Required Python libraries installed. You can install them using the following command:
  - pip install -r requirements.txt

## Usage
1. Clone the repository to your local machine.
2. Replace <cluster_link> in the app.py file with your actual MongoDB cluster link.
3. Navigate to the project directory in your terminal.
4. Run the following command to start the Flask application:
    -  python app.py
5. Access the application by opening a web browser and navigating to http://localhost:5000.

## Application Structure
1. app.py: The main Flask application script containing routing, scraping logic, and MongoDB integration.
2. templates/: This directory contains HTML templates used for rendering web pages.
   - home.html: Template for the homepage where users can enter search queries.
   - result.html: Template for displaying scraped reviews and messages.

## Logging
The application logs its activities into the scrapper.log file. You can refer to this log file to monitor the application's behavior and debug any issues that may arise during scraping or database interactions.

## Disclaimer
This application was created for educational purposes and to demonstrate web scraping and database integration using Flask and MongoDB. Make sure to adhere to the terms of use of websites you scrape and respect their robots.txt file.

## License
This project is licensed under the MIT License.

## Author
This application was created by Harsh Kumar.

Feel free to customize and extend this application according to your needs. If you have any questions or suggestions,feel free to reach out .
