from config import connex_app

# Le indicamos el archivo de especificación Swagger
connex_app.add_api("swagger.yml")

if __name__ == "__main__":
    connex_app.run(port=8000, debug=True)