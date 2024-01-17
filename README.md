# e_orders
e_orders is a Django application for creating, managing and analyzing the orders made by your clients.

## Development
Create .env file as follows
```
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=postgres
DB_PORT=5432
```
Build the image:
```bash
docker-compose build
```

Once the image is built, run the container:
```bash
docker-compose up -d
```

Run the migrations:
```bash
docker-compose exec e_orders python e_orders/manage.py migrate --noinput
```

Build the new image and spin up the two containers(django application and postgres instance) if needed
```bash
docker-compose up -d --build
```

Navigate to http://localhost:8000/api to view the default basic root view for DefaultRouter

## Contributing

Pull requests are welcome.
