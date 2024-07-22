# Unity Asset Store Testing Framework

## Overview

This project provides a testing framework for the Unity Asset Store using Selenium WebDriver. The goal is to ensure that the Unity Asset Store's functionality works as expected through automated tests. The framework includes tests for various API interactions related to tweets and user data.

## Project Structure

The project consists of several components:
- **API Interaction Classes**: These classes handle interactions with the API endpoints.
- **Testing Classes**: These classes define and run tests for different functionalities.
- **Utility Functions**: Helper functions used across tests for common tasks.

## Installation

To get started, you'll need to install the required Python packages. You can do this using `pip`. The necessary packages are listed in the `requirements.txt` file.

### Install Dependencies

1. Ensure you have Python 3.6+ installed.
2. Install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

Tests are organized into different files and can be executed using the `unittest` framework.

1. To run all tests:

    ```bash
    python -m unittest discover
    ```

2. To run a specific test file:

    ```bash
    python -m unittest path.to.test_file
    ```

## Helper Functions

The project includes helper functions to simplify test implementations:

- **`find_tweet_by_id(tweets, tweet_id)`**: Finds a tweet in a list by its ID.
- **`find_follower_by_user_id(followers, user_id)`**: Finds a follower in a list by its user ID.
- **`find_user_media_by_user_id(media_list, user_id)`**: Finds user media in a list by user ID.

## Example Tests

### `test_get_tweet_details`

Tests retrieving tweet details from the API and validating the response.

### `test_post_tweet_details`

Tests posting tweet details to the API and validating the response.

### `test_get_user_media`

Tests getting user media from the API and validating the response.

### `test_get_user_tweets`

Tests the retrieval of user tweets and validating the response.

## Postman Collection

The Postman collection for the API tests is included in the project. It contains pre-configured requests and tests for various endpoints.

### Running Postman Tests

1. Import the Postman collection into your Postman app.
2. Run the collection to execute the defined tests and view the results.

## Contributing

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and improvements are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

