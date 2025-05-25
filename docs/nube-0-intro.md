# ☁️ Computación na nube

## Que é a computación na nube

Se executas os teus servizos, programas, máquinas virtuais ou contedores en servidores de outros entón "estás nas nubes". Este uso de servidores remotos en distintas redes que poden estar localizadas en centros de datos en varios países é o que coñecemos por "computación na nube".

### Vantaxes

- **Mellor conectividade**: Velocidade, latencia, etc.
- **Redundancia e tolerancia a fallos**: Moitos fallos de hardware mesmo son imperceptibles.
- **Escalabilidade e flexibilidade**: Inversión **inicial** case cero.
- **Centros de datos ben adaptados**: Electricidade, seguridade física, lóxica, etc.
- **Distintas ubicacións xeográficas**: Podemos acceder nos proveedores grandes a distintos centros de datos ubicados en tódolos continentes para garantir unha boa conectividade.

### Desvantaxes

- **Custos**: Manter un gran número de recursos a medio/longo prazo é moito máis caro, incluso contando os custos de persoal. Este punto é controvertido, posto que soe dicirse o contrario. Hai que analizar a situación en cada caso particular e non basearse só nunha opinión dun comercial.
- **Protección de datos**: Normalmente os acordos para a protección de datos, que permiten mover os datos a datacenters de fóra de Europa, adoitan ser **efémeros e esotéricos**. Exemplos desto son: Safe Harbour e Privacy Seal, que demostran unha vez máis a grande diferencia de concepto de protección de datos e o distinto tratamento entre Europa e EEUU.
- **Dependencia dun terceiro**: Cambios de condicións unilaterais, fallos, prohibición de uso dos seus servizos (sic), bloqueos...


## Principais proveedores de Cloud Computing / Computación na nube

- Amazon AWS: <https://aws.amazon.com/>
- Microsoft Azure: <https://azure.microsoft.com/>
- Google Cloud: <https://cloud.google.com/>

Segundo varios informes de operadoras, as grandes tecnolóxicas xeran entre o **55% e o 80%** do tráfico das redes mundiais. Estes informes adoitan a forma de notas de prensa e poden ofrecer resultados interesados, máis probablemente se supere o 50% do tráfico mundial total dado o tamaño destas megacorporacións.

Habitualmente escóitase falar do termo **GAFAM** polos nomes das principais empresas tecnolóxicas: Google, Apple, Facebook, Amazon e Microsoft para referirse ao tráfico e conexións que proveñen delas.


## Platform as a Service (PaaS)

### Pago por uso e usos idóneos

O prezo da nube pode chegar a ser moi variable e está íntimamente ligado ao uso de recursos. Se ben é unha das grandes vantaxes porque non require unha inversión inicial en hardware, redes, acondicionamento, instalación e persoal, esta vantaxe vaise diluindo co tempo.

O uso máis adecuado da nube é para aquelas operacións nas que é impredecible o uso de recursos e son momentos puntuais. Tamén para incrementar puntualmente os recursos ou para garantir un SLA superior ao que obteríamos con servidores in-house.

Sen embargo, cando unha empresa coñece ben os seus recursos computacionais e ten persoal adicado é indiscutible que a nube resulta máis cara en prácticamente a totalidade dos escenarios, incluíndo os custes de persoal. Non todos os escenarios requiren as mesmas consideracións e o prezo non é sempre o elemento determinante á hora de escoller entre unha ou outra opción.

Outro uso moi adecuado sería o de gardar unha copia de seguridade dos datos (cifrada) noutra localización. O ideal, se a túa empresa é grande é gardar os datos en distintos continentes para garantir o acceso en todo momento.

Ante unha catástrofe (como a ocorrida nas Torres Xemelgas no 2001) non dependeremos que os nosos [datos e servidores estean nunha das Torres e o backup na outra](https://www.wired.com/2001/09/attack-cant-erase-stored-data/). Tamén deberíamos ter en conta maremotos, terremotos e outras catástrofes naturais así como guerras e a situación xeopolítica de onde gardamos os datos.

Se temos ademáis unha copia dos datos na nube, outra vantaxe é poder levantar as máquinas necesarias en pouco tempo (se temos implementado e practicado un plan de continxencias) para continuar cos servizos. Evidentemente falamos de empresas grandes e que normalmente actúan en varios países.

Normalmente os servizos de virtualización na nube cobran polo uso de recursos: Procesador, memoria RAM, tráfico de rede entrante e saínte, GPU, almacenamento de datos, operacións de lectura/escritura sobre eles...

Non sempre precisamos todos os servizos activos, polo que se queremos aforrar custos, debemos reducir recursos. Unha boa idea se non precisamos as máquinas é destruilas e gardar os volumes de almacenamento ou os datos, tendo en conta o tempo que leva levantar unha máquina cos servizos activos de novo.

### Nomes dos servizos máis habituais

As correspondencias cos nomes poden non ser exactas xa que as veces o concepto cambia un pouco (sobre todo cos nomes xenéricos por nomearse varias alternativas).

- Computación (CPU+RAM):
    - Amazon Web Services (AWS):
        - **Amazon EC2**: Amazon Elastic Compute Cloud.
        - Lightsail: Tipo VPS (Virtual Private Server). Facturación simplificada, elección limitada.
    - Google Cloud Platform (GCP):
        - **GCE**: Google Compute Engine.
    - Microsoft Azure:
        - Azure **Virtual Machine** / Máquina Virtual.
    - OpenStack / Nome xenérico:
        - **Instancia** / Máquina Virtual.
        - Contedor.

- Almacenamento:
    - Amazon Web Services (AWS):
        - **EBS** en instancias.
        - **S3** Obxectos de almacenamento.
        - **Glacier** Obxectos de almacenamento con menor redundancia e de acceso lento.
    - Google Cloud Platform (GCP):
        - **Persistent Disk** / Durable Block Storage
        - **Cloud Storage**.
    - Microsoft Azure:
        - **Azure Blob Storage**.
    - OpenStack / Nome xenérico:
        - **Object** Storage (tamén pode configurarse algo similar a un "Cold Storage").
        - **Block/Volume** Storage (snapshots...).


Hai un montón de servizos máis con nomes comerciais baseados en solucións de software coñecidas. Trátase de vender unha solución con procesamento para case cada nicho de mercado: IA, colas, DNS, Bases de Datos, etc. Cada proveedor tenta poñerlle os seus propios nomes.

## Alternativas

- As solucións *in-house* (servidores físicos na oficina ou en centro propio).
- Montar a túa propia nube:
    - [Openstack](https://www.openstack.org/)
    - [Citrix CloudPlatform](https://citrixready.citrix.com/accelerite/cloudplatform.html)
    - [Eucalyptus](https://www.eucalyptus.cloud/)
    - [Microsoft Azure Stack](https://azure.microsoft.com/es-es/products/azure-stack/)
    - [Red Hat OpenShift](https://www.redhat.com/es/technologies/cloud-computing/openshift)
    - [VMware vSphere](https://www.vmware.com/products/vsphere.html)


### A nube en Europa / Cloud en Europa

Europa trata de reducir a dependencia das grandes tecnolóxicas estadounidenses.

- [ComputerHoy: O poder das grandes tecnolóxicas](https://computerhoy.com/noticias/industria/poder-grandes-tecnologicas-preocupa-union-europea-estados-unidos-colaboraran-limitarlo-937079)
- [El País: A UE blindándose contra as tecnolóxicas](https://elpais.com/tecnologia/2022-05-08/la-excepcion-europea-por-que-la-ue-se-esta-blindando-contra-las-tecnologicas.html)
-  [Informe de Oliver Wyman: EUROPEAN DIGITAL SOVEREIGNTY](https://www.oliverwyman.com/content/dam/oliver-wyman/v2/publications/2020/october/European%20Digital%20Sovereignty.pdf)
- [EU. Cloud Strategy](https://commission.europa.eu/publications/european-commission-cloud-strategy_en)
- [Dataset da penetración da nube nos distintos países da UE](https://ec.europa.eu/eurostat/web/products-datasets/-/isoc_cicce_use)
- [EU. Futures of big tech in Europe. Scenarios and policy implications: Foresight](https://op.europa.eu/en/publication-detail/-/publication/db955dcf-af69-11ee-b164-01aa75ed71a1/language-en)


En China terás oído falar seguramente das prohibicións en internet ás que se enfrentan os seus cidadáns e do "Gran Firewall Chinés". Este movemento dalles tamén unha certa vantaxe competitiva e permítelles desenvolver os seus propios servizos e redes sociais: QQ, Tiktok, etc.

Estamos nunha economía global, os prezos da nube dependen da enerxía, comunicacións, redes, custos de persoal e políticas de cada país. Na ecuación tamén entran os datos.

Un dos activos máis importantes das empresas son os datos. En Europa e EEUU xogamos en diferentes ligas. Cando os datos son en teoría dos cidadáns (Europa) e non das empresas (EEUU) as empresas en Europa teñen un menor valor, posto que os datos non son un activo propiedade destas e deben ser máis garantistas co seu uso.

### Proveedores de Cloud

#### Proveedores de Cloud Computing en Europa

| Empresa | País de orixe | Ano de comezo |
| --- | --- | --- |
| [Contabo](https://contabo.com/) | Alemaña | 2003 | 
| [Fuga Cloud](https://fuga.cloud/) | Holanda | 2006 |
| [Hetzner](https://www.hetzner.com/cloud/) | Alemaña | 1997 |
| [OVH](https://www.ovhcloud.com/es-es/) | Francia | 1999 | 
| [Scaleway](https://www.scaleway.com/) | Francia | 1999 | 
| [Server Space](https://serverspace.io/) | Países Baixos | 2008 | 
| [Upcloud](https://upcloud.com/) | Finlandia | 2012 | 


#### Outros proveedores de Cloud Computing

| Empresa | País de orixe | Ano de comezo |
| --- | --- | --- |
| [Cloud Sigma](https://www.cloudsigma.com/) | Suíza | 2009 |
| [Digital Ocean](http://www.digitalocean.com/) | EEUU | 2012 |
| [Ionos](https://www.ionos.com/) | EEUU | 1988 (1&1) |
| [Linode](https://www.linode.com/) | EEUU | 2003 |
| [Rack Space](https://www.rackspace.com/) | EEUU | 1998 |
| [Vultr](https://www.vultr.com/) | EEUU | 2014 |
| [V2 Cloud](https://v2cloud.com/) | Canadá | 2012 |


⚠️ O ano de comezo pode ser noutras actividades, as empresas máis antigas non se adicaron sempre ao cloud e mesmo as modernas tentan sempre pasar por máis antigas con trucos cosméticos para que se vexa que levan tempo no sector.

**Fonte**: Elaboración propia a partir dos datos presentes nas webs das empresas, pode haber erros.

Tamén hai un listaxe de proveedores de nube públicas empregando tecnoloxía OpenStack: <https://www.openstack.org/marketplace/public-clouds/>

### Elixindo unha compañía de cloud computing

Elixir unha compañía (ou varias) non é tarefa sinxela. Seguramente terás oído comentarios de todo tipo. Por exemplo:

No caso de OVH ten tido problemas no pasado: incendios e incidentes en materia de datos persoais, ademáis non ten moi boa publicidade nas comunidades en internet por algúns erros e formas.

Hetzner tamén ten tido algún problema, parece que moito máis limitado coa súa KonsoleH nalgúns servidores fóra de Europa.

1&1, agora Ionos tamén ten tido mala publicidade por algunhas das súas políticas cos contratos.

En xeral **non hai empresas exentas de problemas**. Se é unha empresa grande e aguanta no tempo, vai ter sempre algún problema. É importante valorar estes incidentes e a súa resposta á hora de elexir un servizo. É conveniente mirar foros especializados en estas empresas de servizos, noticias e experiencias.


