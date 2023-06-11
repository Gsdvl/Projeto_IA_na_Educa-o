udemy_courses <- read.csv("../content/udemy_courses.csv")
courses_data <- read.csv("../content/CoursesData.csv")

# Definir o caminho para o arquivo de texto
caminho_arquivo <- "../content/preferencias.txt"

# Abrir o arquivo em modo de leitura
pref <- file(caminho_arquivo, "r")

# Ler as quatro primeiras linhas
linhas <- readLines(pref, n = 4)

# Fechar o arquivo
close(pref)

#linha[1] float faixaPreco;
filtrado <- subset(udemy_courses, price <= linhas[1])

#linha[2] int duracaoCurso;
switch (linhas[2],
  "1" = filtrado <- subset(filtrado, num_lectures <= 20),
  "2" = filtrado <- subset(filtrado, num_lectures >= 15 & num_lectures <= 50),
  "3" = filtrado <- subset(filtrado, num_lectures >= 45)
)
#linha[3] int nivelCurso;
niveis <- c("Beginner Level","Intermediate Level","Expert Level","All Levels")
switch(linhas[3],
       "1" = filtrado <- subset(filtrado, level != niveis[2] & level != niveis[3]),
       "2" = filtrado <- subset(filtrado, level != niveis[1] & level != niveis[3]),
       "3" = filtrado <- subset(filtrado, level != niveis[1] & level != niveis[2]),
       "4" = cat("")
)
#linha[4] int areaEstudo;
areas <- c("Business Finance","Graphic Design","Musical Instruments","Web Development")
switch(linhas[4],
       "1" = filtrado <- subset(filtrado, subject == areas[1]),
       "2" = filtrado <- subset(filtrado, subject == areas[2]),
       "3" = filtrado <- subset(filtrado, subject == areas[3]),
       "4" = filtrado <- subset(filtrado, subject == areas[4])
)

cat("Base de dados filtrada")
write.csv(filtrado, "../content/udemy_courses_filtred.csv", row.names = FALSE)

