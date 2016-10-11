## Cikibike Null Hypothesis project review

Your code begins with data extraction. Null hypothesis should be forst, so the reader understands why and what data is being downloaded.


The data should be moved to the PUIDATA diretory. It is a very bad habit to keep data in the code directory and in our case having all data in PUIDATA avoids the risk for the graders to have 90 copies of the same dataset in their home directory as they grade 90 notebooks.


Please do not show entire datasets in your notebooks, or just extremely large sections of notebooks! Use DataFrame.head(), DataFrame.tail(), DataFrame.summary() instead and all other methods!

Notice that you should also use datestring to create the file name so that if you want to use a different input file you need to change values only in one place. i left the line incomplete because I want you to complete it and understand it, not just copy and paste it.


The mathematical formulation of the Null is missing (N_WD - N_WE = ...)

The question and Null hypothesis are well formulated.

The data supports the question but there are several mistakes in the data munging portion.

First

data['date'] = pd.to_datetime(data['starttime'])

data.drop(['tripduration', 'starttime', 'stoptime', 'start station id',
       'start station name', 'start station latitude',
       'start station longitude', 'end station id', 'end station name',
       'end station latitude', 'end station longitude', 'bikeid', 'usertype',
       'birth year', 'gender'], axis=1, inplace=True)

why would you copy a column identically, then remove the original? that is a waste of computational time and memory. With a large dataset this could cost a significant amount of time, when you can just rename the column (look at all the functions in the  Chapter 7 notebook from Data Analysis in Python https://github.com/fedhere/UInotebooks/blob/master/dataWrangling/PandasDataWrangling-Chap7.ipynb)


Second

the following chunk of code has some mistakes and can be vastly improved in style and efficiency:

```
        working_day_trip = 0
        weekend_day_trip = 0

        for i in range(0 , 4):  
            working_day_trip = data_count[i] + working_day_trip

        for i in (5,6):
            weekend_day_trip = data_count[i] + weekend_day_trip
    
```
MISTAKE: range(0 , 4)  returns [0,1,2,3], which for you is [M, T, W, Th]. So  you are skipping friday altogether (but accounting for them in the mean so your mean is wrong)


For efficiency those loops should be changed with

```
        working_day_trip  = data_count[:5].sum(),
        weekend_day_trip = ...
        
```

What is up with the norm_w = 1 and division by norm_1??

Once the mistakes are fixed you have to averages, so you can do a test of means, **but for that you also have to extract the standard deviations of the distributions to assess statistical significance, and the way you worked with the data does not help much obtaining it because your data is now grouped by weekday so you can get the std and mean per day of the week (mean trips number on monday over a month, mean trip number on tuesday over the month etc), but to get the mean and std of all weekdays you are going to have to do some more work**.
