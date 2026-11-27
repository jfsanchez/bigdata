# -*- coding: utf-8 -*-
"""Funcións comúns dos notebooks do exercicio (BD|CESGA).

Uso nun notebook:
    from utils_hive import *
"""
import getpass
import os
import subprocess
import tempfile

os.environ["HADOOP_CONF_DIR"] = "/etc/hadoop/conf"   # configuración do clúster para hdfs, beeline e spark
USUARIO = getpass.getuser()                                   # Usuario
BASE = os.path.dirname(os.path.abspath(__file__))             # este cartafol no HOME (NFS)
CSV = os.path.join(BASE, "datos", "netflix_titles.csv")
HDFS_HOME = "/user/" + USUARIO
HDFS_NETFLIX = HDFS_HOME + "/netflix"
HIVE_URL = ("jdbc:hive2://c14-19.bd.cluster.cesga.es:10000/default;ssl=true;"
            "sslTrustStore=/opt/cesga/cdh61/hiveserver2.jks;trustStorePassword=notsecret")

_contrasinal = None

def sh(orde):
    """Executa unha orde de shell e mostra a saída."""
    r = subprocess.run(orde, shell=True, stdin=subprocess.DEVNULL,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       universal_newlines=True)
    print(r.stdout)
    if r.returncode != 0:
        print("[erro] código de saída", r.returncode)
    return r.returncode


def hdfs(argumentos):
    """Atallo para 'hdfs dfs <argumentos>'."""
    return sh("hdfs dfs " + argumentos)


def hive(sql):
    """Executa SQL en Hive con beeline.

    ${USUARIO} substitúese polo teu usuario. A primeira vez pide o contrasinal
    do CESGA; se o servidor non o pide, preme Enter.
    """
    global _contrasinal
    if _contrasinal is None:
        _contrasinal = getpass.getpass("Contrasinal do CESGA (se a pos mal ou non a pos, algúns comandos fallarán!): ")
    sql = sql.replace("${USUARIO}", USUARIO)

    ficheiros = []
    try:
        fsql = tempfile.NamedTemporaryFile("w", suffix=".sql", dir=BASE, delete=False)
        fsql.write(sql)
        fsql.close()
        ficheiros.append(fsql.name)

        orde = 'beeline --silent=true --outputformat=table -u "{}"'.format(HIVE_URL)
        if _contrasinal:
            fpw = tempfile.NamedTemporaryFile("w", dir=BASE, delete=False)
            os.chmod(fpw.name, 0o600)
            fpw.write(_contrasinal)
            fpw.close()
            ficheiros.append(fpw.name)
            orde += ' -n {} -w "{}"'.format(USUARIO, fpw.name)
        orde += ' -f "{}"'.format(fsql.name)
        return sh(orde)
    finally:
        for f in ficheiros:
            os.remove(f)
