from context import Instagram # pylint: disable=no-name-in-module

# If account is public you can query Instagram without auth

instagram = Instagram()

medias = instagram.get_medias("kevin", 25)
media = medias[6]

print(media)
account = media.owner
print(account)
# print('Username', account.username)
# print('Full Name', account.full_name)
# print('Profile Pic Url', account.get_profile_picture_url_hd())


# If account private you should be subscribed and after auth it will be available

# username = ''
# password = ''
# session_folder = ''
# instagram = Instagram()
# instagram.with_credentials(username, password, session_folder)
# instagram = Instagram()
# instagram.login()
# instagram.get_medias('private_account', 100)
