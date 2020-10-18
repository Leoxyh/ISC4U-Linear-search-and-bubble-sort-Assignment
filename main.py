from typing import List
import scipy

class Student:
  
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


def linear_search_algorithms_4(list: List[Student], target: str):
  for i in range(len(list)):
    n = 0
    for j in range(len(target)):
      if len(list[i].name) >= len(target) and list[i].name[j] == target[j]:
        del list[i]
        n = n + 1
      else:
        break
  return list[i]


def Linear_search_algorithms_5(list: List[int], target: str):
  original_list = []
  new_list = []
  for n in range(len(list)):
    if list[n] <= 50:
      new_list.append(list[n])
    else:
      original_list.append(list[n])

  if sum(new_list) % 2 == 0:
    return original_list
  else:
    return new_list


def Bubble_sort_1(list: List[Student]):
  for i in range(len(list) - 1):
    for n in range(len(list) - i - 1):
      if scipy.mean(list[n]) > scipy.mean(list[n + 1]):
        list[n], list[n + 1] = list[n + 1], list[n]
  
  return list


def Bubble_sort_2(list: List[Student]):
  for i in range(len(list) - 1):
    for n in range(len(list) - i -1):
      if len(list[n].exercises) > len(list[n + 1].exercises):
        list[n], list[n + 1] = list[n + 1], list[n] 
