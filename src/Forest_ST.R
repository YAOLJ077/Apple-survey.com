library("forestplot")
library("grid")
library("magrittr")
library("checkmate")
forest_data<-read.csv(("../data/Forest_ST.csv"),header=T)
#head(forest_data)
#View(forest_data)
forestplot(as.matrix(forest_data[,1:4]),mean=forest_data$OR,lower=forest_data$lower,upper=forest_data$upper,
           is.summary=c(T,F,F,F,F,F,F,F),
           zero=1,boxsize=0.3,lineheight=unit(12,'mm'),
           lwd.zero=1.5,lwd.ci=2,xlab="OR",lwd.xaxis=2.7,grid=TRUE,
           align="c",graphwidth=unit(40,"mm"),
           col=fpColors(box="orange",lines="darkorange",zero="black",axes = "black"),
           txt_gp=fpTxtGp(ticks = gpar(cex=1.0),xlab=gpar(cex=1.0),cex=1.2),
           #boxcolor=ifelse(as.numeric(OR)>1.786,"red"),
           hrzl_lines=list("1"=gpar(lwd=2,lty=1),"2"=gpar(lwd=2,lty=1),"9"=gpar(lwd=2,columns=1:5,col="#000044")),
           #hrzl_lines=gpar(col="#444444"),
           title="The role of information source on technology adoption",graph.pos=4,
           ci.vertices=TRUE,ci.vertices.height = 0.2,clip=c(0,3.0))