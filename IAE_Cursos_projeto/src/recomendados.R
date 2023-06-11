data <- read.csv("../content/udemy_courses_filtred.csv")
caminho_arquivo <- "../content/saida_predict.txt"

#abre o arquivo com a saida do predict
saida_predict <- file(caminho_arquivo, "r")

# Ler as quatro primeiras linhas
linhas <- readLines(saida_predict, n = 4)
linhas <- as.numeric(linhas)

# Fechar o arquivo
close(saida_predict)
rm(caminho_arquivo)

recomendaveis <- (data[which(grepl(saida_predict, data$num_subscribers)),])

#Tabelas ordenadas

ordenada_preco <- recomendaveis[order(recomendaveis$price), ]
ordenada_inscritos <- recomendaveis[order(recomendaveis$num_subscribers, decreasing = TRUE), ]
ordenada_relevancia <- recomendaveis[order(recomendaveis$num_reviews, decreasing = TRUE), ]

top_ordenada_preco <- ordenada_preco[1:5,]
top_ordenada_inscritos <- ordenada_inscritos[1:5,]
top_ordeada_relevancia <- ordenada_relevancia[1:5,]

#Junta as melhores recomendações em uma lista tridimensional
recomendacoes <- list(top_ordenada_preco,top_ordenada_inscritos,top_ordeada_relevancia)

# Instalar e carregar a biblioteca "openxlsx"
#install.packages("openxlsx")
library(openxlsx)

# Verificar se o arquivo existe
if (file.exists("../content/Recomendacoes.xlsx")) {
  # Remover o arquivo existente
  file.remove("../content/Recomendacoes.xlsx")
}

# Criar um novo arquivo Excel
wb <- createWorkbook()

# Criar uma nova planilha
addWorksheet(wb, "Recomendacoes")

# Preencher a planilha com os dados da lista
start_row <- 1  # Linha inicial para os dados
space_between <- 1  # Espaço entre os datasets

writeData(wb, sheet = "Recomendacoes", x = recomendacoes[[1]], startRow = start_row)
writeData(wb, sheet = "Recomendacoes", x = recomendacoes[[2]], startRow = start_row + nrow(recomendacoes[[1]]) + space_between)
writeData(wb, sheet = "Recomendacoes", x = recomendacoes[[3]], startRow = start_row + nrow(recomendacoes[[1]]) + nrow(recomendacoes[[3]]) + 2 * space_between)
# Salvar o arquivo Excel
saveWorkbook(wb, file = "../content/Recomendacoes.xlsx")

