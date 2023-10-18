


# Phone Number Information Extractor

This Python script allows you to parse and extract information from phone numbers using the `phonenumbers` library. You can obtain details such as timezone, carrier, geographic location, and more from a given phone number.

## Prerequisites

Before running this script, you need to install the `phonenumbers` library. You can install it using `pip`:

```bash
pip install phonenumbers
```

## Usage

1. Run the script in your Python environment.

2. Enter a phone number in the format `(+country_code)phonenumber`. For example: `(+911234567890)` for a number in India.

3. The script will parse the phone number and provide the following information:

    - Time Zones for the Number
    - Time Zones for Geographical Number
    - Carrier Name for Number
    - Geographic Location for Number
    - Country Name for Number

4. You can customize the default region in the script to match the country for the provided phone number.

## Example

```python
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('Enter Your Phone Number using country code example: (+911234567890): ')

# Set the default region (e.g., 'IN' for India)
default_region = 'IN'
phone = phonenumbers.parse(number, default_region)

# Get and display phone number information
# ...

# Run the script and enter a phone number to see the results.
```

# License

This script is available under the MIT License. See the [LICENSE](LICENSE) file for details.

# Donate

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/trojanhax)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/trojanhax?country.x=IN&locale.x=en_GB)
