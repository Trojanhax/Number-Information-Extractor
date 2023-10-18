import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('Enter Your Phone Number using country code example: (+911234567890): ')

# Parse the phone number with a default region (e.g., 'US' for the United States)
default_region = 'IN'  # You can change this to the appropriate country code
phone = phonenumbers.parse(number, default_region)

# Get the timezone information
time_zones = timezone.time_zones_for_number(phone)
print("Time Zones for the Number:")
for time_zone in time_zones:
    print(time_zone)

# Get the timezone information for geographical numbers
time_zones_geographical = timezone.time_zones_for_geographical_number(phone)
print("\nTime Zones for Geographical Number:")
for time_zone in time_zones_geographical:
    print(time_zone)

# Get the carrier name
carrier_name = carrier.name_for_number(phone, 'en')  # You can specify the language
print("\nCarrier Name for Number:")
print(carrier_name)

# Get geographic information
region = geocoder.description_for_number(phone, 'en')  # You can specify the language
print("\nGeographic Location for Number:")
print(region)


region = geocoder.country_name_for_number(phone, 'en')  # You can specify the language
print("\nCountry name for Number:")
print(region)


