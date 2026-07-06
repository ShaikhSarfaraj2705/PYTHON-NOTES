# =====================================================
# DJANGO FORM VALIDATION
# =====================================================

# Form Validation ensures that user input
# is correct before processing or saving it.

# Django provides:
#
# 1. Built-in Validation
# 2. Custom Field Validation
# 3. Form-Level Validation

# Validation Flow
#
# User Input
#      │
#      ▼
# Django Form
#      │
# form.is_valid()
#      │
#      ▼
# Valid Data
#      │
# cleaned_data
#      │
# Save / Process Data