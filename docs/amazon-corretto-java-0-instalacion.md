# Java / Amazon Corretto / OpenJDK

![Logo OpenJDK](images/openjdk/OpenJDK_logo.svg#derecha "Logo OpenJDK")

## Orixe

A primeira versión de Java (Oak) foi desenvolvida por Sun Microsystems, empresa comprada por Oracle en 2009/2010. Trala compra, houbo [denuncias a grandes empresas que empregaban a API de Java como Google no seu Android](https://es.wikipedia.org/wiki/Caso_Oracle_contra_Google). Tamén houbo cambios no sistema de licenciamento. En 2017 houbo cambios importantes no modelo de actualizacións e outros problemas.

Entre tanto, no 2007 creárase unha máquina virtual de Java libre chamada [OpenJDK](https://openjdk.org/), o seu uso aumentou nos últimos anos. Fai uns anos, Amazon creou unha distribución gratuita baseada en OpenJDK optimizada para nube e con soporte a longo prazo tanto en melloras de rendemento como corrección de erros de seguridade. A historia é moito máis complexa e pode lerse na [páxina da Wikipedia adicada ao OpenJDK](https://es.wikipedia.org/wiki/OpenJDK).


## Instalación de Amazon Corretto

=== "Debian"

     ``` bash
     sudo apt update
     sudo apt -y dist-upgrade
     sudo apt install java-common
     wget https://corretto.aws/downloads/latest/amazon-corretto-21-x64-linux-jdk.deb
     sudo dpkg -i amazon-corretto-21-x64-linux-jdk.deb
     rm amazon-corretto-21-x64-linux-jdk.deb
     ```

=== "Rocky/Fedora"

     ``` bash
     sudo dnf update -y
     sudo curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo
     sudo dnf install -y java-21-amazon-corretto-devel
     ```

=== "GNU/Linux xenérico"

     ``` bash
     mkdir -p $HOME/bin
     cd
     wget https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.tar.gz
     tar -xzf amazon-corretto-11-x64-linux-jdk.tar.gz
     mv amazon-corretto-11*-linux-x64/ bin/amazon-corretto-latest
     rm amazon-corretto-11-x64-linux-jdk.tar.gz
     # Configuro o PATH
     echo "export PATH=$HOME/bin:$HOME/bin/amazon-corretto-latest/bin:$PATH" >> $HOME/.profile
     . ~/.profile
     ```


O paquete mete o binario dentro dun directorio que xa está no PATH e a instalación xenérica configura o PATH a man, polo que poderemos executar:

  ``` bash
  java --version
  ```

## Configuración do JAVA_HOME

Atopar o `JAVA_HOME` é tarefa sinxela. Se executamos o comando `type java` para saber onde reside o binario de java e imos averiguando a onde está apuntado o enlace simbólico con `ls -l RUTA`, sacaremos esta conclusión:

`/usr/bin/java` &rarr; `/etc/alternatives/java` &rarr; `/usr/lib/jvm/java-21-amazon-corretto/bin/java`.

Engadimos o **JAVA_HOME**. É moi conveniente para que os programas atopen o contorno de OpenJDK.

=== "Debian/Rocky/Fedora"

     ``` bash
     echo "export JAVA_HOME='/usr/lib/jvm/java-21-amazon-corretto/'" >> $HOME/.profile
     source ~/.profile
     ```

=== "GNU/Linux xenérico"

     ``` bash
     echo "export JAVA_HOME=$HOME/bin/amazon-corretto-latest" >> $HOME/.profile
     . ~/.profile
     ```

## Comandos útiles

- `jps`: [Ver os procesos en Java](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jps.html).
- `keytool`: [Administrar os certificados empregados por Java nun almacén](https://docs.oracle.com/en/java/javase/21/docs/specs/man/keytool.html).


## Máis información

- Implementación libre de Java: <https://openjdk.org/>
- Amazon Corretto (baseada no OpenJDK): <https://aws.amazon.com/es/corretto/>
- Java de Oracle: <https://www.oracle.com/java/technologies/downloads/>