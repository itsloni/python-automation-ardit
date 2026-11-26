# So here we have to configure the API cause we have to tell google that we are the owner of the
# private google spread sheet. Hence the url for the spreadsheet is not enough
#So essentially google will have to give you an api key which you will then use to access the sheet to change,
# delete data, update, edit etc.

# To do this we need the 'gspread' library and then you get an api key from google.
#To get google api what you do is search for google api console, set up your google-drive API(already did that you only set it up once) AND THEN YOU ENABLE GOOGLE SPREADSHEET API.
import gspread

gc = gspread.service_account("secrets.json") # This line establishes a connection to that google sheet, and that '.service_account()' method accepts the "secrets.json" path so it sees ths info

spreadsheet = gc.open("Automating google-sheet with python") # This is to open the actual google spreadsheet that can have multiple worksheet Tabs

#So now you know that there can be multiple worksheets in a spreadsheet like the '2013' and the '2014' worksheet created at the bottom of the page. remember they are tabs those worksheets and you can create many tabs/worksheet in a single google spreadsheet.
# So one way to call the worksheet you want from that "Automating google-sheet with python" spreadsheet  is by INDEX as shown below:

#worksheet1 = spreadsheet.get_worksheet(0) #------------>>>>  # This first gives the index of the first worksheet and name
#data = worksheet1.get_all_records() #------------>>>>>>>  # So this with the method ".get_all_records()" prints the contents of the
                                                            # worksheet. It returns them in a list of dictionaries, such that each dictionary is a row from the
                                                            # spreadsheet having key, which is the header for the spreadsheet, and value which is the corresponding value of each header for that
                                                            # specific row each.
#data = worksheet1.get_all_values()   #------------>>>>>>>   # this method '.get_all_values()'  returns a list within a list like each list within the
                                                            # list contains a row from the worksheet. the first row in the worksheet is the header filed so that is the fist list and then the
                                                            # subsequent ros are then in their own list each
#data = worksheet1.get_all_cells()  #------------>>>>>>>      # This returns each cell of the worksheet like <Cell R1C1 'name'> the 'name' is just
                                                            # whatever data that's in the specific cell and it does it from left to right before it moves to the
                                                            # next row of cells. NOTE: R1C1 means Row1 Column1

#print(data[10]) #used to extract the 10th when ".get_all_records" row since it's a list of dictionaries


# NOTE: There're are actually better way to extract rows and columns from the worksheet.

#NOW IF YOU WANT TO GET A WORKSHEET BY NAME (LIKE THE '2013' AND '2014' WORKSHEET IN THE 'Automating google-sheet with python' GOOGLE SPREADSHEET) AND NOT INDEX, YOU MUST DO THE FOLLOWING BELOW:

worksheet1 = spreadsheet.worksheet('2013') # Here you input the name of the work sheet "2013" and it gives th same output as the ".get_worksheet(0)" method.
# data = worksheet1.get_all_records()
# print(data)

#To select a specific  cell faster you cn do
#data = worksheet1.get_values("A4:F7") # This is to get row or rows

#column = worksheet1.get_values("B1:B24") # The difference here is the fact you are calling the columns but it is not the most efficient. The easiest is using the '.col_values()' method specific to
# column so that the output will not be a nested list unlike the former and the '.col_values()' method accepts the index of the row instead.
# And the good thing is that you can also use the '.row_values()' to get the specific row you want.

# column = worksheet1.col_values(2)[1:] # I added the square brackets to slice the list so note it can be manipulated.
# row = worksheet1.row_values(1)
# print(column)
# print(row)

# With those methods above you know that there are way you can get just a single cell likes;
# data = worksheet1.get_values("D4") # THIS GIVE YOU THE EXACT D4 cell but remember it's a list withing a list [[]]. so to get the actual value you must
# data = worksheet1.get_values("D4")[0][0]  # This gives the actual value inside D4 cell.

#BUT A BETTER APPROACH TO GETTING CELLS IS USING THE .acell() method as shown below:
# cell = worksheet1.acell("D4").value #This gives the D4 value directly without it being in a list of lists like [[]]
#
# #You can also search using '.find()' method for a particular cell  like a value inside a cell so you know the cell it's in. what you do is:
# cell2 = worksheet1.find("-10") # So in this case i am looking for the exact cell that contains the value '-10'
#
# # To get the coordinate of the cell2 u can do :
# print(cell2.row, cell2.col)
#
# #If you wanna find the all the cells that have a specific value you use the method '.findall()' like below:
# cell3 = worksheet1.findall("-9")
# print(cell3) # This then gives you a list of  where they are.


# NOW WHAT IF YOU WANT TO SEARCH TO MATCH PARTIAL STRING WHERE You only know some part of the value so u want to find all cells that contain that part of the value.
#You have to use REGULAR EXPRESSION library which is 're'.
import re

reg = re.compile(r'99')
cell3 = worksheet1.findall(reg)

for cell in cell3:
    print(cell.row, cell.col)

# HOW TO UPDATE A CELL IN A GOOGLE SPREADSHEET THERE ARE 2 WAYS TO DO THIS
#The first way is below:

worksheet1.update([[-400]], "E4") # So the 'E4' is the value you want to change and the '-400' is what's replacing it.

# You can also just update a single cell by using .update_acel() as shown below:
worksheet1.update_acell("E7", -390)

worksheet1.update_cell(4, 4, -900) # SAME WAY TO UPDATE A CELL THIS TIME USING TEH ROW, COLUM NUMBERS


# BELOW SHOWS HOW TO UPDATE AND ADD A COLUMN
existing_column = worksheet1.get_values("E2:E25")
new_column = [[round((float(i[0]) * 9/5 + 32), 1)] for i in existing_column]
worksheet1.update([["Fahrenheit"]] + new_column,"G1:G25")
print(new_column)




















