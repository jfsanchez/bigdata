#!/bin/bash
# 2025 Jose Sanchez. Basado en: <https://readthedocs.vinczejanos.info/Blog/2021/10/01/How_to_use_MKdocs/>

PUERTO=8080
RUTA_DOCS=$(pwd)

echo 'Escribiendo Dockerfile...'
#Creación imagen docker (Dockerfile)
{
echo 'FROM python:3-alpine'
echo
echo 'ARG USER=1001'
echo
echo 'RUN adduser -h /usr/src/mkdocs -D -u $USER mkdocs && apk add bash && apk add git'
echo
echo 'ENV PATH="${PATH}:/usr/src/mkdocs/.local/bin"'
echo
echo 'RUN apk add weasyprint'
echo
echo 'RUN apk add py3-pip so:libgobject-2.0.so.0 so:libpango-1.0.so.0 so:libharfbuzz.so.0 so:libharfbuzz-subset.so.0 so:libfontconfig.so.1 so:libpangoft2-1.0.so.0'
echo
echo 'USER mkdocs'
echo 'RUN mkdir -p /usr/src/mkdocs/build'
echo 'WORKDIR /usr/src/mkdocs/build'
echo
echo 'RUN pip install --upgrade pip'
echo
echo 'RUN pip install pymdown-extensions && pip install mkdocs \ '
echo '&& pip install mkdocs-material && pip install mkdocs-rtd-dropdown \ '
echo '&& pip install mkdocs-git-revision-date-plugin \ '
echo '&& pip install mkdocs-git-revision-date-localized-plugin mkdocs-pdf-export-plugin'
echo
echo 'ENTRYPOINT ["/usr/src/mkdocs/.local/bin/mkdocs"]'
} > Dockerfile

echo 'Construyendo imagen Dockerfile jfmkdocs:v1...'
docker build -t jfmkdocs:v1 --build-arg=USER=$(id -u) .
echo 'Borrando Dockerfile...'
rm Dockerfile
echo 'Lanzando contenedor temporal Pulsa Ctrl+C para borrarlo...'
docker run -it --rm --name jfmkdoc -p ${PUERTO}:8080 -v ${RUTA_DOCS}:/build jfmkdocs:v1 serve --dev-addr 0.0.0.0:8080 --config-file /build/mkdocs.yml
