# Lead Management Tool


## Table of Contents
- [Introduction](#introduction)
- [Deployment](#deployment)
- [Running the Application](#running-the-application)
- [Nginx Configuration](#nginx-configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Tinder Lead Management Tool is a web application built using Flask that assists in rating and managing URLs, such as Tinder profiles, for some classification or sorting task. The application allows users to rate URLs based on predefined criteria and stores the ratings in a CSV file. It is designed to handle a list of URLs and their corresponding ratings, making it suitable for various data processing tasks.

This documentation provides a guide on deploying and running the Tinder Lead Management Tool, along with details on how to configure Nginx for serving the application.

## Deployment

To deploy the Tinder Lead Management Tool, follow these steps:

1. **Clone the Repository**: Clone the repository from GitHub to your server:

   ```
   git clone https://github.com/your_username/tinder-lead-tool.git
   ```

2. **Install Dependencies**: Change into the project directory and install the required Python packages using `pip`:

   ```
   cd tinder-lead-tool
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**: If necessary, set up any environment variables required by the application.

4. **Run the Application**: Start the Flask development server to run the application:

   ```
   python app.py
   ```

   The application will be accessible at `http://localhost:123/` by default.

## Running the Application

Once the application is deployed, it can be accessed using a web browser. Follow these steps to use the Tinder Lead Management Tool:

1. **Access the Web Interface**: Open a web browser and navigate to the server's IP address or domain name followed by port 123 (default port for the Flask server):

   ```
   http://your_server_ip_or_domain:123/
   ```

2. **Upload Data**: Click on the "Upload" button to upload a CSV file containing a list of URLs to be processed. The file should be in a specific format, with each URL on a new line. Example format:

   ```
   https://tinderprofile1.com
   https://tinderprofile2.com
   ...
   ```

3. **Rate URLs**: The web interface will display one URL at a time from the uploaded list. Rate the URL based on the provided criteria (kein, niedrig, mittel, hoch). Should a website not be accissible trough 

4. **Export Data**: The application will save the ratings to a CSV file named "out.csv" in the project directory. This file can be downloaded after all URLs are rated.

## Nginx Configuration

To serve the Tinder Lead Management Tool using Nginx, you need to configure a reverse proxy. Below is an example Nginx configuration:

```nginx
server {
    listen 80;
    server_name your_server_domain.com;

    location / {
        proxy_pass http://localhost:123;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Replace `your_server_domain.com` with your actual domain name or server IP address. The Nginx configuration will redirect requests from port 80 to the Flask application running on port 123.

## Usage

The Tinder Lead Management Tool can be used for various purposes, including:

- Sorting and rating Tinder profiles based on predefined criteria.
- Managing lists of URLs for marketing or research purposes.
- Any task that involves rating and categorizing a list of items.

Tod start using the app simply navigate to /upload and paste the websites you wish to rate without headers (notice that the app expects tsv format and that the links should be in the C column)

### buttons

- h -> hoch 
- m -> mittel
- n -> niedrig
- k -> kein
- enter -> open current link directly outside of webapp (usefull when page refuses to load in iframe due to security concerns)
## Contributing

We welcome contributions to improve the Tinder Lead Management Tool. If you encounter any issues or have suggestions for enhancements, feel free to open an issue or submit a pull request.

## License

The Tinder Lead Management Tool is open-source and available under the [MIT License](link_to_license). Feel free to use, modify, and distribute it as per the terms of the license.
