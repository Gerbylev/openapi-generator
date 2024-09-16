# FastAPI OpenAPI Generator

## О проекте

Этот проект предназначен для автоматической генерации API на основе спецификации OpenAPI с использованием инструмента [OpenAPI Generator](https://openapi-generator.tech/). Генерация осуществляется через скрипт `generate-api.sh`, который позволяет быстро и удобно создавать API-код для FastAPI.

## Использование

### Генерация API

Для генерации API выполните скрипт:

```bash
sh ./generate-api.sh
```   

### Запустите приложение: 
После генерации API, вы можете запустить сервер FastAPI с помощью Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```
### Проверка работоспособности: 



Перейдите по адресу http://localhost:8080/mock?id=1
для проверки работы API.