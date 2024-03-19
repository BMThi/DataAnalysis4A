idx = which.max(rowSums(housetasks))

print(paste("The task with the highest number of joint responses is", row.names(housetasks)[idx], 
            "with", rowSums(housetasks)[idx], "common answers."))