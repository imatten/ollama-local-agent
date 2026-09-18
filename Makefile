.PHONY: up down logs network-up pull

network-up:
	docker network create ollama-net || true

up: network-up
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

pull:
	docker exec -it ollama ollama pull $(MODEL)
