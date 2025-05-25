# 💧 Apache Nifi &mdash; 🌐 Codificación de caracteres

![Logo Apache Nifi](images/nifi/Apache-nifi-logo.svg#derecha "Logo Apache Nifi")

Fallan acentos/tildes/eñes? Probablemente esteas a ler ou escribir nunha codificación de caracteres incorrecta.

Codificacións de caracteres máis habituais:

- UTF-8
- ISO-8859-1 / ISO-8859-15
- LATIN1
- ASCII
- UTF-16

Procesador **ConvertRecord**:

- Record Reader: **CSVReader**  &rarr; Propiedade **Character Set**.
- Record Writer: **CSVRecordSetWriter** &rarr; Propiedade **Character Set**.

📝 A máxima é: Le na codificación correcta, escribe na desexada.

## Mais información

Se desexas obter máis información acerca das diferentes codificacións de caracteres, podes consultar a páxina da Wikipedia:

- <https://es.wikipedia.org/wiki/Codificaci%C3%B3n_de_caracteres>