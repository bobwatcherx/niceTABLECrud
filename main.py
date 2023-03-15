from nicegui import ui
selected_data = []
mydata = []

mytable = ui.aggrid({
	"columnDefs":[
		{'headerName':"Name","field":"name"},
		{'headerName':"Age","field":"age"},
	],
	"rowData":[],
	"rowSelection":"multiple"
	})


def addnewdata():
	# NOW APPEND TO mydata FROM YOU INPUT NAME AND AGE
	mydata.append({"name":add_name.value,"age":add_age.value})

	# NOW PUSH TO TABLE FROM mydaata
	# THIS SCRIPT ADD FROm mydata AND SORTED FROM A TO Z
	mytable.options['rowData'] = sorted(mydata,key=lambda data:data['name'])
	ui.notify("you success add data",color="green")
	# AND CLOSE THE DIALOG
	new_data_dialog.close()
	mytable.update()




# NOW CREATE DIALOG FOR INPUT NAME AND AGE
with ui.dialog() as new_data_dialog:
	with ui.card():
		add_name = ui.input(label="add name")
		add_age = ui.input(label="add age")
		ui.button("add new",on_click=addnewdata)

def opendata(e):
	# OPEN DIALOG FOR ADD NEW DATA TO TABLE
	new_data_dialog.open()


# REMOVE DATA
async def removedata():
	# NOW GET YOU SELECTED TABLE FROM YOU CLICK THE TABLE
	row = await mytable.get_selected_row()
	# AND REMOVE mydata
	mydata.remove(row)

	# AND NOTIFY DELETE
	ui.notify("delete",color="red")
	mytable.options['rowData'] = sorted(mydata,key=lambda data:data['name'])
	mytable.update()



def savedata():
	# AND NOW UPDATE DATA FROM YOU SELECT FROM TABLE
	for d in mydata:
		# IF NAME IN MYDATA == IN YOU SELECT
		# THEN CHANGE
		if d['name'] == selected_data['name']:
			mydata.remove(d)
			# SHOW NOTIF
			ui.notify("success edit ",color="blue")
			# AND CLOSE DIALOG
			dialogedit.close()

	mydata.append({"name":name_edit.value,"age":age_edit.value})
	# AND UPDATE THE TABLE
	mytable.options['rowData'] = sorted(mydata,key=lambda data:data['name'])
	mytable.update()





# NOW CREATE DIALOG  FOR EDIT NAME AND AGE
with ui.dialog() as dialogedit :
	with ui.card():
		name_edit = ui.input(label="name")
		age_edit = ui.input(label="age")
		ui.button("save data",on_click=savedata)


# EDIT DATA
async def editdata():
	# AND NOW CREATE VARIABLE selected_data FOR 
	# EDIT AND CALl selected_data variable FROM another FUNCTION
	global selected_data

	# AND GET YOU SELECTED FROM YOU CLICK SELECT TABLE
	selected_data = await mytable.get_selected_row()

	# AND IF NOT SELECTED DATA GIVE ALERT NO DATA SELECTED
	if selected_data == None:
		ui.notify("No data select Guys")
		return
	# AND SET NAME_EDIT AND AGE_EDIT FROM YOU SELECTED TABLE
	name_edit.value = selected_data['name']
	age_edit.value = selected_data['age']
	# AND OPEN DIALOG EDIT 
	dialogedit.open()


# CREATE ADD EDIT DELETE BUTTON
with ui.row():
	ui.button("add",on_click=lambda e:opendata(e))
	ui.button("Remove",on_click=removedata)
	ui.button("Edit",on_click=editdata)


ui.run()