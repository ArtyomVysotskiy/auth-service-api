set shell := ["cmd", "-c"]

[no-cd]
e2e:
    docker compose -f docker-compose.test.yml up --build --abort-on-container-exit