# auth-service-api -  минималистичный сервис для аутентификации и управления пользователями
Создан для примера.

1. БЛ в Application
2. Логика чтения в adapters/gateway
3. В Presentation хранятся HTTP-эндпоинты
4. Юзаем dishka, настройки хранятся в bootstrap/di
5. Justfile как замена Makefile
6. Подключена Grafana, но пока пустая

## Запуск локально
### Запуск линтеров
```
just lint
```
### Запуск приложения
```
just dev
```
### Остановка приложения
```
just down
```
### Очистка данных приложения
```
just clear
```
### Тесты (их пока нет)
```
just e2e
```
### Миграции
```
just dev
just migration <название>
```

### Если хочется потыкать проект
```
pre-commit install
uv pip install ".[dev]"
```