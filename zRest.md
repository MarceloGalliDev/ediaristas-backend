# Rest e RESTfull

## 1 - HateOs
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

  > Mais usados
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

> Modelo de maturidade Richardson
  - Possui 4 níveis
    - Level 0 - nossa API nào utiliza nenhum recurso
    - Level 1 - ja é organizado em recursos
    - Level 2 - utilizamos corretamente os método http e status code
    - Level 3 - já o topo da cadeia o HATEOAS

> Autenticação e autorização
  - chave de api
  - autenticação básica de http
  - OAuth
  - JWT Token
  - dicas de segurança
    - sempre utilizar https
    - nunca passe dados de segunraça pela URL
    - utilize rate limit (limite de requisições por minuto)
    - valide os dados recebidos
    - utilize api gateway (parte de segurança da api, vai na frente da api)

## 2 - JWT
  - é uma forma padrão de segurança para objetos JSON
  - JWT utiliza uma chave secreta baseada em algoritimo HMAC, ou par de chaves RSA ou ECDSA
  - Autorização: Este é o cenário mais comum para o uso do JWT. Depois que o usuário estiver autenticado, cada requisição subsequente incluirá o JWT, permitindo que o usuário acesse rotas, serviços e recursos permitidos com esse token.
  - Troca de Informações: JSON Web Tokens são uma boa maneira de transmitir informações com segurança entre as partes. Como os JWTs podem ser assinados, por exemplo, usando pares de chaves pública e privada podemos garantir que os remetentes são quem dizem ser.
  - JWT é composto por 3 etapas:
    - header, onde temos o algoritmo e o type do algoritmo
    - payload, temos as claims, que são:
      - a entidade 
      - e dados adicionais
    - signature, aqui juntamos as duas partes citadas acima e assinamos
  
  - JWT (JSON Web Token): Representa o token propriamente dito;
  - JWS (JSON Web Signature): Representa a assinatura do token;
  - JWE (JSON Web Encryption): Representa a assinatura para criptografia do token;
  - JWK (JSON Web Keys): Representa as chaves para a assinatura;
  - JWA (JSON Web Algorithms): Representa os algoritmos para assinatura do token;

  - Chave IAT, formato timestamp
  - Chave EXP, o tempo que o token vai levar para expirar

  - Utilizar o refresh token