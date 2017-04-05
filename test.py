#vmazza

import numpy as np

#Function that returns the sum of two rows (external to the class)
def sum_rows(row_1, row_2, n):
  row_sum = []
  for j in range(n):
    row_sum.append(row_1[j] + row_2[j])
  return row_sum

#Function that returns the sottraction of two rows (external to the class)   
def sub_rows(row_1, row_2, n):
  row_sub = []
  for j in range(n):
    row_sub.append(row_1[j] - row_2[j])
  return row_sub
    
#Function that returns the sum of a row with an integer    
def sum_int_row(value, row, n):
  row_sum = []
  for j in range(n):
    row_sum.append(value + row[j])
  return row_sum
  
#Function that returns the difference of a row with an integer    
def sub_int_row(value, row, n):
  row_sub = []
  for j in range(n):
    row_sub.append(row[j] - value)
  return row_sub
  

#Definition of the class Matrix (NxN)
class Matrix(object):
  #Init method to set the rows of the matrix; if not inserted the values are all 0
  def __init__(self, *args):
    self.rows = []
    self.n = len(args)
    if len(args) == 0:
      self.rows.append(0)
      print("Matrix 1x1 with value 0")
    else:
      for arg in args:
        self.rows.append(arg)
        
        
        
      
  #Function that returns the sum of two Matrix (overloading the operator +)
  def __add__(self, other):
    result_list = []
      
    #Case self.n is integer  
    if not isinstance(other, Matrix):
      value = other
      for i in range(self.n): #i referred to number of the row
        result_list.append(sum_int_row(value, self.rows[i], self.n))
    #Case dimension n
    elif self.n == other.n:
      for i in range(self.n): #i referred to number of the row
        result_list.append(sum_rows(self.rows[i], other.rows[i], self.n))
    else:
      print("Dimension is wrong!")
    return Matrix(result_list)    
    
    
  #Function that returns the difference of two Matrix (overloading the operator -)
  def __sub__(self, other):
    result_list = []
    
    #Case self.n is integer
    if not isinstance(other, Matrix):
      value = other
      for i in range(self.n): #i referred to number of the row
        result_list.append(sub_int_row(value, self.rows[i], self.n))
    elif other.n == self.n:
      for i in range(self.n): #i referred to number of the row
       result_list.append(sub_rows(self.rows[i], other.rows[i], self.n))
    else:
      print("Dimension is wrong!")
    return Matrix(result_list) 
    
    
  #Function that returns the product of two matrices
  def prod(self, matrix):
    product_rows = np.multiply(self.rows, matrix.rows)
    return Matrix(product_rows)
    
  #Function that prints the Matrix (overloading the function print() )
  def __str__(self):
    return str(np.array(self.rows))
  
  #Definition of iter
  def __iter__(self):
    return iter(self.rows)
  
  #Definition of next  
  def __next__(self):
    i = 0
    if i < self.n:
      return self.rows[i]
      i += 1
    else:
      raise StopIteration()
      
      
self.assert
