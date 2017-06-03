> GoogleProducts[grep("game", GoogleProducts$name),"game"] <- "yes"
> View(GoogleProducts)
>
> GoogleProducts[grep("game", GoogleProducts$description),"game"] <- "yes"
> View(GoogleProducts)
>
> gamesubset <- GoogleProducts[grep("yes", GoogleProducts$game),]
> View(gamesubset)
>
> val <- na.omit(gamesubset)
>
> barplot(prop.table(table(val$manufacturer)), ylab = "Frequency",xlab = "Manufacturer")