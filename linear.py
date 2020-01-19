import pandas as pd
#pandas module is implemented to read the data points

df = pd.read_csv('data.csv')
#data points are read with the help of pandas module,data points are accessed with the help of the object df
  
#print(df.head);  
#To display the data points usually first 30 and last 30 values are displayed

#print(df.shape);
#to display the number of rows and columns

df=df[['length','width']]
#the column names with the name length and width are selected for further computation
#Here we are considering the x value as length and y value as width

#print(df.head);  
#print(df.shape);

length_sum=0;
#initializing the variable length_sum to zero so that it is free of junk values

length_squared_sum=0;
#initializing the variable length_squared_sum to zero so that it is free of junk values

instance=0;
#initializing the variable instance to zero so that it is free of junk values


for leng in df['length']:
   length_sum+=leng;
   length_squared_sum+=(leng*leng);
   instance+=1;
#iterating over the rows whoose column index is length.Here we find the summation value of the length and the summation of the squared value of length attribute which is further needed for the calculation of parameters of linear regression.
#Here we also calculate the number of instances by incrementing it by one.


width_sum=0;
#initializing the variable width_sum to zero so that it is free of junk values

width_squared_sum=0;
#initializing the variable width_squared_sum to zero so that it is free of junk values


for width in df['width']:
   width_sum+=width;
   width_squared_sum+=(width*width);
#iterating over the rows whoose column index is width.Here we find the summation value of the length and the summation of the squared value of width attribute which is further needed for the calculation of parameters of linear regression.

sum_of_product_of_xy=0;
#initializing the variable width_sum to zero so that it is free of junk values
product_of_xy=0
#initializing the variable width_sum to zero so that it is free of junk values

product_of_xy=(df['length']*df['width']);
#A list of values is obtained which is the product of the values present in th length column and the product column.

for i in product_of_xy:
   sum_of_product_of_xy+=i;
#summation of the values present in the product_of_xy is calculated which further needed for the calculation of the linear regression.


length_mean=length_sum/instance;
width_mean=width_sum/instance;
#mean values of the length and width is calculated which is the sum of all the values and the number f instances.


length_mean_square=length_mean*length_mean;
#mean value of the length is squared

width_mean_square=width_mean*width_mean;
#mean value of the length is squared

length_variance=(length_squared_sum-(instance*length_mean_square))/(instance-1);
#the variance of x i.e length is calculated based the variance formula given below
#variance of x=(sum_of_x^2-(n*x_mean^2))/n-1
#variance is the square of the standard deviation

covariance=(sum_of_product_of_xy-(instance*length_mean*width_mean))/(instance-1);
#the covariance for the data is calculated which is based on the formula givn below
#covariance=(sum_xy-(n*x_mean*y_mean))/n-1




