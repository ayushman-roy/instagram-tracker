from context import Instagram # pylint: disable=no-name-in-module

# If account is public you can query Instagram without auth
instagram = Instagram()

# For getting information about account you don't need to auth:
account = instagram.get_account('kevin')

# Available fields
print('Account info:')
print('Id', account.identifier)
print('Username', account.username)
print('Full name', account.full_name)
print('Biography', account.biography)
print('Profile pic url', account.get_profile_picture_url())
print('External Url', account.external_url)
print('Number of published posts', account.media_count)
print('Number of followers', account.followed_by_count)
print('Number of follows', account.follows_count)
print('Is private', account.is_private)
print('Is verified', account.is_verified)
