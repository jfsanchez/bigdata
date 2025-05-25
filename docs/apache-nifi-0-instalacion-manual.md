# 💧 Apache Nifi &mdash; 🧾 Instalación manual

![Logo Apache Nifi](images/nifi/Apache-nifi-logo.svg#derecha "Logo Apache Nifi")

Esta instalación é xenérica para case calquera distribución de GNU/Linux. Recoméndase empregar o docker por ser máis cómodo e rápido.

## Descarga, verificación e outras operacións

⚠️ <u>**AVISO**</u>: Dependendo da versión de Apache Nifi precisaremos como **mínimo** unha determinada versión de Java (OpenJDK/Amazon Corretto):

- Versión **11** para Apache Nifi **v1.2.x**.
- Versión **23** para Apache Nifi **v2.4.x**.

A explicación é para instalar a versión de Apache Nifi 1.24.0, se queres baixar outra versión mira a páxina de descargas: <https://nifi.apache.org/download/>.

1. [Sigue as instruccións para instalar Amazon Corretto](amazon-corretto-java-0-instalacion.md).

2. Descargamos Apache Nifi 1.24.0 e o seu arquivo de firma (asc):

    ``` bash
    wget https://dlcdn.apache.org/nifi/1.24.0/nifi-1.24.0-bin.zip --no-check-certificate
    wget https://dlcdn.apache.org/nifi/1.24.0/nifi-1.24.0-bin.zip.asc --no-check-certificate
    ```

2. Comprobar a firma (e por tanto a integridade do arquivo e que non foi alterado) é unha boa práctica, así que primeiro baixamos a chave SSH coa que foi firmado o arquivo:

    ``` bash
    gpg --keyserver pgpkeys.mit.edu --recv-key 0C07C6D5
    ```

3. E verificamos que coincide:

    ``` bash
    gpg --verify nifi-1.24.0-bin.zip.asc nifi-1.24.0-bin.zip
    ```

    Se todo coincide dirá "Good signature from ...". En caso de non coincidir a sinatura, debemos comprobar de novo os arquivos, volvelos baixar, revisar o sitio oficial e buscar outra descarga, etc.

4. Descomprimimos Apache Nifi e movemos Apache Nifi dentro do directorio bin que temos creado:

    ``` bash
    unzip nifi-1.24.0-bin.zip
    mv nifi-1.24.0 bin/
    ```

5. Finalmente facemos un pouco de limpieza:

    ``` bash
    rm nifi-1.24.0-bin.zip nifi-1.24.0-bin.zip.asc
    ```

## Configuración

Debemos configurar Apache Nifi. Precisamos mudar dous arquivos:

- `bin/nifi-env.sh`
- `conf/nifi.properties`

Editamos primeiro `nifi-env.sh`:

``` bash
nano $HOME/bin/nifi-1.24.0/bin/nifi-env.sh
```

Teremos que indicarlle que máquina de Java coller (descomentamos se fai falta o JAVA_HOME e poñémolo como segue):

``` bash title="$HOME/bin/nifi-1.24.0/bin/nifi-env.sh"
export JAVA_HOME="$HOME/bin/amazon-corretto-latest/"
```

Agora debemos configurar no arquivo `nifi.properties` o porto https, a IP na que vai a escoitar e o interfaz por defecto. Por defecto Apache Nifi abre un porto de xestión aleatorio, máis non abre o porto para a interfaz web.

A instalación é dependente da IP do nodo de login, polo que debemos consultala. A que se pon aquí dase como exemplo e debes mirar a túa.

Miramos a ip co comando `ifconfig`, en concreto interésanos a IPv4 (tamén podemos ver as IP con `hostname -I`):

```
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9000
        inet 10.10.10.101  netmask 255.0.0.0  broadcast 0.0.0.0
        inet6 fe80::0001:0203:0405:0001  prefixlen 64  scopeid 0x20<link>
        ether 00:01:02:03:04:05  txqueuelen 1000  (Ethernet)
        RX packets 324227052  bytes 234877693356 (218.7 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 242422788  bytes 830555348369 (773.5 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Debemos escoller un porto non ocupado por ninguén. Recomendación: Colle un porto algo, por exemplo 648XX e substitúe XX polo teu número de usuario.

Anota nalgún sitio a IP do comando anterior o porto que acabas de escoller. Vou empregar de exemplo a IP: 10.10.10.101 e o porto 64801. Ollo! emprega os datos correctos ou non che funcionará.

Editamos o arquivo `nifi.properties`:

``` bash
nano $HOME/bin/nifi-1.24.0/conf/nifi.properties
```

E cubrimos cos datos anteriores as seguintes variables no arquivo:

``` title="$HOME/bin/nifi-1.24.0/conf/nifi.properties"
nifi.web.https.host=10.10.10.101
nifi.web.https.port=64801
```

### Inicio de Nifi

Dentro de nifi hai un directorio bin que contén os scripts de lanzamento. En concreto interésanos: `bin/nifi.sh`

Entramos dentro do directorio:

``` bash
cd $HOME/bin/nifi-1.24.0/bin
```

E executamos:

``` bash
./nifi.sh start
```

Agora debemos consultar o usuario e clave por defecto en: `logs/nifi-app.log`.

Buscaremos o texto "**Generated**":

``` bash
cat $HOME/bin/nifi-1.24.0/logs/nifi-app.log| grep Generated
```

Con eses datos xa podemos entrar nun navegador web na IP do nodo do paso anterior (no meu exemplo: https://10.10.10.101:64801). Por favor non esquezas o **https**.

Para parar Apache Nifi executaremos:

``` bash
./nifi.sh stop
```
