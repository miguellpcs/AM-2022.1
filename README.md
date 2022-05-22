# AM-2022.1
## Questão 1

Considere os dados "Avila Data Set" (Data set e artigo relevante em anexo) do site uci machine learning
repository (https://archive.ics.uci.edu/ml/datasets/Avila.
Fusione os arquivos avila-tr.txt e avila-ts.txt no arquivo avila.txt, DESCONSIDERANDO a variavel de classe (os rotulos).
A partir do arquivo avila.txt produza 3 matrizes de dissililaridade usando a distancia Euclidiana (L2), a distancia de city-block (L1) e a
distancia de Chebyshev (Linf).
Implemente e execute o algoritmo "VFCMddV" 50 vezes para obter uma partição fuzzy em 12 grupos e selecione o melhor resultado segundo a função objetivo.
A descrição do algoritmo "VFCMddV" esta no artigo: "Francisco de A.T. de Carvalho, Filipe M de Melo, Yves Lechevallier, 
A multi-view relational fuzzy c-medoid vectors clustering algorithm. Neurocomputing, v. 163, p. 115-123, 2015".
Calcule o Modified partition coefficient e o Partition entropy. Comente.
Produza uma partição crisp em 12 grupos e calcule o índice de Rand corrigido, e a F-measure
(adaptada para agrupamento). Comente.

Observações:
Normalize as matrizes de dissimilaridade conforme descrito no artigo que descreve o
algoritmo VFCMddV (pagina 119, coluna 1, terceiro paragrafo);
Parametros: k = 12; T = 150;  = 10−10;
Para o melhor resultado imprimir: i) os protótipos ii) a matrix de confusão da partição crisp
versus a partição a priori; iv) a matrix de pesos de relevância das matrizes de
dissimilaridade.
