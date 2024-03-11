##Api constants
# 1. base URL

def base_url():
    return "https://restful-booker.herokuapp.com"

def create_url():
    return "https://restful-booker.herokuapp.com/booking"


def token_url():
    return "https://restful-booker.herokuapp.com/auth"

#update and delete : put , patch  , delete : we need booking id here

def update_del_patch_put(booking_id):
    return "https://restful-booker.herokuapp.com/booking/", +str(booking_id)




