# 💧 Apache Nifi &mdash; 🐳 Instalación

![Logo Apache Nifi](images/nifi/Apache-nifi-logo.svg#derecha "Logo Apache Nifi")

## Instalación rápida de Apache Nifi empregando Docker
📝 Antes de seguir [asegúrate de ter instalado docker no equipo](docker-0-base-simple.md).

Baseado no repositorio do proxecto Apache coa imaxe "non" oficial de Apache Nifi: <https://hub.docker.com/r/apache/nifi/>.

Imos crear un contedor que terá acceso a un directorio compartido para meter os drivers JDBC e os datasets que precisemos.

``` bash
mkdir -p $HOME/nifi-compartido/{jdbc,datasets}

docker run --name nifi \
  -p 8443:8443 \
  -e NIFI_WEB_HTTPS_PORT=8443 \
  -e SINGLE_USER_CREDENTIALS_USERNAME=admin \
  -e SINGLE_USER_CREDENTIALS_PASSWORD=EsteEunContrasinalMoiLongo1234567890 \
  -v $HOME/nifi-compartido:/opt/nifi/compartido \
  --restart unless-stopped -d apache/nifi:latest
```

Se o queremos **expoñer á rede local**, debemos darlle un **nome** coa opción: `--hostname srvnifiniano` e que ese nome responda á IP do servidor.

⚠️ **Advertencia**: Para conectar emprega **localhost** como nome da máquina (fai un túnel SSH cando sexa preciso). Do contrario vaiche dar un erro de SNI incorrecto. Se quixeras conectar cun DNS personalizado (por exemplo: nifi.jfsanchez.es) terías que xerar un certificado SSL e mudar o arquivo de configuración de nifi.

**Datos de conexión**

- 👤 Usuario por defecto: **admin**
- 🔑 Contrasinal de exemplo: **EsteEunContrasinalMoiLongo1234567890**
- 📝 Emprega **https** para conectar. Exemplo: <https://localhost:8443>. Lembra facer o [tunel SSH](ssh-0-chaves-tuneles.md).


## Descargando e configurando o driver JDBC para MySQL

 1. Imos a <https://www.mysql.com/products/connector/> e seleccionamos **JDBC for MySQL (connector J)** &rarr; Download.
 2. Select Operating system &rarr; **Platform independent**.
 3. Platform Independent (Architecture Independent) &rarr; **Compressed TAR Archive** &rarr; Click dereito no botón Download e copiar a URL da ligazón.

Se quixésemos unha versión antiga (por exemplo a: 8.4.0), teríamos que ir a: <https://downloads.mysql.com/archives/c-j/>

Podes empregar o seguinte script que baixa as versión anteriormente citadas, descomprímeas e garda o .jar no directorio `$HOME/nifi-compartido/jdbc/`.

⚠️ Se deixa de funcionar podes corrixilo buscando a nova URL do driver.

~~~~bash
wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-j-9.2.0.tar.gz
wget https://downloads.mysql.com/archives/get/p/3/file/mysql-connector-j-8.4.0.tar.gz
tar -xzf mysql-connector-j-9.2.0.tar.gz -C $HOME/nifi-compartido/jdbc
tar -xzf mysql-connector-j-8.4.0.tar.gz -C $HOME/nifi-compartido/jdbc
mv $HOME/nifi-compartido/jdbc/mysql-connector-j-9.2.0/mysql-connector-j-9.2.0.jar $HOME/nifi-compartido/jdbc/
mv $HOME/nifi-compartido/jdbc/mysql-connector-j-8.4.0/mysql-connector-j-8.4.0.jar $HOME/nifi-compartido/jdbc/
rm -rf $HOME/nifi-compartido/jdbc/mysql-connector-j-9.2.0 $HOME/nifi-compartido/jdbc/mysql-connector-j-8.4.0
rm mysql-connector-j-8.4.0.tar.gz mysql-connector-j-9.2.0.tar.gz
~~~~

Podes empregar un parámetro dentro dun contexto coa **ruta completa ao JDBC** para engadila rápidamente cando fose preciso. Mira a [páxina de parámetros](apache-nifi-2-parametros.md) para atopar como configuralo deste xeito.

