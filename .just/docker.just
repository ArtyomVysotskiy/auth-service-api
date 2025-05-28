set shell := ["cmd", "-c"]

[no-cd]
up:
    docker compose up --build

[no-cd]
down:
    docker compose down
    docker compose -f docker-compose.test.yml down

[no-cd]
clear:
    docker compose down -v