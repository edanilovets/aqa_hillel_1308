import re

# re.match
# re.findall
# re.sub

# Example 1
phone = "383883483"
def is_only_digits(text):
    pattern = "^\d+$"
    match = re.match(pattern, text)
    return match is not None

print("Is only digits?", is_only_digits(phone))

# Example 2
def is_valid_username(username):
    pattern = "^\w{3,15}$"
    match = re.match(pattern, username)
    return match is not None

print("Is valid user?", is_valid_username("UUser_123"))

# Example 3: check date mm/dd/yyyy
def is_valid_date(text):
    pattern = "^\d{2}/\d{2}/\d{4}$"
    match = re.match(pattern, text)
    return match is not None

print("Is valid date?", is_valid_date("11/33/2024"))

# Example 4: find links in text/html
def find_links(html_content):
    pattern = r'href=["\'](https?://[^\s"\']+)["\']'
    return re.findall(pattern, html_content)


content = """
<div class="KxwPGc AghGtd"><a class="pHiOh" href="https://about.google/?utm_source=google-UA&amp;utm_medium=referral&amp;utm_campaign=hp-footer&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://about.google/%3Futm_source%3Dgoogle-UA%26utm_medium%3Dreferral%26utm_campaign%3Dhp-footer%26fg%3D1&amp;ved=0ahUKEwiMkpXgsteJAxX-VfEDHdjGMtwQkNQCCCM&amp;opi=89978449">About</a><a class="pHiOh" href="https://www.google.com/intl/en_ua/ads/?subid=ww-ww-et-g-awa-a-g_hpafoot1_1!o2&amp;utm_source=google.com&amp;utm_medium=referral&amp;utm_campaign=google_hpafooter&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://www.google.com/intl/en_ua/ads/%3Fsubid%3Dww-ww-et-g-awa-a-g_hpafoot1_1!o2%26utm_source%3Dgoogle.com%26utm_medium%3Dreferral%26utm_campaign%3Dgoogle_hpafooter%26fg%3D1&amp;ved=0ahUKEwiMkpXgsteJAxX-VfEDHdjGMtwQkdQCCCQ&amp;opi=89978449">Advertising</a><a class="pHiOh" href="https://www.google.com/services/?subid=ww-ww-et-g-awa-a-g_hpbfoot1_1!o2&amp;utm_source=google.com&amp;utm_medium=referral&amp;utm_campaign=google_hpbfooter&amp;fg=1" ping="/url?sa=t&amp;rct=j&amp;source=webhp&amp;url=https://www.google.com/services/%3Fsubid%3Dww-ww-et-g-awa-a-g_hpbfoot1_1!o2%26utm_source%3Dgoogle.com%26utm_medium%3Dreferral%26utm_campaign%3Dgoogle_hpbfooter%26fg%3D1&amp;ved=0ahUKEwiMkpXgsteJAxX-VfEDHdjGMtwQktQCCCU&amp;opi=89978449">Business</a><a class="pHiOh" href="https://google.com/search/howsearchworks/?fg=1"> How Search works </a></div>
"""

links = find_links(content)




