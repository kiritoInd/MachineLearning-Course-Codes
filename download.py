!tar -czf C5w1a1.tar.xz *
file_data = !ls -l C5w1a1.tar.xz 
file_size = int(file_data.s.split()[4])
print(file_data)
if file_size > 50*1024*1024:
    !split -b 50m C5w1a1.tar.xz C5w1a1.tar.part.
    print("As the file size is > 50 MB, the file has been split into parts. Look for file names with *part* and download them individually.")
else:
    print("Your workspace has been saved into C5w1a1.tar.xz. You may download the same.")
#END