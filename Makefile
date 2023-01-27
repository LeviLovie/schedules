main:
	@python3 main.py

dev:
	@echo ""
	@echo "Running..." >> log.log
	@echo "$n" >> log.log
	@echo "Running..." >> log.log
	@python3 main.py --dev