# Write a Python script to check if a given key already exists in a dictionary.
it_company ={
               "c++" :10000,
               "python":30000,
               "java":40000,
}
key="python"
if key in it_company:
    print(f"{key} exits in a dictionary")
else:
      print(f"{key} not exits in a dictionary")    