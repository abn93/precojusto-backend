# Endpoints

## 1. GET http://localhost:5000/load_posts

Carrega os posts da API pública https://jsonplaceholder.typicode.com/posts e salva no banco de dados.

No insonmia ou Postman:
```bash
http://localhost:5000/load_posts
```

## 2. POST http://localhost:5000/posts

Cria um novo post

Exemplo de JSON:
```json
{
  "userId": 1,
  "title": "My new post",
  "body": "This is the content of the new post.",
  "comments": [
    {
      "name": "User",
      "email": "user@example.com",
      "body": "new comment."
    }
  ]
}
```

## 3. GET http://localhost:5000/posts

Lê posts com suporte a paginação e busca por título.

```bash
GET http://localhost:5000/posts
```

Com paginação

```bash
GET GET "http://localhost:5000/posts?page=1&per_page=5"
```

Filtrados por title:

```bash
GET "http://localhost:5000/posts?title=My%20new%20post"
```

## 4. GET http://localhost:5000/posts/101

Lê um post específico pelo ID.

```bash
GET http://localhost:5000/posts/101
```

## 5. PUT http://localhost:5000/posts/101

 Atualiza um post específico pelo ID.
 
```json
{
    "userId": 1,
    "title": "Updated title for the new post",
    "body": "This is the updated content of the new post."
}
```

## 6. DELETE http://localhost:5000/posts/101

Deleta um post específico pelo ID.

```bash
DELETE http://localhost:5000/posts/101
```

## 7. POST http://localhost:5000/posts/101/comments

Cria um novo comentário para um post específico pelo ID do post.

```json
{
    "name": "Test user",
    "email": "testuser@example.com",
    "body": "This is a comment on the post."
}
```

## 8. GET http://localhost:5000/posts/101/comments

Lê todos os comentários de um post específico pelo ID do post, ordenados por ID em ordem decrescente.

```bash
GET http://localhost:5000/posts/101/comments
```

## 9. PUT http://localhost:5000/comments/1

Atualiza um comentário específico pelo ID.

```json
{
    "name": "Update comment",
    "email": "updatecomment@example.com",
    "body": "This is an updated comment on the post."
}
```

## 10. DELETE http://localhost:5000/comments/1

Deleta um comentário específico pelo ID.

```json
{
    "name": "Update comment",
    "email": "updatecomment@example.com",
    "body": "This is an updated comment on the post."
}
```

```bash
10. DELETE http://localhost:5000/comments/1
```