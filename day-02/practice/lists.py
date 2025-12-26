clouds = list()
print(type(clouds))
clouds.append("Azure")
clouds.append("AWS")
clouds.append("GCP")
clouds.append("IBM")
clouds.append("Oracle")
print(clouds)

print("The length of the clouds list is :", len(clouds))
print("The first cloud in the list is : ", clouds[0])
print("The last cloud in the list is : ", clouds[-1])
print("The clouds from index 1 to 3 are : ", clouds[1:4])
print("The clouds from start to index 2 are : ", clouds[:3])
print("The clouds from index 2 to end are : ", clouds[2:])

clouds.remove("IBM")
print("The clouds list after removing IBM is : ", clouds)

clouds.append("DigitalOcean")
for search_cloud in clouds:
    if search_cloud == "GCP":
        print(f"{search_cloud} found in the list!")
    elif search_cloud == "AWS":
        print(f"{search_cloud} found in the list!")
    elif search_cloud == "Azure":
        print(f"{search_cloud} found in the list!")
    elif search_cloud == "Oracle":
        print(f"{search_cloud} found in the list!")
    else:
        print("Cloud Provider not found: ", f"{search_cloud}")
        print("End of the program")