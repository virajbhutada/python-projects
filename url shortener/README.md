
# URL Shortener with Python and Flask

This project implements a URL shortener using Python, Flask (a web framework), and SQLite for data storage. The application allows users to shorten URLs and provides statistics on the number of clicks for each shortened URL.

## Author: Viraj N. Bhutada

## Installation

1. Clone this repository or download the source code.
2. Install the required packages using the following command:

   ```bash
   pip install Flask hashids
   ```

3. Save the code in a file, for example, `url_shortener.py`.

## Usage

1. Run the Python script:

   ```bash
   python url_shortener.py
   ```

2. Access the URL Shortener at `http://127.0.0.1:5000/`.

3. To shorten a URL, enter the original URL in the provided form on the homepage.

4. The shortened URL will be displayed, and you can use it to redirect to the original URL.

5. Visit the `/stats` endpoint to view statistics, including the number of clicks for each shortened URL.

## Code Overview

- The `get_db_connection` function establishes a connection to the SQLite database.
- Flask routes (`index`, `url_redirect`, `stats`) handle URL shortening, redirection, and statistics.
- The Hashids library is used to encode and decode URL identifiers.
- SQLite is used to store URL data, including original URLs, shortened URLs, and click counts.

## Considerations

- This project uses SQLite for simplicity; in a production environment, consider using a more robust database.
- Error handling and validation for invalid URLs could be enhanced based on specific use cases.

Feel free to modify and extend the code to meet your specific requirements. Happy shortening!
```

Make sure to update the README with any additional information or customization specific to your implementation.