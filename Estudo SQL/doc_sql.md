- [Orientações gerais](#orientações-gerais)
  - [Aplique o DRY principle](#aplique-o-dry-principle)
  - [Evite cláusulas de `SELECT` enormes](#evite-cláusulas-de-select-enormes)
- [Formatação](#formatação)
  - [Linhas não devem ser maiores que 120 caracteres](#linhas-não-devem-ser-maiores-que-120-caracteres)
  - [Keywords SQL em maiúsculo](#keywords-sql-em-maiúsculo)
  - [Utilize espaços para indentação](#utilize-espaços-para-indentação)
  - [Alinhe tudo à esquerda](#alinhe-tudo-à-esquerda)
  - [Vírgulas no final da linha](#vírgulas-no-final-da-linha)
  - [Use aspas simples para strings](#use-aspas-simples-para-strings)
  - [Cláusula `SELECT`](#cláusula-select)
    - [Single line](#single-line)
  - [Cláusula `FROM`](#cláusula-from)
    - [Cláusulas `JOIN`](#cláusulas-join)
  - [Cláusula `WHERE`](#cláusula-where)
    - [Explicite condições booleanas](#explicite-condições-booleanas)
  - [Cláusulas `ORDER BY` e `GROUP BY`](#cláusulas-order-by-e-group-by)
  - [Window functions](#window-functions)
  - [Listas `IN`](#listas-in)
    - [Não coloque espaços extras dentro de parênteses](#não-coloque-espaços-extras-dentro-de-parênteses)
  - [Cláusula `CASE/WHEN`](#cláusula-casewhen)
- [Ordenação das colunas](#ordenação-das-colunas)
- [Operadores](#operadores)
  - [Use `!=` em vez de `<>`](#use--em-vez-de-)
  - [Use `||` em vez de `CONCAT`](#use--em-vez-de-concat)
  - [Use `COALESCE` em vez de `IFNULL` ou `NVL`](#use-coalesce-em-vez-de-ifnull-ou-nvl)
  - [Use `IS NULL` em vez de `ISNULL`, e `IS NOT NULL` em vez de `NOTNULL`](#use-is-null-em-vez-de-isnull-e-is-not-null-em-vez-de-notnull)
  - [Use `CASE` em vez de `IFF` ou `IF`](#use-case-em-vez-de-iff-ou-if)
  - [Use `WHERE` em vez de `HAVING` quando possível](#use-where-em-vez-de-having-quando-possível)
  - [Use `UNION ALL` em vez de `UNION`, a menos que linhas repetidas realmente devam ser removidas](#use-union-all-em-vez-de-union-a-menos-que-linhas-repetidas-realmente-devam-ser-removidas)
  - [Use `SELECT DISTINCT` em vez de agrupar por todas as colunas](#use-select-distinct-em-vez-de-agrupar-por-todas-as-colunas)
  - [Para funções que tomam expressões de data como parâmetro, especificar a expressão como string em vez de keyword](#para-funções-que-tomam-expressões-de-data-como-parâmetro-especificar-a-expressão-como-string-em-vez-de-keyword)
  - [Use funções especializadas para extração de datas](#use-funções-especializadas-para-extração-de-datas)
  - [Simplifique expressões `CASE` sempre que possível](#simplifique-expressões-case-sempre-que-possível)
- [JOINS](#joins)
  - [Não utilize `USING` em joins](#não-utilize-using-em-joins)
  - [Explicite o tipo do `JOIN`](#explicite-o-tipo-do-join)
  - [Evite a utilização de `RIGHT JOINS`](#evite-a-utilização-de-right-joins)
  - [Nas condições da junção, ordene as tabelas de acordo com sua aparição](#nas-condições-da-junção-ordene-as-tabelas-de-acordo-com-sua-aparição)
    - [Na junção de mútiplas tabelas, prefixe as colunas com a tabela/alias](#na-junção-de-mútiplas-tabelas-prefixe-as-colunas-com-a-tabelaalias)
  - [Declare filtros no `WHERE` em vez de utilizar a cláusula do `JOIN`](#declare-filtros-no-where-em-vez-de-utilizar-a-cláusula-do-join)
  - [Ordene os `JOINS` de forma semântica](#ordene-os-joins-de-forma-semântica)
- [Comentários](#comentários)
  - [Comentários devem ser colocados no topo da query](#comentários-devem-ser-colocados-no-topo-da-query)
  - [Sempre utilize a sintaxe `/* */`](#sempre-utilize-a-sintaxe--)
  - [Respeite o limite de caracteres das linhas](#respeite-o-limite-de-caracteres-das-linhas)
  - [Cálculos devem ser brevemento descritos](#cálculos-devem-ser-brevemento-descritos)
  - [Não deixe comentários `TODO`](#não-deixe-comentários-todo)
- [CTEs](#ctes)
  - [Use CTEs, não subqueries](#use-ctes-não-subqueries)
  - [CTEs complexos devem ser comentados](#ctes-complexos-devem-ser-comentados)
  - [CTE duplicado entre modelos deve ser extraído no seu próprio modelo](#cte-duplicado-entre-modelos-deve-ser-extraído-no-seu-próprio-modelo)
  - [CTEs devem realizar uma única unidade lógica de trabalho, quando possível](#ctes-devem-realizar-uma-única-unidade-lógica-de-trabalho-quando-possível)
  - [Utilize CTEs como declarações de imports](#utilize-ctes-como-declarações-de-imports)
  - [Nome do CTE deve ser conciso o possível mas mantendo a clareza](#nome-do-cte-deve-ser-conciso-o-possível-mas-mantendo-a-clareza)
  - [Crie um CTE `final`, ou similar](#crie-um-cte-final-ou-similar)
  - [Mantenha a formatação adequada](#mantenha-a-formatação-adequada)
- [Aliases](#aliases)
  - [Evite alias de tabela desnecessários, especialmente abreviaturas](#evite-alias-de-tabela-desnecessários-especialmente-abreviaturas)
  - [Sempre utilize a keyword `AS` para alias de colunas, expressões e tabelas](#sempre-utilize-a-keyword-as-para-alias-de-colunas-expressões-e-tabelas)
  - [Sempre renomeie agregações e outras expressões de coluna](#sempre-renomeie-agregações-e-outras-expressões-de-coluna)
  - [Tire vantagem de alias lateral quando agrupar colunas por nome](#tire-vantagem-de-alias-lateral-quando-agrupar-colunas-por-nome)
- [Convenções de nomenclatura](#convenções-de-nomenclatura)
  - [Tabelas](#tabelas)
  - [Colunas](#colunas)
    - [Colunas boolean](#colunas-boolean)
    - [Colunas date](#colunas-date)
    - [Colunas timestamp](#colunas-timestamp)
  - [Funções/procedures](#funçõesprocedures)
- [Tipos de Dados](#tipos-de-dados)
- [Referências](#referências)

Orientações gerais
------------------

_DO NOT OPTIMIZE FOR A SMALLER NUMBER OF LINES OF CODE. NEWLINES ARE CHEAP._ [_BRAIN TIME IS EXPENSIVE._](https://blog.getdbt.com/write-better-sql-a-defense-of-group-by-1/)

### Aplique o DRY principle

[DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) é o acrónimo para "**Don't repeat yourself**", conceito de desenvolvimento de software que prega a remoção de código repetido visando diminuir a complexidade. Utilize CTEs, jinja e macros no dbt sempre que possível.

### Evite cláusulas de `SELECT` enormes

Uma cláusula de `SELECT` grande é difícil de ser compreendida. Refatore-a em mútiplos CTEs menores que possam ser unidos.

Formatação
----------

### Linhas não devem ser maiores que 120 caracteres

Linhas muito longas são difíceis de ler, especialmente em situações onde o espaço é limitado, como telas menores e side-by-side diffs.

### Keywords SQL em maiúsculo

Todas as keywords SQL devem estar sempre em maísculo (e.g. `SELECT,` `AS`, `FROM`, `JOIN`, etc.).

### Utilize espaços para indentação

Cada nível de indentação deve ser feito com 4 caracteres de espaço. **Nunca utilize tabs**.

```
/* Good */
SELECT
    id,
    email
FROM customers
WHERE
    email LIKE '%@domain.com' AND
    plan_name != 'free'

/* Bad */
SELECT
  id,
  email
FROM customers
WHERE
  email LIKE '%@domain.com' AND
  plan_name != 'free'
```

### Alinhe tudo à esquerda

Manter todo o alinhamento à esquerda facilita a escrita e a consistência.

```
/* Good */
SELECT email
FROM customers
WHERE email LIKE '%@domain.com'

/* Bad */
SELECT email
  FROM customers
 WHERE email LIKE '%@domain.com'
```

### Vírgulas no final da linha

```
/* Good */
SELECT
    deleted AS is_deleted,
    accountId AS account_id
FROM table

/* Bad */
SELECT
  deleted AS is_deleted
  , accountId AS account_id
FROM table
```

### Use aspas simples para strings

Alguns dialetos SQL suportam a utilização de aspas duplas, ou mesmo triplas, para strings. Para a maioria dos dialetos, porém:

* Strings com aspas duplas representam identificadores.

* Strings com aspas triplas são interpretadas como se a string tivesse aspas simples no início e fim.


```
/* Good */
SELECT *
FROM customers
WHERE email LIKE '%@domain.com'

/* Bad */
SELECT *
FROM customers
WHERE email LIKE "%@domain.com"
/* Provavelmente resultará em erro como \`column "%@domain.com" does not exist\`. */

/* Bad */
SELECT *
FROM customers
WHERE email LIKE '''%@domain.com'''
/* Provavelmente será interpretado como '\\'%domain.com\\''. */
```

### Cláusula `SELECT`

* Se existir apenas uma coluna referenciada, coloque na mesma linha do `SELECT`.

* Se múltiplas colunas referenciadas, coloque cada uma na sua própria linha (incluindo a primeira), indentando um nível a mais que o `SELECT`.

* Se existir o qualificador `DISTINCT`, coloque-o na mesma linha do `SELECT`.


```
/* Good */
SELECT id

/* Good */
SELECT
    id,
    email

/* Good */
SELECT DISTINCT country

/* Good */
SELECT DISTINCT
    state,
    country

/* Bad */
SELECT id, email

/* Bad */
SELECT id,
    email

/* Bad */
SELECT DISTINCT state, country
```

#### Single line

Uma expressão SQL pode ser colocada toda em uma única linha caso selecione somente um campo e não houver complexidade adicional na cosulta.

```
/* Good */
SELECT * FROM users

/* Good */
SELECT id FROM users

/* Good */
SELECT COUNT(*) FROM users

/* Bad */
SELECT id, name FROM users

/* Bad */
SELECT name FROM users WHERE id = 1
```

### Cláusula `FROM`

A tabela inicial sendo selecionada deve estar na mesma linha do `FROM`.

```
/* Good */
FROM customers

/* Bad */
FROM
    customers
```

Apenas uma tabela deve estar referenciada no `FROM`, nunca use `FROM`\-joins:

```
/* Good */
SELECT
    projects.name AS project_name,
    COUNT(backings.id) AS backings_count
FROM projects
INNER JOIN backings ON projects.id = backings.project_id
GROUP BY 1

/* Bad */
SELECT
  projects.name AS project_name,
  COUNT(backings.id) AS backings_count
FROM projects, backings
WHERE projects.id = backings.project_id
GROUP BY 1
```

#### Cláusulas `JOIN`

Se existirem outras tabelas sendo referenciadas em junção:

* Coloque cada `JOIN` na sua própria linha, no mesmo nível de indentação do `FROM`.

* Se existir apenas uma condição na junção, coloque na mesma linha do `JOIN`.

* Se existirem múltiplas condições na junção, finalize a linha do `JOIN` com `ON` e coloque cada condição na sua própria linha (incluindo a primeira), indentando um nível maior que o `JOIN`.


```
/* Good */
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id

/* Bad */
FROM customers
    LEFT JOIN orders ON customers.id = orders.customer_id

/* Bad */
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id

/* Good */
FROM customers
LEFT JOIN orders ON
    customers.id = orders.customer_id AND
    customers.region_id = orders.region_id

/* Bad */
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
    AND customers.region_id = orders.region_id

/* Bad */
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id
    AND customers.region_id = orders.region_id
```

### Cláusula `WHERE`

* Se existir apenas uma condição, coloque na mesma linha do `WHERE`.

* Se existirem múltiplas condições, coloque cada condição na sua própria linha (incluindo a primeira), indentando um nível maior que o `WHERE`.

  * O operador lógico deve estar no final de cada linha.


```
/* Good */
WHERE email LIKE '%@domain.com'

/* Good */
WHERE
    email LIKE '%@domain.com' AND
    plan_name != 'free'

/* Good */
WHERE email LIKE '%@domain.com' AND plan_name != 'free'

/* Bad */
WHERE email LIKE '%@domain.com'
    AND plan_name != 'free'

```

#### Explicite condições booleanas

```
/* Good */
SELECT *
FROM customers
WHERE is_cancelled = TRUE

SELECT *
FROM customers
WHERE is_cancelled = FALSE

/* Bad */
SELECT *
FROM customers
WHERE is_cancelled

SELECT *
FROM customers
WHERE NOT is_cancelled
```

### Cláusulas `ORDER BY` e `GROUP BY`

* Utilize o número da coluna para ordenação e agrupamento, não utilize o nome da coluna (e.g. `GROUP BY 1, 2`).

* Se o agrupamento estiver sendo feito em muitas colunas, revise a modelagem.

* Coloque todos os números das colunas na mesma linha do `GROUP BY`/`ORDER BY`.

* Na ordenação, sempre explicite o sentido da mesma: `ASC` ou `DESC`.

* Quando agrupar por 3 ou mais colunas em um modelo dbt, utilize a macro `group_by` do pacote dbt-utils.

```
/* Good */
GROUP BY 1, 2, 3

/* Good */
ORDER BY 1 ASC, 2 DESC, 3 ASC

/* Bad */
GROUP BY
    1,
    2,
    3

/* Bad */
ORDER BY plan_name

/* Bad */
ORDER BY
    plan_name,
    signup_month

/* Bad */
ORDER BY plan_name, signup_month

/* Bad */
ORDER BY plan_name,
    signup_month
```

### Window functions

* Você pode colocar todas as cláusulas da window function em uma mesma linha, desde que não a torne mais extensa que o padrão.

* Se quebrar a window function em múltiplas linhas:

  * Coloque cada sub-cláusula do `OVER ()` na sua própria linha, indentando um nível maior que a window function:

    * `PARTITION BY`

    * `ORDER BY`

    * `ROWS BETWEEN` / `RANGE BETWEEN`

  * Coloque o parênteses de fechamento do `OVER ()` na sua própria linha no mesmo nível de indentação da window function.


```
/* Good */
SELECT
    customer_id,
    invoice_number,
    row_number() OVER (PARTITION BY customer_id ORDER BY created_at) AS order_rank
FROM orders

/* Good */
SELECT
    customer_id,
    invoice_number,
    row_number() OVER (
        PARTITION BY customer_id
        ORDER BY created_at
    ) AS order_rank
FROM orders

/* Bad */
SELECT
    customer_id,
    invoice_number,
    row_number() OVER (PARTITION BY customer_id
                         ORDER BY created_at) AS order_rank
FROM orders
```

### Listas `IN`

Quebre listas longas dos valores do `IN` em múltiplas linhas indentadas, com um valor por linha.

```
/* Good */
WHERE email IN (
        'user-1@example.com',
        'user-2@example.com',
        'user-3@example.com'
    )

/* Bad */
WHERE email IN ('user-1@example.com', 'user-2@example.com', 'user-3@example.com')
```

#### Não coloque espaços extras dentro de parênteses

```
/* Good */
SELECT *
FROM customers
WHERE plan_name IN ('monthly', 'yearly')

/* Bad */
SELECT *
FROM customers
WHERE plan_name IN ( 'monthly', 'yearly' )
```

### Cláusula `CASE/WHEN`

Cada sub-cláusula `WHEN` deve estar na sua própria linha (nenhuma na mesma linha do `CASE`) e deve ser indentada um nível maior que a indentação do `CASE`. O `THEN` pode estar na mesma linha, ou na sua própria linha abaixo, com um nível de indentação maior.

```
/* Good */
SELECT
    CASE
        WHEN event_name = 'viewed_homepage' THEN 'Homepage'
        WHEN event_name = 'viewed_editor' THEN 'Editor'
        ELSE 'Other'
    END as page_name
FROM events

/* Good too */
SELECT
    CASE
        WHEN event_name = 'viewed_homepage'
            THEN 'Homepage'
        WHEN event_name = 'viewed_editor'
            THEN 'Editor'
        ELSE 'Other'
    END AS page_name
FROM events

/* Bad */
SELECT
    CASE WHEN event_name = 'viewed_homepage' THEN 'Homepage'
        WHEN event_name = 'viewed_editor' THEN 'Editor'
        ELSE 'Other'
    END AS page_name
FROM events
```

Ordenação das colunas
---------------------

Os campos de um modelo devem ser ordenados da seguinte forma:

1. chave primária

2. chaves estrangeiras

3. demais campos

4. metadados (`created_at`, `updated_at`, `is_deleted`, etc.)


```
/* Good */
SELECT
    id,
    name,
    created_at
FROM users

/* Bad */
SELECT
    created_at,
    name,
    id,
FROM users
```

Em agrupamentos, as colunas agrupadas devem aparecer no início.

```
/* Good */
SELECT
    com_created_at AS signup_year,
    COUNT(*) AS total_companies
FROM companies
GROUP BY 1

/* Bad */
SELECT
  COUNT(*) AS total_companies,
  com_created_at AS signup_year
FROM companies
GROUP BY 2
```

Operadores
----------

### Use `!=` em vez de `<>`

Não há um argumento técnico para esta definição, somente visão a padronização do operador.

### Use `||` em vez de `CONCAT`

`||` é um operador SQL padrão e, em alguns bancos, como o Redshift, `CONCAT` aceita somente dois argumentos.

### Use `COALESCE` em vez de `IFNULL` ou `NVL`

* Suportado por praticamente todos os bancos.
* Mais flexível e aceita um número arbitrário de argumentos.

### Use `IS NULL` em vez de `ISNULL`, e `IS NOT NULL` em vez de `NOTNULL`

`IS NULL` e `IS NOT NULL` são operadores padrão SQL suportados universalmente.

### Use `CASE` em vez de `IFF` ou `IF`

`CASE` é um operador SQL padrão suportado universalmente.

### Use `WHERE` em vez de `HAVING` quando possível

Filtros `WHERE` são mais performático pois são processados antes.

### Use `UNION ALL` em vez de `UNION`, a menos que linhas repetidas realmente devam ser removidas

`UNION ALL` é mais performático uma vez que não necessita das operações de ordenação e remoção das linhas duplicadas.

### Use `SELECT DISTINCT` em vez de agrupar por todas as colunas

Isso torna a intenção da consulta mais clara.

```
/* Good */
SELECT DISTINCT
    customer_id,
    DATE_TRUNC('day', created_at) AS purchase_date
FROM orders

/* Bad */
SELECT
    customer_id,
    DATE_TRUNC('day', created_at) AS purchase_date
FROM orders
GROUP BY 1, 2
```

### Para funções que tomam expressões de data como parâmetro, especificar a expressão como string em vez de keyword

Utilizar uma string deixa claro que não está fazendo referência a uma coluna.

```
/* Good */
DATE_TRUNC('month', created_at)

/* Bad */
DATE_TRUNC(month, created_at)
```

### Use funções especializadas para extração de datas

No MySQL use as funções específicas.

```
/* Good */
SELECT DAY(created_at)

/* Good */
SELECT MONTH(created_at)

/* Good */
SELECT YEAR(created_at)

/* Bad */
SELECT EXTRACT(DAY FROM created_at)

/* Bad */
SELECT EXTRACT(MONTH FROM created_at)

/* Bad */
SELECT EXTRACT(YEAR FROM created_at)
```

No Redshift use `DATE_PART` em vez de `EXTRACT`.

```
/* Good */
SELECT DATE_PART('month', created_at)

/* Bad */
SELECT EXTRACT('month' FROM created_at)
```

### Simplifique expressões `CASE` sempre que possível

```
/* OK */
CASE
    WHEN field_id = 1 THEN 'date'
    WHEN field_id = 2 THEN 'integer'
    WHEN field_id = 3 THEN 'currency'
    WHEN field_id = 4 THEN 'boolean'
    WHEN field_id = 5 THEN 'variant'
    WHEN field_id = 6 THEN 'text'
END AS field_type

/* Better */
CASE field_id
    WHEN 1 THEN 'date'
    WHEN 2 THEN 'integer'
    WHEN 3 THEN 'currency'
    WHEN 4 THEN 'boolean'
    WHEN 5 THEN 'variant'
    WHEN 6 THEN 'text'
END AS field_type
```

JOINS
-----

### Não utilize `USING` em joins

* Explicitar o `ON` em todos as junções torna o código mais consistente.

* Se condições extras precisarem serem adicionadas posteriormente, a utilização do `ON` facilita a modificação.

* `USING` pode produzir resultados inconsistentes em alguns bancos de dados.


### Explicite o tipo do `JOIN`

Sempre declare o tipo da junção, utilizando `INNER JOIN`, `LEFT JOIN`, etc., nunca somente `JOIN`.

```
/* Good */
SELECT *
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id

/* Bad */
SELECT *
FROM customers
JOIN orders ON customers.id = orders.customer_id
```

### Evite a utilização de `RIGHT JOINS`

A necessidade de usar `RIGHT JOINS` é um forte indício de que você deve inverter a tabela utilizada no `FROM` e a tabela da junção.

### Nas condições da junção, ordene as tabelas de acordo com sua aparição

Facilita a identificação de situações onde pode ocorrer um fan out do resultado.

```
/* Good */
SELECT *
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
/* primary key = foreign key --> one-to-many --> fan out */

/* Good */
SELECT *
FROM orders
LEFT JOIN customers ON orders.customer_id = customers.id
/* foreign key = primary key --> many-to-one --> no fan out */

/* Bad */
SELECT *
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
```

#### Na junção de mútiplas tabelas, prefixe as colunas com a tabela/alias

Dessa forma você consegue identificar rapidamente de onde determinada coluna está vindo.

```
/* Good */
SELECT
    customers.email,
    orders.invoice_number,
    orders.total_amount
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id

/* Bad */
SELECT
    email,
    invoice_number,
    total_amount
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
```

Quando não houver junção, omita o prefixo nas colunas.

```
/* Good */
SELECT
    email,
    name
FROM customers

/* Bad */
SELECT
    customers.email,
    customers.name
FROM customers
```

### Declare filtros no `WHERE` em vez de utilizar a cláusula do `JOIN`

Somente condições de junção devem ser colocadas na cláusula do `JOIN`. Todos os filtros de condição devem ser colocados na cláusula `WHERE`.

```
/* Good */
SELECT
    ...
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id
WHERE
    orders.total_amount >= 100 AND
    customers.email like '%@domain.com'

/* Bad */
SELECT
    ...
FROM orders
INNER JOIN customers ON
    orders.customer_id = customers.id AND
    customers.email LIKE '%@domain.com'
WHERE orders.total_amount >= 100
```

### Ordene os `JOINS` de forma semântica

Inicie com `INNER JOIN`s e então liste `LEFT JOIN`s. Não intercale `LEFT JOIN`s com `INNER JOIN`s a menos que necessário.

```
/* Good */

INNER JOIN backings ON ...
INNER JOIN users ON ...
INNER JOIN locations ON ...
LEFT JOIN backer_rewards ON ...
LEFT JOIN ...

/* Bad */
LEFT JOIN backer_rewards ON ...
INNER JOIN users ON ...
LEFT JOIN ...
INNER JOIN locations ON ...
```

Comentários
-----------

### Comentários devem ser colocados no topo da query

Os comentários devem ser colocados no início da query, num formato de documentação, evitando comentários inline.

```
/* Good */

/* Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Dolor sed viverra ipsum nunc aliquet bibendum enim. */

SELECT
    name,
    email,
    phone
FROM customers

/* Bad */

SELECT
    name,
    email,
    phone /* Lorem ipsum dolor sit amet, consectetur adipiscing elit. */
FROM customers
```

### Sempre utilize a sintaxe `/* */`

Isso permite que comentários de linha única naturalmente sejam expandidos para comentários de múltiplas linhas sem a necessidade de alteração da sintaxe.

Quando expandir um comentário para múltiplas linhas:

* Mantenha o `/*` de abertura na mesma linha do início do texto e o `*/` de fechamento na mesma linha do fim do texto.

* Indente as linhas seguintes com 4 espaços e adicione um espaço extra no início do texto da primeira linha de forma a alinhar com o restante das linhas.


```
/* Good */

-- Bad

/*  Good:  Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Dolor sed viverra ipsum nunc aliquet bibendum enim. */

/* Bad:  Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Dolor sed viverra ipsum nunc aliquet bibendum enim. */

-- Bad:  Lorem ipsum dolor sit amet, consectetur adipiscing elit,
-- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
-- Dolor sed viverra ipsum nunc aliquet bibendum enim.
```

### Respeite o limite de caracteres das linhas

Mova para uma nova linha, ou para a documentação, se um comentário for muito extenso.

### Cálculos devem ser brevemento descritos

Para cálculos realizados no SQL, deve haver uma descrição breve explicando a lógica e um link para o detalhamento da métrica no handbook.

### Não deixe comentários `TODO`

Em vez de deixar comentários, crie uma nova tarefa para melhoria.

CTEs
----

### Use CTEs, não subqueries

CTEs tornam o código mais legível e performático, principalmente nos Data Warehouses modernos, como o Redshift. Além disso, podem ser referenciados múltiplas vezes, e são fáceis de adaptar e refatorar posteriormente. Ler [CTEs versus Subqueries](https://www.alisa-in.tech/post/2019-10-02-ctes/) e [Why the Fishtown SQL style guide uses so many CTEs](https://discourse.getdbt.com/t/why-the-fishtown-sql-style-guide-uses-so-many-ctes/1091).

```
/* Good */
WITH paying_customers AS (

    SELECT *
    FROM customers
    WHERE plan_name != 'free'

)

SELECT ...
FROM paying_customers

/* Bad */
SELECT ...
FROM (
    SELECT *
    FROM customers
    WHERE plan_name != 'free'
) AS paying_customers
```

### CTEs complexos devem ser comentados

Comente brevemente a lógica sobre o CTE e documente de forma detalhada no handbook. O comentário deve ser colocado dentro dos parênteses do CTE no mesmo nível de indentação do `SELECT`.

```
/* Good */
WITH customers AS (

    /* CTE comments... */
    SELECT ...
    FROM customers

)

SELECT ...
FROM customers

/* Bad */

/* CTE comments... */
WITH customers AS (

    SELECT ...
    FROM customers

)

SELECT ...
FROM customers
```

### CTE duplicado entre modelos deve ser extraído no seu próprio modelo

Seguindo o **DRY concept,** se um CTE estiver duplicado em vários modelos o mesmo deve ser extraído num modelo próprio e referenciado nos demais.

### CTEs devem realizar uma única unidade lógica de trabalho, quando possível

Se a performance permitir, CTE deve realizar uma única operação lógica, como uma agregação, junção, etc., de forma a simplificar a leitura e compreensão.

Por exemplo, considere o SQL abaixo onde, no CTE `joined` está sendo feita a agregação dos campos da `payments` além da junção com `orders`, o que torna o código complexo de ser compreendido, além da necessidade de agrupar por múltiplos campos.

```
WITH orders AS (

    SELECT * FROM staging.orders

),

payments AS (

    SELECT * FROM staging.payments

),

joined AS (

    SELECT
        orders.order_id,
        orders.customer_id,
        orders.order_date,
        orders.status,

        COUNT(payments.payment_id) AS n_payments,
        SUM(CASE WHEN payments.payment_method = 'credit_card' THEN payments.amount ELSE 0 END) AS credit_card_amount,
        SUM(payments.amount) AS total_amount

    FROM orders
    LEFT JOIN payments ON (orders.order_id = payments.order_id)
    GROUP BY 1, 2, 3, 4

)

SELECT * FROM joined
```

De forma a simplificar, o SQL anterior pode ser reescrito da seguinte maneira:

```
WITH orders AS (

    SELECT * FROM staging.orders

),

payments AS (

    SELECT * FROM staging.payments

),

order_payments AS (

    SELECT
        order_id,

        count(payment_id) AS n_payments,
        SUM(CASE WHEN payment_method = 'credit_card' THEN amount ELSE 0 end) AS credit_card_amount
        SUM(amount) AS total_amount

    FROM payments
    GROUP BY 1
),

joined AS (

  SELECT
      orders.order_id,
      orders.customer_id,
      orders.order_date,
      orders.status,

      order_payments.n_payments,
      order_payments.credit_card_amount,
      order_payments.total_amount

    FROM orders
    LEFT JOIN order_payments ON (orders.order_id = payments.order_id)

)

SELECT * FROM joined
```

### Utilize CTEs como declarações de imports

Dentro de um modelo, inclua todas as tabelas referenciadas em CTEs no início do arquivo, como se fossem imports.

```
WITH customers AS (

    SELECT * FROM customers

),

orders AS (

    SELECT * FROM orders

),

final AS (

    SELECT
      ...
    FROM customers
    LEFT JOIN orders ON (cutomers.customer_id = orders.customer_id)

)

SELECT * FROM final
```

### Nome do CTE deve ser conciso o possível mas mantendo a clareza

* Evite nomes longos como `replace_sfdc_account_id_with_master_record_id` e prefira um nome menor com um comentário no CTE. Isso ajudará a evitar a necessidade de alias em junções.

* Evite prefixos e sufixos, como `cte`.

### Crie um CTE `final`, ou similar

Utilizar um CTE `final` facilita o debug do código dentro do modelo.

```
WITH events AS (

    ...

),

final AS (

    ...

)

SELECT * FROM final
```

### Mantenha a formatação adequada

* A declaração do primeiro CTE deve estar na mesma linha do `WITH`.

* O `(` de abertura deve estar na mesma linha da declaração do nome.

* Deve haver uma linha em branco entre a declaração do CTE e qualquer statement interno

* Deve haver uma linha em branco entre o final do `SELECT` e o `)` de fechamento do CTE.

* A `,` entre cada CTE deve estar na mesma linha do `)` de fechamento.

* Cada novo CTE deve ser declarado numa nova linha no mesmo nível de indentação do `WITH`.

* Deve haver uma linha em branco entre o último CTE e o `SELECT` final.

* Comentários devem seguir o padrão definido anteriormente.

```
    WITH events AS (

        ...

    ),

    filtered_events AS (

        /* CTE comments... */
        ...

    )

    SELECT * FROM filtered_events
```

Aliases
-------

### Evite alias de tabela desnecessários, especialmente abreviaturas

Convenções sugeridas:

* Se o nome da tabela consistir de 3 letras ou menos, não utilize alias.

* Utilize um subconjunto das palavras como alias se fizer sentido (ex. se `partner_shipments_order_line_items` é a única tabela de itens sendo referenciada, faz sentido utilizar `line_items` como alias).


```
/* Good */
SELECT
    customers.email,
    orders.invoice_number
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id

/* Bad */
SELECT
    c.email,
    o.invoice_number
FROM customers AS c
INNER JOIN orders AS o on c.id = o.customer_id
```

### Sempre utilize a keyword `AS` para alias de colunas, expressões e tabelas

```
/* Good */
SELECT COUNT(*) AS customers_count
FROM customers

/* Bad */
SELECT COUNT(*) customers_count
FROM customers
```

### Sempre renomeie agregações e outras expressões de coluna

```
/* Good */
SELECT MAX(id) AS max_customer_id
FROM customers

/* Bad */
SELECT MAX(id)
FROM customers

/* Good */
SELECT DATE_TRUNC('month', created_at) AS created_at_month
FROM companies

/* Bad */
SELECT DATE_TRUNC('month', created_at)
FROM companies
```

### Tire vantagem de alias lateral quando agrupar colunas por nome

```
/* Good */
SELECT
    DATE_TRUNC('month', created_at) AS created_at_month,
    COUNT(*) as total_companies
FROM companies
GROUP BY created_at_month

/* Bad */
SELECT
  DATE_TRUNC('month', created_at) AS created_at_month,
  COUNT(*) AS total_companies
FROM companies
GROUP BY DATE_TRUNC('month', created_at)
```

Convenções de nomenclatura
--------------------------

Todos os identificadores (bancos, tabelas, colunas, views, CTEs e functions/procedures) devem estar em minúsculo e seguir o padrão `snake_case`, uma vez que torna o código mais simples de ser compreendido.

Além disso, palavras reservadas não devem ser utilizadas de modo a evitar a necessidade de utilização de aspas/crases para referência.

### Tabelas

Nomes de tabelas devem ser substativos no plural.

```
/* Good */
SELECT * FROM users
SELECT * FROM visit_logs

/* Bad */
SELECT * FROM user
SELECT * FROM visitLog
```

### Colunas

Evite nomes genéricos e ambíguos como `id`, `name`, `type`, `month`, `date`, etc. Prefixe com o que o campo está identificando.

```
/* Good */
SELECT
    id AS account_id,
    name AS account_name,
    type AS account_type,
    ...

/* Bad */
SELECT
    id,
    name,
    type,
    ...
```

De modo a evitar ambiguidade, quando realizar a junção de diferentes sources o campo deve ser prefixado com o nome do data source, e.g. `sfdc_account_id`.

```
/* Good */
SELECT
    sfdc_account.account_id AS sfdc_account_id,
    zuora_account.account_id AS zuora_account_id
FROM sfdc_account
LEFT JOIN zuora_account ON ...

/* Bad */
SELECT
    sfdc_account.account_id,
    zuora_account.account_id AS zuora_id
FROM sfdc_account
LEFT JOIN zuora_account ON ...
```

#### Colunas boolean

Devem ser prefixadas com o presente ou passado do verbo na terceira pessoa do singular, como:

* `is_` ou `was_`. e.g. `is_customer`

* `has_` ou `had_`. e.g. `has_unsubscribed`

* `does_` ou `did_`. e.g. `did_pay`

#### Colunas date

* Para colunas de data utilizar o sufixo `_date`, e.g. `report_date`.

* Colunas que representem mês devem terminar em `_month`, e.g. `deal_closed_month`.

#### Colunas timestamp

* Colunas timestamp no fuso BRT devem utilizar o sufixo `_at`, e.g. `created_at`.

* Para colunas baseadas em outros fusos, como UTC, utilizar o padrão `<event>_at_<timezone indicator>` (e.g `created_at_utc`).

### Funções/procedures

Nomes de funções/procedures devem ser claros o suficiente para que não seja necessário consultar uma documentação, e/ou visualizar o código fonte, para compreender a operação que a mesma se propõe a executar.

Considerando que a função/procedure executará uma ação, o nome da mesma deve ter verbos que explicitem a ação realizada.

```
/* Good */
SELECT EXTRACT_DAY_FROM_DATE('2021-09-10');

/* Bad */
SELECT DAY_FROM_DATE('2021-09-10');
```

A tabela abaixo apresenta alguns casos com padronização já definida, de acordo com o objetivo da função.

|**Objetivo**|**Padrão**|**Exemplo**|
| ---------- | -------- | --------- |
|Conversão de um dado para outro equivalente porém de tipo diferente | `parse_X_to_Y` | `parse_cpf_cnpj_to_person_type` |
|Extrair uma informação presente no dado|`extract_X_from_Y`|`extract_domain_from_url`|


Tipos de Dados
--------------

Use os tipos de dados padrão, e não aliases. Verifique a [relação de tipos de dados do Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) para mais detalhes.

* `SMALLINT` em vez de `INT2`

* `INTEGER` em vez de `INT`, `INT4`

* `BIGINT` em vez de `INT8`

* `VARCHAR` em vez de `CHAR`, `CHARACTER VARYING`, `TEXT`

* `DATE`

* `TIMESTAMP`

* `TIMESTAMPTZ`

* `TIME`

* `TIMETZ`

Referências
-----------

Esse style guide foi parcialmente inspirado por:

* [https://about.gitlab.com/handbook/business-technology/data-team/platform/sql-style-guide/](https://about.gitlab.com/handbook/business-technology/data-team/platform/sql-style-guide/)

* [https://github.com/brooklyn-data/co/blob/master/sql_style_guide.md](https://github.com/brooklyn-data/co/blob/master/sql_style_guide.md)

* [https://github.com/fishtown-analytics/corp/blob/master/dbt_coding_conventions.md#sql-style-guide](https://github.com/fishtown-analytics/corp/blob/master/dbt_coding_conventions.md#sql-style-guide)

* [https://github.com/mattm/sql-style-guide](https://github.com/mattm/sql-style-guide)

* [https://gist.github.com/fredbenenson/7bb92718e19138c20591](https://gist.github.com/fredbenenson/7bb92718e19138c20591)
