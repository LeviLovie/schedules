main:
	@python3 main.py

dev:
	@echo "$(shell date +%Y-%m-%d-%H-%M-%S) Running..." >> log.log
	@python3 main.py --dev
	@echo "" >> log.log