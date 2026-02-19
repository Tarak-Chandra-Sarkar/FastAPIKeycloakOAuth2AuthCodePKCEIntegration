# 🔐 FastAPI + Keycloak OAuth2 (PKCE) Integration

A modular, production-ready FastAPI project integrated with <strong>Keycloak</strong> using <strong>OAuth2 Authorization Code Flow</strong> with <strong>PKCE</strong> and <strong>JWKS-based JWT</strong> validation.

---
[![GitHub license](https://img.shields.io/github/license/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg)](https://github.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration/blob/master/LICENSE.txt)
[![GitHub contributors](https://img.shields.io/github/contributors/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg)](https://GitHub.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg)](https://GitHub.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg)](https://GitHub.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration)

[![GitHub watchers](https://img.shields.io/github/watchers/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg?style=social&label=Watch)](https://GitHub.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration)
[![GitHub forks](https://img.shields.io/github/forks/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg?style=social&label=Fork)](https://GitHub.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration/network/)
[![GitHub stars](https://img.shields.io/github/stars/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration.svg?style=social&label=Star)](https://GitHub.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration/stargazers/)

---

## 📁 Project Structure

```bash
app/
├── main.py
├── core/
│   └── config.py
├── middleware/
│   └── auth_middleware.py
├── services/
│   └── keycloak_service.py
├── api/
│   ├── routes.py
│   └── protected.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Features

* OAuth2 Authorization Code Flow
* PKCE (S256)
* JWKS-based JWT validation
* Environment-based configuration
* Modular project structure
* Swagger UI integration

---

## 🛠 Requirements

* Python 3.9+
* Running Keycloak instance
* Docker Desktop [optional]

### Install dependencies:

#### Step1:
- Create Python Virtual Environment to avaoid python packages versions conflicts
```sh
python -m venv .venv
```
where <b>.venv</b> given user name for Python Virtual Environment
- Activate the virtual environment (.venv)
in Windows
```sh
.venv/Scripts/Activate.ps1
```
#### Step2:
You need to have Python and pip installed. Start by setting up a project directory and installing the necessary packages: 
```sh
pip install -r requirements.txt
```

Note: python-jose and passlib[bcrypt] are highly recommended for secure password hashing and JWT token handling.

---

## ⚙️ Keycloak Setup
### Refer to Insapring & Fantastic Blog for detailed steps
[Integrate Keycloak with ASP.NET Core Using OAuth 2.0](https://www.milanjovanovic.tech/blog/integrate-keycloak-with-aspnetcore-using-oauth-2)

### 1️⃣ Create Realm

```
keycloak-demo
```

### 2️⃣ Create Client

```
Client ID: demo-api
```

### 3️⃣ Client Configuration

* Access Type → Public
* Client Authentication → OFF
* Standard Flow → Enabled
* PKCE Code Challenge Method → S256

### 4️⃣ Valid Redirect URI

```
http://localhost:8001/docs/oauth2-redirect
```

---

## 📝 .env Configuration
Create a `.env` file in the project root:

```pwsh
copy .env.example .env
```
Change settings as per required:
```env
KEYCLOAK_URL=http://localhost:8080
KEYCLOAK_REALM=keycloak-demo
KEYCLOAK_CLIENT_ID=demo-api
KEYCLOAK_AUDIENCE=account
KEYCLOAK_ALGORITHM=RS256

APP_HOST=127.0.0.1
APP_PORT=8001
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open in browser:

```
http://localhost:8001/docs
```

Click **Authorize**, login via Keycloak, then access protected endpoints.

---

## 📌 Available Endpoints

### Public Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Hello, anonymous user!"
}
```

---

### Protected Endpoint

```http
GET /protected/
```

Requires valid JWT token.

Response:

```json
{
  "message": "Hello, <username>! This is protected."
}
```

---

## 🔐 Authentication Flow

1. Swagger initiates OAuth2 Authorization Code Flow
2. PKCE (S256) challenge is generated
3. Keycloak authenticates user
4. Access token is returned
5. FastAPI validates:

   * Signature (RS256)
   * Audience
   * Issuer
   * Expiration

---

## 🏗 Architecture Overview

* **core/** → Environment configuration
* **services/** → Keycloak & JWKS logic
* **middleware/** → Authentication dependency
* **api/** → Route definitions

---

## 🛡 Security Practices

* No hardcoded secrets
* PKCE enforced
* Dynamic JWKS retrieval
* Proper issuer & audience validation
* Clean separation of concerns

---

## 🚀 Future Improvements

* JWKS caching
* Role-based access control (RBAC)
* Docker setup
* Logging & monitoring
* Unit & integration tests

---
## Author

👤 **Tarak Chandra Sarkar**

* Github: [@tarak-chandra-sarkar](https://github.com/Tarak-Chandra-Sarkar)
* LinkedIn: [@tarak-chandra-sarkar](https://www.linkedin.com/in/tarak-chandra-sarkar/)

## 🤝 Contributing

N/A

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright &copy; 2026 [Tarak Chandra Sarkar](https://github.com/Tarak-Chandra-Sarkar/FastAPIKeycloakOAuth2AuthCodePKCEIntegration).

This project is [MIT](/LICENSE) licensed.

***