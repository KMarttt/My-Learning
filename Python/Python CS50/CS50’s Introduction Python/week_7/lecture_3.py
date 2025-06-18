import  re
#twitter.py

# the goal is to prompt the user of the URL of their Twitter profile
# then extract the username from the URL

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

# replace - replace (string you want to change, string you want to replace in the old string)


# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# https or http
# no $ at the end because the username is placed there



# if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(3))



if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
