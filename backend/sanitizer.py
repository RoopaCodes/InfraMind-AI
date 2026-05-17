import re

def sanitize_logs(log_data):

    # Mask IP addresses
    log_data = re.sub(
        r'\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b',
        '[IP_MASKED]',
        log_data
    )

    # Mask hostnames
    log_data = re.sub(
        r'prod-[a-zA-Z0-9-]+',
        '[HOST_MASKED]',
        log_data
    )

    # Mask usernames
    log_data = re.sub(
        r'user=\\w+',
        'user=[USER_MASKED]',
        log_data
    )

    # Mask emails
    log_data = re.sub(
        r'[\\w\\.-]+@[\\w\\.-]+',
        '[EMAIL_MASKED]',
        log_data
    )

    return log_data