
# InvestAI Backend – Railway Ready

Este es el backend de InvestAI listo para desplegar en [https://railway.app](https://railway.app).

### 🚀 Cómo desplegar

1. Ve a [https://github.com](https://github.com) y crea un repositorio vacío llamado `investai-backend`.
2. Descomprime este ZIP y arrastra todo su contenido al repositorio en GitHub.
3. Entra a [https://railway.app](https://railway.app) y haz login.
4. Clic en **New Project → Deploy from GitHub Repo**
5. Selecciona el repositorio que creaste
6. Railway detectará FastAPI automáticamente y lo desplegará.

### 🧠 Requiere

- Python 3.9+
- Conexión a internet para acceder a datos de Yahoo Finance
- Puedes agregar variables de entorno opcionalmente

---

¡Listo! El backend estará disponible en una URL como:

```
https://investai-backend.up.railway.app
```

Prueba con:

```
GET /ai/recomendacion
```
