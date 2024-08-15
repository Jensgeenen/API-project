# API Project

Dit project is een eenvoudige API voor het beheren van gebruikers, projecten en taken, gebouwd met Flask en SQLite.

## Thema en Uitbreidingen

Deze API is ontworpen voor het beheren van taken en projecten. Het biedt eindpunten voor het aanmaken, bijwerken, ophalen en verwijderen van gebruikers, projecten en taken. Deze API kan worden uitgebreid met authenticatie, autorisatie en geavanceerde querymogelijkheden.

## API Endpoints

### Gebruikers Endpoints
- **POST /users**: Maak een nieuwe gebruiker aan.
- **GET /users/{id}**: Haal een specifieke gebruiker op door ID.

### Projecten Endpoints
- **POST /projects**: Maak een nieuw project aan.
- **GET /projects**: Haal alle projecten op.
- **GET /projects/{id}**: Haal een specifiek project op door ID.

### Taken Endpoints
- **POST /tasks**: Maak een nieuwe taak aan.
- **GET /tasks**: Haal alle taken op.
- **GET /tasks/{id}**: Haal een specifieke taak op door ID.
- **PUT /tasks/{id}**: Werk een bestaande taak bij.
- **DELETE /tasks/{id}**: Verwijder een taak.
- **GET /projects/{id}/tasks**: Haal alle taken op die horen bij een specifiek project.

## API Testen met Postman

### GET /projects
![Get Projects](https://github.com/Jensgeenen/API-project/raw/main/project%20api/get_projects.png)

### GET /projects/{id}
![Get Project By ID](https://github.com/Jensgeenen/API-project/raw/main/project%20api/get_project_by_id.png)

### POST /projects
![Post Projects](https://github.com/Jensgeenen/API-project/raw/main/project%20api/post_projects.png)

### POST /tasks
![Post Tasks](https://github.com/Jensgeenen/API-project/raw/main/project%20api/post_tasks.png)

### GET /tasks/{id}
![Get Task By ID](https://github.com/Jensgeenen/API-project/raw/main/project%20api/get_task_by_id.png)

### PUT /tasks/{id}
![Put Task By ID](https://github.com/Jensgeenen/API-project/raw/main/project%20api/put_task_by_id.png)

### GET /projects/{id}/tasks
![Get Tasks By Project ID](https://github.com/Jensgeenen/API-project/raw/main/project%20api/get_tasks_by_project_id.png)

### POST /users
![Post Users](https://github.com/Jensgeenen/API-project/raw/main/project%20api/post_users.png)

## OpenAPI Documentatie

(Schermopname van de OpenAPI-documentatie toevoegen)

## Docker

Dit project kan worden uitgevoerd in een Docker-container. Gebruik de volgende instructies om de container te bouwen en uit te voeren:

```bash
docker build -t api-project .
docker run -p 5000:5000 api-project
