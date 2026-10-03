---@diagnostic disable: missing-return
local simUI={}
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addCurve
--- Adds a curve to a plot widget.
---@param handle string
---@param id integer
---@param type integer
---@param name string
---@param color integer[]
---@param style integer
---@param options curve_options
function simUI.addCurve(handle,id,type,name,color,style,options) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addCurveTimePoints
--- Adds time points to the specified curve of the plot widget.
---@param handle string
---@param id integer
---@param name string
---@param x number[]
---@param y number[]
function simUI.addCurveTimePoints(handle,id,name,x,y) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addCurveXYPoints
--- Adds points to the specified curve of the plot widget.
---@param handle string
---@param id integer
---@param name string
---@param t number[]
---@param x number[]
---@param y number[]
function simUI.addCurveXYPoints(handle,id,name,t,x,y) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addScene3DNode
--- Add a node in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param parentNodeId integer
---@param type integer
function simUI.addScene3DNode(handle,id,nodeId,parentNodeId,type) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addTreeItem
--- Add an item to the specified tree widget.
---@param handle string
---@param id integer
---@param item_id integer
---@param text string[]
---@param parent_id integer
---@param expanded boolean
---@param suppressEvents boolean
function simUI.addTreeItem(handle,id,item_id,text,parent_id,expanded,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#adjustSize
--- Adjusts the size of the window to fit its contents.
---@param handle string
function simUI.adjustSize(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#appendText
--- Append text in a text-browser widget.
---@param handle string
---@param id integer
---@param text string
---@param suppressEvents boolean
function simUI.appendText(handle,id,text,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#bannerCreate
--- 
---@param text string
---@param btnKeys string[]
---@param btnLabels string[]
---@param callback string
---@return integer id
function simUI.bannerCreate(text,btnKeys,btnLabels,callback) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#bannerDestroy
--- 
---@param id integer
function simUI.bannerDestroy(id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#clearCurve
--- Clear points of the specified curve of the plot widget.
---@param handle string
---@param id integer
---@param name string
function simUI.clearCurve(handle,id,name) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#clearTable
--- Clear the specified table widget.
---@param handle string
---@param id integer
---@param suppressEvents boolean
function simUI.clearTable(handle,id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#clearTree
--- Clear the specified tree widget.
---@param handle string
---@param id integer
---@param suppressEvents boolean
function simUI.clearTree(handle,id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#collapseAll
--- Collapse all nodes in the specified tree widget.
---@param handle string
---@param id integer
---@param suppressEvents boolean
function simUI.collapseAll(handle,id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#colorDialog
--- Display a color dialog.
---@param title string
---@param showAlphaChannel boolean
---@param native boolean
---@return number[] result
function simUI.colorDialog(title,showAlphaChannel,native) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#create
--- Create a window.
---@param xml string
---@return string uiHandle
function simUI.create(xml) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#destroy
--- Destroy a window.
---@param handle string
function simUI.destroy(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#expandAll
--- Expand all nodes in the specified tree widget.
---@param handle string
---@param id integer
---@param suppressEvents boolean
function simUI.expandAll(handle,id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#expandToDepth
--- Expand nodes up to a certain depth in the specified tree widget.
---@param handle string
---@param id integer
---@param depth integer
---@param suppressEvents boolean
function simUI.expandToDepth(handle,id,depth,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#fileDialog
--- Display a file dialog.
---@param type integer
---@param title string
---@param startPath string
---@param initName string
---@param extName string
---@param ext string
---@param native boolean
---@return string[] result
function simUI.fileDialog(type,title,startPath,initName,extName,ext,native) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCheckboxValue
--- Get the value of a checkbox widget.
---@param handle string
---@param id integer
---@return integer value
function simUI.getCheckboxValue(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getColumnCount
--- Get the number of columns in the specified table/tree widget.
---@param handle string
---@param id integer
---@return integer count
function simUI.getColumnCount(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxItemCount
--- Get the number of items in the specified combobox widget.
---@param handle string
---@param id integer
---@return integer count
function simUI.getComboboxItemCount(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxItemText
--- Get the text of an item in a combobox widget.
---@param handle string
---@param id integer
---@param index integer
---@return string text
function simUI.getComboboxItemText(handle,id,index) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxItems
--- Get the content of a combobox.
---@param handle string
---@param id integer
---@return string[] items
function simUI.getComboboxItems(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxSelectedIndex
--- Get the selected item index in a combobox widget.
---@param handle string
---@param id integer
---@return integer index
function simUI.getComboboxSelectedIndex(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCurrentEditWidget
--- Get the edit widget with focus and selected text.
---@param handle string
---@return integer id
function simUI.getCurrentEditWidget(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCurrentTab
--- Get the current tab index of a tabs widget.
---@param handle string
---@param id integer
---@return integer index
function simUI.getCurrentTab(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCurveData
--- Get the data contained in the specified curve.
---@param handle string
---@param id integer
---@param name string
---@return number[] t
---@return number[] x
---@return number[] y
function simUI.getCurveData(handle,id,name) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getEditValue
--- Get the value of a edit widget.
---@param handle string
---@param id integer
---@return string value
function simUI.getEditValue(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getItem
--- Get the table widget item text.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
---@return string text
function simUI.getItem(handle,id,row,column) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getKeyboardModifiers
--- returns the current state of the modifier keys on the keyboard
---@return keyboard_modifiers m
function simUI.getKeyboardModifiers() end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getLabelText
--- Get the text of a label widget.
---@param handle string
---@param id integer
---@return string text
function simUI.getLabelText(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getPosition
--- Get the position of a UI window.
---@param handle string
---@return integer x
---@return integer y
function simUI.getPosition(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getPropertiesState
--- 
---@param handle string
---@param id integer
---@return string state
function simUI.getPropertiesState(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getRadiobuttonValue
--- Get the value of a radiobutton widget.
---@param handle string
---@param id integer
---@return integer value
function simUI.getRadiobuttonValue(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getRowCount
--- Get the table widget number of rows.
---@param handle string
---@param id integer
---@return integer count
function simUI.getRowCount(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getSize
--- Get the size of a UI window.
---@param handle string
---@return integer w
---@return integer h
function simUI.getSize(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getSliderValue
--- Get the value of a slider widget.
---@param handle string
---@param id integer
---@return integer value
function simUI.getSliderValue(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getSpinboxValue
--- Get the value of a spinbox widget.
---@param handle string
---@param id integer
---@return number value
function simUI.getSpinboxValue(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getTitle
--- Get the title of a UI window.
---@param handle string
---@return string title
function simUI.getTitle(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getWidgetVisibility
--- Get the visibility status of a widget.
---@param handle string
---@param id integer
---@return boolean visibility
function simUI.getWidgetVisibility(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#growPlotRanges
--- Increase the ranges of the plot widget by a fixed amount.
---@param handle string
---@param id integer
---@param xmin number
---@param xmax number
---@param ymin number
---@param ymax number
function simUI.growPlotRanges(handle,id,xmin,xmax,ymin,ymax) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#growPlotXRange
--- Increase the X range of the plot widget.
---@param handle string
---@param id integer
---@param xmin number
---@param xmax number
function simUI.growPlotXRange(handle,id,xmin,xmax) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#growPlotYRange
--- Increase the Y range of the plot widget.
---@param handle string
---@param id integer
---@param ymin number
---@param ymax number
function simUI.growPlotYRange(handle,id,ymin,ymax) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#hide
--- Hide the UI window.
---@param handle string
function simUI.hide(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#inputDialog
--- Display an input dialog.
---@param initValue string
---@param label string
---@param title string
---@return string result
function simUI.inputDialog(initValue,label,title) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#insertComboboxItem
--- Insert an item in a combobox widget.
---@param handle string
---@param id integer
---@param index integer
---@param text string
---@param suppressEvents boolean
function simUI.insertComboboxItem(handle,id,index,text,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#insertTableColumn
--- insert a column in a table widget
---@param ui integer
---@param widget integer
---@param index integer
function simUI.insertTableColumn(ui,widget,index) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#insertTableRow
--- insert a row in a table widget
---@param ui integer
---@param widget integer
---@param index integer
function simUI.insertTableRow(ui,widget,index) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#isVisible
--- Check if the window is visible.
---@param handle string
---@return boolean visibility
function simUI.isVisible(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#msgBox
--- Display a message box.
---@param type integer
---@param buttons integer
---@param title string
---@param message string
---@return integer result
function simUI.msgBox(type,buttons,title,message) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#qtVersion
--- Returns the version of the Qt library.
---@return integer[] version
function simUI.qtVersion() end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeComboboxItem
--- Remove an item from a combobox widget.
---@param handle string
---@param id integer
---@param index integer
---@param suppressEvents boolean
function simUI.removeComboboxItem(handle,id,index,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeCurve
--- Remove the specified curve from the plot widget.
---@param handle string
---@param id integer
---@param name string
function simUI.removeCurve(handle,id,name) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeScene3DNode
--- Remove a node in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
function simUI.removeScene3DNode(handle,id,nodeId) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeTableColumn
--- remove a column from a table widget
---@param ui integer
---@param widget integer
---@param index integer
function simUI.removeTableColumn(ui,widget,index) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeTableRow
--- remove a row from a table widget
---@param ui integer
---@param widget integer
---@param index integer
function simUI.removeTableRow(ui,widget,index) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeTreeItem
--- Remove an item from the specified tree widget.
---@param handle string
---@param id integer
---@param item_id integer
---@param suppressEvents boolean
function simUI.removeTreeItem(handle,id,item_id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#replot
--- Refresh all the plots of a plot widget.
---@param handle string
---@param id integer
function simUI.replot(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#rescaleAxes
--- Rescales the axes such that the specified curve in the plot is fully visible.
---@param handle string
---@param id integer
---@param name string
---@param onlyEnlargeX boolean
---@param onlyEnlargeY boolean
function simUI.rescaleAxes(handle,id,name,onlyEnlargeX,onlyEnlargeY) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#rescaleAxesAll
--- Rescales the axes such that all curves in the plot are fully visible.
---@param handle string
---@param id integer
---@param onlyEnlargeX boolean
---@param onlyEnlargeY boolean
function simUI.rescaleAxesAll(handle,id,onlyEnlargeX,onlyEnlargeY) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#restoreState
--- Restore a previously saved header state of the specified table/tree widget.
---@param handle string
---@param id integer
---@param state string
function simUI.restoreState(handle,id,state) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#saveState
--- Save header state of the specified table/tree widget.
---@param handle string
---@param id integer
---@return string state
function simUI.saveState(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setButtonPressed
--- Set the state of a button.
---@param handle string
---@param id integer
---@param pressed boolean
function simUI.setButtonPressed(handle,id,pressed) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setButtonText
--- Set the text of a button.
---@param handle string
---@param id integer
---@param text string
function simUI.setButtonText(handle,id,text) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setCheckboxValue
--- Set the value of a checkbox widget.
---@param handle string
---@param id integer
---@param value integer
---@param suppressEvents boolean
function simUI.setCheckboxValue(handle,id,value,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setClipboardText
--- Set the content of the clipboard to the specified text.
---@param text string
function simUI.setClipboardText(text) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setColumnCount
--- Resize the specified table/tree widget.
---@param handle string
---@param id integer
---@param count integer
---@param suppressEvents boolean
function simUI.setColumnCount(handle,id,count,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setColumnHeaderText
--- Set the column header text of the specified table/tree widget.
---@param handle string
---@param id integer
---@param column integer
---@param text string
function simUI.setColumnHeaderText(handle,id,column,text) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setColumnWidth
--- Resize a column in the specified table/tree widget.
---@param handle string
---@param id integer
---@param column integer
---@param min_size integer
---@param max_size integer
function simUI.setColumnWidth(handle,id,column,min_size,max_size) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setComboboxItems
--- Populate a combobox widget with the specified items, and set the selected item to the specified index.
---@param handle string
---@param id integer
---@param items string[]
---@param index integer
---@param suppressEvents boolean
function simUI.setComboboxItems(handle,id,items,index,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setComboboxSelectedIndex
--- Change the selected item index in a combobox widget.
---@param handle string
---@param id integer
---@param index integer
---@param suppressEvents boolean
function simUI.setComboboxSelectedIndex(handle,id,index,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setCurrentEditWidget
--- Set the edit widget focus and selected text.
---@param handle string
---@param id integer
function simUI.setCurrentEditWidget(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setCurrentTab
--- Set the current tab index in a tabs widget.
---@param handle string
---@param id integer
---@param index integer
---@param suppressEvents boolean
function simUI.setCurrentTab(handle,id,index,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setEditValue
--- Set the value of a edit widget.
---@param handle string
---@param id integer
---@param value string
---@param suppressEvents boolean
function simUI.setEditValue(handle,id,value,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setEnabled
--- Enable or disable a widget.
---@param handle string
---@param id integer
---@param enabled boolean
---@param suppressEvents boolean
function simUI.setEnabled(handle,id,enabled,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setImageData
--- Set image content using specified bitmap (RGB888) data.
---@param handle string
---@param id integer
---@param data string
---@param width integer
---@param height integer
function simUI.setImageData(handle,id,data,width,height) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItem
--- Change item value in the specified table widget.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
---@param text string
---@param suppressEvents boolean
function simUI.setItem(handle,id,row,column,text,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItemEditable
--- Change item editable flag in the specified table widget.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
---@param editable boolean
function simUI.setItemEditable(handle,id,row,column,editable) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItemImage
--- Change item image in the specified table widget.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
---@param data string
---@param width integer
---@param height integer
---@param suppressEvents boolean
function simUI.setItemImage(handle,id,row,column,data,width,height,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItems
--- 
---@param handle string
---@param id integer
---@param data string
---@param suppressEvents boolean
function simUI.setItems(handle,id,data,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setLabelText
--- Set the text of a label widget.
---@param handle string
---@param id integer
---@param text string
---@param suppressEvents boolean
function simUI.setLabelText(handle,id,text,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setLegendVisibility
--- Set visibility of the plot legend (default is hidden).
---@param handle string
---@param id integer
---@param visible boolean
function simUI.setLegendVisibility(handle,id,visible) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setMouseOptions
--- Set plot widget options for interacting with mouse.
---@param handle string
---@param id integer
---@param panX boolean
---@param panY boolean
---@param zoomX boolean
---@param zoomY boolean
function simUI.setMouseOptions(handle,id,panX,panY,zoomX,zoomY) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotLabels
--- Set the labels of the plot widget.
---@param handle string
---@param id integer
---@param x string
---@param y string
function simUI.setPlotLabels(handle,id,x,y) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotRanges
--- Set the ranges of the plot widget.
---@param handle string
---@param id integer
---@param xmin number
---@param xmax number
---@param ymin number
---@param ymax number
function simUI.setPlotRanges(handle,id,xmin,xmax,ymin,ymax) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotXLabel
--- Set the X label of the plot widget.
---@param handle string
---@param id integer
---@param label string
function simUI.setPlotXLabel(handle,id,label) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotXRange
--- Set the X range of the plot widget.
---@param handle string
---@param id integer
---@param xmin number
---@param xmax number
function simUI.setPlotXRange(handle,id,xmin,xmax) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotYLabel
--- Set the Y label of the plot widget.
---@param handle string
---@param id integer
---@param label string
function simUI.setPlotYLabel(handle,id,label) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotYRange
--- Set the Y range of the plot widget.
---@param handle string
---@param id integer
---@param ymin number
---@param ymax number
function simUI.setPlotYRange(handle,id,ymin,ymax) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPosition
--- Set the position of a UI window.
---@param handle string
---@param x integer
---@param y integer
---@param suppressEvents boolean
function simUI.setPosition(handle,x,y,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setProgress
--- Chnge the value of a progressbar widget.
---@param handle string
---@param id integer
---@param value integer
function simUI.setProgress(handle,id,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setProperties
--- 
---@param handle string
---@param id integer
---@param pnames string[]
---@param ptypes string[]
---@param pvalues string[]
---@param pflags integer[]
---@param pdisplayk string[]
---@param pdisplayv string[]
---@param icons integer[]
---@param suppressEvents boolean
function simUI.setProperties(handle,id,pnames,ptypes,pvalues,pflags,pdisplayk,pdisplayv,icons,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesContextMenu
--- 
---@param handle string
---@param id integer
---@param keys string[]
---@param titles string[]
function simUI.setPropertiesContextMenu(handle,id,keys,titles) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesRows
--- 
---@param handle string
---@param id integer
---@param rows integer[]
---@param pnames string[]
---@param ptypes string[]
---@param pvalues string[]
---@param pflags integer[]
---@param pdisplayk string[]
---@param pdisplayv string[]
---@param icons integer[]
---@param suppressEvents boolean
function simUI.setPropertiesRows(handle,id,rows,pnames,ptypes,pvalues,pflags,pdisplayk,pdisplayv,icons,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesSelection
--- 
---@param handle string
---@param id integer
---@param row integer
---@param suppressEvents boolean
function simUI.setPropertiesSelection(handle,id,row,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesState
--- 
---@param handle string
---@param id integer
---@param state string
function simUI.setPropertiesState(handle,id,state) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRadiobuttonValue
--- Set the value of a radiobutton widget.
---@param handle string
---@param id integer
---@param value integer
---@param suppressEvents boolean
function simUI.setRadiobuttonValue(handle,id,value,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRowCount
--- Resize the specified table widget.
---@param handle string
---@param id integer
---@param count integer
---@param suppressEvents boolean
function simUI.setRowCount(handle,id,count,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRowHeaderText
--- Set the row header text of the specified table widget.
---@param handle string
---@param id integer
---@param row integer
---@param text string
function simUI.setRowHeaderText(handle,id,row,text) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRowHeight
--- Resize a row in the specified table widget.
---@param handle string
---@param id integer
---@param row integer
---@param min_size integer
---@param max_size integer
function simUI.setRowHeight(handle,id,row,min_size,max_size) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeEnabled
--- Enable or disable a node in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param enabled boolean
function simUI.setScene3DNodeEnabled(handle,id,nodeId,enabled) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeFloatParam
--- Set node float parameter in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param paramName string
---@param value number
function simUI.setScene3DNodeFloatParam(handle,id,nodeId,paramName,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeIntParam
--- Set node int parameter in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param paramName string
---@param value integer
function simUI.setScene3DNodeIntParam(handle,id,nodeId,paramName,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeParam
--- polymorphic version of the onSetScene3DNodeXXXParam() functions
---@param ui integer
---@param widget integer
---@param nodeId integer
---@param paramName string
---@param paramValue any
function simUI.setScene3DNodeParam(ui,widget,nodeId,paramName,paramValue) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeStringParam
--- Set node string parameter in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param paramName string
---@param value string
function simUI.setScene3DNodeStringParam(handle,id,nodeId,paramName,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeVector2Param
--- Set node vector2 parameter in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param paramName string
---@param x number
---@param y number
function simUI.setScene3DNodeVector2Param(handle,id,nodeId,paramName,x,y) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeVector3Param
--- Set node vector3 parameter in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param paramName string
---@param x number
---@param y number
---@param z number
function simUI.setScene3DNodeVector3Param(handle,id,nodeId,paramName,x,y,z) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeVector4Param
--- Set node vector4 parameter in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
---@param paramName string
---@param x number
---@param y number
---@param z number
---@param w number
function simUI.setScene3DNodeVector4Param(handle,id,nodeId,paramName,x,y,z,w) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setSize
--- Set the size of a UI window.
---@param handle string
---@param w integer
---@param h integer
---@param suppressEvents boolean
function simUI.setSize(handle,w,h,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setSliderValue
--- Set the value of a slider widget.
---@param handle string
---@param id integer
---@param value integer
---@param suppressEvents boolean
function simUI.setSliderValue(handle,id,value,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setSpinboxValue
--- Set the value of a spinbox widget.
---@param handle string
---@param id integer
---@param value number
---@param suppressEvents boolean
function simUI.setSpinboxValue(handle,id,value,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setStyleSheet
--- Set the stylesheet of a widget.
---@param handle string
---@param id integer
---@param styleSheet string
function simUI.setStyleSheet(handle,id,styleSheet) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setTableSelection
--- Set selection in a table widget.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
---@param suppressEvents boolean
function simUI.setTableSelection(handle,id,row,column,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setText
--- Set the text in a text-browser widget.
---@param handle string
---@param id integer
---@param text string
---@param suppressEvents boolean
function simUI.setText(handle,id,text,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setTitle
--- Set the title of a UI window.
---@param handle string
---@param title string
---@param suppressEvents boolean
function simUI.setTitle(handle,title,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setTreeSelection
--- Set selection in a tree widget.
---@param handle string
---@param id integer
---@param item_id integer
---@param suppressEvents boolean
function simUI.setTreeSelection(handle,id,item_id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setUrl
--- Load an url in a text-browser widget.
---@param handle string
---@param id integer
---@param url string
function simUI.setUrl(handle,id,url) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setWidgetVisibility
--- Hide or show a widget.
---@param handle string
---@param id integer
---@param visibility boolean
function simUI.setWidgetVisibility(handle,id,visibility) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setWindowEnabled
--- Enable or disable a UI window.
---@param handle string
---@param enabled boolean
---@param suppressEvents boolean
function simUI.setWindowEnabled(handle,enabled,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#show
--- Show the UI window.
---@param handle string
function simUI.show(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#supportedImageFormats
--- Return a list of supported image formats
---@param separator string
---@return string[] formatList
---@return string formatListStr
function simUI.supportedImageFormats(separator) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#svgLoadData
--- Load a SVG document in a SVG widget.
---@param handle string
---@param id integer
---@param data string
function simUI.svgLoadData(handle,id,data) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#svgLoadFile
--- Load a SVG file in a SVG widget.
---@param handle string
---@param id integer
---@param file string
function simUI.svgLoadFile(handle,id,file) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#updateTreeItemParent
--- Modify the parent of an existing item in the specified tree widget.
---@param handle string
---@param id integer
---@param item_id integer
---@param parent_id integer
---@param suppressEvents boolean
function simUI.updateTreeItemParent(handle,id,item_id,parent_id,suppressEvents) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#updateTreeItemText
--- Modify the text of an existing item in the specified tree widget.
---@param handle string
---@param id integer
---@param item_id integer
---@param text string[]
function simUI.updateTreeItemText(handle,id,item_id,text) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onclickCallback
--- Callback for button click event.
---@param handle string
---@param id integer
function simUI.onclickCallback(handle,id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onLinkActivatedCallback
--- Callback for when a link is clicked.
---@param handle string
---@param id integer
---@param link string
function simUI.onLinkActivatedCallback(handle,id,link) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onchangeIntCallback
--- Callback for widget change event.
---@param handle string
---@param id integer
---@param value integer
function simUI.onchangeIntCallback(handle,id,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onchangeDoubleCallback
--- Callback for widget change event.
---@param handle string
---@param id integer
---@param value number
function simUI.onchangeDoubleCallback(handle,id,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onchangeStringCallback
--- Callback for widget change event.
---@param handle string
---@param id integer
---@param value string
function simUI.onchangeStringCallback(handle,id,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#oneditingfinishedCallback
--- Callback for editing finished event.
---@param handle string
---@param id integer
---@param value string
function simUI.oneditingfinishedCallback(handle,id,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#oncloseCallback
--- Callback for window close event. It will be called when the user clicks the close button of the window. When an onclose callback is specified, the window will not close automatically when the user clicks the window close button.
---@param handle string
function simUI.oncloseCallback(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPlottableClickCallback
--- Callback for plot widget plottableClick event.
---@param handle string
---@param id integer
---@param curve string
---@param index integer
---@param x number
---@param y number
function simUI.onPlottableClickCallback(handle,id,curve,index,x,y) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onLegendClickCallback
--- Callback for plot widget legendClick event.
---@param handle string
---@param id integer
---@param curve string
function simUI.onLegendClickCallback(handle,id,curve) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onCellActivateCallback
--- Callback for table widget cellActivated event.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
---@param cellValue string
function simUI.onCellActivateCallback(handle,id,row,column,cellValue) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onTableSelectionChangeCallback
--- Callback for table widget selectionChanged event.
---@param handle string
---@param id integer
---@param row integer
---@param column integer
function simUI.onTableSelectionChangeCallback(handle,id,row,column) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesSelectionChangeCallback
--- 
---@param handle string
---@param id integer
---@param row integer
function simUI.onPropertiesSelectionChangeCallback(handle,id,row) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesDoubleClickCallback
--- 
---@param handle string
---@param id integer
---@param row integer
---@param col integer
function simUI.onPropertiesDoubleClickCallback(handle,id,row,col) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesContextMenuTriggeredCallback
--- 
---@param handle string
---@param id integer
---@param key string
function simUI.onPropertiesContextMenuTriggeredCallback(handle,id,key) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesPropertyEditCallback
--- 
---@param handle string
---@param id integer
---@param key string
---@param value string
function simUI.onPropertiesPropertyEditCallback(handle,id,key,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onTreeSelectionChangeCallback
--- Callback for tree widget selectionChanged event.
---@param handle string
---@param id integer
---@param item_id integer
function simUI.onTreeSelectionChangeCallback(handle,id,item_id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onMouseEventCallback
--- Callback for a mouse event.
---@param handle string
---@param id integer
---@param type integer
---@param mods keyboard_modifiers
---@param x integer
---@param y integer
function simUI.onMouseEventCallback(handle,id,type,mods,x,y) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onKeyPressCallback
--- Callback called when a key is pressed in a widget.
---@param handle string
---@param id integer
---@param key integer
---@param text string
function simUI.onKeyPressCallback(handle,id,key,text) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onScene3DObjectClickCallback
--- Callback called when an object is clicked in a scene3d widget.
---@param handle string
---@param id integer
---@param nodeId integer
function simUI.onScene3DObjectClickCallback(handle,id,nodeId) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onBannerButtonClickCallback
--- Callback for banner button click event.
---@param bannerId integer
---@param btnKey string
function simUI.onBannerButtonClickCallback(bannerId,btnKey) end
return simUI