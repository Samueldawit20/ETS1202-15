text = "Today is laundry day"

# Checking
starts_with_today = text.startswith("Today")      # Should return True
starts_with_laundry = text.startswith("laundry")   # Should return False
starts_with_today_lower = text.startswith("today")  # Should return False (case-sensitive)

# To Print
print(f"Starts with 'Today': {starts_with_today}")          # Output: True
print(f"Starts with 'laundry': {starts_with_laundry}")      # Output: False
print(f"Starts with 'today': {starts_with_today_lower}")    # Output: False
