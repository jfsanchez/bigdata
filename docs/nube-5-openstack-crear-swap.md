# 🐢 SWAP en GNU/Linux

A SWAP é a memoria virtual en GNU/Linux. Cando se acaba a memoria física, baixanse algunhas páxinas de memoria ao almacenamento secundario adicado especialmente a isto.

Algunhas veces pode que non chegue esta memoria virtual (ou que non fose configurada). Esto podémolo ver co comando:

``` bash
free -m
```

Se non vemos swap ou creemos que é insuficiente, podemos engadir un arquivo para reservar parte do noso disco a esta memoria secundaria.

## Pasos para engadir un arquivo SWAP

1. Creamos un arquivo para swap e o formateamos:

``` bash
dd if=/dev/zero of=/arquivoswap bs=1024K count=4096
mkswap /arquivoswap
```

2. Editamos como root o ´/etc/fstab´. Este ficheiro de configuración indícanos que sistemas de arquivos se usan e se montan no sistema, tanto para o arranque, como para dar permisos de montaxe a usuarios.

``` bash
sudo nano /etc/fstab
```

3. Nese arquivo metemos que o arquivo de swap se monte ao arranque:

```
/arquivoswap none swap sw 0 0
```

Curiosidade: Podes saber cando espacio ocupa un arquivo ou directorio co comando: `du -hs /directorio/`

4. Pon de máscara de permisos 0600 ao arquivo /arquivoswap. Emprega o comando chmod. Estes permisos son bastante restrictivos, non queremos que calquer usuario poida acceder a este arquivo:

``` bash
chmod 0600 /ficherito
```

5. Gardamos o arquivo e logo montamos tódolos arquivos de swap (para non ter que reiniciar a máquina):

``` bash
swapon -a
```

6. Podemos ver que este espacio de swap foi engadido empregando de novo:

``` bash
free -m
```
