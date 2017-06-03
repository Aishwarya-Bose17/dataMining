> Amazon <- read.csv("C:/Users/ab822/Downloads/Amazon.csv")
>   View(Amazon)
>
> microsoft_subtable <- Amazon[grep("microsoft", Amazon$manufacturer),]
> View(microsoft_subtable)
>
> boxplot(microsoft_subtable$price, horizontal=T)