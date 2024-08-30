
# Post-Comments Service

## Overview

This project implements a simple Post-Comments Service, allowing users to create text-based posts and enable other users to comment on these posts. The service is designed with RESTful APIs to handle post and comment creation, retrieval, updates, and deletion.

## Features

- **Post Creation**: Users can create text-based posts.
- **Commenting System**: Users can comment on posts. Each post can have multiple comments, and a comment can have child comments.

## Tech Stack

- **Backend Framework**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM for data persistence
- **API Documentation**: OpenAPI with FastAPI's automatic interactive docs

## Architecture

The service is structured into several core components:

- **API Layer**: Handles incoming HTTP requests and routes them to the appropriate service layer.
- **Service Layer**: Contains business logic for creating, updating, and retrieving posts and comments.
- **Data Layer**: Manages database operations using SQLAlchemy ORM.

## Project Structure

```
├── api
│   ├── docs                 # Documentation files
│   ├── routers              # API route handlers
│   ├── schemas              # Request and response schemas
├── core
│   ├── comments             # Comment-related logic
│   ├── database             # Database connection and CRUD operations
│   ├── posts                # Post-related logic
│   ├── users                # User-related logic
│   ├── utils                # Utility functions
├── migrations               # Database migrations
└── README.md                # Project documentation
```

## Setup and Installation

### Prerequisites

- **Docker**

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/35C4n0r/CloudSEK.git
    cd post-comments-service
    ```

2. **Start your docker service**:
   ```bash
   docker compose up --build
   ```

3. **Access API documentation**:
    - Open [http://localhost:8080/docs](http://localhost:8000/docs) to view the interactive API documentation.

## Usage

### API Endpoints

- **Sanity Check**: `GET /`
- **Create a User**: `POST /api/v1/user`
- **Get User by Username**: `GET /api/v1/user/{username}`
- **Create a Post**: `POST /api/v1/posts`
- **Get a Post**: `GET /api/v1/posts/{post_id}`
- **Update a Post**: `PUT /api/v1/posts`
- **Delete a Post**: `DELETE /api/v1/posts/{post_id}`
- **Create a Comment**: `POST /api/v1/comments`
- **Get Comments by Post ID**: `GET /api/v1/comments?post_id={post_id}`
- **Update a Comment**: `PUT /api/v1/comments`
- **Delete a Comment**: `DELETE /api/v1/comments/{comment_id}`

### Example Requests

- **Create a Post**:
    ```json
    {
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "user_id": "user-uuid-here"
    }
    ```

- **Create a Comment**:
    ```json
    {
        "content": "This is a comment.",
        "user_id": "user-uuid-here",
        "post_id": "post-uuid-here",
        "is_child_comment": false
    }
    ```

## Data Storage

Posts and comments are stored in a PostgreSQL database. SQLAlchemy ORM is used to interact with the database, providing an abstraction layer that simplifies CRUD operations. PostgreSQL was chosen for its reliability, scalability, and compatibility with SQLAlchemy.

## Code Quality and Best Practices

- **PEP 8**: The code adheres to PEP 8 standards.
- **Modular Design**: The project is designed with separation of concerns in mind, making it easy to extend and maintain.
- **Comments and Documentation**: Inline comments and documentation are provided to explain the codebase.
