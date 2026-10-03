---@diagnostic disable: missing-return
local simROS2={}
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionClientTreatUInt8ArrayAsString
--- After calling this function, this action client will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
---@param actionClientHandle string
function simROS2.actionClientTreatUInt8ArrayAsString(actionClientHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionAbort
--- Indicate that a goal could not be reached and has been aborted. Only call this if the goal was executing but cannot be completed. This is a terminal state, no more methods should be called on a goal after this is called.
---@param actionServerHandle string
---@param goalUUID string
---@param result table
function simROS2.actionServerActionAbort(actionServerHandle,goalUUID,result) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionCanceled
--- Indicate that a goal has been canceled. Only call this if the goal is executing or pending, but has been canceled. This is a terminal state, no more methods should be called on a goal after this is called.
---@param actionServerHandle string
---@param goalUUID string
---@param result table
function simROS2.actionServerActionCanceled(actionServerHandle,goalUUID,result) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionExecute
--- Indicate that the server is starting to execute a goal. Only call this if the goal is pending.
---@param actionServerHandle string
---@param goalUUID string
function simROS2.actionServerActionExecute(actionServerHandle,goalUUID) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionIsActive
--- Check if goal is pending or executing
---@param actionServerHandle string
---@param goalUUID string
---@return boolean result
function simROS2.actionServerActionIsActive(actionServerHandle,goalUUID) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionIsCanceling
--- Check if there is a cancel request
---@param actionServerHandle string
---@param goalUUID string
---@return boolean result
function simROS2.actionServerActionIsCanceling(actionServerHandle,goalUUID) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionIsExecuting
--- Check if the goal is executing
---@param actionServerHandle string
---@param goalUUID string
---@return boolean result
function simROS2.actionServerActionIsExecuting(actionServerHandle,goalUUID) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionSucceed
--- Indicate that a goal has succeeded. Only call this if the goal is executing and has reached the desired final state. This is a terminal state, no more methods should be called on a goal after this is called.
---@param actionServerHandle string
---@param goalUUID string
---@param result table
function simROS2.actionServerActionSucceed(actionServerHandle,goalUUID,result) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerPublishFeedback
--- Send an update about the progress of this goal. This must be only called when the goal is executing. If execution of a goal is deferred then
---@param actionServerHandle string
---@param goalUUID string
---@param feedback table
function simROS2.actionServerPublishFeedback(actionServerHandle,goalUUID,feedback) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerTreatUInt8ArrayAsString
--- After calling this function, this action server will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
---@param actionServerHandle string
function simROS2.actionServerTreatUInt8ArrayAsString(actionServerHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#call
--- Call the service associated with this service client.
---@param clientHandle string
---@param request table
---@return table result
function simROS2.call(clientHandle,request) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#cancelLastGoal
--- Cancel last submitted goal on the specified action client.
---@param actionClientHandle string
---@return boolean success
function simROS2.cancelLastGoal(actionClientHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#clientTreatUInt8ArrayAsString
--- After calling this function, this service client will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
---@param clientHandle string
function simROS2.clientTreatUInt8ArrayAsString(clientHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createActionClient
--- Create a action client.
---@param actionName string
---@param actionType string
---@param goalResponseCallback function
---@param feedbackCallback function
---@param resultCallback function
---@return string actionClientHandle
function simROS2.createActionClient(actionName,actionType,goalResponseCallback,feedbackCallback,resultCallback) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createActionServer
--- Create an action server.
---@param actionName string
---@param actionType string
---@param handleGoalCallback function
---@param handleCancelCallback function
---@param handleAcceptedCallback function
---@return string actionServerHandle
function simROS2.createActionServer(actionName,actionType,handleGoalCallback,handleCancelCallback,handleAcceptedCallback) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createClient
--- Create a service client.
---@param serviceName string
---@param serviceType string
---@return string clientHandle
function simROS2.createClient(serviceName,serviceType) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createInterface
--- Construct an interface of the specified type, initialized with the default values.
---@param type string
---@return table result
function simROS2.createInterface(type) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createPublisher
--- Create a topic publisher.
---@param topicName string
---@param topicType string
---@param unused integer
---@param unused2 boolean
---@param qos simros2_qos
---@return string publisherHandle
function simROS2.createPublisher(topicName,topicType,unused,unused2,qos) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createService
--- Create a service.
---@param serviceName string
---@param serviceType string
---@param serviceCallback function
---@return string serviceHandle
function simROS2.createService(serviceName,serviceType,serviceCallback) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createSubscription
--- Create a subscription to a topic.
---@param topicName string
---@param topicType string
---@param topicCallback function
---@param unused integer
---@param qos simros2_qos
---@return string subscriptionHandle
function simROS2.createSubscription(topicName,topicType,topicCallback,unused,qos) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#deleteParam
--- Delete a parameter in the ROS Parameter Server.
---@param name string
function simROS2.deleteParam(name) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getInterfaceConstants
--- Get an object with the constants defined in the specified interface.
---@param type string
---@return table result
function simROS2.getInterfaceConstants(type) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamBool
--- Retrieve a boolean parameter from the ROS Parameter Server.
---@param name string
---@param defaultValue boolean
---@return boolean exists
---@return boolean value
function simROS2.getParamBool(name,defaultValue) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamDouble
--- Retrieve a double parameter from the ROS Parameter Server.
---@param name string
---@param defaultValue number
---@return boolean exists
---@return number value
function simROS2.getParamDouble(name,defaultValue) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamInt
--- Retrieve an integer parameter from the ROS Parameter Server.
---@param name string
---@param defaultValue integer
---@return boolean exists
---@return integer value
function simROS2.getParamInt(name,defaultValue) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamString
--- Retrieve a string parameter from the ROS Parameter Server.
---@param name string
---@param defaultValue string
---@return boolean exists
---@return string value
function simROS2.getParamString(name,defaultValue) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getSimulationTime
--- 

function simROS2.getSimulationTime() end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getSystemTime
--- 

function simROS2.getSystemTime() end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getTime
--- Return the current time according to the specified clock.
---@param clock_type integer
---@return simros2_time time
function simROS2.getTime(clock_type) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#hasParam
--- Check wether a parameter exists in the ROS Parameter Server.
---@param name string
---@return boolean exists
function simROS2.hasParam(name) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportCreatePublisher
--- Create a publisher using ImageTransport.
---@param topicName string
---@param queueSize integer
---@return string publisherHandle
function simROS2.imageTransportCreatePublisher(topicName,queueSize) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportCreateSubscription
--- Create a subscription using ImageTransport.
---@param topicName string
---@param topicCallback function
---@param queueSize integer
---@return string subscriptionHandle
function simROS2.imageTransportCreateSubscription(topicName,topicCallback,queueSize) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportPublish
--- Publish a message on the topic associated with this publisher using ImageTransport.
---@param publisherHandle string
---@param data string
---@param width integer
---@param height integer
---@param frame_id string
function simROS2.imageTransportPublish(publisherHandle,data,width,height,frame_id) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportShutdownPublisher
--- Shutdown the publisher using ImageTransport.
---@param publisherHandle string
function simROS2.imageTransportShutdownPublisher(publisherHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportShutdownSubscription
--- Shutdown the subscription using ImageTransport.
---@param subscriptionHandle string
function simROS2.imageTransportShutdownSubscription(subscriptionHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#importInterface
--- 
---@param name string
function simROS2.importInterface(name) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#publish
--- Publish a message on the topic associated with this publisher.
---@param publisherHandle string
---@param message table
function simROS2.publish(publisherHandle,message) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#publisherTreatUInt8ArrayAsString
--- After calling this function, this publisher will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
---@param publisherHandle string
function simROS2.publisherTreatUInt8ArrayAsString(publisherHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#sendGoal
--- Send a goal using the specified action client.
---@param actionClientHandle string
---@param goal table
---@return boolean success
function simROS2.sendGoal(actionClientHandle,goal) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#sendTransform
--- Publish a TF transformation between frames.
---@param transform table
function simROS2.sendTransform(transform) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#sendTransforms
--- Publish several TF transformations between frames.
---@param transforms table
function simROS2.sendTransforms(transforms) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#serviceTreatUInt8ArrayAsString
--- After calling this function, this service will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
---@param serviceHandle string
function simROS2.serviceTreatUInt8ArrayAsString(serviceHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamBool
--- Set a boolean parameter in the ROS Parameter Server.
---@param name string
---@param value boolean
function simROS2.setParamBool(name,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamDouble
--- Set a double parameter in the ROS Parameter Server.
---@param name string
---@param value number
function simROS2.setParamDouble(name,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamInt
--- Set a integer parameter in the ROS Parameter Server.
---@param name string
---@param value integer
function simROS2.setParamInt(name,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamString
--- Set a string parameter in the ROS Parameter Server.
---@param name string
---@param value string
function simROS2.setParamString(name,value) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownActionClient
--- Shutdown the action client.
---@param actionClientHandle string
function simROS2.shutdownActionClient(actionClientHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownActionServer
--- Shutdown the action server.
---@param actionServerHandle string
function simROS2.shutdownActionServer(actionServerHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownClient
--- Shutdown the service client.
---@param clientHandle string
function simROS2.shutdownClient(clientHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownPublisher
--- Shutdown the specified publisher.
---@param publisherHandle string
function simROS2.shutdownPublisher(publisherHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownService
--- Shutdown the service.
---@param serviceHandle string
function simROS2.shutdownService(serviceHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownSubscription
--- Shutdown the subscription.
---@param subscriptionHandle string
function simROS2.shutdownSubscription(subscriptionHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#spinSome
--- Calls spin_some(node).

function simROS2.spinSome() end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#subscriptionTreatUInt8ArrayAsString
--- After calling this function, this subscription will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
---@param subscriptionHandle string
function simROS2.subscriptionTreatUInt8ArrayAsString(subscriptionHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#supportedInterfaces
--- Retrieve a list of supported interfaces.
---@return string[] result
function simROS2.supportedInterfaces() end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#timeFromFloat
--- 
---@param t number
function simROS2.timeFromFloat(t) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#timeToFloat
--- 
---@param t table
function simROS2.timeToFloat(t) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#waitForService
--- Wait for the service associated with this service client.
---@param clientHandle string
---@param timeout number
---@return boolean result
function simROS2.waitForService(clientHandle,timeout) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#subscriptionCallback
--- Callback for ROS subscription.
---@param message table
function simROS2.subscriptionCallback(message) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportCallback
--- Callback for ROS ImageTransport subscription.
---@param data string
---@param width integer
---@param height integer
function simROS2.imageTransportCallback(data,width,height) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionGoalResponseCallback
--- Callback for action client goal response.
---@param goalID string
---@param accepted boolean
function simROS2.actionGoalResponseCallback(goalID,accepted) end
return simROS2