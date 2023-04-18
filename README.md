<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenidos a mi primer proyecto individual de la etapa de labs! En esta ocasión, resolveré una serie de funciones en el rol de un ***MLOps Engineer***.  

<hr>  

## **Introducción**

En esta ocasión me encuentro realizando un proyecto para la etapa de Labs para la carrera Data Scientis en la plataforma Henry.

Como parte fundamental de nuestro entrenamiento, voy a realizar una API que me permita realizar consultas y la misma se alojará en Render


## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Tienes tu modelo de recomendación entrenado dando unas buenas métricas :smirk:, y ahora, cómo lo llevas al mundo real? :eyes:

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.


## Rol a desarrollar

Empezaste a trabajar como **`Data Scientist`** en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha! 

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula :sob:): Datos sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas….  haciendo tu trabajo imposible :weary:. 

Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para la próxima semana! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir :exclamation:. Así que te espantas los miedos y te pones manos a la obra :muscle:

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>

<sub> Nota que aqui se reflejan procesos no herramientas tecnologicas. Has el ejercicio de entender cual herramienta del stack corresponde a cual parte del proceso<sub/>

## **Tratamiento de datos**

**`Transformaciones`**:  Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, ***y solo estas***, transformaciones a los datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

[ETL_Completo.ipynb](https://github.com/Vansik4/MLOpsReviews_PI/blob/main/ETL_Completo.ipynb)

<br/>

**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***, generando diferentes endpoints que se consumiran en la API.

Creas 6 funciones (recuerda que deben tener un decorador por cada una (@app.get(‘/’)):

+ Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración. La función debe llamarse get_max_duration(year, platform, duration_type) y debe devolver sólo el string del nombre de la película.
+ Cantidad de películas (sólo películas, no series, etc) según plataforma, con un puntaje mayor a XX en determinado año. La función debe llamarse get_score_count(platform, scored, year) y debe devolver un int, con el total de películas que cumplen lo solicitado.

+ Cantidad de películas (sólo películas, no series, etc) según plataforma. La función debe llamarse get_count_platform(platform) y debe devolver un int, con el número total de películas de esa plataforma. Las plataformas deben llamarse amazon, netflix, hulu, disney.

+ Actor que más se repite según plataforma y año. La función debe llamarse get_actor(platform, year) y debe devolver sólo el string con el nombre del actor que más se repite según la plataforma y el año dado.

+ La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año. La función debe llamarse prod_per_county(tipo,pais,anio) deberia devolver la cantidada de contenidos/productos segun el tipo de contenido (pelicula,serie) por pais y año en un diccionario con las variables llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (cantidad de contenidos/productos).

+ La cantidad total de contenidos/productos (todo lo disponible en streaming, series, peliculas etc) según el rating de audiencia dado (para que publico fue clasificada la pelicula). La función debe llamarse get_contents(rating) y debe devolver el numero total de contenido con ese rating de audiencias.

[main.py](https://github.com/Vansik4/MLOpsReviews_PI/blob/main/main.py) 

<br/>


**`Deployment`**: 
Para el despliegue de nuestra API, utilizamos Render, una plataforma en la nube que nos permitió implementar y escalar rápidamente nuestra aplicación. Render garantiza una alta disponibilidad y rendimiento de la API, y nos proporciona herramientas para monitorear y depurar en tiempo real. Además, ofrece integraciones con servicios externos para construir aplicaciones complejas y escalables. En definitiva, Render nos permitió crear una API confiable y escalable, sin preocuparnos por la infraestructura subyacente

[MLOpsReviews_PI](https://mlopsreviews-pi.onrender.com/docs).

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Una vez que he transformado y limpiado mis datos, mi siguiente paso es buscar patrones y anomalías en ellos para obtener información valiosa y sacar conclusiones. Para ello, utilizaré técnicas de análisis exploratorio de datos (EDA) como visualización y estadística descriptiva. Con EDA, podré detectar relaciones entre variables, identificar valores atípicos y evaluar la distribución de los datos.

Después de realizar el análisis exploratorio, podré hacer inferencias y sacar conclusiones sobre lo que mis datos están diciendo. Por ejemplo, podré descubrir relaciones causales entre variables, patrones estacionales o tendencias a largo plazo que podrían ser útiles para predecir futuros comportamientos o tomar decisiones estratégicas.

En resumen, el análisis exploratorio de datos es una parte esencial de mi proceso de análisis de datos y me permitirá tomar decisiones informadas basadas en los resultados de mis datos.

[EDA_Completo.ipynb](https://github.com/Vansik4/MLOpsReviews_PI/blob/main/EDA_Completo.ipynb)

**`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score y devolverá una lista de Python con 5 valores.

[desarrollo_system.ipynb](https://github.com/Vansik4/MLOpsReviews_PI/blob/main/desarrollo_system.ipynb)

<br/>




