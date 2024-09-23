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
Jogos: 58
Vitórias: 34
Empates: 12
Derrotas: 12 
Gols pro: 93
Gols contra: 41
Saldo de gols: +52
Gols/jogo: 1.6
Gols sofridos/jogo: 0.71
Jogos em que marcou: 48
Jogos em que sofreu gol: 28 
Aproveitamento: 65.52%
Aproveitamento pontos: 114/174
```

| Jogador           |   Gols |   Assistências |
|:------------------|-------:|---------------:|
| Pedro             |     32 |              8 |
| Bruno Henrique    |      8 |              1 |
| Arrascaeta        |      8 |              9 |
| Everton Cebolinha |      6 |              4 |
| Luiz Araújo       |      6 |             10 |
| Gabi              |      4 |              1 |
| Léo Pereira       |      3 |              0 |
| Ayrton Lucas      |      3 |              5 |
| Gerson            |      3 |              7 |
| Carlinhos         |      2 |              0 |
| David Luiz        |      2 |              0 |
| de la Cruz        |      2 |              5 |
| Viña              |      1 |              2 |
| Lorran            |      1 |              3 |




## Gráficos

![img1.png](notebooks/figures/figure.png)

![img1.png](notebooks/figures/figure2.png)

![img1.png](notebooks/figures/figure3.png)



## Referências e Dados

- [Sofascore](https://www.sofascore.com/)
- [Fotmob](https://www.fotmob.com/)
- [ge](https://ge.globo.com/)
- [Flashscore](https://www.flashscore.com)
