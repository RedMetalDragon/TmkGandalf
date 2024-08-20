# Define the name of the header to verify in the request to match subscription tiers
SUBSCRIPTION_HEADER = "X-Tier"

# Define the dictionary with subscription tiers and token limits
SUBSCRIPTION_TIERS = {"free": 124, "basic": 248, "premium": 512, "enterprise": 1024}

# Define the list of accepted content types
ACCEPTED_CONTENT_TYPES = ["application/json; charset=utf-8"]