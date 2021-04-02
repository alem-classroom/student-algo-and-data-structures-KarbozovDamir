def linear_search(lst, to_find):
    for i in range(len(lst)):
        if to_find == lst[i]:
            return i
        else:
            return -1
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1