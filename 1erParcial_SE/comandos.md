# 📝 Guía Rápida de Comandos: Pytest y Git

## 🧪 1. Comandos de Pytest

Estos comandos te ayudarán a ejecutar tus pruebas en diferentes niveles de detalle. Asegúrate de estar en el directorio raíz de tu proyecto (donde está tu entorno virtual o tus archivos).

*   **Ejecutar todas las pruebas:** Busca automáticamente todos los archivos que empiecen con `test_` o terminen en `_test.py`.
    ```bash
    pytest
    ```

*   **Ejecutar pruebas con más detalle (Verbose):** Muestra el nombre de cada prueba y su resultado (PASSED/FAILED) paso a paso, similar a lo que tienes en tu terminal.
    ```bash
    pytest -v
    ```

*   **Ejecutar un archivo de pruebas específico:** Útil cuando solo quieres probar los casos de un módulo, por ejemplo el que tienes abierto.
    ```bash
    pytest tests/test_nuevos_casos.py
    ```

*   **Ejecutar una función de prueba específica:** Si solo quieres correr un test puntual dentro de un archivo.
    ```bash
    pytest tests/test_nuevos_casos.py::test_rotate_left_maneja_pasos_negativos_y_lista_vacia
    ```

*   **Mostrar los `print()` durante las pruebas:** Por defecto, pytest oculta las salidas por consola si la prueba pasa. Con `-s` fuerzas a que se muestren.
    ```bash
    pytest -s
    ```

---

## 🌿 2. Flujo de Trabajo Básico en Git y GitHub

Aquí tienes el orden lógico de comandos para crear una rama, hacer cambios y subirlos a tu repositorio remoto en GitHub.

### A. Ver el estado actual
Antes de hacer nada, siempre es bueno saber en qué rama estás y qué archivos han sido modificados.
```bash
git status
```

### B. Manejo de Ramas (Branches)
*   **Crear una rama nueva y moverte a ella:** (Recomendado para nuevas características o arreglos).
    ```bash
    git checkout -b nombre-de-tu-rama
    # O la versión más moderna:
    git switch -c nombre-de-tu-rama
    ```
*   **Cambiar a una rama existente:** (Por ejemplo, para volver a `main` o `master`).
    ```bash
    git checkout main
    # O la versión más moderna:
    git switch main
    ```

### C. Guardar cambios (Add y Commit)
*   **Añadir archivos al "Área de preparación" (Staging):**
    ```bash
    # Para añadir TODOS los archivos modificados o nuevos:
    git add .
    
    # Para añadir un archivo específico:
    git add nombre_del_archivo.py
    ```
*   **Crear un Commit (Guardar el estado):** Escribe un mensaje claro sobre lo que hiciste.
    ```bash
    git commit -m "Agrega pruebas para rotate_left y round_score en test_nuevos_casos.py"
    ```

### D. Subir cambios a GitHub (Push)
*   **Subir una rama nueva por primera vez:** Como la rama solo existe en tu computadora, debes decirle a GitHub que la cree allá también.
    ```bash
    git push -u origin nombre-de-tu-rama
    ```
*   **Subir cambios posteriores en la misma rama:** Una vez que ya hiciste el comando anterior, los siguientes pushes son más cortos.
    ```bash
    git push
    ```

### 💡 Extra: Actualizar tu rama local
Si alguien más hizo cambios en GitHub y quieres traerlos a tu computadora:
```bash
git pull origin nombre-de-tu-rama
```

# 📝 Guía Rápida de Comandos: Pytest y Git

## ⚙️ 0. Configuración Inicial de Git

Antes de empezar a trabajar, es fundamental configurar tu identidad para que tus commits aparezcan con tu nombre y correo correctos.

* **Configurar tu nombre de usuario globalmente:**
  ```bash
  git config --global user.name "Hugo Rafael Zúñiga Daza"
  ```

* **Configurar tu correo electrónico globalmente:**
  ```bash
  git config --global user.email "hugodaza1@upb.edu"
  ```

* **Verificar tu configuración actual:**
  ```bash
  git config --list
  ```
```