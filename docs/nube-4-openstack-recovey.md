# ☁️ OpenStack &mdash; ⛈️ Recuperación

## Recuperando instancias do OpenStack a través dos volumes

Se te tes quedado fora dunha instancia, sempre podes borrala (sen borrar o volume de datos asociado) e meter ese volume noutra instancia (nova ou existente). Desde esa máquina a que tes acceso podes facer os cambios necesarios no volume, por exemplo copiar unha chave SSH ou poñerlle contrasinal ao usuario co que conectas (esto último é inseguro).

Un volume non debe estar asociado a outra instancia para poder asocialo (attach). Unha vez está libre, pódese asociar a unha instancia en execución.

``` bash
sudo su
lsblk # (1)!
mkdir /mnt/volume-a-recuperar
mount /dev/DISPOSITIVO /mnt/volume-a-recuperar
```

1.  Este comando serve para averiguar o nome e número do dispositivo (o último).

### Opción 1: Mudando o contrasinal de usuario

  ``` bash
  chroot /mnt/volume-a-recuperar /bin/bash
  passwd USUARIO # (1)!
  ```

1.  En usuario debes poñer o usuario que empregas para conectar (mudarás a clave del).

### Opción 2: Copiando a chave SSH ao authorized_keys

  ``` bash
  mkdir /mnt/volume-a-recuperar/home/USUARIO/.ssh/
  cp $HOME/.ssh/id_rsa.pub /mnt/volume-a-recuperar/home/USUARIO/.ssh/
  ```

Emprega os comandos con sentido. Debes adaptalos ao teu caso.

Esta técnica pódese empregar tamén nos servicios de computación na nube como: Amazon AWS, Google Cloud Services, Microsoft Azure e outros.