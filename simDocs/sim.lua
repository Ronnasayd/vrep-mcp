---@diagnostic disable: missing-return
local sim={}
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointTargetPosition.htm
--- Sets the target linear/angular position of a joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum velocity, acceleration and jerk values. In dynamic and position/custom control mode, the controller is instructed about the desired position
---@param objectHandle integer
---@param targetPosition number
---@param motionParams number[]
function sim.setJointTargetPosition(objectHandle,targetPosition,motionParams) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleDynamics.htm
--- Handles the dynamics functionality in a scene
---@param deltaTime number
---@return integer result
function sim.handleDynamics(deltaTime) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckDistance.htm
--- Checks the minimum distance between two entities. The measurable flags of the entities are overridden if the entities are objects. If the entities are both the same collection (i.e. with the same collection handle), then same objects will not be checked against themselve
---@param entity1Handle integer
---@param entity2Handle integer
---@param threshold number
---@return integer result
---@return number[] distanceData
---@return integer[] objectHandlePair
function sim.checkDistance(entity1Handle,entity2Handle,threshold) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckCollisionEx.htm
--- Checks whether two entities are colliding, and will return all intersections between the two entities. The collidable flags of the entities are overridden if the entities are objects
---@param entity1Handle integer
---@param entity2Handle integer
---@return integer result
---@return number[] intersections
function sim.checkCollisionEx(entity1Handle,entity2Handle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckCollision.htm
--- Checks whether two entities are colliding. The collidable flags of the entities are overridden if the entities are objects. If the entities are both the same collection (i.e. with the same collection handle), then same objects will not be checked against themselve
---@param entity1Handle integer
---@param entity2Handle integer
---@return integer result
---@return integer[] collidingObjectHandles
function sim.checkCollision(entity1Handle,entity2Handle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleSandboxScript.htm
--- Lua only. Calls a specific function in the  sandbox . sim.handleSandboxScript should only be called from the  main script
---@param callType integer
function sim.handleSandboxScript(callType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleAddOnScripts.htm
--- Lua only. Calls a specific function in  add-ons . Should only be called from the  main script
---@param callType integer
---@return integer count
function sim.handleAddOnScripts(callType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleEmbeddedScripts.htm
--- Lua only. Calls a specific  system callback function  in  simulation scripts  and  customization scripts . Simulation- and customization scripts will be executed in a  precise order . This function should only be called from the  main script
---@param callType integer
---@return integer scriptCount
function sim.handleEmbeddedScripts(callType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleSimulationScripts.htm
--- Lua only. Calls a specific  system callback function  in  simulation scripts . Simulation scripts will be executed in a  precise order . This function should only be called from the  main script .
---@param callType integer
---@return integer scriptCount
function sim.handleSimulationScripts(callType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetReferencedHandlesTags.htm
--- Retrieves a list of all referenced handles tags
---@param objectHandle integer
---@return string[] tags
function sim.getReferencedHandlesTags(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetReferencedHandles.htm
--- Retrieves a list of custom handles, linking a given scene object to other scene objects
---@param objectHandle integer
---@param tag string
---@return integer[] referencedHandles
function sim.getReferencedHandles(objectHandle,tag) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetReferencedHandles.htm
--- Attaches a list of custom handles to a given scene object. Those custom handles are handles of other scene objects, that are linked to the given scene object (for whatever purpose). The advantage of storing references to other objects with this function is that CoppeliaSim will take care of correctly adjusting the references if needed: For instance, imagine  objectA  storing the handle of  objectB  via this function. If  objectB  is deleted, then the stored handle becomes -1. If  objectA  and  objectB  are duplicated at the same time, then the duplicate of  objectA  stores the handle of the duplicate of  objectB . Optionally, if  sim.handleflag_keeporiginal  is specified, then linking to original objects is guaranteed, e.g. in above example, after a duplication of  objectA , the duplicate of  objectA  will store the handle of the original  objectB  (if  objectB  still exists)
---@param objectHandle integer
---@param referencedHandles integer[]
---@param tag string
function sim.setReferencedHandles(objectHandle,referencedHandles,tag) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetCollectionObjects.htm
--- Retrieves the object handles that compose a  collection
---@param collectionHandle integer
---@return integer[] objectHandles
function sim.getCollectionObjects(collectionHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectsInTree.htm
--- Retrieves object handles in a given hierarchy tree
---@param treeBaseHandle integer
---@param objectType integer
---@param options integer
---@return integer[] objects
function sim.getObjectsInTree(treeBaseHandle,objectType,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjects.htm
--- Retrieves object handles. Use this in a loop where index starts at 0 and is incremented to get all object handles in the scene
---@param index integer
---@param objectType integer
---@return integer objectHandle
function sim.getObjects(index,objectType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simIsHandle.htm
--- Checks whether a general object handle is still valid. When a general object is destroyed (e.g. programmatically or via the user interface), then its related handle is not valid anymore and will trigger an error when used. Use this function to avoid triggering an error
---@param objectHandle integer
---@return boolean result
function sim.isHandle(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCancelScheduledExecution.htm
--- Cancels a scheduled execution of a function
---@param id integer
---@return boolean canceled
function sim.cancelScheduledExecution(id) end
--- url:https://manual.coppeliarobotics.com/en/sim/simScheduleExecution.htm
--- Schedules execution of a function
---@param f function
---@param args any[]
---@param timePoint number
---@param simTime boolean
---@return integer id
function sim.scheduleExecution(f,args,timePoint,simTime) end
--- url:https://manual.coppeliarobotics.com/en/sim/simModuleEntry.htm
--- Creates, modifies or destroys module menu entries. Those are user selectable items located in [Menu bar > Modules]. When selected, the corresponding script will have its  sysCall_moduleEntry  callback function triggered, or  sim_message_eventcallback_moduleentry  triggered
---@param handle integer
---@param label string
---@param state integer
---@return integer handle
function sim.moduleEntry(handle,label,state) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetUserVariables.htm
--- Lua only. Returns all variables, except those set by CoppeliaSim.
---@return string[] variables
function sim.getUserVariables() end
--- url:https://manual.coppeliarobotics.com/en/sim/simQuitSimulator.htm
--- Triggers a quit signal after which the application eventually ends

function sim.quitSimulator() end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetExplicitHandling.htm
--- Sets the explicit handling flags for a scene object
---@param objectHandle integer
---@param explicitFlags integer
function sim.setExplicitHandling(objectHandle,explicitFlags) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetExplicitHandling.htm
--- Retrieves the explicit handling flags for a scene object
---@param objectHandle integer
---@return integer explicitHandlingFlags
function sim.getExplicitHandling(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRefreshDialogs.htm
--- Refreshes CoppeliaSim's internal dialogs. Calling  sim.refreshDialogs  will not trigger a  sim.message_eventcallback_refreshdialogs  message
---@param refreshDegree integer
function sim.refreshDialogs(refreshDegree) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetSystemTime.htm
--- Retrieves the system time.
---@return number systemTime
function sim.getSystemTime() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPluginInfo.htm
--- Returns auxiliary information about a loaded plugin
---@param pluginName string
---@param infoType integer
---@return integer info
function sim.getPluginInfo(pluginName,infoType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPluginName.htm
--- Retrieves a plugin name based on an index
---@param index integer
---@return string pluginName
function sim.getPluginName(index) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetLastInfo.htm
--- Retrieves and clears the information string generated by last API call
---@return string info
function sim.getLastInfo() end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetPage.htm
--- Switches between pages (main scene views)
---@param index integer
function sim.setPage(index) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPage.htm
--- Retrieves the current page index (view)
---@return integer pageIndex
function sim.getPage() end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetNavigationMode.htm
--- Sets the navigation and selection mode for the mouse
---@param navigationMode integer
function sim.setNavigationMode(navigationMode) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetNavigationMode.htm
--- Retrieves the navigation and selection mode for the mouse
---@return integer navigationMode
function sim.getNavigationMode() end
--- url:https://manual.coppeliarobotics.com/en/sim/simAnnounceSceneContentChange.htm
--- Announces a change in the scene. This is required for the undo/redo function to operate properly when performing changes via the API. Only call this function directly after a change was made through a dialog element (e.g. a checkbox was checked/unchecked) and that change was reported to the scene. What this call will do is following: the whole scene will be serialized (saved) to memory as a "scene image" and compared to a previously memorized "scene image". If both images are same, then the last image is discarded, otherwise only the changes between the two images are memorized. A call to this function has no effect (and doesn't generate any error) when called during simulation or when in edit mode.
---@return integer result
function sim.announceSceneContentChange() end
--- url:https://manual.coppeliarobotics.com/en/sim/simTransformBuffer.htm
--- Modifies a buffer than contains packed data
---@param inBuffer string
---@param inFormat integer
---@param mult number
---@param off number
---@param outFormat integer
---@return string outBuff
function sim.transformBuffer(inBuffer,inFormat,mult,off,outFormat) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCopyTable.htm
--- Lua only. Duplicates a table, i.e. makes a deep copy
---@param original table
---@return table copy
function sim.copyTable(original) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackDoubleTable.htm
--- Unpacks a string (or part of it) into an array of double floating-point numbers
---@param data string
---@param startDoubleIndex integer
---@param doubleCount integer
---@param additionalByteOffset integer
---@return number[] doubleNumbers
function sim.unpackDoubleTable(data,startDoubleIndex,doubleCount,additionalByteOffset) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackDoubleTable.htm
--- Packs ab array of double floating-point numbers into a string
---@param doubleNumbers number[]
---@param startDoubleIndex integer
---@param doubleCount integer
---@return string data
function sim.packDoubleTable(doubleNumbers,startDoubleIndex,doubleCount) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackFloatTable.htm
--- Unpacks a string (or part of it) into an array of floating-point numbers
---@param data string
---@param startFloatIndex integer
---@param floatCount integer
---@param additionalByteOffset integer
---@return number[] floatingNumbers
function sim.unpackFloatTable(data,startFloatIndex,floatCount,additionalByteOffset) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackFloatTable.htm
--- Packs an array of floating-point numbers into a string
---@param floatingNumbers number[]
---@param startFloatIndex integer
---@param floatCount integer
---@return string data
function sim.packFloatTable(floatingNumbers,startFloatIndex,floatCount) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackInt32Table.htm
--- Unpacks a string (or part of it) into an array of int32 numbers
---@param data string
---@param startInt32Index integer
---@param int32Count integer
---@param additionalByteOffset integer
---@return integer[] int32Numbers
function sim.unpackInt32Table(data,startInt32Index,int32Count,additionalByteOffset) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackInt32Table.htm
--- Packs an array of int32 numbers into a string
---@param int32Numbers integer[]
---@param startInt32Index integer
---@param int32Count integer
---@return string data
function sim.packInt32Table(int32Numbers,startInt32Index,int32Count) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackUInt32Table.htm
--- Unpacks a string (or part of it) into an array of uint32 numbers
---@param data string
---@param startUint32Index integer
---@param uint32Count integer
---@param additionalByteOffset integer
---@return integer[] uint32Numbers
function sim.unpackUInt32Table(data,startUint32Index,uint32Count,additionalByteOffset) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackUInt32Table.htm
--- Packs an array of uint32 numbers into a string
---@param uint32Numbers integer[]
---@param startUint32Index integer
---@param uint32Count integer
---@return string data
function sim.packUInt32Table(uint32Numbers,startUint32Index,uint32Count) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackUInt16Table.htm
--- Unpacks a string (or part of it) into an array of uint16 numbers
---@param data string
---@param starUint16Index integer
---@param uint16Count integer
---@param additionalByteOffset integer
---@return integer[] uint16Numbers
function sim.unpackUInt16Table(data,starUint16Index,uint16Count,additionalByteOffset) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackUInt16Table.htm
--- Packs an array of uint16 numbers into a string
---@param uint16Numbers integer[]
---@param startUint16Index integer
---@param uint16Count integer
---@return string data
function sim.packUInt16Table(uint16Numbers,startUint16Index,uint16Count) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackUInt8Table.htm
--- Unpacks a string (or part of it) into an array of uint8 numbers
---@param data string
---@param startUint8Index integer
---@param uint8Count integer
---@return integer[] uint8Numbers
function sim.unpackUInt8Table(data,startUint8Index,uint8Count) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackUInt8Table.htm
--- Packs an array of uint8 numbers into a string
---@param uint8Numbers integer[]
---@param startUint8Index integer
---@param uint8count integer
---@return string data
function sim.packUInt8Table(uint8Numbers,startUint8Index,uint8count) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUnpackTable.htm
--- Unpacks a buffer into a table
---@param buffer string
---@return table aTable
function sim.unpackTable(buffer) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPackTable.htm
--- Packs a table into a buffer. The table may contain other nested arrays, maps, None/nil, bool, number or string values. All other types (e.g. functions) will be considered as string or None/nil values. You can also use sim.packTable to quickly compare two tables or to perform a deep copy of a table
---@param aTable table
---@param packingScheme integer
---@return string buffer
function sim.packTable(aTable,packingScheme) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRuckigRemove.htm
--- Removes an object previously created via  sim.ruckigPos  or  sim.ruckigVel .
---@param handle integer
function sim.ruckigRemove(handle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRuckigVel.htm
--- Executes a call to the  Ruckig online trajectory generator . The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a velocity-based trajectory generation object, that can then be calculated with  sim.ruckigStep . When this object is not needed anymore, remove it with  sim.ruckigRemove
---@param dofs integer
---@param baseCycleTime number
---@param flags integer
---@param currentPosVelAccel number[]
---@param maxAccelJerk number[]
---@param selection integer[]
---@param targetVel number[]
---@return integer handle
function sim.ruckigVel(dofs,baseCycleTime,flags,currentPosVelAccel,maxAccelJerk,selection,targetVel) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRuckigPos.htm
--- Executes a call to the  Ruckig online trajectory generator . The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a position-based trajectory generation object, that can then be calculated with  sim.ruckigStep . When this object is not needed anymore, remove it with  sim.ruckigRemove
---@param dofs integer
---@param baseCycleTime number
---@param flags integer
---@param currentPosVelAccel number[]
---@param maxVelAccelJerk number[]
---@param selection integer[]
---@param targetPosVel number[]
---@return integer handle
function sim.ruckigPos(dofs,baseCycleTime,flags,currentPosVelAccel,maxVelAccelJerk,selection,targetPosVel) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose_cleanup.htm
--- Destroys a motion object
---@param motionObject table
function sim.moveToPose_cleanup(motionObject) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose_step.htm
--- Steps a motion object
---@param motionObject table
---@return integer res
---@return table data
function sim.moveToPose_step(motionObject) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose_init.htm
--- Initiates an object motion using the  Ruckig online trajectory generator , by performing interpolations between two poses. The function can operate by handling 4 motion variables (x,y,z and angle between the two poses), or a single movement variable (t, which requires a metric to be specified for distance calculation between the two poses)
---@param params table
---@return table motionObject
function sim.moveToPose_init(params) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_cleanup.htm
--- Destroys a motion object
---@param motionObject table
function sim.moveToConfig_cleanup(motionObject) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_step.htm
--- Steps a motion object
---@param motionObject table
---@return integer res
---@return table data
function sim.moveToConfig_step(motionObject) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_init.htm
--- Initiates a n-DoF motion using the  Ruckig online trajectory generator
---@param params table
---@return table motionObject
function sim.moveToConfig_init(params) end
--- url:https://manual.coppeliarobotics.com/en/sim/simFloatingViewRemove.htm
--- Removes a floating view previously added with  sim.floatingViewAdd .
---@param floatingViewHandle integer
---@return integer result
function sim.floatingViewRemove(floatingViewHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simFloatingViewAdd.htm
--- Adds a floating view to current page
---@param posX number
---@param posY number
---@param sizeX number
---@param sizeY number
---@param options integer
---@return integer floatingViewHandle
function sim.floatingViewAdd(posX,posY,sizeX,sizeY,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simTextEditorShow.htm
--- Shows or hides a text edition window previously opened with  sim.textEditorOpen
---@param handle integer
---@param showState boolean
function sim.textEditorShow(handle,showState) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRuckigStep.htm
--- Executes a call to the  Ruckig online trajectory generator . The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function steps forward a trajectory generation algorithm previously prepared via  sim.ruckigPos  or  sim.ruckigVel
---@param handle integer
---@param cycleTime number
---@return integer result
---@return number[] newPosVelAccel
---@return number synchronizationTime
function sim.ruckigStep(handle,cycleTime) end
--- url:https://manual.coppeliarobotics.com/en/sim/simTextEditorOpen.htm
--- Opens a text edition window
---@param initText string
---@param properties string
---@return integer handle
function sim.textEditorOpen(initText,properties) end
--- url:https://manual.coppeliarobotics.com/en/sim/simTextEditorGetInfo.htm
--- Retieves information from a text edition window previously opened with  sim.textEditorOpen
---@param handle integer
---@return string text
---@return integer[] pos
---@return integer[] size
---@return boolean visible
function sim.textEditorGetInfo(handle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simTextEditorClose.htm
--- Closes a text edition window previously opened with  sim.textEditorOpen
---@param handle integer
---@return string text
---@return integer[] pos
---@return integer[] size
function sim.textEditorClose(handle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleShow.htm
--- Shows or hides an auxiliary console window
---@param consoleHandle integer
---@param showState boolean
---@return integer result
function sim.auxiliaryConsoleShow(consoleHandle,showState) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose.htm
--- Executes an object motion using the  Ruckig online trajectory generator , by performing interpolations between two poses. The function can operate by handling 4 motion variables (x,y,z and angle between the two poses), or a single movement variable (t, which requires a metric to be specified for distance calculation between the two poses). This function can only be called from a script running in a thread, since this is a blocking operation
---@param params table
---@return table data
function sim.moveToPose(params) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig.htm
--- Executes a n-DoF motion using the  Ruckig online trajectory generator . This function can only be called from scripts running in a thread, since this is a blocking operation
---@param params table
---@return table data
function sim.moveToConfig(params) end
--- url:https://manual.coppeliarobotics.com/en/sim/simWait.htm
--- Waits for a certain amount of time
---@param deltaTime number
---@param simulationTime boolean
---@return number deltaTimeLeft
function sim.wait(deltaTime,simulationTime) end
--- url:https://manual.coppeliarobotics.com/en/sim/simWriteTexture.htm
--- Overwrites a specific texture (or a portion of it) with RGB data
---@param textureId integer
---@param options integer
---@param textureData string
---@param posX integer
---@param posY integer
---@param sizeX integer
---@param sizeY integer
---@param interpolation number
function sim.writeTexture(textureId,options,textureData,posX,posY,sizeX,sizeY,interpolation) end
--- url:https://manual.coppeliarobotics.com/en/sim/simTransformImage.htm
--- Transforms an image in various ways
---@param image string
---@param resolution integer[]
---@param options integer
---@return string newImage
function sim.transformImage(image,resolution,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetScaledImage.htm
--- Generates a scaled-up or scaled down version of the input image
---@param imageIn string
---@param resolutionIn integer[]
---@param desiredResolutionOut integer[]
---@param options integer
---@return string imageOut
---@return integer[] effectiveResolutionOut
function sim.getScaledImage(imageIn,resolutionIn,desiredResolutionOut,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simLoadImage.htm
--- Loads an image from file or memory
---@param options integer
---@param filenameOrBuffer string
---@return string image
---@return integer[] resolution
function sim.loadImage(options,filenameOrBuffer) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSaveImage.htm
--- Saves an image to file or to memory
---@param image string
---@param resolution integer[]
---@param options integer
---@param filename string
---@param quality integer
---@return string imgBuffer
function sim.saveImage(image,resolution,options,filename,quality) end
--- url:https://manual.coppeliarobotics.com/en/sim/simReadTexture.htm
--- Retrieves the RGB data (or a portion of it) related to a specific texture
---@param textureId integer
---@param options integer
---@param posX integer
---@param posY integer
---@param sizeX integer
---@param sizeY integer
---@return string textureData
function sim.readTexture(textureId,options,posX,posY,sizeX,sizeY) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetTextureId.htm
--- Retrieves the texture ID of a specific texture
---@param textureName string
---@return integer textureId
---@return integer[] resolution
function sim.getTextureId(textureName) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSystemSemaphore.htm
--- Acquires or releases a system-wide semaphore, i.e. across several CoppeliaSim instances
---@param key string
---@param acquire boolean
function sim.systemSemaphore(key,acquire) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPushUserEvent.htm
--- Pushes a user-triggered event. Messages are received asynchronously via the sysCall_event  callback function  and via the plugin  sim_message_eventcallback_events  message call
---@param event string
---@param handle integer
---@param uid integer
---@param eventData table
---@param options integer
function sim.pushUserEvent(event,handle,uid,eventData,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simBroadcastMsg.htm
--- Broadcasts a message to all scripts, except for the emitting script. Messages are received synchronously via the sysCall_msg  callback function
---@param message table
---@param options integer
function sim.broadcastMsg(message,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsolePrint.htm
--- Prints to an auxiliary console window
---@param consoleHandle integer
---@param text string
---@return integer result
function sim.auxiliaryConsolePrint(consoleHandle,text) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleOpen.htm
--- Opens an auxiliary console window for text display. This console window is different from the application main console window. Console window handles are shared across all simulator scenes
---@param title string
---@param maxLines integer
---@param mode integer
---@param position integer[]
---@param size integer[]
---@param textColor number[]
---@param backgroundColor number[]
---@return integer consoleHandle
function sim.auxiliaryConsoleOpen(title,maxLines,mode,position,size,textColor,backgroundColor) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleClose.htm
--- Closes an auxiliary console window
---@param consoleHandle integer
---@return integer result
function sim.auxiliaryConsoleClose(consoleHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetSimulatorMessage.htm
--- Retrieves and removes the next message in the C/C++ or Lua message queues. Use this in a while-loop until all messages have been extracted. While the C/C++ interface has one single message queue, each Lua script has its own message queue. The C/C++ version of this function should only be called from the CoppeliaSim client application. A given message queue cannot hold more than 64 messages, unread messages will be discarded.
---@return integer message
---@return integer[] auxiliaryData
---@return integer[] auxiliaryData2
function sim.getSimulatorMessage() end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddLog.htm
--- Adds a log message that will be output in the console or status bar
---@param verbosity integer
---@param message string
function sim.addLog(verbosity,message) end
--- url:https://manual.coppeliarobotics.com/en/sim/simYawPitchRollToAlphaBetaGamma.htm
--- Converts Yaw-Pitch-Roll angles to CoppeliaSim's alpha-beta-gamma angles
---@param yaw number
---@param pitch number
---@param roll number
---@return number alpha
---@return number beta
---@return number gamma
function sim.yawPitchRollToAlphaBetaGamma(yaw,pitch,roll) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAlphaBetaGammaToYawPitchRoll.htm
--- Converts CoppeliaSim's alpha-beta-gamma angles to Yaw-Pitch-Roll angles
---@param alpha number
---@param beta number
---@param gamma number
---@return number yaw
---@return number pitch
---@return number roll
function sim.alphaBetaGammaToYawPitchRoll(alpha,beta,gamma) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRotateAroundAxis.htm
--- Rotates a pose or transformation matrix around a random axis in space. This function, when used in combination with  sim.getRotationAxis , can be used to build interpolations between poses or transformation matrices
---@param axis number[]
---@param axisPos number[]
---@param angle number
function sim.rotateAroundAxis(axis,axisPos,angle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetRotationAxis.htm
--- Retrieves an axis and rotation angle that brings one pose or transformation matrix onto another one. The translation part of the poses/matrices is ignored. This function, when used in combination with  sim.rotateAroundAxis , can be used to build interpolations between transformation matrices
---@return number[] axis
---@return number angle
function sim.getRotationAxis() end
--- url:https://manual.coppeliarobotics.com/en/sim/simMultiplyVector.htm
--- Multiplies a vector with a quaternion, a pose, or a matrix (e.g. v = m * v)

function sim.multiplyVector() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPoseInverse.htm
--- Inverts a pose
---@param pose number[]
---@return number[] pose
function sim.getPoseInverse(pose) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetMatrixInverse.htm
--- Inverts a transformation matrix

function sim.getMatrixInverse() end
--- url:https://manual.coppeliarobotics.com/en/sim/simInterpolatePoses.htm
--- Computes the interpolated pose between poseIn1 and poseIn2
---@param poseIn1 number[]
---@param poseIn2 number[]
---@param interpolFactor number
---@return number[] resultPose
function sim.interpolatePoses(poseIn1,poseIn2,interpolFactor) end
--- url:https://manual.coppeliarobotics.com/en/sim/simInterpolateMatrices.htm
--- Computes the interpolated transformation matrix between matrixIn1 and matrixIn2. Quaternions are used internally
---@param interpolFactor number
function sim.interpolateMatrices(interpolFactor) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMultiplyPoses.htm
--- Multiplies two poses
---@param poseIn1 number[]
---@param poseIn2 number[]
---@return number[] resultPose
function sim.multiplyPoses(poseIn1,poseIn2) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMultiplyMatrices.htm
--- Multiplies two transformation matrices

function sim.multiplyMatrices() end
--- url:https://manual.coppeliarobotics.com/en/sim/simPoseToMatrix.htm
--- Converts a pose to a transformation matrix
---@param pose number[]
function sim.poseToMatrix(pose) end
--- url:https://manual.coppeliarobotics.com/en/sim/simMatrixToPose.htm
--- Converts a transformation matrix to a pose
---@return number[] pose
function sim.matrixToPose() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetEulerAnglesFromMatrix.htm
--- Retrieves the  Euler angles  from a transformation matrix
---@return number[] eulerAngles
function sim.getEulerAnglesFromMatrix() end
--- url:https://manual.coppeliarobotics.com/en/sim/simBuildPose.htm
--- Builds a pose based on a position vector and  Euler angles  or axes
---@param position number[]
---@param eulerAnglesOrAxis1 number[]
---@param mode integer
---@param axis2 number[]
---@return number[] pose
function sim.buildPose(position,eulerAnglesOrAxis1,mode,axis2) end
--- url:https://manual.coppeliarobotics.com/en/sim/simBuildMatrix.htm
--- Builds a transformation matrix based on a position vector and  Euler angles
---@param position number[]
---@param eulerAngles number[]
function sim.buildMatrix(position,eulerAngles) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleExtCalls.htm
--- Handles the message pump for threaded scripts

function sim.handleExtCalls() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetSimulationStopping.htm
--- Convenience function that returns true when the simulation is about to stop or stopped.
---@return boolean stopping
function sim.getSimulationStopping() end
--- url:https://manual.coppeliarobotics.com/en/sim/simReleaseLock.htm
--- Counterpart function to  sim.acquireLock . Unlocking is cumulative

function sim.releaseLock() end
--- url:https://manual.coppeliarobotics.com/en/sim/simAcquireLock.htm
--- Allows to have CoppeliaSim wait for a threaded code section to be executed without interruption. Locking is cumulative

function sim.acquireLock() end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetAutoYieldDelay.htm
--- Allows specifying a thread interruption or yield delay, that will be automatically enforced by the system (preemptive threading). By default this value is 2 ms
---@param dt number
function sim.setAutoYieldDelay(dt) end
--- url:https://manual.coppeliarobotics.com/en/sim/simStep.htm
--- Triggers the next simulation step, when in stepping operation mode. When simulation is running, then sim.step only returns once the simulation time has changed

function sim.step() end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetStepping.htm
--- Enables or disables the stepping operation mode for a threaded script. If enabled, then the current script has to trigger each simulation step explicitly, via  sim.step . Is applied cumulatively, i.e. if the stepping operation mode is enabled n times, it needs to be disabled n times to return to the initial state                 (Lua specific: in stepping operation mode, automatic thread interruptions, i.e. preemptive threading, is supressed)
---@param enable boolean
---@param desiredStepLevel integer
---@return integer prevStepLevel
function sim.setStepping(enable,desiredStepLevel) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetRealTimeSimulation.htm
--- Indicates whether the simulation is real-time
---@return integer result
function sim.getRealTimeSimulation() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetSimulationTimeStep.htm
--- Retrieves the simulation time step (the simulation time (i.e. not real-time) that passes at each main script simulation pass). This value might not be constant for a given simulation.
---@return number timeStep
function sim.getSimulationTimeStep() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetSimulationState.htm
--- Retrieves current  simulation state
---@return integer simulationState
function sim.getSimulationState() end
--- url:https://manual.coppeliarobotics.com/en/sim/simStopSimulation.htm
--- Requests a stop of the running simulation
---@param wait boolean
function sim.stopSimulation(wait) end
--- url:https://manual.coppeliarobotics.com/en/sim/simPauseSimulation.htm
--- Requests a pause of a simulation

function sim.pauseSimulation() end
--- url:https://manual.coppeliarobotics.com/en/sim/simStartSimulation.htm
--- Requests a start of a simulation (or a resume of a paused simulation)

function sim.startSimulation() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetGenesisEvents.htm
--- Retrieves all events that allow to reconstruct a scene's (mostly) visual content remotely
---@return string events
function sim.getGenesisEvents() end
--- url:https://manual.coppeliarobotics.com/en/sim/simRestoreEntityColor.htm
--- Restores the color of an  entity , previously modified with  sim.changeEntityColor
---@param originalColorData table[]
function sim.restoreEntityColor(originalColorData) end
--- url:https://manual.coppeliarobotics.com/en/sim/simChangeEntityColor.htm
--- Changes the color of an  entity , and returns its original color. Currently only takes into account  collections  and  shapes
---@param entityHandle integer
---@param newColor number[]
---@param colorComponent integer
---@return table[] originalColorData
function sim.changeEntityColor(entityHandle,newColor,colorComponent) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemoveDrawingObject.htm
--- Removes a previously added drawing object
---@param objectHandle integer
function sim.removeDrawingObject(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddDrawingObjectItem.htm
--- Adds an item (or clears all items) to a previously inserted drawing object
---@param drawingObjectHandle integer
---@param itemData number[]
---@return integer result
function sim.addDrawingObjectItem(drawingObjectHandle,itemData) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddDrawingObject.htm
--- Adds a drawing object that will be displayed in the scene. Drawing objects are containers that hold several items of a given type. This can be used for several different applications (simulation of paint, simulation of welding seam, display of 3D objects, etc.). Drawing objects created in a  simulation script  will be automatically removed at simulation end
---@param objectType integer
---@param size number
---@param duplicateTolerance number
---@param parentObjectHandle integer
---@param maxItemCount integer
---@param color number[]
---@return integer drawingObjectHandle
function sim.addDrawingObject(objectType,size,duplicateTolerance,parentObjectHandle,maxItemCount,color) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSerialSend.htm
--- Writes data to a previously opened serial port (RS-232)
---@param portHandle integer
---@param data string
---@return integer charsSent
function sim.serialSend(portHandle,data) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSerialRead.htm
--- Reads from a previously opened serial port (RS-232). The C version of the function cannot be blocking
---@param portHandle integer
---@param dataLengthToRead integer
---@param blockingOperation boolean
---@param closingString string
---@param timeout number
---@return string data
function sim.serialRead(portHandle,dataLengthToRead,blockingOperation,closingString,timeout) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSerialOpen.htm
--- Opens a serial port (RS-232) for communication. When called from a script, the function can only be called when the simulation is running (and in that case the port is automatically closed at simulation stop)
---@param portString string
---@param baudRate integer
---@return integer result
function sim.serialOpen(portString,baudRate) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSerialClose.htm
--- Closes a serial port (RS-232)
---@param portHandle integer
function sim.serialClose(portHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSerialCheck.htm
--- Reads how many bytes are waiting to be read on a serial port (RS-232)
---@param portHandle integer
---@return integer result
function sim.serialCheck(portHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddItemToCollection.htm
--- Adds an item to a  collection
---@param collectionHandle integer
---@param what integer
---@param objectHandle integer
---@param options integer
function sim.addItemToCollection(collectionHandle,what,objectHandle,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simDestroyCollection.htm
--- Removes a  collection
---@param collectionHandle integer
function sim.destroyCollection(collectionHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateCollection.htm
--- Creates a new  collection . A collection created in a  simulation script , a  customization script  or in the  main script  are automatically destroyed when the script ends
---@param options integer
---@return integer collectionHandle
function sim.createCollection(options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPropertiesInfos.htm
--- Convenience function to fetches all properties infos of a specific target item
---@param target integer
---@param options table
---@return table propertiesInfo
function sim.getPropertiesInfos(target,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetProperties.htm
--- Convenience function to set several properties at once
---@param target integer
---@param properties table
function sim.setProperties(target,properties) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetProperties.htm
--- Convenience function to fetches all properties of a specific target item
---@param target integer
---@param options table
---@return table properties
function sim.getProperties(target,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetProperty.htm
--- Convenience function to set a property
---@param target integer
---@param propertyName string
---@param propertyState any
---@param propertyType integer
function sim.setProperty(target,propertyName,propertyState,propertyType) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPropertyInfo.htm
--- Fetches information about a specific property
---@param target integer
---@param propertyName string
---@param options table
---@return integer type
---@return integer flags
---@return string description
function sim.getPropertyInfo(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPropertyName.htm
--- Fetches the name of a property, based on an index
---@param target integer
---@param index integer
---@param options table
---@return string propertyName
function sim.getPropertyName(target,index,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemoveProperty.htm
--- Removes a removable property
---@param target integer
---@param propertyName string
---@param options table
function sim.removeProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetColorProperty.htm
--- Fetches a color property (float[3])
---@param target integer
---@param propertyName string
---@param options table
---@return number[] propertyState
function sim.getColorProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetColorProperty.htm
--- Sets a color property (float[3])
---@param target integer
---@param propertyName string
---@param propertyState number[]
---@param options table
function sim.setColorProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPoseProperty.htm
--- Fetches a pose property (double[7]: x, y, z, qx, qy, qz, qw)
---@param target integer
---@param propertyName string
---@param options table
---@return number[] propertyState
function sim.getPoseProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetPoseProperty.htm
--- Sets a pose property (double[7]: x, y, z, qx, qy, qz, qw)
---@param target integer
---@param propertyName string
---@param propertyState number[]
---@param options table
function sim.setPoseProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetProperty.htm
--- Convenience functon to fetch a property
---@param target integer
---@param propertyName string
---@param options table
---@return any propertyState
function sim.getProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetQuaternionProperty.htm
--- Fetches a quaternion property (double[4]: qx, qy, qz, qw)
---@param target integer
---@param propertyName string
---@param options table
---@return number[] propertyState
function sim.getQuaternionProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetQuaternionProperty.htm
--- Sets a quaternion property (double[4]: qx, qy, qz, qw)
---@param target integer
---@param propertyName string
---@param propertyState number[]
---@param options table
function sim.setQuaternionProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetVector3Property.htm
--- Fetches a vector3 property (double[3])
---@param target integer
---@param propertyName string
---@param options table
---@return number[] propertyState
function sim.getVector3Property(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetVector3Property.htm
--- Sets a vector3 property (double[3])
---@param target integer
---@param propertyName string
---@param propertyState number[]
---@param options table
function sim.setVector3Property(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetVector2Property.htm
--- Fetches a vector2 property (double[2])
---@param target integer
---@param propertyName string
---@param options table
---@return number[] propertyState
function sim.getVector2Property(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetVector2Property.htm
--- Sets a vector2 property (double[2])
---@param target integer
---@param propertyName string
---@param propertyState number[]
---@param options table
function sim.setVector2Property(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetFloatArrayProperty.htm
--- Fetches a float array property (double[])
---@param target integer
---@param propertyName string
---@param options table
---@return number[] propertyState
function sim.getFloatArrayProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetFloatArrayProperty.htm
--- Sets a float array property (double[])
---@param target integer
---@param propertyName string
---@param propertyState number[]
---@param options table
function sim.setFloatArrayProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetIntArray2Property.htm
--- Fetches an int[2] property
---@param target integer
---@param propertyName string
---@param options table
---@return integer[] propertyState
function sim.getIntArray2Property(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetIntArray2Property.htm
--- Sets an int[2] property
---@param target integer
---@param propertyName string
---@param propertyState integer[]
---@param options table
function sim.setIntArray2Property(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetIntArrayProperty.htm
--- Fetches an int array property (int[])
---@param target integer
---@param propertyName string
---@param options table
---@return integer[] propertyState
function sim.getIntArrayProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetIntArrayProperty.htm
--- Sets an int array property (int[])
---@param target integer
---@param propertyName string
---@param propertyState integer[]
---@param options table
function sim.setIntArrayProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetBufferProperty.htm
--- Fetches a buffer property
---@param target integer
---@param propertyName string
---@param options table
---@return string propertyState
function sim.getBufferProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetBufferProperty.htm
--- Sets a buffer property
---@param target integer
---@param propertyName string
---@param propertyState string
---@param options table
function sim.setBufferProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetStringProperty.htm
--- Fetches a string property (text)
---@param target integer
---@param propertyName string
---@param options table
---@return string propertyState
function sim.getStringProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetStringProperty.htm
--- Sets a string property (text)
---@param target integer
---@param propertyName string
---@param propertyState string
---@param options table
function sim.setStringProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetFloatProperty.htm
--- Fetches a float property (double)
---@param target integer
---@param propertyName string
---@param options table
---@return number propertyState
function sim.getFloatProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetFloatProperty.htm
--- Sets a float property (double)
---@param target integer
---@param propertyName string
---@param propertyState number
---@param options table
function sim.setFloatProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetLongProperty.htm
--- Fetches an int64 property
---@param target integer
---@param propertyName string
---@param options table
---@return integer propertyState
function sim.getLongProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetLongProperty.htm
--- Sets an int64 property
---@param target integer
---@param propertyName string
---@param propertyState integer
---@param options table
function sim.setLongProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetIntProperty.htm
--- Fetches an int32 property
---@param target integer
---@param propertyName string
---@param options table
---@return integer propertyState
function sim.getIntProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetIntProperty.htm
--- Sets an int32 property
---@param target integer
---@param propertyName string
---@param propertyState integer
---@param options table
function sim.setIntProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetBoolProperty.htm
--- Fetches a boolean property
---@param target integer
---@param propertyName string
---@param options table
---@return boolean propertyState
function sim.getBoolProperty(target,propertyName,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetBoolProperty.htm
--- Sets a boolean property
---@param target integer
---@param propertyName string
---@param propertyState boolean
---@param options table
function sim.setBoolProperty(target,propertyName,propertyState,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectColor.htm
--- Sets the color of a scene object
---@param objectHandle integer
---@param index integer
---@param colorComponent integer
---@param rgbData number[]
function sim.setObjectColor(objectHandle,index,colorComponent,rgbData) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectColor.htm
--- Retrieves the color of a scene object
---@param objectHandle integer
---@param index integer
---@param colorComponent integer
---@return number[] rgbData
function sim.getObjectColor(objectHandle,index,colorComponent) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectVelocity.htm
--- Retrieves the linear and/or angular velocity of an object, in absolute coordinates. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all objects in the scene
---@param objectHandle integer
---@return number[] linearVelocity
---@return number[] angularVelocity
function sim.getObjectVelocity(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simScaleObjects.htm
--- Scales specified objects. All related values are automatically scaled appropriately (e.g. masses, forces, etc.)
---@param objectHandles integer[]
---@param scalingFactor number
---@param scalePositionsToo boolean
function sim.scaleObjects(objectHandles,scalingFactor,scalePositionsToo) end
--- url:https://manual.coppeliarobotics.com/en/sim/simScaleObject.htm
--- Scales specified objects in a non-isometric fashion, if possible. Only non-compound shapes can be non-isometrically scaled. Some primitive shapes can have some constraints between their axes
---@param objectHandle integer
---@param xScale number
---@param yScale number
---@param zScale number
---@param options integer
function sim.scaleObject(objectHandle,xScale,yScale,zScale,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCopyPasteObjects.htm
--- Copies and pastes objects
---@param objectHandles integer[]
---@param options integer
---@return integer[] copiedObjectHandles
function sim.copyPasteObjects(objectHandles,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectSizeFactor.htm
--- Retrieves the size factor of a scene object. The size factor is different from the real object size. Use this to be able to adapt to scaling operations
---@param objectHandle integer
---@return number sizeFactor
function sim.getObjectSizeFactor(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectSel.htm
--- Sets the object selection state
---@param objectHandles integer[]
function sim.setObjectSel(objectHandles) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectSel.htm
--- Retrieves the handles of selected objects
---@return integer[] selectedObjects
function sim.getObjectSel() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectType.htm
--- Retrieves the type of an object
---@param objectHandle integer
---@return integer objectType
function sim.getObjectType(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectQuaternion.htm
--- Sets the quaternion of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
---@param objectHandle integer
---@param quaternion number[]
---@param relativeToObjectHandle integer
function sim.setObjectQuaternion(objectHandle,quaternion,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectQuaternion.htm
--- Retrieves the quaternion of an object
---@param objectHandle integer
---@param relativeToObjectHandle integer
---@return number[] quaternion
function sim.getObjectQuaternion(objectHandle,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectOrientation.htm
--- Sets the orientation ( Euler angles ) of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
---@param objectHandle integer
---@param eulerAngles number[]
---@param relativeToObjectHandle integer
function sim.setObjectOrientation(objectHandle,eulerAngles,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectOrientation.htm
--- Retrieves the orientation ( Euler angles ) of an object
---@param objectHandle integer
---@param relativeToObjectHandle integer
---@return number[] eulerAngles
function sim.getObjectOrientation(objectHandle,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectPosition.htm
--- Sets the position (x, y and z-coordinates) of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
---@param objectHandle integer
---@param position number[]
---@param relativeToObjectHandle integer
function sim.setObjectPosition(objectHandle,position,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectPosition.htm
--- Retrieves the position of an object
---@param objectHandle integer
---@param relativeToObjectHandle integer
---@return number[] position
function sim.getObjectPosition(objectHandle,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectPose.htm
--- Sets the pose of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
---@param objectHandle integer
---@param pose number[]
---@param relativeToObjectHandle integer
function sim.setObjectPose(objectHandle,pose,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectPose.htm
--- Retrieves the pose of an object
---@param objectHandle integer
---@param relativeToObjectHandle integer
---@return number[] pose
function sim.getObjectPose(objectHandle,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectMatrix.htm
--- Sets the transformation matrix of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
---@param objectHandle integer
---@param relativeToObjectHandle integer
function sim.setObjectMatrix(objectHandle,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectMatrix.htm
--- Retrieves the transformation matrix of an object
---@param objectHandle integer
---@param relativeToObjectHandle integer
function sim.getObjectMatrix(objectHandle,relativeToObjectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectChild.htm
--- Retrieves the handle of an object's child object
---@param objectHandle integer
---@param index integer
---@return integer childHandle
function sim.getObjectChild(objectHandle,index) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectHierarchyOrder.htm
--- Moves an object up or down among its siblings in the scene hierarchy
---@param objectHandle integer
---@param order integer
function sim.setObjectHierarchyOrder(objectHandle,order) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectHierarchyOrder.htm
--- Retrieves the zero-based position of an object among its siblings in the scene hierarchy
---@param objectHandle integer
---@return integer order
---@return integer totalSiblingsCount
function sim.getObjectHierarchyOrder(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectParent.htm
--- Sets an object's parent object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
---@param objectHandle integer
---@param parentObjectHandle integer
---@param keepInPlace boolean
function sim.setObjectParent(objectHandle,parentObjectHandle,keepInPlace) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectParent.htm
--- Retrieves the handle of an object's parent object
---@param objectHandle integer
---@return integer parentHandle
function sim.getObjectParent(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectAlias.htm
--- Sets the alias of an object
---@param objectHandle integer
---@param objectAlias string
function sim.setObjectAlias(objectHandle,objectAlias) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectAlias.htm
--- Retrieves the alias or path of an object based on its handle
---@param objectHandle integer
---@param options integer
---@return string alias
function sim.getObjectAlias(objectHandle,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemoveModel.htm
--- Removes a model from the scene
---@param objectHandle integer
---@param delayedRemoval boolean
---@return integer removedCnt
function sim.removeModel(objectHandle,delayedRemoval) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemoveObjects.htm
--- Removes one or several objects from the scene
---@param objectHandles integer[]
---@param delayedRemoval boolean
function sim.removeObjects(objectHandles,delayedRemoval) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectUid.htm
--- Retrieves the unique identifier of an object: throughout a CoppeliaSim session, there won't be two identical unique identifiers. Unique identifiers are however not persistent (i.e. are not saved with the object)
---@param objectHandle integer
---@return integer uid
function sim.getObjectUid(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetClosestPosOnPath.htm
--- Returns the position or distance along a path that is closest to a specified point in space
---@param path number[]
---@param pathLengths number[]
---@param absPt number[]
---@return number posAlongPath
function sim.getClosestPosOnPath(path,pathLengths,absPt) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGenerateTimeOptimalTrajectory.htm
--- Generates a time optimal trajectory, based on the TOPPRA library
---@param path number[]
---@param pathLengths number[]
---@param minMaxVel number[]
---@param minMaxAccel number[]
---@param trajPtSamples integer
---@param boundaryCondition string
---@param timeout number
---@param calculationScriptHandle integer
---@return number[] outP
---@return number[] times
---@return integer scriptHandle
function sim.generateTimeOptimalTrajectory(path,pathLengths,minMaxVel,minMaxAccel,trajPtSamples,boundaryCondition,timeout,calculationScriptHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simResamplePath.htm
--- Returns a resampled path
---@param path number[]
---@param pathLengths number[]
---@param finalConfigCnt integer
---@param method table
---@param types integer[]
---@return number[] outputPath
function sim.resamplePath(path,pathLengths,finalConfigCnt,method,types) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPathInterpolatedConfig.htm
--- Returns an interpolated configuration from a path
---@param path number[]
---@param pathLengths number[]
---@param t number
---@param method table
---@param types integer[]
---@return number[] config
function sim.getPathInterpolatedConfig(path,pathLengths,t,method,types) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPathLengths.htm
--- Returns the lengths of a path in 1, 2 or 3D Cartesian space, even if more coordinates are provided. Each path point will have a corresponding length value (taken as the distance from the path's first point, along the path)
---@param path number[]
---@param dof integer
---@param distCallback string
---@return number[] pathLengths
---@return number totalLength
function sim.getPathLengths(path,dof,distCallback) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetConfigDistance.htm
--- Returns the distance between two configurations points
---@param configA number[]
---@param configB number[]
---@param metric number[]
---@param types integer[]
---@return number distance
function sim.getConfigDistance(configA,configB,metric,types) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreatePath.htm
--- Creates a  path .
---@param ctrlPts number[]
---@param options integer
---@param subdiv integer
---@param smoothness number
---@param orientationMode integer
---@param upVector number[]
---@return integer pathHandle
function sim.createPath(ctrlPts,options,subdiv,smoothness,orientationMode,upVector) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPointCloudPoints.htm
--- Retrieves point positions from a  point cloud
---@param pointCloudHandle integer
---@return number[] points
function sim.getPointCloudPoints(pointCloudHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simInsertObjectIntoPointCloud.htm
--- Inserts an object into a  point cloud , as points
---@param pointCloudHandle integer
---@param objectHandle integer
---@param options integer
---@param gridSize number
---@param color integer[]
---@param duplicateTolerance number
---@return integer totalPointCnt
function sim.insertObjectIntoPointCloud(pointCloudHandle,objectHandle,options,gridSize,color,duplicateTolerance) end
--- url:https://manual.coppeliarobotics.com/en/sim/simIntersectPointsWithPointCloud.htm
--- Removes points from a  point cloud , that do not intersect with the provided points (i.e. the result in the point cloud will be the intersection between the two sets of points). When a point cloud doesn't use an OC tree calculation structure, then this operation cannot be performed
---@param pcHandle integer
---@param options integer
---@param points number[]
---@param tolerance number
---@return integer totalPointCnt
function sim.intersectPointsWithPointCloud(pcHandle,options,points,tolerance) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSubtractObjectFromPointCloud.htm
--- Removes an object from a  point cloud , as a subtraction
---@param pcHandle integer
---@param objectHandle integer
---@param options integer
---@param tolerance number
---@return integer totalPointCnt
function sim.subtractObjectFromPointCloud(pcHandle,objectHandle,options,tolerance) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemovePointsFromPointCloud.htm
--- Removes points from a  point cloud . When a point cloud doesn't use an OC tree calculation structure, then individual points cannot be removed, only all points can be removed in that case
---@param pointCloudHandle integer
---@param options integer
---@param points number[]
---@param tolerance number
---@return integer totalPointCnt
function sim.removePointsFromPointCloud(pointCloudHandle,options,points,tolerance) end
--- url:https://manual.coppeliarobotics.com/en/sim/simInsertPointsIntoPointCloud.htm
--- Inserts points into a  point cloud
---@param pcHandle integer
---@param options integer
---@param points number[]
---@param color integer[]
---@param duplicateTolerance number
---@return integer totalPointCnt
function sim.insertPointsIntoPointCloud(pcHandle,options,points,color,duplicateTolerance) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetPointCloudOptions.htm
--- Sets various properties of a  point cloud
---@param pcHandle integer
---@param maxVoxelSize number
---@param maxPtCntPerVoxel integer
---@param options integer
---@param pointSize number
function sim.setPointCloudOptions(pcHandle,maxVoxelSize,maxPtCntPerVoxel,options,pointSize) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetPointCloudOptions.htm
--- Gets various properties of a  point cloud
---@param pcHandle integer
---@return number maxVoxelS
---@return integer maxPtCntPerVoxel
---@return integer opt
---@return number ps
function sim.getPointCloudOptions(pcHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreatePointCloud.htm
--- Creates an empty  point cloud
---@param maxVoxelSize number
---@param maxPtCntPerVoxel integer
---@param options integer
---@param pointSize number
---@return integer handle
function sim.createPointCloud(maxVoxelSize,maxPtCntPerVoxel,options,pointSize) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckOctreePointOccupancy.htm
--- Checks whether the provided points collide with the  OC tree  voxels
---@param octreeHandle integer
---@param options integer
---@param points number[]
---@return integer res
---@return integer tag
---@return integer locLow
---@return integer locHigh
function sim.checkOctreePointOccupancy(octreeHandle,options,points) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetOctreeVoxels.htm
--- Retrieves voxel positions from an  OC tree
---@param octreeHandle integer
---@return number[] voxels
function sim.getOctreeVoxels(octreeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSubtractObjectFromOctree.htm
--- Removes an object from an  OC tree , as voxel subtractions
---@param octreeHandle integer
---@param objectHandle integer
---@param options integer
---@return integer totalVoxelCnt
function sim.subtractObjectFromOctree(octreeHandle,objectHandle,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simInsertObjectIntoOctree.htm
--- Inserts an object into an  OC tree , as voxels. Each voxel will store a color and a tag value
---@param octreeHandle integer
---@param objectHandle integer
---@param options integer
---@param color integer[]
---@param tag integer
---@return integer totalVoxelCnt
function sim.insertObjectIntoOctree(octreeHandle,objectHandle,options,color,tag) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemoveVoxelsFromOctree.htm
--- Removes voxels from an  OC tree
---@param octreeHandle integer
---@param options integer
---@param points number[]
---@return integer totalVoxelCnt
function sim.removeVoxelsFromOctree(octreeHandle,options,points) end
--- url:https://manual.coppeliarobotics.com/en/sim/simInsertVoxelsIntoOctree.htm
--- Inserts voxels into an  OC tree . Each voxel will store a color and a tag value
---@param octreeHandle integer
---@param options integer
---@param points number[]
---@param color integer[]
---@param tag integer[]
---@return integer totalVoxelCnt
function sim.insertVoxelsIntoOctree(octreeHandle,options,points,color,tag) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateOctree.htm
--- Creates an empty  OC tree
---@param voxelSize number
---@param options integer
---@param pointSize number
---@return integer handle
function sim.createOctree(voxelSize,options,pointSize) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCameraFitToView.htm
--- Shifts and adjusts a camera associated with a view to fill the view entirely with the specified objects or models
---@param viewHandleOrIndex integer
---@param objectHandles integer[]
---@param options integer
---@param scaling number
---@return integer result
function sim.cameraFitToView(viewHandleOrIndex,objectHandles,options,scaling) end
--- url:https://manual.coppeliarobotics.com/en/sim/simResetGraph.htm
--- Resets a graph object (i.e. clears all its data streams)
---@param graphHandle integer
function sim.resetGraph(graphHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleGraph.htm
--- Handles a graph object (i.e. records another value for each curve, given that such value was provided via  sim.setGraphStreamValue
---@param graphHandle integer
---@param time number
function sim.handleGraph(graphHandle,time) end
--- url:https://manual.coppeliarobotics.com/en/sim/simDuplicateGraphCurveToStatic.htm
--- Duplicates a graph stream or curve, and freezes it
---@param graphHandle integer
---@param curveId integer
---@param staticCurveName string
---@return integer staticCurveId
function sim.duplicateGraphCurveToStatic(graphHandle,curveId,staticCurveName) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddGraphCurve.htm
--- Adds or updates a graph curve. A graph curve is persistent, but can be removed with  sim.destroyGraphCurve
---@param graphHandle integer
---@param curveName string
---@param dim integer
---@param streamIds integer[]
---@param defaultValues number[]
---@param unitStr string
---@param options integer
---@param color number[]
---@param curveWidth integer
---@return integer curveId
function sim.addGraphCurve(graphHandle,curveName,dim,streamIds,defaultValues,unitStr,options,color,curveWidth) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetGraphStreamValue.htm
--- Sets the next value to be recorded for a graph stream
---@param graphHandle integer
---@param streamId integer
---@param value number
function sim.setGraphStreamValue(graphHandle,streamId,value) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetGraphStreamTransformation.htm
--- Applies a transformation to a graph stream
---@param graphHandle integer
---@param streamId integer
---@param trType integer
---@param mult number
---@param off number
---@param movingAvgPeriod integer
function sim.setGraphStreamTransformation(graphHandle,streamId,trType,mult,off,movingAvgPeriod) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddGraphStream.htm
--- Adds or updates a graph stream. A graph stream is persistent, but can be removed with  sim.destroyGraphCurve
---@param graphHandle integer
---@param streamName string
---@param unitStr string
---@param options integer
---@param color number[]
---@return integer streamId
function sim.addGraphStream(graphHandle,streamName,unitStr,options,color) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateVisionSensor.htm
--- Creates a  vision sensor .
---@param options integer
---@param intParams integer[]
---@return integer sensorHandle
function sim.createVisionSensor(options,intParams) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAdjustView.htm
--- Adjusts parameters of a view
---@param viewHandleOrIndex integer
---@param objectHandle integer
---@param options integer
---@param viewLabel string
---@return integer res
function sim.adjustView(viewHandleOrIndex,objectHandle,options,viewLabel) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorRes.htm
--- Returns the resolution of the vision sensor
---@param sensorHandle integer
---@return integer[] resolution
function sim.getVisionSensorRes(sensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetVisionSensorImg.htm
--- Writes the image of a vision sensor (and applies any image processing via the  vision callback functions ). Make sure the vision sensor is flagged as  external input
---@param sensorHandle integer
---@param image string
---@param options integer
---@param pos integer[]
---@param size integer[]
function sim.setVisionSensorImg(sensorHandle,image,options,pos,size) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorImg.htm
--- Reads the image of a vision sensor. The returned data doesn't make sense if  sim.handleVisionSensor  wasn't called previously
---@param sensorHandle integer
---@param options integer
---@param rgbaCutOff number
---@return string image
---@return integer[] resolution
function sim.getVisionSensorImg(sensorHandle,options,rgbaCutOff) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorDepth.htm
--- Reads the depth buffer of a vision sensor. The returned data doesn't make sense if  sim.handleVisionSensor  wasn't called previously
---@param sensorHandle integer
---@param options integer
---@param pos integer[]
---@param size integer[]
---@return string depth
---@return integer[] resolution
function sim.getVisionSensorDepth(sensorHandle,options,pos,size) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckVisionSensorEx.htm
--- Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleVisionSensor . The  vision callback functions  will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object
---@param sensorHandle integer
---@param entityHandle integer
---@param returnImage boolean
---@return number[] buff
function sim.checkVisionSensorEx(sensorHandle,entityHandle,returnImage) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckVisionSensor.htm
--- Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleVisionSensor . The  vision callback functions  will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object
---@param sensorHandle integer
---@param entityHandle integer
---@return integer result
---@return number[] auxPacket1
---@return number[] auxPacket2
function sim.checkVisionSensor(sensorHandle,entityHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simResetVisionSensor.htm
--- Clears the detection state, etc. of a proximity sensor object
---@param sensorHandle integer
function sim.resetVisionSensor(sensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simReadVisionSensor.htm
--- Reads the state of a vision sensor. This function doesn't perform detection, it merely reads the result from a previous call to  sim.handleVisionSensor
---@param visionSensorHandle integer
---@return integer result
---@return number[] packet1
---@return number[] packet2
function sim.readVisionSensor(visionSensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleVisionSensor.htm
--- Handles (performs sensing, etc. of) a vision sensor object. It (1) clear previous computed image processing data, (2) reads an image and (3) performs image processing via the  vision callback functions  (if the vision sensor is using an  external input  only (1) is performed)
---@param visionSensorHandle integer
---@return integer detectionCount
---@return number[] packet1
---@return number[] packet2
function sim.handleVisionSensor(visionSensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateProximitySensor.htm
--- Creates a  proximity sensor
---@param sensorType integer
---@param subType integer
---@param options integer
---@param intParams integer[]
---@return integer sensorHandle
function sim.createProximitySensor(sensorType,subType,options,intParams) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensorEx2.htm
--- Checks whether the proximity sensor detects the indicated points, segments or triangles. Detection is silent (no visual feedback)
---@param sensorHandle integer
---@param vertices number[]
---@param itemType integer
---@param itemCount integer
---@param mode integer
---@param threshold number
---@param maxAngle number
---@return integer res
---@return number dist
---@return number[] point
---@return number[] n
function sim.checkProximitySensorEx2(sensorHandle,vertices,itemType,itemCount,mode,threshold,maxAngle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensorEx.htm
--- Checks whether the proximity sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleProximitySensor . Also, the detectable flags of the entity are overridden if the entity is an object
---@param handle integer
---@param entityHandle integer
---@param detectionMode integer
---@param detectionthreshold number
---@param maxAngle number
---@return integer res
---@return number dist
---@return number[] point
---@return integer object
---@return number[] n
function sim.checkProximitySensorEx(handle,entityHandle,detectionMode,detectionthreshold,maxAngle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensor.htm
--- Checks whether the proximity sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleProximitySensor . Also, the detectable flags of the entity are overridden if the entity is an object
---@param sensorHandle integer
---@param entityHandle integer
---@return integer res
---@return number dist
---@return number[] point
---@return integer obj
---@return number[] n
function sim.checkProximitySensor(sensorHandle,entityHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simResetProximitySensor.htm
--- Clears the detection state, detection color, detection segments, etc. of a proximity sensor object
---@param sensorHandle integer
function sim.resetProximitySensor(sensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simReadProximitySensor.htm
--- Reads the state of a proximity sensor. This function doesn't perform detection, it merely reads the result from a previous call to  sim.handleProximitySensor
---@param sensorHandle integer
---@return integer res
---@return number dist
---@return number[] point
---@return integer obj
---@return number[] n
function sim.readProximitySensor(sensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGenerateTextShape.htm
--- Generates a 3D text model.
---@param txt string
---@param color number[]
---@param height number
---@param centered boolean
---@param alphabetLocation string
---@return integer modelHandle
function sim.generateTextShape(txt,color,height,centered,alphabetLocation) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetShapeBB.htm
--- Sets the size of a shape's bounding box, effectively scaling the shape. Non-isometric scaling is not always possible
---@param shapeHandle integer
---@param size number[]
function sim.setShapeBB(shapeHandle,size) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeBB.htm
--- Returns the size and relative pose of a shape's bounding box
---@param shapeHandle integer
---@return number[] size
---@return number[] pose
function sim.getShapeBB(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRelocateShapeFrame.htm
--- Repositions and reorients the reference frame of a shape, while keeping the mesh in place. The shape's inertia properties are unaffected.
---@param shapeHandle integer
---@param pose number[]
---@return boolean result
function sim.relocateShapeFrame(shapeHandle,pose) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAlignShapeBB.htm
--- Reorients the bounding box of a shape, while keeping the shape frame in place. The shape's inertia properties are unaffected
---@param shapeHandle integer
---@param pose number[]
---@return boolean result
function sim.alignShapeBB(shapeHandle,pose) end
--- url:https://manual.coppeliarobotics.com/en/sim/simUngroupShape.htm
--- Ungroups a compound shape into several  shapes
---@param shapeHandle integer
---@return integer[] shapeHandles
function sim.ungroupShape(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGroupShapes.htm
--- Groups (or merges) several shapes into a  compound shape  (or  simple shape )
---@param shapeHandles integer[]
---@param merge boolean
---@return integer shapeHandle
function sim.groupShapes(shapeHandles,merge) end
--- url:https://manual.coppeliarobotics.com/en/sim/simHandleProximitySensor.htm
--- Handles (performs sensing, etc. of) a registered proximity sensor object
---@param sensorHandle integer
---@return integer res
---@return number dist
---@return number[] point
---@return integer obj
---@return number[] n
function sim.handleProximitySensor(sensorHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetExtensionString.htm
--- Retrieves a string that describes additional environment or object properties, mainly used by extension plugins.
---@param objectHandle integer
---@param index integer
---@param key string
---@return string theString
function sim.getExtensionString(objectHandle,index,key) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeViz.htm
--- Retrieves a shape's visual information.
---@param shapeHandle integer
---@param index integer
---@return table data
function sim.getShapeViz(shapeHandle,index) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeMesh.htm
--- Retrieves a shape's mesh information
---@param shapeHandle integer
---@return number[] vertices
---@return integer[] indices
---@return number[] normals
function sim.getShapeMesh(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateHeightfieldShape.htm
--- Creates a heightfield  shape
---@param options integer
---@param shadingAngle number
---@param xPointCount integer
---@param yPointCount integer
---@param xSize number
---@param heights number[]
---@return integer objectHandle
function sim.createHeightfieldShape(options,shadingAngle,xPointCount,yPointCount,xSize,heights) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreatePrimitiveShape.htm
--- Creates a primitive shape
---@param primitiveType integer
---@param sizes number[]
---@param options integer
---@return integer shapeHandle
function sim.createPrimitiveShape(primitiveType,sizes,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateShape.htm
--- Creates a mesh shape
---@param options integer
---@param shadingAngle number
---@param vertices number[]
---@param indices integer[]
---@param normals number[]
---@param textureCoordinates number[]
---@param texture string
---@param textureResolution integer[]
---@return integer objectHandle
function sim.createShape(options,shadingAngle,vertices,indices,normals,textureCoordinates,texture,textureResolution) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetShapeTexture.htm
--- Applies/removes a texture to/from a shape
---@param shapeHandle integer
---@param textureId integer
---@param mappingMode integer
---@param options integer
---@param uvScaling number[]
---@param position number[]
---@param orientation number[]
function sim.setShapeTexture(shapeHandle,textureId,mappingMode,options,uvScaling,position,orientation) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeTextureId.htm
--- Retrieves the texture ID of a texture that is applied to a specific shape
---@param shapeHandle integer
---@return integer textureId
function sim.getShapeTextureId(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetShapeColor.htm
--- Sets the color of a shape
---@param shapeHandle integer
---@param colorName string
---@param colorComponent integer
---@param rgbData number[]
function sim.setShapeColor(shapeHandle,colorName,colorComponent,rgbData) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeColor.htm
--- Retrieves the color of a shape
---@param shapeHandle integer
---@param colorName string
---@param colorComponent integer
---@return integer result
---@return number[] rgbData
function sim.getShapeColor(shapeHandle,colorName,colorComponent) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointDependency.htm
--- Retrieves joint dependency information, when the joint is in dependent mode
---@param jointHandle integer
---@return integer masterJointHandle
---@return number offset
---@return number multCoeff
function sim.getJointDependency(jointHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointDependency.htm
--- Sets a joint dependent of another joint. The dependent joint should first be set into dependent mode via  sim.setJointMode
---@param jointHandle integer
---@param masterJointHandle integer
---@param offset number
---@param multCoeff number
function sim.setJointDependency(jointHandle,masterJointHandle,offset,multCoeff) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointMode.htm
--- Retrieves the operation mode of a joint
---@param jointHandle integer
---@return integer jointMode
function sim.getJointMode(jointHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointMode.htm
--- Sets the operation mode of a joint
---@param jointHandle integer
---@param jointMode integer
function sim.setJointMode(jointHandle,jointMode) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateJoint.htm
--- Creates a  joint
---@param jointType integer
---@param jointMode integer
---@param options integer
---@param sizes number[]
---@return integer jointHandle
function sim.createJoint(jointType,jointMode,options,sizes) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointType.htm
--- Retrieves the type of a joint
---@param objectHandle integer
---@return integer jointType
function sim.getJointType(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointInterval.htm
--- Retrieves the interval parameters of a joint
---@param objectHandle integer
---@return boolean cyclic
---@return number[] interval
function sim.getJointInterval(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointInterval.htm
--- Sets the interval parameters of a joint (i.e. range values). The attributes or interval parameters might have no effect, depending on the joint-type
---@param objectHandle integer
---@param cyclic boolean
---@param interval number[]
function sim.setJointInterval(objectHandle,cyclic,interval) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetObjectChildPose.htm
--- Can be used to set a spherical joint's rotational transformation (the translational part is ignored)
---@param objectHandle integer
---@param pose number[]
function sim.setObjectChildPose(objectHandle,pose) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectChildPose.htm
--- Retrieves the intrinsic or internal transformation of an object. For a joint, this is the transformation caused by the joint movement, mainly. For joints and force sensors, this will also include a possible error transformation caused by the physics engine (a physics engine can cause joints and force sensors to come apart, when constraints can't be perfectly resolved)
---@param objectHandle integer
---@return number[] pose
function sim.getObjectChildPose(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointVelocity.htm
--- Retrieves the linear or angular velocity of a joint. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all joints in the scene
---@param jointHandle integer
---@return number velocity
function sim.getJointVelocity(jointHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointTargetVelocity.htm
--- Retrieves the target linear/angular velocity of a non-spherical joint
---@param objectHandle integer
---@return number targetVelocity
function sim.getJointTargetVelocity(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointTargetPosition.htm
--- Retrieves the target linear/angular position of a joint
---@param objectHandle integer
---@return number targetPosition
function sim.getJointTargetPosition(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointPosition.htm
--- Retrieves the linear/angular position of a joint. This function cannot be used with spherical joints (use  sim.getObjectChildPose  instead)
---@param objectHandle integer
---@return number position
function sim.getJointPosition(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointPosition.htm
--- Sets the linear/angular position of a joint. Cannot be used with spherical joints (use  sim.setObjectChildPose  instead)
---@param objectHandle integer
---@param position number
function sim.setJointPosition(objectHandle,position) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetEventFilters.htm
--- Specifies filters for the sysCall_event callback. Operates on a per script basis
---@param filters table
function sim.setEventFilters(filters) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetStackTraceback.htm
--- Lua only. Retrieves and clears the last generated stack traceback for a script
---@param scriptHandle integer
---@return string stackTraceback
function sim.getStackTraceback(scriptHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRegisterScriptFuncHook.htm
--- Registers a script function hook for  callback functions , that will be executed before or after the specified function. Calling this function a second time with the same arguments will unregister a previous hook
---@param funcToHook string
---@param userFunc function
---@param execBefore boolean
---@return integer result
function sim.registerScriptFuncHook(funcToHook,userFunc,execBefore) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetApiInfo.htm
--- Returns the call tip (or info text) for an API function
---@param scriptHandle integer
---@param apiWord string
---@return string info
function sim.getApiInfo(scriptHandle,apiWord) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetApiFunc.htm
--- Retrieves all API functions and variables that match a specific word. Useful for script code auto-completion functionality
---@param scriptHandle integer
---@param apiWord string
---@return string[] funcsAndVars
function sim.getApiFunc(scriptHandle,apiWord) end
--- url:https://manual.coppeliarobotics.com/en/sim/simExecuteScriptString.htm
--- Executes some code in a specific script (from a  plugin ,  the main client application , or from another script). The target script must be initialized for this call to succeed, e.g. when calling  simulation scripts , then simulation must be running                 From C/C++, data exchange between a plugin and a script happens via a  stack . Reading and writing arguments from/to the stack gives you a maximum of flexibility, and you wil be able to exchange also complex data structures. But it can also be tedious and error prone. Use instead the helper classes located in  programming/include/simStack
---@param stringToExecute string
---@param scriptHandle integer
---@return integer result
function sim.executeScriptString(stringToExecute,scriptHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetScriptFunctions.htm
--- Retrieves a map of another script functions, that can be called
---@param scriptHandle integer
---@return table object
function sim.getScriptFunctions(scriptHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCallScriptFunction.htm
--- Calls a script function (from a  plugin ,  the main client application , or from another script). This represents a  user callback  inside of a script. The target script must be initialized for this call to succeed, e.g. when calling  simulation scripts , then simulation must be running
---@param functionName string
---@param scriptHandle integer
function sim.callScriptFunction(functionName,scriptHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simInitScript.htm
--- Initializes/reinitializes a script. Operates in an asynchronous way, and cannot be called from within the script being reinitialized
---@param scriptHandle integer
function sim.initScript(scriptHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetScript.htm
--- Retrieves the handle of a script. For script objects, use sim.getObject instead
---@param scriptType integer
---@param scriptName string
---@return integer scriptHandle
function sim.getScript(scriptType,scriptName) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetRandom.htm
--- Generates a random value in the range between 0.0 and 1.0. The value is generated from an individual generator attached to the calling script
---@param seed integer
---@return number randomValue
function sim.getRandom(seed) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateScript.htm
--- Creates a  script object .
---@param scriptType integer
---@param scriptText string
---@param options integer
---@return integer scriptHandle
function sim.createScript(scriptType,scriptText,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateDummy.htm
--- Creates a  dummy .
---@param size number
---@return integer dummyHandle
function sim.createDummy(size) end
--- url:https://manual.coppeliarobotics.com/en/sim/simIsDynamicallyEnabled.htm
--- Checks whether a scene object is dynamically enabled, i.e. is being handled and simulated by the physics engine. Note that until the physics engine has parsed the scene in the first simulation step (i.e. the first time  sim.handleDynamics  is called), no object will be dynamically enabled
---@param objectHandle integer
---@return boolean dynamicallyEnabled
function sim.isDynamicallyEnabled(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateForceSensor.htm
--- Creates a  force sensor .
---@param options integer
---@param intParams integer[]
---@param floatParams number[]
---@return integer sensorHandle
function sim.createForceSensor(options,intParams,floatParams) end
--- url:https://manual.coppeliarobotics.com/en/sim/simComputeMassAndInertia.htm
--- Computes and applies the mass and inertia matrix for a shape, based on its convex representation. When calling this function while the simulation is running, one should then call  sim.resetDynamicObject , for the changes to take effect
---@param shapeHandle integer
---@param density number
---@return integer result
function sim.computeMassAndInertia(shapeHandle,density) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetShapeInertia.htm
--- Applies a new inertia matrix to a shape. If simulation is running, the shape is dynamically reset (similar to calling  sim.resetDynamicObject  right after)
---@param shapeHandle integer
---@param inertiaMatrix number[]
function sim.setShapeInertia(shapeHandle,inertiaMatrix) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeInertia.htm
--- Retrieves the inertia information from a shape
---@param shapeHandle integer
---@return number[] inertiaMatrix
function sim.getShapeInertia(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetShapeMass.htm
--- Applies a new mass value to a shape. If simulation is running, the shape is dynamically reset (similar to calling  sim.resetDynamicObject  right after)
---@param shapeHandle integer
---@param mass number
function sim.setShapeMass(shapeHandle,mass) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeMass.htm
--- Retrieves the mass of a shape
---@param shapeHandle integer
---@return number mass
function sim.getShapeMass(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetContactInfo.htm
--- Retrieves contact point information of a dynamic simulation pass.
---@param dynamicPass integer
---@param objectHandle integer
---@param index integer
---@return integer[] coll
---@return number[] point
---@return number[] rForce
---@return number[] n
function sim.getContactInfo(dynamicPass,objectHandle,index) end
--- url:https://manual.coppeliarobotics.com/en/sim/simRemoveParticleObject.htm
--- Removes a previously added particle object
---@param objectHandle integer
function sim.removeParticleObject(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddParticleObjectItem.htm
--- Adds an item (or clears all items) to a previously inserted particle object
---@param particleObjectHandle integer
---@param itemData number[]
function sim.addParticleObjectItem(particleObjectHandle,itemData) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddParticleObject.htm
--- Adds a particle object that will be simulated and displayed in the scene. Particle objects are containers that hold several items (particles) of a given type. This can be used for several different applications (e.g. simulation of air/water jets)
---@param objectType integer
---@param size number
---@param density number
---@param parameters number[]
---@param lifeTime number
---@param maxItemCount integer
---@param color number[]
---@return integer particleObjectHandle
function sim.addParticleObject(objectType,size,density,parameters,lifeTime,maxItemCount,color) end
--- url:https://manual.coppeliarobotics.com/en/sim/simResetDynamicObject.htm
--- Dynamically resets an object that is dynamically simulated. This means that the object representation in the dynamics engine is removed, and added again. This can be useful when the set-up of a dynamically simulated chain needs to be modified during simulation (e.g. joint or shape attachement position/orientation changed)
---@param objectHandle integer
function sim.resetDynamicObject(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetLinkDummy.htm
--- Defines (or breaks) a dummy-dummy link pair. Useful to create dynamic loop closure constraints on the fly (among others)
---@param dummyHandle integer
---@param linkedDummyHandle integer
function sim.setLinkDummy(dummyHandle,linkedDummyHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetLinkDummy.htm
--- Retrieves the object handle of the dummy linked to this one
---@param dummyHandle integer
---@return integer linkedDummyHandle
function sim.getLinkDummy(dummyHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetVelocity.htm
--- Retrieves the linear and/or angular velocity of the center of mass of a non-static shape. Data is provided by the selected physics engine
---@param shapeHandle integer
---@return number[] linearVelocity
---@return number[] angularVelocity
function sim.getVelocity(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddForce.htm
--- Adds a non-central force to a shape object that is dynamically enabled. Added forces are cumulative, applied relative to the center of mass, and are reset to zero after  sim.handleDynamics  was called (or by using the following flag: sim.handleflag_resetforcetorque)
---@param shapeHandle integer
---@param position number[]
---@param force number[]
function sim.addForce(shapeHandle,position,force) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointTargetForce.htm
--- Sets the force or torque that a joint can exert
---@param objectHandle integer
---@param forceOrTorque number
---@param signedValue boolean
function sim.setJointTargetForce(objectHandle,forceOrTorque,signedValue) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointTargetForce.htm
--- Retrieves the force or torque that a joint can exert
---@param jointHandle integer
---@return number forceOrTorque
function sim.getJointTargetForce(jointHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetJointForce.htm
--- Retrieves the force or torque applied to a joint along/about its active axis. This function retrieves meaningful information only if the joint is prismatic or revolute, and is dynamically enabled. With the Bullet, MuJoCo and Newton engine, this function returns the force or torque applied to the joint motor  (torques from joint limits are not taken into account). With the ODE and Vortex engine, this function returns the total force or torque applied to a joint along/about its z-axis
---@param jointHandle integer
---@return number forceOrTorque
function sim.getJointForce(jointHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simReadForceSensor.htm
--- Reads the force and torque applied to a force sensor (filtered values are read)
---@param objectHandle integer
---@return integer result
---@return number[] forceVector
---@return number[] torqueVector
function sim.readForceSensor(objectHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSetJointTargetVelocity.htm
--- Sets the target linear/angular velocity of a non-spherical joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum acceleration and jerk values. In dynamic and velocity control mode, the controller is instructed about the desired velocity
---@param objectHandle integer
---@param targetVelocity number
---@param motionParams number[]
function sim.setJointTargetVelocity(objectHandle,targetVelocity,motionParams) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObjectFromUid.htm
--- Retrieves an object handle based on its unique identifier
---@param objectUid integer
---@param options table
---@return integer objectHandle
function sim.getObjectFromUid(objectUid,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simAddForceAndTorque.htm
--- Adds a force and/or torque to a shape object that is dynamically enabled. Forces are applied at the center of mass. Added forces and torques are cumulative, and are reset to zero after  sim.handleDynamics  was called (or by using the following flags: sim.handleflag_resetforce and/or sim.handleflag_resettorque)
---@param shapeHandle integer
---@param force number[]
---@param torque number[]
function sim.addForceAndTorque(shapeHandle,force,torque) end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetObject.htm
--- Retrieves an object handle based on its path and alias
---@param objectPath string
---@param options table
---@return integer objectHandle
function sim.getObject(objectPath,options) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCreateTexture.htm
--- Creates a planar shape, that will be textured with a new, or imported texture
---@param fileName string
---@param options integer
---@param planeSizes number[]
---@param scalingUV number[]
---@param xy_g number[]
---@param fixedResolution integer
---@param resolution integer[]
---@return integer shape
---@return integer id
---@return integer[] res
function sim.createTexture(fileName,options,planeSizes,scalingUV,xy_g,fixedResolution,resolution) end
--- url:https://manual.coppeliarobotics.com/en/sim/simLaunchExecutable.htm
--- Launches an executable. Similar to os.execute or io.popen, but is system independent.
---@param filename string
---@param parameters string
---@param showStatus integer
function sim.launchExecutable(filename,parameters,showStatus) end
--- url:https://manual.coppeliarobotics.com/en/sim/simExportMesh.htm
--- Exports a mesh to a file
---@param fileformat integer
---@param pathAndFilename string
---@param options integer
---@param scalingFactor number
---@param vertices number[]
---@param indices integer[]
function sim.exportMesh(fileformat,pathAndFilename,options,scalingFactor,vertices,indices) end
--- url:https://manual.coppeliarobotics.com/en/sim/simImportMesh.htm
--- Imports a mesh from a file
---@param fileformat integer
---@param pathAndFilename string
---@param options integer
---@param identicalVerticeTolerance number
---@param scalingFactor number
---@return number[] vertices
---@return integer[] indices
function sim.importMesh(fileformat,pathAndFilename,options,identicalVerticeTolerance,scalingFactor) end
--- url:https://manual.coppeliarobotics.com/en/sim/simImportShape.htm
--- Imports a  shape  from a file (first imports meshes, then groups/merges them into a shape)
---@param fileformat integer
---@param pathAndFilename string
---@param options integer
---@param identicalVerticeTolerance number
---@param scalingFactor number
---@return integer shapeHandle
function sim.importShape(fileformat,pathAndFilename,options,identicalVerticeTolerance,scalingFactor) end
--- url:https://manual.coppeliarobotics.com/en/sim/simLoadModel.htm
--- Loads a previously saved model, and selects it
---@param filename string
---@return integer objectHandle
function sim.loadModel(filename) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSaveModel.htm
--- Saves a model (an object marked as "Object is model base" and all other objects in its hierarchy tree). Any existing file with same name will be overwritten
---@param baseOfModelHandle integer
---@param filename string
---@return string modelData
function sim.saveModel(baseOfModelHandle,filename) end
--- url:https://manual.coppeliarobotics.com/en/sim/simLoadScene.htm
--- Loads a previously saved scene
---@param filenameOrBuffer string
function sim.loadScene(filenameOrBuffer) end
--- url:https://manual.coppeliarobotics.com/en/sim/simSaveScene.htm
--- Saves a scene. Any existing file with same name will be overwritten
---@param filename string
---@return string buffer
function sim.saveScene(filename) end
--- url:https://manual.coppeliarobotics.com/en/sim/simCloseScene.htm
--- Closes current scene, and switches to another open scene. If there is no other open scene, a new scene is then created. Can only be called from an  add-on , or from the sanbox script, when called from within CoppeliaSim
---@return integer result
function sim.closeScene() end
--- url:https://manual.coppeliarobotics.com/en/sim/simGetShapeGeomInfo.htm
--- Retrieves geometric information related to a shape
---@param shapeHandle integer
---@return integer result
---@return integer pureType
---@return number[] dimensions
function sim.getShapeGeomInfo(shapeHandle) end
--- url:https://manual.coppeliarobotics.com/en/sim/simDestroyGraphCurve.htm
--- Destroys a graph stream or curve
---@param graphHandle integer
---@param curveId integer
function sim.destroyGraphCurve(graphHandle,curveId) end
sim.handle_world=0
sim.objecttype_sceneobject=0
sim.objecttype_collection=0
sim.objecttype_mesh=0
sim.objecttype_texture=0
sim.sceneobject_shape=0
sim.sceneobject_joint=0
sim.sceneobject_graph=0
sim.sceneobject_camera=0
sim.sceneobject_light=0
sim.sceneobject_dummy=0
sim.sceneobject_proximitysensor=0
sim.sceneobject_octree=0
sim.sceneobject_pointcloud=0
sim.sceneobject_visionsensor=0
sim.sceneobject_forcesensor=0
sim.sceneobject_script=0
sim.light_omnidirectional=0
sim.light_spot=0
sim.light_directional=0
sim.joint_revolute=0
sim.joint_prismatic=0
sim.joint_spherical=0
sim.shape_simple=0
sim.shape_compound=0
sim.proximitysensor_ray=0
sim.proximitysensor_pyramid=0
sim.proximitysensor_cylinder=0
sim.proximitysensor_disc=0
sim.proximitysensor_cone=0
sim.message_model_loaded=0
sim.message_scene_loaded=0
sim.message_keypress=0
sim.displayattribute_renderpass=0
sim.displayattribute_depthpass=0
sim.displayattribute_pickpass=0
sim.displayattribute_selected=0
sim.displayattribute_groupselection=0
sim.displayattribute_mainselection=0
sim.displayattribute_forcewireframe=0
sim.displayattribute_forbidwireframe=0
sim.displayattribute_forbidedges=0
sim.displayattribute_originalcolors=0
sim.displayattribute_ignorelayer=0
sim.displayattribute_forvisionsensor=0
sim.displayattribute_trianglewireframe=0
sim.displayattribute_simplifyasboundingbox=0
sim.displayattribute_thickedges=0
sim.displayattribute_dynamiccontentonly=0
sim.displayattribute_useauxcomponent=0
sim.displayattribute_ignorerenderableflag=0
sim.displayattribute_noopenglcallbacks=0
sim.displayattribute_nopointclouds=0
sim.displayattribute_nodrawingobjects=0
sim.displayattribute_noparticles=0
sim.displayattribute_colorcodedtriangles=0
sim.simulation_stopped=0
sim.simulation_paused=0
sim.simulation_advancing_firstafterstop=0
sim.simulation_advancing_running=0
sim.simulation_advancing_lastbeforepause=0
sim.simulation_advancing_firstafterpause=0
sim.simulation_advancing_abouttostop=0
sim.simulation_advancing_lastbeforestop=0
sim.scripttype_main=0
sim.scripttype_simulation=0
sim.scripttype_addon=0
sim.scripttype_customization=0
sim.scripttype_sandbox=0
sim.scripttype_passive=0
sim.scriptexecorder_first=0
sim.scriptexecorder_normal=0
sim.scriptexecorder_last=0
sim.handle_absolute=0
sim.handle_all=0
sim.handle_all_except_explicit=0
sim.handle_self=0
sim.handle_main_script=0
sim.handle_tree=0
sim.handle_chain=0
sim.handle_single=0
sim.handle_default=0
sim.handle_all_except_self=0
sim.handle_parent=0
sim.handle_scene=0
sim.handle_app=0
sim.handle_appstorage=0
sim.handle_inverse=0
sim.handleflag_assembly=0
sim.handleflag_model=0
sim.handleflag_rawvalue=0
sim.handleflag_togglevisibility=0
sim.handleflag_greyscale=0
sim.handleflag_depthbuffermeters=0
sim.handleflag_depthbuffer=0
sim.handleflag_abscoords=0
sim.handleflag_codedstring=0
sim.handleflag_keeporiginal=0
sim.handleflag_camera=0
sim.handleflag_axis=0
sim.handleflag_silenterror=0
sim.handleflag_resetforce=0
sim.handleflag_resettorque=0
sim.handleflag_absolutecoords=0
sim.handleflag_relativecoords=0
sim.handleflag_wxyzquat=0
sim.handleflag_reljointbaseframe=0
sim.handleflag_addmultiple=0
sim.dlgstyle_message=0
sim.dlgstyle_input=0
sim.dlgstyle_ok=0
sim.dlgstyle_ok_cancel=0
sim.dlgstyle_yes_no=0
sim.dlgret_still_open=0
sim.dlgret_ok=0
sim.dlgret_cancel=0
sim.dlgret_yes=0
sim.dlgret_no=0
sim.drawing_points=0
sim.drawing_lines=0
sim.drawing_linestrip=0
sim.drawing_triangles=0
sim.drawing_trianglepts=0
sim.drawing_quadpts=0
sim.drawing_discpts=0
sim.drawing_cubepts=0
sim.drawing_spherepts=0
sim.drawing_cyclic=0
sim.drawing_local=0
sim.drawing_painttag=0
sim.drawing_overlay=0
sim.particle_points1=0
sim.particle_points2=0
sim.particle_points4=0
sim.particle_roughspheres=0
sim.particle_spheres=0
sim.particle_respondable1to4=0
sim.particle_respondable5to8=0
sim.particle_particlerespondable=0
sim.particle_ignoresgravity=0
sim.particle_invisible=0
sim.particle_painttag=0
sim.particle_cyclic=0
sim.particle_water=0
sim.verbosity_useglobal=0
sim.verbosity_none=0
sim.verbosity_errors=0
sim.verbosity_warnings=0
sim.verbosity_loadinfos=0
sim.verbosity_questions=0
sim.verbosity_scripterrors=0
sim.verbosity_scriptwarnings=0
sim.verbosity_scriptinfos=0
sim.verbosity_infos=0
sim.verbosity_debug=0
sim.verbosity_trace=0
sim.verbosity_tracelua=0
sim.verbosity_traceall=0
sim.verbosity_default=0
sim.plugininfo_extversionstr=0
sim.plugininfo_builddatestr=0
sim.plugininfo_extversionint=0
sim.plugininfo_verbosity=0
sim.plugininfo_statusbarverbosity=0
sim.navigation_passive=0
sim.navigation_camerashift=0
sim.navigation_camerarotate=0
sim.navigation_camerazoom=0
sim.navigation_cameratilt=0
sim.navigation_cameraangle=0
sim.navigation_objectshift=0
sim.navigation_objectrotate=0
sim.navigation_clickselection=0
sim.navigation_ctrlselection=0
sim.navigation_shiftselection=0
sim.navigation_camerazoomwheel=0
sim.navigation_camerarotatemiddlebutton=0
sim.jointmode_kinematic=0
sim.jointmode_dependent=0
sim.jointmode_dynamic=0
sim.jointdynctrl_free=0
sim.jointdynctrl_force=0
sim.jointdynctrl_velocity=0
sim.jointdynctrl_position=0
sim.jointdynctrl_spring=0
sim.jointdynctrl_callback=0
sim.ruckig_phasesync=0
sim.ruckig_timesync=0
sim.ruckig_nosync=0
sim.primitiveshape_none=0
sim.primitiveshape_plane=0
sim.primitiveshape_disc=0
sim.primitiveshape_cuboid=0
sim.primitiveshape_spheroid=0
sim.primitiveshape_cylinder=0
sim.primitiveshape_cone=0
sim.primitiveshape_capsule=0
sim.primitiveshape_heightfield=0
sim.dummytype_default=0
sim.dummytype_assembly=0
sim.dummytype_dynloopclosure=0
sim.dummytype_dyntendon=0
sim.texturemap_plane=0
sim.texturemap_cylinder=0
sim.texturemap_sphere=0
sim.texturemap_cube=0
sim.colorcomponent_ambient_diffuse=0
sim.colorcomponent_diffuse=0
sim.colorcomponent_specular=0
sim.colorcomponent_emission=0
sim.colorcomponent_transparency=0
sim.colorcomponent_auxiliary=0
sim.volume_pyramid=0
sim.volume_cylinder=0
sim.volume_disc=0
sim.volume_cone=0
sim.volume_ray=0
sim.volume_randomizedray=0
sim.buffer_uint8=0
sim.buffer_uint8rgb=0
sim.buffer_uint8bgr=0
sim.buffer_uint8rgba=0
sim.buffer_uint8argb=0
sim.buffer_float=0
sim.buffer_int32=0
sim.buffer_double=0
sim.buffer_base64=0
sim.imgcomb_vertical=0
sim.imgcomb_horizontal=0
sim.stream_transf_raw=0
sim.stream_transf_derivative=0
sim.stream_transf_integral=0
sim.stream_transf_cumulative=0
sim.bullet_constraintsolvertype_sequentialimpulse=0
sim.bullet_constraintsolvertype_nncg=0
sim.bullet_constraintsolvertype_dantzig=0
sim.bullet_constraintsolvertype_projectedgaussseidel=0
sim.vortex_bodyfrictionmodel_box=0
sim.vortex_bodyfrictionmodel_scaledbox=0
sim.vortex_bodyfrictionmodel_proplow=0
sim.vortex_bodyfrictionmodel_prophigh=0
sim.vortex_bodyfrictionmodel_scaledboxfast=0
sim.vortex_bodyfrictionmodel_neutral=0
sim.vortex_bodyfrictionmodel_none=0
sim.objintparam_visibility_layer=0
sim.objfloatparam_abs_x_velocity=0
sim.objfloatparam_abs_y_velocity=0
sim.objfloatparam_abs_z_velocity=0
sim.objfloatparam_abs_rot_velocity=0
sim.objfloatparam_objbbox_min_x=0
sim.objfloatparam_objbbox_min_y=0
sim.objfloatparam_objbbox_min_z=0
sim.objfloatparam_objbbox_max_x=0
sim.objfloatparam_objbbox_max_y=0
sim.objfloatparam_objbbox_max_z=0
sim.objfloatparam_modelbbox_min_x=0
sim.objfloatparam_modelbbox_min_y=0
sim.objfloatparam_modelbbox_min_z=0
sim.objfloatparam_modelbbox_max_x=0
sim.objfloatparam_modelbbox_max_y=0
sim.objfloatparam_modelbbox_max_z=0
sim.objintparam_collection_self_collision_indicator=0
sim.objfloatparam_transparency_offset=0
sim.objintparam_manipulation_permissions=0
sim.objintparam_illumination_handle=0
sim.objfloatparam_size_factor=0
sim.objstringparam_unique_id=0
sim.objintparam_visible=0
sim.visionfloatparam_near_clipping=0
sim.visionfloatparam_far_clipping=0
sim.visionintparam_resolution_x=0
sim.visionintparam_resolution_y=0
sim.visionfloatparam_perspective_angle=0
sim.visionfloatparam_ortho_size=0
sim.visionintparam_disabled_light_components=0
sim.visionintparam_rendering_attributes=0
sim.visionintparam_entity_to_render=0
sim.visionintparam_windowed_size_x=0
sim.visionintparam_windowed_size_y=0
sim.visionintparam_windowed_pos_x=0
sim.visionintparam_windowed_pos_y=0
sim.visionintparam_pov_focal_blur=0
sim.visionfloatparam_pov_blur_distance=0
sim.visionfloatparam_pov_aperture=0
sim.visionintparam_pov_blur_sampled=0
sim.visionintparam_render_mode=0
sim.visionintparam_perspective_operation=0
sim.visionfarrayparam_viewfrustum=0
sim.visionintparam_rgbignored=0
sim.visionintparam_depthignored=0
sim.jointfloatparam_intrinsic_x=0
sim.jointfloatparam_intrinsic_y=0
sim.jointfloatparam_intrinsic_z=0
sim.jointfloatparam_intrinsic_qx=0
sim.jointfloatparam_intrinsic_qy=0
sim.jointfloatparam_intrinsic_qz=0
sim.jointfloatparam_intrinsic_qw=0
sim.jointfloatparam_velocity=0
sim.jointfloatparam_spherical_qx=0
sim.jointfloatparam_spherical_qy=0
sim.jointfloatparam_spherical_qz=0
sim.jointfloatparam_spherical_qw=0
sim.jointfloatparam_upper_limit=0
sim.jointfloatparam_kc_k=0
sim.jointfloatparam_kc_c=0
sim.jointfloatparam_error_x=0
sim.jointfloatparam_error_y=0
sim.jointfloatparam_error_z=0
sim.jointfloatparam_error_a=0
sim.jointfloatparam_error_b=0
sim.jointfloatparam_error_g=0
sim.jointfloatparam_error_pos=0
sim.jointfloatparam_error_angle=0
sim.jointintparam_vortex_dep_handle=0
sim.jointfloatparam_vortex_dep_multiplication=0
sim.jointfloatparam_vortex_dep_offset=0
sim.jointfloatparam_screwlead=0
sim.jointfloatparam_maxvel=0
sim.jointfloatparam_maxaccel=0
sim.jointfloatparam_maxjerk=0
sim.jointintparam_dynctrlmode=0
sim.jointintparam_dynvelctrltype=0
sim.jointintparam_dynposctrltype=0
sim.shapefloatparam_init_velocity_x=0
sim.shapefloatparam_init_velocity_y=0
sim.shapefloatparam_init_velocity_z=0
sim.shapeintparam_static=0
sim.shapeintparam_kinematic=0
sim.shapeintparam_respondable=0
sim.shapeintparam_respondablesuspendcnt=0
sim.shapefloatparam_mass=0
sim.shapefloatparam_texture_x=0
sim.shapefloatparam_texture_y=0
sim.shapefloatparam_texture_z=0
sim.shapefloatparam_texture_a=0
sim.shapefloatparam_texture_b=0
sim.shapefloatparam_texture_g=0
sim.shapefloatparam_texture_scaling_x=0
sim.shapefloatparam_texture_scaling_y=0
sim.shapeintparam_culling=0
sim.shapeintparam_wireframe=0
sim.shapeintparam_compound=0
sim.shapeintparam_convex=0
sim.shapeintparam_convex_check=0
sim.shapeintparam_respondable_mask=0
sim.shapefloatparam_init_velocity_a=0
sim.shapefloatparam_init_velocity_b=0
sim.shapefloatparam_init_velocity_g=0
sim.shapestringparam_colorname=0
sim.shapeintparam_edge_visibility=0
sim.shapefloatparam_shading_angle=0
sim.shapefloatparam_edge_angle=0
sim.shapeintparam_edge_borders_hidden=0
sim.shapeintparam_component_cnt=0
sim.shapeintparam_sleepmodestart=0
sim.proxintparam_ray_invisibility=0
sim.proxintparam_volume_type=0
sim.proxintparam_entity_to_detect=0
sim.forcefloatparam_error_x=0
sim.forcefloatparam_error_y=0
sim.forcefloatparam_error_z=0
sim.forcefloatparam_error_a=0
sim.forcefloatparam_error_b=0
sim.forcefloatparam_error_g=0
sim.forcefloatparam_error_pos=0
sim.forcefloatparam_error_angle=0
sim.graphintparam_needs_refresh=0
sim.lightintparam_pov_casts_shadows=0
sim.lightfloatparam_spot_exponent=0
sim.lightfloatparam_spot_cutoff=0
sim.lightfloatparam_const_attenuation=0
sim.lightfloatparam_lin_attenuation=0
sim.lightfloatparam_quad_attenuation=0
sim.cameraintparam_disabled_light_components=0
sim.camerafloatparam_perspective_angle=0
sim.camerafloatparam_ortho_size=0
sim.cameraintparam_rendering_attributes=0
sim.cameraintparam_pov_focal_blur=0
sim.camerafloatparam_pov_blur_distance=0
sim.camerafloatparam_pov_aperture=0
sim.cameraintparam_pov_blur_samples=0
sim.camerafloatparam_near_clipping=0
sim.camerafloatparam_far_clipping=0
sim.cameraintparam_perspective_operation=0
sim.cameraintparam_remotecameramode=0
sim.camerafarrayparam_viewfrustum=0
sim.dummyintparam_dummytype=0
sim.dummyfloatparam_size=0
sim.dummystringparam_assemblytag=0
sim.scriptintparam_execorder=0
sim.scriptintparam_execcount=0
sim.scriptintparam_type=0
sim.scriptintparam_enabled=0
sim.scriptintparam_autorestartonerror=0
sim.scriptstringparam_description=0
sim.scriptstringparam_name=0
sim.scriptstringparam_text=0
sim.scriptstringparam_namext=0
sim.scriptstringparam_lang=0

return sim