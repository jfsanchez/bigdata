# 🧾 SQLite

![Logo SQLite](images/sqlite/SQLite370.svg#derecha "Logo SQLite")

É unha base de datos relacional/libraría que pode cumprir coas caraterísticas ACID.

Como realmente é un executable de pequeno tamaño (cunha libraría escrita en C que pode empregarse dende outros programas) a conexión é directa. Para o almacenamento emprégase un arquivo local.

 - Baseado na imaxe que ten alpine: <https://hub.docker.com/r/alpine/sqlite>

Para empregar SQLite, podémolo baixar directamente. Nos empregaremos un docker mínimo cunha imaxe de alpine e o executable sqlite.

Vemos aquí un exemplo cun contedor non persistente (`--rm`).

1. Creamos un arquivo no directorio actual que se chame `dieta.db` cunha táboa `alimento_saudable`:

    ~~~ bash
    docker run -ti --rm -v $(pwd):/apps -w /apps alpine/sqlite dieta.db "CREATE TABLE alimento_saudable (id INTEGER PRIMARY KEY, nome TEXT);"
    ~~~

2. Insertamos datos:

    ~~~ bash
    docker run -ti --rm -v $(pwd):/apps -w /apps alpine/sqlite dieta.db "INSERT INTO alimento_saudable(id, nome) VALUES(1, 'Chourizo');"
    ~~~

3. Recuperamos datos:

    ~~~ bash
    docker run -ti --rm -v $(pwd):/apps -w /apps alpine/sqlite dieta.db "SELECT * FROM alimento_saudable;"
    ~~~

Realmente os ; finais non farían falta nunha chamada directa como esta.

SQLite ten conectores JDBC e pódese empregar en case calquer linguaxe, por exemplo está dispoñible para Java e Python.

Emprégase moito sobre todo en contornos móbiles.

## Máis información

- [Páxina oficial de SQLite](https://sqlite.org/)
- Exemplo de uso en Python: <https://github.com/jfsanchez/SBD/blob/main/notebooks/bbdd/sqlite3.ipynb>
