# NanoFast Results Compiler

🌐 Leer en: [English](README.md) | [Português (Brasil)](README.pt-br.md) | [Português (Portugal)](README.pt-pt.md) | [Español](README.es.md) | [Français](README.fr.md)

## Para qué sirve el Script
El Compilador de Resultados NanoFast es una herramienta de automatización en Python diseñada para agilizar el procesamiento y la presentación de los resultados de las pruebas Nanofast. Compila automáticamente los resultados individuales desde un lector o guardados localmente en una plantilla maestra de Excel estructurada y de fácil lectura para su análisis posterior.

## Cómo funciona
1. **Extracción de Datos:** El script escanea los datos dentro del directorio `Raw Data` o desde el dispositivo lector en busca de carpetas de resultados. Para cada carpeta, abre el archivo CSV de destino y su archivo `result.json` complementario.
2. **Extracción de Metadatos:** Extrae metadatos específicos del JSON (incluyendo el ID de la Muestra, el Identificador del Casete, el Código de Lote, los detalles del Protocolo, la Fecha/Hora y el Resultado Final) y los superpone sobre los datos sin procesar del CSV.
3. **Inyección en la Plantilla:** El script crea una hoja de cálculo de Excel y pega los datos compilados en la hoja `Raw Data`, asignando una columna por cada resultado de prueba.
4. **Agrupación y Nomenclatura:** Para evitar desbordamientos en la plantilla, el script procesa los resultados en lotes de 40. Genera dinámicamente archivos de salida nombrados con la fecha actual, la hora y el número de lote (por ejemplo, `Compiled NanoFast Results - 07 Jul 26 - 15.43 - Part 1.xlsx`).
5. **Limpieza:** Tras completarse con éxito, si el script se ejecuta localmente, purga automáticamente la carpeta `Raw Data` con los datos copiados para asegurar que quede vacía y lista para la siguiente ejecución.

## Cómo Instalar
### Requisitos previos
* Instale Python *directamente desde la Microsoft Store*. El script ha sido probado con `Python 3.13`.
* Descargue la última versión del repositorio en GitHub, utilizando la sección de lanzamientos (releases) en la barra lateral.
* En la sección de recursos (assets) de la página de lanzamientos, descargue el archivo .zip.
### Instalación
* Extraiga el archivo .zip directamente en su disco C:. No se recomiendan instalaciones en otros lugares, ya que pueden provocar errores en la ruta de los archivos.

### Primera ejecución
* En el primer uso, el script descarga automáticamente las dependencias necesarias. Por favor, permita que este proceso finalice.
* Después de la instalación de los paquetes, se le pedirá que seleccione su idioma preferido.
* Las ejecuciones posteriores omitirán esta fase de configuración y procederán directamente al compilador.

## Cómo Usar
### Pasos de Ejecución
1. Si procesa datos desde un dispositivo, conecte el lector Nanofast al PC mediante un cable USB-C, encienda el lector y ponga el dispositivo en 'Modo de Almacenamiento Masivo' (Mass Storage Mode) usando el Menú del lector. Si utiliza datos locales, copie todas las carpetas de resultados de pruebas individuales (cada una con un CSV y un `result.json`) en la carpeta `Raw Data`.
2. Ejecute el archivo `Solus NanoFast Compliler.bat` haciendo doble clic.
3. Seleccione la ubicación adecuada para el procesamiento de datos.
    * Presione 1 para Automático. Esto obtiene los resultados automáticamente desde el dispositivo.
    * Presione 2 para Manual. Para esta opción, copie manualmente los resultados en la carpeta llamada `Raw Data`.  
4. Seleccione el rango de fechas para el procesamiento de datos utilizando las flechas hacia arriba y hacia abajo y seleccionando con Enter.
5. El script mostrará una advertencia en la terminal indicando que la carpeta `Raw Data` será eliminada después del procesamiento. Escriba `Y` y/o presione **Enter** para continuar. Los datos almacenados en un Lector no se pueden eliminar; esto solo importa si ha transferido archivos manualmente.
6. La terminal mostrará el progreso a medida que agrupa y exporta los datos.
7. Una vez completado, recupere sus archivos `Compiled NanoFast Results` recién generados desde el directorio principal. La carpeta `Raw Data` ahora estará vacía.

## Problemas Conocidos
1. Durante la primera ejecución, el script instala pandas con éxito, pero falla al inicializarse en la misma sesión. Como solución temporal, reiniciar el script resolverá el problema. Este es un problema conocido programado para ser resuelto en un próximo parche.

## Traducción
La traducción ha sido realizada por Google y no por un hablante nativo. Por favor, envíe sus comentarios sobre la traducción en GitHub. Pedimos disculpas por cualquier error.

---
Script creado por Steve Carter en 2026.