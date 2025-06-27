Запуск тестов осуществляется командой pytest в терминале
Запуск самого скрипта осуществялется через терминал командой:
    python3 main.py --file epl_players.csv 
можно добавлять аргументы такие как --where & --aggregate
    python3 main.py --file epl_players.csv --where "club=liverpool" --aggregate "goals=min"

--where поддерживает так же символы "<=" ">="
