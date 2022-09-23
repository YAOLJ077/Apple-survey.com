library(ggplot2)
library(wesanderson)
data <- read.csv(("../data/pie.csv"),header = T)
data$Type_number <- as.character(data$Type_number)
ggplot(data,mapping = aes(Production_stage,Count,fill=Type_number))+
  geom_bar(stat='identity',position='fill') +labs(x = 'Production_stage',y = 'Perecent') +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))+ theme_bw() + 
  theme(panel.grid.major = element_blank(),panel.grid.minor = element_blank())+
  theme(axis.text = element_text(size = 12),axis.title = element_text(size = 14, color = 'black'),
        legend.title = element_text(size = 12, color = 'black'),legend.text = element_text(size=10))+
  scale_fill_manual(values = c( "1"="#33a02c", "2"="#377eb8", "3"="#984ea3", "4"="#d95f02", "5"="#e41a1c"))

