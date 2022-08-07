mydata<-read.csv("F:/R/Data_bank/Column.csv")
library(ggplot2)
library(dplyr)
library(ggsci)
Col6<-pal_npg("nrc", alpha = 0.7)(5)
ggplot(data=mydata,aes(Source,Count,group=Stage,fill=Stage))+
  geom_bar(stat="identity",position="stack", colour="black", width=0.7,size=0.25)+scale_fill_manual(values = Col6)+labs(x="Information Source")+geom_text(aes(label=Count),position=position_stack(vjust=0.5))
