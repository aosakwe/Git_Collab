library(tidyverse)
library(ggplot2)

setwd("D:/Git_Collab/")
breasecancer <- read.csv("BreastCancerData.csv")

ggplot(breasecancer, aes(x = diagnosis, y = radius_mean)) +
  geom_violin()
