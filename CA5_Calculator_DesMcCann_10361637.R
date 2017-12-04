#Author - Des McCann
#Student ID: 10361637
#CA 5a - writing an R calculator


#1 the mean take a list of numbers in form (C(num1,num2,num3..etc))
my_mean <- function(datain) 
  {
  s= sum(datain)
  l=length(datain)
  s/l

}

#2 add 2 numbers
my_sum <- function(a,b) 
{
  a+b

}

#3 subtraction
my_takeaway <- function (c,d)
{
  c-d
}

#4 Remainder ( with the modulus function)
my_remainder <- function(num, divisor) 
  {
  num%%divisor
  }

#5 division
my_divisor <- function(num,divisor)
{
  num/divisor
}

#6 multiplication of 2 numbers
my_multiply <- function (numa,numb)
{
  numa*numb
}

#7 the square of a number
my_square <- function (numin)
{  numin*numin
}

#8 Raise number to the power of
my_power <- function (base,index)
  {
  base**index
}

#9 reciprocal
my_reciprocal <- function (numba)
{
  1/numba
}

#10 Percentage 
my_percentage <- function (numz)
{
  paste(numz*100,"%",sep="")
}


