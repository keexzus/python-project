filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filenames in filenames:
    filenames = filenames.replace('.', '-', 1)
    print(filenames)
    print(filenames[0])
    # print(type(filenames))


    # //for real world use// 
    # file.rename(filenames)