DISCOUNTS = {
    "hiva30": 30,
    "vip50": 50,
}

def apply_coupon(code):
    return DISCOUNTS.get(code.lower(), 0)
