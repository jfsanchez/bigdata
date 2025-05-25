# ☁️ OpenStack &mdash; ⚙️ Crear instancias automáticamente

Esta receita está creada para o contorno do CESGA, sen embargo, pode adaptarse de xeito sinxelo a calquer outro contorno con OpenStack.

1. Conectar á VPN.

2. Conectar por SSH.

    ``` bash
    ssh USUARIO@hadoop.cesga.es
    ```

3. Imos a: <https://cloud.srv.cesga.es> &rarr; Acceso a API &rarr; Descargar fichero RC de OpenStack &rarr; Fichero Openstack RC.

    ``` bash
    nano openstack.sh
    ```

4. Pegamos o contenido de OpenStack que temos baixado e gardamos (Ctrl+o, Enter) e saímos (Ctrl+x).


5. Cargar o contorno de openstack, PATH e autocompletado, así como as variables de contorno.

    ``` bash
    module load openstack
    source /opt/cesga/openstack/osc.bash_completion
    source ./openstack.sh
    ```

6. Pediranos o contrasinal do noso usuario, introducímolo. Tamén aproveitamos para configurar un par de variables de contorno.

    ``` bash
    USUARIO=${OS_USERNAME}
    CENTRO='aqui-o-teu-centro'
    ```

7. Probamos se todo funciona.

    ``` bash
    openstack server list
    ```

8. Crear un par de claves no servidor e subir a chave pública ao OpenStack.

    ``` bash
    ssh-keygen
    openstack keypair create --public-key ~/.ssh/id_rsa.pub key-${USUARIO}-${CENTRO}-srvhadoop
    ```

9. Creamos o noso grupo de seguridade chamado segrup-USUARIO e que permita acceder a todo o mundo por SSH (normalmente abriríamolo só ao noso enderezo IP).

    ``` bash
    openstack security group create sg-centro-${USUARIO}
    openstack security group rule list sg-centro-${USUARIO}
    openstack security group rule create --proto tcp --dst-port 22 --ingress --remote-ip 0.0.0.0/0 sg-centro-${USUARIO}
    ```

10. Creamos **catro** instancias.

    ``` bash
    for numero in {1..4..1}; do \
      openstack server create --boot-from-volume 80 --image baseos-Rocky-8.7-v4 --flavor a1.4c8m --key-name key-${USUARIO}-${CENTRO}-srvhadoop --network provnet-formacion-vlan-133 --security-group segrup-${USUARIO} ${USUARIO}-${CENTRO}-srv${numero}; done
    ```

11. Se quixéramos **borrar** as instancias

    ``` bash
    for numero in {1..4..1}; do \
       openstack server delete ${USUARIO}-${CENTRO}-srv${numero}; done
    ```

Se queremos executar comandos en varias instancias á vez debemos empregar clustershell (clush) qu está instalado no servidor FT3.

Para evitar que nos pregunte se confiamos na clave dunha instancia a primeira vez que conecte, podemos empregar:

``` bash
ssh-keyscan -H IP_OU_DNS_DO_SERVIDOR >> $HOME/.ssh/known_hosts
```
