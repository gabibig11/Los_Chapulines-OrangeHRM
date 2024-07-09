

def clean_data_location(item):
        return {
            "name": item.get("name"),
            "city": item.get("city"),
            "phone": item.get("phone"),
            "time_zone": item.get("time_zone"),
            "province": item.get("province"),
            "state": item.get("province"),  # Assuming "province" should be used for "state"
            "address": item.get("address"),
            "zipCode": item.get("zipCode"),
            "fax": item.get("fax"),
            "notes": item.get("notes"),
            "countryCode": item.get("countryCode"),
            "eeo_applicable": int(item.get("eeo_applicable"))
        }
