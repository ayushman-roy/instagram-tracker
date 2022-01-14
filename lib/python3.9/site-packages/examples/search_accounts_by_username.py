from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()

accounts = instagram.search_accounts_by_username('Kevin M')

account = accounts[0]
# Following fields are available in this request
print('Account info:')
print('Username', account.username)
print('Full name', account.full_name)
print('Profile pic url', account.getProfilePicUrlHd())