from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()

media = instagram.get_media_by_id('1880687465858169462')

#not optimal to many calls
tagged_users = instagram.get_media_tagged_users_by_code(media.shortCode)

print(tagged_users)
