# Simulação Discreta - Projeto Final

## Resultado do tempo final da simulação

A simulação base terminou no minuto 3270, com o avião 102 finalizando a decolagem.

## Identificação dos gargalos do sistema e criação de cenários que reduzam os gargalos

Para identificar os gargalos do sistema, realizamos um grid search simples com 192 combinações, variando em -1, +1 e +2 os parâmetros bases: quantidade de plataformas, quantidade de hangares, quantidade de pistas pequenas e quantidade de pistas grandes.

| Parâmetro                     | -1  | Base | +1  | +2  |
| ----------------------------- | --- | ---- | --- | --- |
| Quantidade de plataformas     | 4   | 5    | 6   | 7   |
| Quantidade de hangares        | 2   | 3    | 4   | 5   |
| Quantidade de pistas pequenas | 1   | 2    | 3   | 4   |
| Quantidade de pistas grandes  | -   | 1    | 2   | 3   |

Essa análise revelou que os gargalos do sistema estão concentrados nas pistas: com apenas 1 pista pequena o tempo total dispara para 6000 minutos independentemente dos demais recursos, e com a configuração atual (2 pistas pequenas e 1 pista grande) o sistema leva 3270 minutos, sendo que aumentar plataformas ou hangares isoladamente não produz nenhuma redução nesse tempo. A partir dessa análise, foram criados cenários que combinam o aumento de pistas pequenas e grandes simultaneamente, já que alterar apenas uma delas não resolve o problemam, a pista que permanece inalterada se torna o novo gargalo.

## Resultado do tempo final da simulação para os cenários criados

Os tempos finais obtidos para os cenários testados foram: 2060 min para a combinação de 3 pistas pequenas e 2 grandes (redução de 37%), 1815 min para 4 pistas pequenas e 2 grandes (redução de 44%), e 1728 min para 4 pistas pequenas e 3 grandes (redução de 47%). Todos os cenários que mantiveram as pistas inalteradas e variaram apenas plataformas e hangares resultaram em 3270 min, confirmando que estes recursos não são o gargalo atual.

## Análise sobre o impacto econômico dos cenários sugeridos

Do ponto de vista econômico, o cenário de melhor custo-benefício é a adição de apenas 1 pista pequena e 1 pista grande (totalizando 3 e 2, respectivamente), que entrega uma redução de 37% no tempo total de operação com o menor investimento em infraestrutura. O cenário máximo (4 pistas pequenas e 3 grandes) reduz mais 10 pontos percentuais, para 47%, mas exige o dobro de pistas adicionais, o que representa um custo de construção significativamente maior para um ganho marginal decrescente. Plataformas e hangares não precisam ser alterados, pois já operam com folga na configuração atual e aumentá-los não trouxe benefício significativo em nenhum cenário testado.
