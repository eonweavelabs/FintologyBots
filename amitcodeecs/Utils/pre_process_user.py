from Utils.remove_special_chars import remove_special_chars
from Utils.database_queries import check_email_exists
from Utils.create_inbox import create_inbox
import phonenumbers
from phonenumbers import geocoder

def get_base_phone_number(international_phone_number):
    try:
        phone_number = phonenumbers.parse(international_phone_number)
        base_phone_number = phonenumbers.format_number(
            phone_number, phonenumbers.PhoneNumberFormat.NATIONAL
        )
        clean_phone_number = "".join(
            [char for char in base_phone_number if char.isnumeric()]
        )
        country = geocoder.country_name_for_number(phone_number, "en")
        if clean_phone_number[0] == "0":
            clean_phone_number = clean_phone_number[1:]
        return clean_phone_number
    except phonenumbers.NumberParseException as e:
        return str(e)

def fix_dob(user):
    dob = user.get("personal").get("dob")
    if dob:
        dob_parts = dob.split("-")
        if len(dob_parts) == 3:
            dob = dob_parts[1] + dob_parts[2] + dob_parts[0]
            user["personal"]["dob"] = dob
    return user

def fix_phone_number(user):
    personal_data = user.get("personal", {})
    business_data = user.get("business", {})

    mobile_number = personal_data.get("mobileNumber")
    business_phone = business_data.get("businessPhone")

    if mobile_number:
        personal_data["mobileNumber"] = get_base_phone_number(mobile_number)

    if business_phone:
        business_data["businessPhone"] = get_base_phone_number(business_phone)

    user["personal"] = personal_data
    user["business"] = business_data
    return user

def pre_process_user(user):
    if not user:
        raise ValueError("User data cannot be None")

    personal = user.get("personal", {})
    business = user.get("business", {})

    # Update position field if it is "Other"
    if personal.get("position") == "Other":
        personal["position"] = "Executive"

    # Remove special characters from specific personal fields
    for field in [
        "firstName",
        "middleName",
        "lastName",
        "motherMaidenName",
        "currentEmployer",
    ]:
        if personal.get(field):
            personal[field] = remove_special_chars(personal.get(field))

    # Remove special characters from business fields if needed
    if user.get("preApproval", {}).get("businessFunding"):
        for field in ["businessName"]:
            if business.get(field):
                business[field] = remove_special_chars(business.get(field))

    # Update user with the modified personal and business data
    user["personal"] = personal
    user["business"] = business

    # Check if email exists or create an inbox
    email_exists, email = check_email_exists(user)
    if email_exists:
        user["email"] = email
    else:
        user["email"] = create_inbox(user)

    # Fix date of birth and phone numbers
    user = fix_dob(user)
    user = fix_phone_number(user)

    return user
