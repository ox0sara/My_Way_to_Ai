
name <- c("Ali", "Sara", "Reza", "Niloofar", "Omid", 
          "Hamed", "Maryam", "Arash", "Zahra", "Lila")

score <- c(18, 17, 19.5, 16, 14.5, 20, 18.5, 13, 15.5, 19)


plot(score, type = "o", col = "blue", 
     xaxt = "n",                
     ylim = c(0, 20),            
     main = "Student Scores", 
     xlab = "Student", 
     ylab = "Score")

axis(1, at = 1:10, labels = name, las = 2, cex.axis = 0.8)

