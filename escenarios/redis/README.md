# Redis-Server

Este escenario de vagrant permite montar rápidamente un servidor redis.

Redis é unha base de datos clave-valor, que almacena os datos en memoria (e tamén admite persistencia).

Principalmente ven sendo utilizado como almacenamento de caché, por exemplo para páxinas web.

Permite varios tipos de datos: <https://redis.io/docs/data-types/>

## Exemplos de uso

Configurar o contrasinal:\
    `config set requirepass 123quetal123`\
    `AUTH 123quetal123`

Comprobar o funcionamento:\
    `redis-cli PING`

Almacenar unha variable:\
    `redis-cli`\
    `set variable valor`\
    `get variable`

Redis soporta JSON: <https://redis.io/docs/stack/json/>

## Exemplo con Python

Este exemplo foi obtido da páxina de redis anteriormente citada.

Emprega a libraría: `redis-py` <https://github.com/redis/redis-py>:\

**Instalación da libraría:**

     conda install -c conda-forge redis-py

*Código*

    import redis
    
    data = {
        'dog': {
            'scientific-name' : 'Canis familiaris'
        }
    }

    r = redis.Redis()
    r.json().set('doc', '$', data)
    doc = r.json().get('doc', '$')
    dog = r.json().get('doc', '$.dog')
    scientific_name = r.json().get('doc', '$..scientific-name')

