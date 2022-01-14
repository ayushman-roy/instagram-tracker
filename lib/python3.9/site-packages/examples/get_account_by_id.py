from context import Instagram # pylint: disable=no-name-in-module

account = Instagram().get_account_by_id('3')

# Available fields
print(account)
# print('Account info:')
# print('Id', account.identifier)
# print('Username', account.username)
# print('Full name', account.full_name)
# print('Biography', account.biography)
# print('Profile pic url', account.getProfilePicUrlHd())
# print('External Url', account.external_url)
# print('Number of published posts', account.mediaCount)
# print('Number of followers', account.followed_by_count)
# print('Number of follows', account.follows_count)
# print('Is private', account.is_private)
# print('Is verified', account.is_verified)