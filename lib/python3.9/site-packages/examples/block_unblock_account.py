from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('', '', 'pathtocache')
instagram.login()

instagram.block('user_id')
instagram.unblock('user_id')
