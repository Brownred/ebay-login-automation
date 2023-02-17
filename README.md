# eBay Login Automation Script

This is an automation script created to log in to an eBay account using Python and the Selenium web driver. The script is designed to handle scenarios where the user is prompted to enter a verification code or solve a CAPTCHA.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:

```
pip install selenium
```

3. Download the appropriate web driver for your browser and operating system. For example, if you are using Google Chrome on Windows, download the Chrome web driver for Windows from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. Update the `WEBDRIVER_PATH` constant in `config.py` with the path to your downloaded web driver.

## Usage

To run the script, navigate to the root directory of the project and run the following command:

```
python ebay_login.py
```

The script will automatically navigate to the eBay login page, enter the login credentials specified in `config.py`, and log in to the account. If the user is prompted to enter a verification code or solve a CAPTCHA, the script will automatically handle these scenarios.

To schedule the script to run at specific times, you can use a task scheduling tool like `cron` on Linux or Task Scheduler on Windows.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improving the script, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

