from context import Instagram # pylint: disable=no-name-in-module

instagram = Instagram()
instagram.with_credentials('username', 'password', 'path/to/cache/folder')
instagram.login()


# add comment to post
mediaId = '1874597980243548658'
comment = instagram.add_comment(mediaId, 'nice!!')
# replied to comment
comment_b = instagram.add_comment(mediaId, 'cool man', comment)

    
instagram.delete_comment(mediaId, comment)

