read.csv()

df <- read.csv("/Users/aardesta/GitHub/Git_Collab/BreastCancerData.csv")

library(ggplot2)

ggplot(df, aes(x = 1:nrow(df), y = radius_mean)) +
  geom_point() +
  labs(x = "Index", y = "Radius Mean") +
  ggtitle("Scatter Plot of Radius Mean")

