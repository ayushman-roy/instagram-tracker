from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()

# Location id from facebook
location = instagram.get_location_by_id(1)
print(location)

