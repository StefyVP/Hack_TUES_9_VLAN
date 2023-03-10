import requests

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }

    city = response.get("city")
    region = response.get("region")
    country = response.get("country")

    location_data2 = f"ip: {ip_address}, city: {city}, region: {region}, country: {country} "

    return location_data2


# print(get_location())