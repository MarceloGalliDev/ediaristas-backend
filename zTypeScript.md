## TypeScript 

# 1 - Node.js
  - Necessário ter node.js instalado

# 2 - TS comandos
  - npx tsc --init
  - criado o arquivo tsconfig.json
    - mudar "module": "ESNext" = é a utilização da ultima versão do ECMAScript
    - mudar "outDir": "./Dist" = é onde será a saída dos arquivos JS
  - npx tsc = gera o arquivo js na pasta Dist
  - npx tsc -w = watch mode, modo de observação, para gerar automático o js

# 3 - Funções TS
  - let a: number; = para declarar a tipagem usamos :
  - let a: number[] = []; = para declarar a tipagem de array, usamos [] anterior ao tipo
  - let a: number | string; = indicamos que pode ser number ou string
  - let a: (number | string)[] = []; indicamos que é um array de number ou string
  - let a: (number | 'zero)[] = []; indicamos que ele pode receber qualquer número ou a string 'zero' somente

# 4 - Types
  - type MeuTipo = (string | 5)[];
    let a: MeuTipo = [];
  - idade?: number;

# 5 - Enum
  - Definir valores fixos, impede de mudar o valor
  enum Direction{
    left = 'esquerda',
    rigth = 'direita'
  }
  function handleMovement(direction: Direction){
    if(direction == Direction.left){
      return 1
    }
  }

# 6 - Type any
  - Identifica um tipo forçado, na situação abaixo quando usamos o operador diamante, obtivemos as funções de string na logica
  let minhaVariavel: any = 'teste';
  (<string>minhaVariavel).lowerCase()
  (minhaVariavel as string).lowerCase()

# 7 - Interfaces
  - A diferença para types, é que podemos declarar mais de uma vez o mesmo type, com o mesmo nome
  - ou seja é uma extensão de tipagem

# 8 - Generics
  - Pode receber qualquer tipo de variavél
  let minhaLista: number[] = [1, 2, 3];
  function primeitoNumero<T>(lista: T[]): T{
    return lista[0];
  }
  primeiroNumero<number>(minhaLista);
  primeiroNumero<string>(minhaLista);

  - neste caso estamos nomeando um tipo que assume quando nos declaramos a variável