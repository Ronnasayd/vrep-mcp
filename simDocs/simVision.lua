---@diagnostic disable: missing-return
local simVision={}
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.createVelodyneHDL64E
--- Creates a handle for generating data similar to a Velodyne HDL64E. See also
---@param visionSensorHandles integer[]
---@param frequency number
---@param options integer
---@param pointSize integer
---@param coloring_closeFarDist number[]
---@param displayScalingFactor number
---@param pointCloudHandle integer
---@return integer handle
function simVision.createVelodyneHDL64E(visionSensorHandles,frequency,options,pointSize,coloring_closeFarDist,displayScalingFactor,pointCloudHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.createVelodyneVPL16
--- Creates a handle for generating data similar to a Velodyne VPL16. See also
---@param visionSensorHandles integer[]
---@param frequency number
---@param options integer
---@param pointSize integer
---@param coloring_closeFarDist number[]
---@param displayScalingFactor number
---@param pointCloudHandle integer
---@return integer handle
function simVision.createVelodyneVPL16(visionSensorHandles,frequency,options,pointSize,coloring_closeFarDist,displayScalingFactor,pointCloudHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.destroyVelodyneHDL64E
--- Deletes a Velodyne HDL64E handle previously created with
---@param velodyneHandle integer
function simVision.destroyVelodyneHDL64E(velodyneHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.destroyVelodyneVPL16
--- Deletes a Velodyne VPL16 handle previously created with
---@param velodyneHandle integer
function simVision.destroyVelodyneVPL16(velodyneHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.distort
--- Transforms (distorts) a vision sensor image via pixel remapping.
---@param visionSensorHandle integer
---@param pixelMap integer[]
---@param depthScalings number[]
function simVision.distort(visionSensorHandle,pixelMap,depthScalings) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleAnaglyphStereo
--- Allows to generate an anaglyph stereo image from two individual vision sensors (for the left and right eye).
---@param rgbVisionSensorHandle integer
---@param handlesOfTwoVisionSensors integer[]
---@param leftAndRightColors number[]
function simVision.handleAnaglyphStereo(rgbVisionSensorHandle,handlesOfTwoVisionSensors,leftAndRightColors) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleSpherical
--- Allows to generate an RGB and/or depth image that covers all directions, i.e. spherical vision, based on the input of 6 individual vision sensors, each looking into a different and perpendicular direction.
---@param rgbVisionSensorHandle integer
---@param handlesOfSixVisionSensors integer[]
---@param horizontalAngle number
---@param verticalAngle number
---@param depthVisionSensorHandle integer
function simVision.handleSpherical(rgbVisionSensorHandle,handlesOfSixVisionSensors,horizontalAngle,verticalAngle,depthVisionSensorHandle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleVelodyneHDL64E
--- Handles a velodyne HDL64E sensor (i.e. generates and displays detection points. See also
---@param velodyneHandle integer
---@param dt number
---@return string points
---@return string colors
function simVision.handleVelodyneHDL64E(velodyneHandle,dt) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleVelodyneVPL16
--- Handles a velodyne VPL16 sensor (i.e. generates and displays detection points. See also
---@param velodyneHandle integer
---@param dt number
---@return string points
---@return string colors
function simVision.handleVelodyneVPL16(velodyneHandle,dt) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.addBuffer1ToWorkImg
--- Performs a pixel wise addition between the
---@param handle integer
function simVision.addBuffer1ToWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.addWorkImgToBuffer1
--- Performs a pixel wise addition between the
---@param handle integer
function simVision.addWorkImgToBuffer1(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.binaryWorkImg
--- Transforms the
---@param handle integer
---@param threshold number
---@param oneProportion number
---@param oneTol number
---@param xCenter number
---@param xCenterTol number
---@param yCenter number
---@param yCenterTol number
---@param orient number
---@param orientTol number
---@param roundness number
---@param enableTrigger boolean
---@param overlayColor number[]
---@return integer trigger
---@return string packedPacket
function simVision.binaryWorkImg(handle,threshold,oneProportion,oneTol,xCenter,xCenterTol,yCenter,yCenterTol,orient,orientTol,roundness,enableTrigger,overlayColor) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.blobDetectionOnWorkImg
--- Performs blob detection on the
---@param handle integer
---@param threshold number
---@param minBlobSize number
---@param diffColor boolean
---@param overlayColor number[]
---@return integer trigger
---@return string packedPacket
function simVision.blobDetectionOnWorkImg(handle,threshold,minBlobSize,diffColor,overlayColor) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.buffer1ToWorkImg
--- Copies buffer
---@param handle integer
function simVision.buffer1ToWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.buffer2ToWorkImg
--- Copies buffer
---@param handle integer
function simVision.buffer2ToWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.changedPixelsOnWorkImg
--- Returns the pixels that changed the
---@param handle integer
---@param threshold number
---@return integer trigger
---@return string packedPacket
function simVision.changedPixelsOnWorkImg(handle,threshold) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.circularCutWorkImg
--- Performs a circular cut on the
---@param handle integer
---@param radius number
---@param toBuffer1 boolean
function simVision.circularCutWorkImg(handle,radius,toBuffer1) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.colorSegmentationOnWorkImg
--- Performs a color segmentation on the
---@param handle integer
---@param colorDistance number
function simVision.colorSegmentationOnWorkImg(handle,colorDistance) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.coordinatesFromWorkImg
--- Extracts coordinates from the
---@param handle integer
---@param pointCount integer[]
---@param angularSpace boolean
---@param returnColorData boolean
---@return integer trigger
---@return string packedPacket
---@return string colorData
function simVision.coordinatesFromWorkImg(handle,pointCount,angularSpace,returnColorData) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.edgeDetectionOnWorkImg
--- Applies an edge detection filter to the
---@param handle integer
---@param threshold number
function simVision.edgeDetectionOnWorkImg(handle,threshold) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.horizontalFlipWorkImg
--- Horizontally flips the
---@param handle integer
function simVision.horizontalFlipWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.intensityScaleOnWorkImg
--- Transforms the
---@param handle integer
---@param start number
---@param end number
---@param greyscale boolean
function simVision.intensityScaleOnWorkImg(handle,start,end,greyscale) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.matrix3x3OnWorkImg
--- Applies a 3X3 matrix filter to the
---@param handle integer
---@param passes integer
---@param multiplier number
---@param matrix number[]
function simVision.matrix3x3OnWorkImg(handle,passes,multiplier,matrix) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.matrix5x5OnWorkImg
--- Applies a 5X5 matrix filter to the
---@param handle integer
---@param passes integer
---@param multiplier number
function simVision.matrix5x5OnWorkImg(handle,passes,multiplier) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.multiplyWorkImgWithBuffer1
--- Multiplies (pixel wise) the
---@param handle integer
function simVision.multiplyWorkImgWithBuffer1(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.normalizeWorkImg
--- Normalizes the
---@param handle integer
function simVision.normalizeWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.rectangularCutWorkImg
--- Performs a rectangular cut on the
---@param handle integer
---@param rectangle number[]
---@param toBuffer1 boolean
function simVision.rectangularCutWorkImg(handle,rectangle,toBuffer1) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.resizeWorkImg
--- Scales the
---@param handle integer
---@param scaling number[]
function simVision.resizeWorkImg(handle,scaling) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.rotateWorkImg
--- Performs a rotation of the
---@param handle integer
---@param angle number
function simVision.rotateWorkImg(handle,angle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.scaleAndOffsetWorkImg
--- Shifts and scales colors of the
---@param handle integer
---@param colorPreOffset number[]
---@param colorScaling number[]
---@param colorPostOffset number[]
---@param rgbSpace boolean
function simVision.scaleAndOffsetWorkImg(handle,colorPreOffset,colorScaling,colorPostOffset,rgbSpace) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.selectiveColorOnWorkImg
--- Selects a specific color in the RGB or HSL space of the
---@param handle integer
---@param nominalColor number[]
---@param colorTolerance number[]
---@param rgbSpace boolean
---@param keepColor boolean
---@param toBuffer1 boolean
function simVision.selectiveColorOnWorkImg(handle,nominalColor,colorTolerance,rgbSpace,keepColor,toBuffer1) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.sensorDepthMapToWorkImg
--- Copies the depth buffer acquired by a vision sensor to the
---@param handle integer
function simVision.sensorDepthMapToWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.sensorImgToWorkImg
--- Copies the RGB image acquired by a vision sensor to the
---@param handle integer
function simVision.sensorImgToWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.sharpenWorkImg
--- Sharpens the
---@param handle integer
function simVision.sharpenWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.shiftWorkImg
--- Shifts the
---@param handle integer
---@param shift number[]
---@param wrap boolean
function simVision.shiftWorkImg(handle,shift,wrap) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.subtractBuffer1FromWorkImg
--- Subtracts (pixel wise subtraction) buffer
---@param handle integer
function simVision.subtractBuffer1FromWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.subtractWorkImgFromBuffer1
--- Subtracts (pixel wise subtraction) the
---@param handle integer
function simVision.subtractWorkImgFromBuffer1(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.swapBuffers
--- Swaps buffer
---@param handle integer
function simVision.swapBuffers(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.swapWorkImgWithBuffer1
--- Swaps the
---@param handle integer
function simVision.swapWorkImgWithBuffer1(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.uniformImgToWorkImg
--- Applies a uniform color to the
---@param handle integer
---@param color number[]
function simVision.uniformImgToWorkImg(handle,color) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.velodyneDataFromWorkImg
--- Extracts Velodyne coordinates from the
---@param handle integer
---@param pointCount integer[]
---@param verticalScanAngle number
---@param returnColorData boolean
---@return integer trigger
---@return string packedPacket
---@return string colorData
function simVision.velodyneDataFromWorkImg(handle,pointCount,verticalScanAngle,returnColorData) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.verticalFlipWorkImg
--- Vertically flips the
---@param handle integer
function simVision.verticalFlipWorkImg(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToBuffer1
--- Copies the
---@param handle integer
function simVision.workImgToBuffer1(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToBuffer2
--- Copies the
---@param handle integer
function simVision.workImgToBuffer2(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToSensorDepthMap
--- Copies the
---@param handle integer
function simVision.workImgToSensorDepthMap(handle) end
--- url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToSensorImg
--- Copies the
---@param handle integer
function simVision.workImgToSensorImg(handle) end
return simVision