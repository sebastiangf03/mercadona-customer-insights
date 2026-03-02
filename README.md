
#  Mercadona Insights: Análisis Estadístico de Consumo y Customer Intelligence

Este proyecto, denominado **ProyectoTD2024**, fue desarrollado por el **Grupo M** de la **Universitat de València**. Consiste en un pipeline completo de tratamiento de datos, desde la extracción de información no estructurada en tickets físicos hasta la generación de inteligencia de negocio.

## 📊 Resumen Estratégico
El objetivo principal fue procesar y analizar una muestra de tickets de compra de Mercadona para identificar patrones de comportamiento del consumidor y la influencia de factores externos en el volumen de ventas.

### Preguntas de Negocio Atacadas:
* **Efecto del Estacionamiento:** ¿Cómo influye el uso del parking en el importe total de la compra?
* **Impacto de la Competencia:** ¿Afecta la proximidad de otros supermercados al gasto por ticket?
* **Patrones Horarios:** ¿Existen horas pico donde el gasto promedio es mayor?
* **Dinámica Temporal:** ¿Cómo varían las ventas entre los distintos días de la semana?

## Pipeline Tecnológico
Para este análisis implementamos un flujo de trabajo híbrido que combina lo mejor de **Python** y **R**:

1. **Extracción (Python):** Transformación de tickets en formato PDF a TXT mediante scripts de parsing y expresiones regulares (Regex).
2. **Limpieza (Python):** Automatización del renombrado y depuración de archivos.
3. **Análisis Estadístico (R):** Uso de `tidyverse` para la gestión de datos y análisis exploratorio profundo.
4. **Geolocalización:** Integración de datos de **OpenStreetMap** para calcular distancias a competidores mediante distancias euclidianas.

## 💡 Hallazgos Clave
* **Sinergia Parking-Gasto:** Se observó una tendencia positiva inicial entre el tiempo de estancia en el parking y el importe de la compra.
* **Estabilidad frente a Competencia:** Los análisis de correlación de Pearson sugieren que la competencia cercana no tiene un impacto negativo significativo en el importe total de las compras en las ubicaciones analizadas.
* **Segmentación Geográfica:** Las compras de mayor valor y volumen se concentran en núcleos urbanos principales como Valencia y Denia.
* **Eficiencia Horaria:** Se detectó una tendencia a realizar compras de mayor volumen durante las horas de la mañana.

## 📂 Estructura del Proyecto
* `src/`: Scripts de Python para extracción y limpieza.
* `analysis/`: Código fuente en RMarkdown y archivos de estilo (.css, .tex).
* `docs/`: Informe final detallado y presentación del proyecto.
* `pictures/`: Soporte visual y evidencias del procesamiento de datos.

---
### 🤝 Agradecimientos
Agradecemos al profesor de la asignatura por su dedicación y a todas las personas que facilitaron los tickets para este estudio.

**Integrantes del Grupo :** David Ricci, Hugo Frasquet, Juan Gómez, Mateo Méndez, Pablo Quesada y Sebastian David Gutierrez Ferreira.
