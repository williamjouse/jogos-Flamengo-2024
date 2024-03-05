# Dados dos jogos do Flamengo temporada 2024

Nesse repositório são encontradas tabelas com informações e análises sobre os jogos do Flamengo na temporada 2024. A tabela [matches_FLA2024.csv](https://github.com/williamjouse/jogos-Flamengo-2024/blob/main/data/raw/matches_FLA2024.csv)
contém as seguintes colunas:

- id_match: ID do jogo
- home_team: Time mandante
- away_team: Time visitante
- home_score: Gols marcado pelo mandante
- away_score: Gols marcado pelo visitante
- tournament: Torneio ou competição e rodada
- kick-off: Data e hora da partida
- stadium: Estádio da partida
- attendance: Público da partida


Na segunda tabela de nome [goal_scorers_2024.csv](https://github.com/williamjouse/jogos-Flamengo-2024/blob/main/data/raw/goal_scorers_2024.csv) contém as seguites colunas:

- id_match: ID do jogo
- gols: Jogador que marcou gol na partida
- assist: Assistência para o gol

No arquivo [matches_FLA2024.xlsx](https://github.com/williamjouse/jogos-Flamengo-2024/blob/main/data/matches_FLA2024.xlsx) contém a junção das 2 tabelas em um único lugar.

No arquivo [Data-wrangling](https://github.com/williamjouse/jogos-Flamengo-2024/blob/main/notebooks/01-Data-wrangling.ipynb) é criado colunas derivadas dos dados originais. A análise 
é feita no [Statistics_Analysis-2024](https://github.com/williamjouse/jogos-Flamengo-2024/blob/main/notebooks/02-Statistics_Analysis-2024.ipynb) é calculado algumas estatísticas que são mostradas abaixo.
E [Plotting](https://github.com/williamjouse/jogos-Flamengo-2024/blob/main/notebooks/03-Plotting.ipynb) é plotado os gráficos.

## Estatísticas


```
Jogos: 13
Vitórias: 9
Empates: 4
Derrotas: 0 
Gols pro: 26
Gols contra: 2
Saldo de gols: +24
Gols/jogo: 2.0
Gols sofridos/jogo: 0.15
Jogos em que marcou: 11
Jogos em que sofreu gol: 2 
Aproveitamento: 79.49%
Aproveitamento pontos: 31/39
```

| Jogador           |   Gols |   Assistências |
|:------------------|-------:|---------------:|
| Pedro             |     10 |              1 |
| Léo Pereira       |      3 |              0 |
| Everton Cebolinha |      3 |              1 |
| Arrascaeta        |      3 |              3 |
| Gabi              |      2 |              0 |
| Varela            |      1 |              1 |
| Thiaguinho        |      1 |              0 |
| Bruno Henrique    |      1 |              0 |
| Ayrton Lucas      |      1 |              2 |
| Luiz Araujo       |      1 |              0 |




## Gráficos


## Referências e Dados

- [Sofascore](https://www.sofascore.com/)
- [Fotmob](https://www.fotmob.com/)
- [ge](https://ge.globo.com/)
