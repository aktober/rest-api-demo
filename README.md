**API endpoints:**

`[POST] /api/users/create/`  - create user

`[POST] /api/token/` [params: username, password] - obtain jwt token

`[POST] /api/posts/` - create post (require: token, title, text)

`[GET] /api/posts/` - posts list (require: token)

`[GET] /api/posts/<pk>/` - post details (require: token)

`[PUT] /api/posts/<pk>/` - post update (require: token)

`[DELETE] /api/posts/<pk>/` - delete post (require: token)