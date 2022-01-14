from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('', '', '/pathtofolder')
instagram.login()

# Get media comments by shortcode
likes = instagram.get_media_likes_by_code('BG3Iz-No1IZ', 100)

print("Result count: " + str(len(likes['accounts'])))

for like in likes['accounts']:
    print(like)

# ...



