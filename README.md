# CC3S2-EF-Pipeline-Mocks-Stubs

Esta aplicacion python realiza un analisis de datos mediante la invocacion a un
binario externo(/usr/bin/external-analyzer) y tambien consulta una API REST de un tercero.

#### Ejecución con Docker

1. **Construir la imagen**

   ```bash
   docker build -t app-analyzer .
   ```

2. **Arrancar el contenedor**

   ```bash
   docker run -d \
     --name my-app-analyzer \
     -p 80:80 \
     app-analyzer
   ```
