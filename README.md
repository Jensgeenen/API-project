# To-Do API

Dit project is een eenvoudig te beheren To-Do API waarmee gebruikers taken kunnen aanmaken, bijwerken, verwijderen en opvragen. De API beheert drie entiteiten: `User`, `Project`, en `Task`.

### Entiteiten:
- **User**: Beheert gebruikersinformatie.
- **Project**: Verzamelt taken in een project.
- **Task**: Een specifieke taak die binnen een project valt.

### API Endpoints

- **GET /tasks**: Haal alle taken op.
- **GET /tasks/:id**: Haal een specifieke taak op basis van ID.
- **POST /tasks**: Maak een nieuwe taak aan.
- **PUT /tasks/:id**: Werk een specifieke taak bij.
- **DELETE /tasks/:id**: Verwijder een specifieke taak.
- **GET /projects**: Haal alle projecten op.
- **POST /projects**: Maak een nieuw project aan.
- **GET /users**: Haal alle gebruikers op.
- **POST /users**: Maak een nieuwe gebruiker aan.

### Aantoonbare werking

Hieronder zijn de screenshots toegevoegd van de Postman requests:

- **GET /projects**: 
  ![Get Projects](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20224036.png)

- **GET /projects/1**: 
  ![Get Project 1](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20224100.png)

- **POST /tasks**: 
  ![Post Task](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20224139.png)

- **GET /tasks/1**: 
  ![Get Task 1](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20224243.png)

- **PUT /tasks/1**: 
  ![Put Task](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20224314.png)

- **GET /tasks**: 
  ![Get Tasks](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20224413.png)

- **POST /users**: 
  ![Post User](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20223310.png)

- **POST /projects**: 
  ![Post Project](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20223358.png)

### OpenAPI Documentatie

Zie hieronder de screenshot van de OpenAPI (Swagger) documentatie:

![Swagger Screenshot](https://github.com/Jensgeenen/API-project/raw/main/project%20api/Schermafbeelding%202024-08-15%20223909.png)

### Docker Container

De API is verpakt in een Docker container die automatisch wordt opgebouwd via GitHub Actions. Zie het bestand `Dockerfile` en `docker-compose.yml` voor details.

### Deployment via Docker Compose

Het project kan lokaal worden gestart door de volgende commando's uit te voeren:

```bash
docker-compose up --build
