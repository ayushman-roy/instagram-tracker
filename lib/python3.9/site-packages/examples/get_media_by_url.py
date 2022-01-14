from context import Instagram # pylint: disable=no-name-in-module

# If account is public you can query Instagram without auth
instagram = Instagram()

# If account is private and you subscribed to it, first login
# instagram.with_credentials('username', 'password', 'cachePath')
# instagram.login()

media = instagram.get_media_by_url('https://www.instagram.com/p/BHaRdodBouH')

print(media)
print(media.owner)
