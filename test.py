def first_k_views(views, target):
  """
  Finds the first moment in which the video reaches K views.

  Args:
    views: A list of integers representing the view times.
    target: An integer representing the target number of views.

  Returns:
    The first moment in which the video reaches K views, or -1 if it never does.
  """

  # Sort the view times in ascending order.
  views.sort()

  # Count the number of views so far.
  count = 0

  # Find the first moment when the count reaches or exceeds the target.
  for time in views:
    count += 1
    if count >= target:
      return time

  # The target was never reached.
  return -1

# Get the number of people, the target number of views, and the view times.
n, k = map(int, input().split())

# Initialize an empty list to store view times
views = []

for _ in range(n):
  # Get the view times for each person
  ai, bi = map(int, input().split())
  
  # Add the first view time (ai) to the list
  views.append(ai)
  
  # Add subsequent view times based on bi
  for _ in range(bi - 1):
    views.append(ai + views[-1] - ai)

# Find the first moment when the video reaches K views.
result = first_k_views(views, k)

# Print the result.
print(result)
