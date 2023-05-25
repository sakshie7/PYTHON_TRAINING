#Write a Python script to concatenate following dictionaries to create a new one.
it_company ={
               "c++" :10000,
               "python":30000,
               "java":40000,
}

university={
        
        "b.com":18000,
        "bsc-it":24500,
        "mba":20000,
}

it_company.update(university)
print(it_company)