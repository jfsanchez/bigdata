# 🧾 Microsoft SQL Server

## Microsoft SQL Server en Ubuntu (con docker).

 - Baseado na imaxe oficial: <https://hub.docker.com/_/microsoft-mssql-server>

## Instalación con docker
``` bash
docker run \
 -e "ACCEPT_EULA=Y" \
 -e "MSSQL_SA_PASSWORD=Abc12300" \
 -e "MSSQL_PID=Evaluation" \
 -p 41433:1433  \
 --name sqlpreview \
 --hostname sqlpreview \
 -d mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
```

## Datos de conexión

- Usuario por defecto (admin): sa
- Contrasinal de exemplo: Abc12300. **Advertencia**: O contrasinal debe ter alomenos unha letra maiúscula, unha minúscula, un número e alomenos oito caracteres, do contrario o docker finalizará.
- Porto ao que conectarse de forma exterior: `41433`: Elíxese este porto posto que o habitual `1433` está bloqueado no contorno que empregamos por algúns filtros automáticos que non se pode abrir no grupo de seguridade.
- Existe o cliente: **mssql-cli** que se pode instalar con pip:

``` bash
pip install mssql-cli
pip install --upgrade cli_helpers
pip install --upgrade tabulate
export DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true
```

#### Cómo conectar dende Python

- <https://github.com/jfsanchez/SBD/blob/main/notebooks/bbdd/mssql-pyodbc.ipynb>
