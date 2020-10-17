from typing import List
import scipy

class Student(object):
  
  def __init__(self, name: str, marks: List[int], exercises: List[int]):
    self.name = name
    self.marks = marks
    self.exercises = exercises
  

  def Linear_search_algorithms_1(list: List, target):
    for n in range(len(list)):
      if target == list[n]:
        return n
        n = n + 1
        break
      else:
        n = n + 1

    return -1


  def Linear_search_algorithms_2(list: List[int], cut_off_value: int):
    i = len(list) - 1
    while i >= 0:
      if list[i] < cut_off_value:
        del list[i]
        i = i - 1
      else:
        i = i - 1
    return list


  def Linear_search_algorithms_3(list: List[str], target: str):
    i = len(list) - 1
    while i >= 0:
      for n in range(len(target)):
        if len(list[i]) == len(target):
          if list[i][n] == target[n]:
            result = list[i][n]
            del result
            list.insert(0, result)
            i = i - 1
        else:
          i = i - 1
    return list


  


  def Linear_search_algorithms_5(list: Lise[int], target: str):
    original_list = []
    new_list = []
    for n in range(len(list)):
      if list[n] <= 50:
        new_list.append(list[i])
      else:
        original_list.append(list[i])

    if sum(new_list) % 2 == 0:
      return original_list
    else:
      return new_list



                
  (scipy.mean(a))


  def Bubble_sort_2(list: List[Student]):
