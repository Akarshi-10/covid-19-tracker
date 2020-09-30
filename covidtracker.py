from covid import Covid # from covid libarary import covid function
import matplotlib.pyplot as plt # beacuse I dont want to write the long one . so I replaced it with plt


covid = Covid() # saved covid function in a covid variable
name = input("Enter the country name :") # name varialbe stored input of country name


virusdata = covid.get_status_by_country_name(name)# virusdata by covid libarary , get_status_by_country_name(name) is a method

remove =['id','country','latitude', 'longitude', 'last_update'] # removed these 5 datas as we dont want them , only wanted active , recovered and dead
for i in remove:
    virusdata.pop(i)
    
all = virusdata.pop('confirmed') #to make visulation more perferctook comfirmed cases as all

id = list(virusdata.keys()) # this is id list
value = [str(i) for i in virusdata.values()] # this is value list as both are dictionaries so key value pair

plt.pie(value, labels=id, colors = ['r','y','g','b'], autopct='%1.1f%%') # method to create a pie chart autopct is used for %
plt.title('COUNTRY : ' +name.upper() +'\n TOTAL CASES : '+ str(all)) #title for the window
plt.legend() # function to understand what colour depicts what
plt.show() # to show the tracker
