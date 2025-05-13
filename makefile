start-dev:
	uvicorn app.main:app --reload
start:
  uvicorn app.main:app
# Initialize your local database
psql-up:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans db
# Remove your local database
psql-down:
	sudo docker compose -f docker-compose.yml down -v --remove-orphans
# up all services
all-up:
	docker compose up --build
# down all services
all-down:
	docker compose down