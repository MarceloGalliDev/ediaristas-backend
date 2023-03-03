## Rest e RESTfull

# 1 - HateOs
  - necessário possuir uma URI indicando o caminho do recurso solicitado
  - na montagem do api em json por exemplo, o modelo REST é necessario incluir uma uri (url indicando caminho), demonstrar o retorno do status CODE correto
  - usamos o content negociation, é o acordo realizado entre API e USER, onde o user pode escolher o tipo que será recebido os dados


> Analise de recursos
  > métodos
  - GET
  - POST
  - PUT
  - DELETE
  - PATCH

> Status CODE
  - 100 a 199 - informações
  - 200 a 299 - sucesso
  - 300 a 399 - redirecionamento
  - 400 a 499 - erro cliente
  - 500 a 599 - erro servidor

  > mais usados
    - 200 - OK
    - 201 - criação de recurso
    - 301 - movido permanentemente
    - 302 - movido temporariamente
    - 400 - bad request,erro na requisição
    - 401 - não autorizado
    - 402 - pagamento necessário
    - 403 - forbidden, proibido
    - 404 - não encontrado o recurso
    - 405 - método não aceito
    - 422 - entidade não processavel
    - 500 - erro interno do servidor
    - 504 - timeout, sem resposta do servidor

