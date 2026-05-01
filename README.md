# QA Automation — API + Web

Projeto de automação de testes cobrindo API REST (Swagger Petstore) e fluxo E2E web (SauceDemo), com pipeline de CI no GitHub Actions.

## Tecnologias

| Camada | Stack |
|--------|-------|
| API    | Python, Requests, Pytest |
| Web    | Python, Selenium, Pytest, Page Object Model |
| CI     | GitHub Actions (jobs paralelos) |
| Relatórios | pytest-html |

## Estrutura

```
.
├── api-tests/
│   ├── tests/
│   ├── conftest.py
│   └── requirements.txt
├── web-tests/
│   ├── pages/
│   ├── tests/
│   ├── conftest.py
│   └── requirements.txt
├── .github/workflows/ci.yml
└── README.md
```

## Pré-requisitos

- Python 3.11+
- Google Chrome instalado (para os testes web)
- pip

## Instalação e execução local

```bash
git clone <repo-url>
cd qa-automation
```

### API tests

```bash
pip install -r api-tests/requirements.txt
pytest api-tests/tests/ -v
```

### Web tests

```bash
pip install -r web-tests/requirements.txt
pytest web-tests/tests/ -v
```

## Cenários cobertos

### API — Swagger Petstore (`https://petstore.swagger.io/v2`)

- **Pet**: `POST /pet`, `GET /pet/{id}`, `PUT /pet`, `DELETE /pet/{id}`, `GET /pet/findByStatus`, `GET /pet/findByTags`, `POST /pet/{id}/uploadFile`
- **Store**: `GET /store/inventory`, `POST /store/order`, `GET /store/order/{id}`, `DELETE /store/order/{id}`
- **User**: `POST /user`, `POST /user/createWithList`, `GET /user/{username}`, `PUT /user/{username}`, `GET /user/login`, `GET /user/logout`, `DELETE /user/{username}`

### Web — SauceDemo E2E

Fluxo completo de compra: login → adicionar 2 produtos ao carrinho → checkout → preencher dados → finalizar → assertar mensagem de confirmação.

## CI/CD

Pipeline definida em `.github/workflows/ci.yml` com dois jobs paralelos (`api-tests` e `web-tests`). Cada job gera um relatório HTML disponível como artifact na execução do workflow (aba **Actions** → run → **Artifacts**).

## Prints

<!-- adicionar prints aqui -->
