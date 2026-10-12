# Operaciones con git en databricks

### Clonar un repo

* Desde el workspace de Databricks -> Create -> Git Floder
* Rellenamos con los datos de nuestro repo como en la imagen siguiente: 

![Clonado de repo](./imagenes-databricks/git-databricks-1.png)

* Click en "Create Git Folder"

### Pull al repo remoto

* Una vez clonado el repo, si le damos a los tres puntos de la carpeta -> Git, se nos abre el diálogo para realizar operaciones Git:

![Operaciones git](./imagenes-databricks/git-databricks-2.png)

* Desde este diálogo podremos hacer pull de los cambios del repo remoto, hacer un Commit & Push al repo remoto e incluso crear una nueva rama dentro del repo.
* Para realizar operaciones sobre un repo, tenemos que tener configurado una credencial, desde los Settings de Databricks -> Linked Accounts -> Add Git Credential y seleccionamos Personal Access Token y en Token tenemos que pegar el token creado desde GitHub.
* Si no tenemos creado el Token en GitHub, desde GitHub vamos a los Settings de la cuenta -> Developper Settings -> Personal Access Tokens -> Fine-grained tokens -> Generate new token
