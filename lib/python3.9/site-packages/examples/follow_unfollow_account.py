from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('', '', 'pathtocache')
instagram.login()

instagram.follow('user_id')
instagram.unfollow('user_id')