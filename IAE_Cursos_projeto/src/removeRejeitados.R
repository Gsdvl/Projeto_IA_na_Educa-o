rejeitados <- read.csv("../content/rejeitados.txt")
filtrados <- read.csv("../content/udemy_courses_filtred.csv")

aprovados <- subset(filtrados, !course_id %in% rejeitados[,1])

cat("Rejeitados removidos")
write.csv(aprovados, "../content/udemy_courses_filtred.csv", row.names = FALSE)