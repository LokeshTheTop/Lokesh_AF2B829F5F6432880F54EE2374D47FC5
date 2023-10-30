def linear_search_product(products, target_product):
  indices = []
  for index, product in enumerate(products):
      if product == target_product:
          indices.append(index)
  return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(products, target)
if result:
  print(f"The product '{target}' was found at indices: {result}")
else:
  print(f"The product '{target}' was not found in the list.")