# demo-streamlit-snowflake

## 1. Create config file config.toml and insert values 
### Example: 

```python
[connections.snowflake]
account = "YOUR_ACCOUNT"
user = "YOUR_USER"
password = "YOUR_PASSWORD"
role = "YOUR_ROLE"
warehouse = "YOUR_WAREHOUSE"
database = "YOUR_DATABASE"
schema = "YOUR_SCHEMA"
client_session_keep_alive = true
```
## 2. run docker compose up --build
## 3. go to http://localhost:8501/ to see the map