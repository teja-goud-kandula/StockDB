# StockDB
In the future if I have replicate this again, then download all the files from the desired start date to the latest stock market end date into a single folder, then run the script ```LoadYearWiseHistoricData.py``` script to load all of that data into the ```[source].[bhavcopysrc]``` table.

For setting up the connection between Python and SQL Server I am using Windows Authentication so there is no need for the username and the password. 

Then for daily runs there after run the incremental script. 