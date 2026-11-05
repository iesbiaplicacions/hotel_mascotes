# 🐾 Hotel Mascotes API

Una API backend dissenyada per a la gestió integral d'un hotel o residència de mascotes. Aquesta aplicació permet administrar registres d'animals, reserves d'estades, clients (propietaris) i serveis addicionals.

## 🚀 Característiques

- **Gestió de Mascotes:** Registre detallat d'animals, races, edats i necessitats especials.
- **Control de Reserves:** Validació de dates, disponibilitat d'habitacions o gàbies i estats de les estades.
- **Administració de Clients:** Dades de contacte dels propietaris i historial de mascotes associades.
- **Arquitectura Neta:** Organització del codi seguint el patró MVC/Clean Architecture amb rutes, models de base de dades i esquemes de validació.

## 📁 Estructura del Projecte

El repositori està organitzat de la següent manera:

* **`app/`**: Nucli de l'aplicació backend.
* **`models/`**: Definicions de les taules i entitats de la base de dades (ex. SQLAlchemy).
* **`routes/`**: Controladors i punts d'accés (endpoints) de l'API distribuïts per mòduls.
* **`schemas/`**: Mòduls de validació i serialització de dades d'entrada/sortida (ex. Pydantic).
* **`.env`**: Fitxer de configuració per a variables d'entorn (claus privades, connexió a BD).
* **`requirements.txt`**: Llista de dependències i llibreries del projecte.

## 🛠️ Requisits previs

Abans de començar, assegura't de tenir instal·lat:
- Python 3.9 o superior
- Pip (gestor de paquets de Python)
- Un entorn virtual (opcional però recomanat)

## 💻 Instal·lació i Configuració

Segueix aquests passos per a aixecar el projecte en entorn local:

1. **Clona el repositori:**
   ```bash
   git clone https://github.com
   cd hotel_mascotes
   ```

2. **Crea i activa un entorn virtual:**
   ```bash
   # A Linux/macOS
   python3 -m venv venv
   source venv/bin/activate

   # A Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instal·la les dependències:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Córrer un contenidor de MongoDB:**

   ```bash
   docker run -d \
     --name mongodb_hotel_mascotes \
     -p 27017:27017 \
     -e MONGO_INITDB_ROOT_USERNAME=admin \
     -e MONGO_INITDB_ROOT_PASSWORD=la_teva_clau_secreta_aqui \
     -v mongo_data_mascotes:/data/db \
     mongo:latest
   ```

## 🏃 Execució de l'Aplicació

Per iniciar el servidor de desenvolupament, executa la comanda principal de la teva solució (per exemple, amb Uvicorn si utilitzes FastAPI):

```bash
uvicorn app.main:app --reload
```
*Nota: Ajusta la comanda anterior si el teu fitxer d'entrada principal té un altre nom (ex. `python run.py` o `flask run`).*

Un cop en marxa, podràs accedir a la documentació interactiva de l'API (Swagger UI) a: `http://127.0.0`.

## 🛠️ Tecnologies Utilitzades

- **Llenguatge:** Python
- **Framework Principal:** FastAPI / Flask
- **ORM / Base de dades:** SQLAlchemy
- **Validació de dades:** Pydantic

