# 🗂️ Arquivos en Python

![Logo Python](images/python/python-logo-generic.svg#derecha "Logo Python")

## Rutas absolutas e relativas en Microsoft Windows e GNU/Linux

Así de xeito rápido poderíamos definir:

- **Ruta absoluta**: Ruta completa, todas as indicacións dende cero para chegar á ruta.
- **Ruta relativa**: Partindo do directorio actual, as indicacións para chegar á ruta.

## Son cuestións de formato (de texto)...

Hai diferentes maneiras de poñer unha ruta (absoluta ou relativa) e que a mesma sexa compatible con Microsoft Windows e GNU/Linux.

A máis simple é poñendo barras inclinadas / en lugar das invertidas \\

No caso de querer empregar barras invertidas, debemos empregar dobre barra invertida para escapar o carácter de escape por defecto, que é a mesma barra invertida.

 **Exemplo**: `'C:\\Users\\USUARIO\\Downloads\\datasets\\proba.csv'`

Ademáis debemos detectar o sistema se pretendemos que o noso programa funcione en ambos e pretendemos empregar rutas escritas "a man".

🗒️ **Nota**: En Microsoft Windows poderíamos omitir a letra da unidade nas rutas «absolutas» e collería por defecto a letra da unidade onde se está a executar o script.

⚠️ **AVISO**: Neste exemplo empregaremos rutas absolutas.


```python
import platform
sistema = platform.system()

if sistema.casefold() == 'Windows'.casefold():
    path_base='C:/Users/USUARIO/Downloads/datasets/'
else:
    path_base='/home/usuario/Downloads/datasets/'
```

## Comparación de cadeas de texto

💡 Curiosidade polo método **casefold()** empregado no código de enriba? É unha boa práctica para comparar **determinadas** cadeas de texto, podes mirar a documentación en: <https://docs.python.org/3/library/stdtypes.html#str.casefold>. Básicamente ignora as maiúsculas e minúsculas e ten en conta cousas como que a dobre ss no alemán pode equivaler á: ß. O algoritmo de casefold está descrito aquí: <https://www.unicode.org/versions/Unicode15.0.0/ch03.pdf>. Se simplemente queres ignorar maiúsculas, podes aplicar un **lower()** a ambas cadeas.

Para engadir subdirectorios á ruta, temos varias opcións:

### Suma de cadeas de texto


```python
with open(path_base+'a-coruna.csv') as ficheiro:
    print(ficheiro.readline().rstrip())
```

💡 Curiosidade do que fai o método **rstrip()**? Básicamente borra os caracteres da cola que lle indiquemos. Se non indicamos ningún, entón borrará os caracteres que sexan de tipo espacio en branco: **espacios** ' ', **tabuladores** '\t' e **novas liñas** '\n'. <https://www.w3schools.com/python/ref_string_rstrip.asp> e <https://docs.python.org/3/library/stdtypes.html>.

### Con os.path.join


```python
import os

with open(os.path.join(path_base, 'lugo.csv')) as ficheiro:
    print(ficheiro.readline().rstrip())
```

Tamén existe a libraría **pathlib**: <https://docs.python.org/3/library/pathlib.html>.

### Con f-string (format string)

Poñeremos unha f antes das comillas e logo as variables entre chaves {}:


```python
with open(f'{path_base}pontevedra.csv') as ficheiro:
    print(ficheiro.readline().rstrip())
```

### Con r-string (raw string)

E se nos poñemos burros, con r-string tamén podemos empregas as barras invertidas sen necesidade de escapalas. O texto non se interpreta, é tal cual.


```python
with open(r'C:\Users\USUARIO\Downloads\datasets\ourense.csv') as ficheiro:
    print(ficheiro.readline().rstrip())
```

### Con fr-string (format e raw)

Tamén podemos mezclar ambas combinacións para obter o mellor de ambos mundos.



```python
arquivo='ourense.csv'
with open(fr'C:\Users\USUARIO\Downloads\datasets\{arquivo}') as ficheiro:
    print(ficheiro.readline().rstrip())
```


## Cómo crear un arquivo temporal


```python
import os
import tempfile

arquivo_temporal = os.path.join(tempfile.mktemp())
print(arquivo_temporal)
```

Esto daranos unha ruta a un novo arquivo que non existe cun nome que empezará por `tmp` e logo terá varios caracteres aleatorios. **Exemplos**: `tmp3yas5ei1`, `tmpvtwvejgk`.

Dependendo do sistema, creará o arquivo en distintas ubicacións:

- En **Microsoft Windows** no cartafol: `C:\Users\USUARIO\AppData\Local\Temp\`
- En **GNU/Linux** no directorio temporal: `/tmp/`

## Ler arquivos (modo simple)


```python
f = open("tmp.txt", "r")
print(f.read())
```

## Ler arquivos por liñas


```python
ficheiro = open('/tmp/tmp.tmp', 'r')

while liña := ficheiro.readline():
    print(liña.rstrip())
```

## Escribir (e sobreescribir) nun arquivo


```python
ficheiro = open("tmp.txt", "w")
ficheiro.write("Hola mundo!")
ficheiro.close()
```

## Cómo engadir contido ao final dun arquivo


```python
## Ler arquivos (modo simple)
ficheiro = open("tmp.txt", "a")
ficheiro.write("Outra liña!")
ficheiro.close()
```

## ❗ Manexo de erros


```python
import sys

ruta_arquivo="/tmp/tmp.tmp"

try:
  ficheiro = open(ruta_arquivo) #Se engado: 'rb' podo abrir o arquivo en binario
except FileNotFoundError:
    print(f"Non se pode atopar o arquivo: {ruta_arquivo}.")
    sys.exit(1)
except OSError:
    print(f"Erro de sistema abrindo o arquivo: {ruta_arquivo}")
    sys.exit(1)
except Exception as err:
    print(f"Ocorreu un erro descoñecido abrindo o arquivo: {ruta_arquivo} Erro: ",repr(err))
    sys.exit(1)
else:
  while liña := ficheiro.readline():
    print(liña.rstrip())
```

## Manexo de erros con with


```python
ruta_arquivo="/tmp/tmp.tmp"

with open(ruta_arquivo) as ficheiro:
    while liña := ficheiro.readline():
        print(liña.rstrip())

```

### Tipos de apertura

No **open()** podemos especificar principalmente: **r** (lectura, por defecto), **w** (escritura), **a** (append ou engadir ao final) entre outras.

Tamén podemos abrir o arquivo no modo por defecto que é modo texto (**t**) ou en binario (**b**)


**Máis información**:

- <https://www.w3schools.com/python/python_file_write.asp>
