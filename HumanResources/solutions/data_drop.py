data = data.drop(['EmployeeCount', 'Over18', 'StandardHours', 'EmployeeNumber'], axis=1)
display( data.head().style.background_gradient(cmap='BuPu') )