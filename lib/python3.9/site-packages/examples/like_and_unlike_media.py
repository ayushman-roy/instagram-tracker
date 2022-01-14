from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()

instagram.like('1874597980243548658')
instagram.unlike('1874597980243548658')