# Loading Packages
require(foreign)
require(nnet)
require(ggplot2)
require(reshape2)

# Setting up directory
setwd("/Users/Joseph/Python Projects/Cell-Data")

# Creating a data frame
data1 = read.csv("CellDataCleaned.csv")

mlogit1 = multinom(choice ~ fam_size + rinc + college + married + urban + male + white + age_ref + year, data = data1)
summary(mlogit1)

dses <- data.frame(fam_size = c(1, 4, 1), rinc = c(7750, 86000, 19000), college = c(0, 1, 1), married = c(0, 1, 0), urban= c(1, 1, 1), male= c(1, 1, 0), white = c(1, 1, 1), age_ref = c(20, 45, 75), year = c(2010, 2010, 2010))
                  
predict(mlogit1, newdata = dses, "probs")

dyear1 <- data.frame(fam_size = rep(c(1, 4, 1), each = 18), rinc = rep(c(7750, 86000, 19000), each= 18), college = rep(c(0, 1, 1), each = 18), married = rep(c(0, 1, 0), each = 18), urban= rep(c(1, 1, 1), each = 18), male= rep(c(1, 1, 0), each = 18), white = rep(c(1, 1, 1), each = 18), age_ref = rep(c(20, 45, 75), each = 18), year = rep(c(1993:2010), 3))

pp.year1 <- cbind(dyear1, predict(mlogit1, newdata = dyear1, type = "probs", se = TRUE))

lpp <- melt(pp.year1, id.vars = c("fam_size", "rinc", "college", "married", "urban", "male", "white", "age_ref", "year"), value.name = "probability")
head(lpp) 

ggplot(lpp, aes(x = year, y = probability, colour = factor(age_ref))) + geom_line() + scale_color_manual(name = "Group IDs", labels = c("Group 1 (Younger)", "Group 2 (Middle Aged)", "Group 3 (Older)"), values = c("red", "darkgreen", "blue")) +  facet_grid(variable ~., scales = "fixed") + ggtitle("Probability of Phone Choice from 1993-2010", subtitle = NULL) + xlab("Year") + ylab("Probability") 
ggsave("PhoneChoice1993-2010.png", plot = last_plot())
