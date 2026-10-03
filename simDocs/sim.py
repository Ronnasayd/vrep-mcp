from typing import Union


class Sim:
    handle_world: int
    objecttype_sceneobject: int
    objecttype_collection: int
    objecttype_mesh: int
    objecttype_texture: int
    sceneobject_shape: int
    sceneobject_joint: int
    sceneobject_graph: int
    sceneobject_camera: int
    sceneobject_light: int
    sceneobject_dummy: int
    sceneobject_proximitysensor: int
    sceneobject_octree: int
    sceneobject_pointcloud: int
    sceneobject_visionsensor: int
    sceneobject_forcesensor: int
    sceneobject_script: int
    light_omnidirectional: int
    light_spot: int
    light_directional: int
    joint_revolute: int
    joint_prismatic: int
    joint_spherical: int
    shape_simple: int
    shape_compound: int
    proximitysensor_ray: int
    proximitysensor_pyramid: int
    proximitysensor_cylinder: int
    proximitysensor_disc: int
    proximitysensor_cone: int
    message_model_loaded: int
    message_scene_loaded: int
    message_keypress: int
    displayattribute_renderpass: int
    displayattribute_depthpass: int
    displayattribute_pickpass: int
    displayattribute_selected: int
    displayattribute_groupselection: int
    displayattribute_mainselection: int
    displayattribute_forcewireframe: int
    displayattribute_forbidwireframe: int
    displayattribute_forbidedges: int
    displayattribute_originalcolors: int
    displayattribute_ignorelayer: int
    displayattribute_forvisionsensor: int
    displayattribute_trianglewireframe: int
    displayattribute_simplifyasboundingbox: int
    displayattribute_thickedges: int
    displayattribute_dynamiccontentonly: int
    displayattribute_useauxcomponent: int
    displayattribute_ignorerenderableflag: int
    displayattribute_noopenglcallbacks: int
    displayattribute_nopointclouds: int
    displayattribute_nodrawingobjects: int
    displayattribute_noparticles: int
    displayattribute_colorcodedtriangles: int
    simulation_stopped: int
    simulation_paused: int
    simulation_advancing_firstafterstop: int
    simulation_advancing_running: int
    simulation_advancing_lastbeforepause: int
    simulation_advancing_firstafterpause: int
    simulation_advancing_abouttostop: int
    simulation_advancing_lastbeforestop: int
    scripttype_main: int
    scripttype_simulation: int
    scripttype_addon: int
    scripttype_customization: int
    scripttype_sandbox: int
    scripttype_passive: int
    scriptexecorder_first: int
    scriptexecorder_normal: int
    scriptexecorder_last: int
    handle_absolute: int
    handle_all: int
    handle_all_except_explicit: int
    handle_self: int
    handle_main_script: int
    handle_tree: int
    handle_chain: int
    handle_single: int
    handle_default: int
    handle_all_except_self: int
    handle_parent: int
    handle_scene: int
    handle_app: int
    handle_appstorage: int
    handle_inverse: int
    handleflag_assembly: int
    handleflag_model: int
    handleflag_rawvalue: int
    handleflag_togglevisibility: int
    handleflag_greyscale: int
    handleflag_depthbuffermeters: int
    handleflag_depthbuffer: int
    handleflag_abscoords: int
    handleflag_codedstring: int
    handleflag_keeporiginal: int
    handleflag_camera: int
    handleflag_axis: int
    handleflag_silenterror: int
    handleflag_resetforce: int
    handleflag_resettorque: int
    handleflag_absolutecoords: int
    handleflag_relativecoords: int
    handleflag_wxyzquat: int
    handleflag_reljointbaseframe: int
    handleflag_addmultiple: int
    dlgstyle_message: int
    dlgstyle_input: int
    dlgstyle_ok: int
    dlgstyle_ok_cancel: int
    dlgstyle_yes_no: int
    dlgret_still_open: int
    dlgret_ok: int
    dlgret_cancel: int
    dlgret_yes: int
    dlgret_no: int
    drawing_points: int
    drawing_lines: int
    drawing_linestrip: int
    drawing_triangles: int
    drawing_trianglepts: int
    drawing_quadpts: int
    drawing_discpts: int
    drawing_cubepts: int
    drawing_spherepts: int
    drawing_cyclic: int
    drawing_local: int
    drawing_painttag: int
    drawing_overlay: int
    particle_points1: int
    particle_points2: int
    particle_points4: int
    particle_roughspheres: int
    particle_spheres: int
    particle_respondable1to4: int
    particle_respondable5to8: int
    particle_particlerespondable: int
    particle_ignoresgravity: int
    particle_invisible: int
    particle_painttag: int
    particle_cyclic: int
    particle_water: int
    verbosity_useglobal: int
    verbosity_none: int
    verbosity_errors: int
    verbosity_warnings: int
    verbosity_loadinfos: int
    verbosity_questions: int
    verbosity_scripterrors: int
    verbosity_scriptwarnings: int
    verbosity_scriptinfos: int
    verbosity_infos: int
    verbosity_debug: int
    verbosity_trace: int
    verbosity_tracelua: int
    verbosity_traceall: int
    verbosity_default: int
    plugininfo_extversionstr: int
    plugininfo_builddatestr: int
    plugininfo_extversionint: int
    plugininfo_verbosity: int
    plugininfo_statusbarverbosity: int
    navigation_passive: int
    navigation_camerashift: int
    navigation_camerarotate: int
    navigation_camerazoom: int
    navigation_cameratilt: int
    navigation_cameraangle: int
    navigation_objectshift: int
    navigation_objectrotate: int
    navigation_clickselection: int
    navigation_ctrlselection: int
    navigation_shiftselection: int
    navigation_camerazoomwheel: int
    navigation_camerarotatemiddlebutton: int
    jointmode_kinematic: int
    jointmode_dependent: int
    jointmode_dynamic: int
    jointdynctrl_free: int
    jointdynctrl_force: int
    jointdynctrl_velocity: int
    jointdynctrl_position: int
    jointdynctrl_spring: int
    jointdynctrl_callback: int
    ruckig_phasesync: int
    ruckig_timesync: int
    ruckig_nosync: int
    primitiveshape_none: int
    primitiveshape_plane: int
    primitiveshape_disc: int
    primitiveshape_cuboid: int
    primitiveshape_spheroid: int
    primitiveshape_cylinder: int
    primitiveshape_cone: int
    primitiveshape_capsule: int
    primitiveshape_heightfield: int
    dummytype_default: int
    dummytype_assembly: int
    dummytype_dynloopclosure: int
    dummytype_dyntendon: int
    texturemap_plane: int
    texturemap_cylinder: int
    texturemap_sphere: int
    texturemap_cube: int
    colorcomponent_ambient_diffuse: int
    colorcomponent_diffuse: int
    colorcomponent_specular: int
    colorcomponent_emission: int
    colorcomponent_transparency: int
    colorcomponent_auxiliary: int
    volume_pyramid: int
    volume_cylinder: int
    volume_disc: int
    volume_cone: int
    volume_ray: int
    volume_randomizedray: int
    buffer_uint8: int
    buffer_uint8rgb: int
    buffer_uint8bgr: int
    buffer_uint8rgba: int
    buffer_uint8argb: int
    buffer_float: int
    buffer_int32: int
    buffer_double: int
    buffer_base64: int
    imgcomb_vertical: int
    imgcomb_horizontal: int
    stream_transf_raw: int
    stream_transf_derivative: int
    stream_transf_integral: int
    stream_transf_cumulative: int
    bullet_constraintsolvertype_sequentialimpulse: int
    bullet_constraintsolvertype_nncg: int
    bullet_constraintsolvertype_dantzig: int
    bullet_constraintsolvertype_projectedgaussseidel: int
    vortex_bodyfrictionmodel_box: int
    vortex_bodyfrictionmodel_scaledbox: int
    vortex_bodyfrictionmodel_proplow: int
    vortex_bodyfrictionmodel_prophigh: int
    vortex_bodyfrictionmodel_scaledboxfast: int
    vortex_bodyfrictionmodel_neutral: int
    vortex_bodyfrictionmodel_none: int
    objintparam_visibility_layer: int
    objfloatparam_abs_x_velocity: int
    objfloatparam_abs_y_velocity: int
    objfloatparam_abs_z_velocity: int
    objfloatparam_abs_rot_velocity: int
    objfloatparam_objbbox_min_x: int
    objfloatparam_objbbox_min_y: int
    objfloatparam_objbbox_min_z: int
    objfloatparam_objbbox_max_x: int
    objfloatparam_objbbox_max_y: int
    objfloatparam_objbbox_max_z: int
    objfloatparam_modelbbox_min_x: int
    objfloatparam_modelbbox_min_y: int
    objfloatparam_modelbbox_min_z: int
    objfloatparam_modelbbox_max_x: int
    objfloatparam_modelbbox_max_y: int
    objfloatparam_modelbbox_max_z: int
    objintparam_collection_self_collision_indicator: int
    objfloatparam_transparency_offset: int
    objintparam_manipulation_permissions: int
    objintparam_illumination_handle: int
    objfloatparam_size_factor: int
    objstringparam_unique_id: int
    objintparam_visible: int
    visionfloatparam_near_clipping: int
    visionfloatparam_far_clipping: int
    visionintparam_resolution_x: int
    visionintparam_resolution_y: int
    visionfloatparam_perspective_angle: int
    visionfloatparam_ortho_size: int
    visionintparam_disabled_light_components: int
    visionintparam_rendering_attributes: int
    visionintparam_entity_to_render: int
    visionintparam_windowed_size_x: int
    visionintparam_windowed_size_y: int
    visionintparam_windowed_pos_x: int
    visionintparam_windowed_pos_y: int
    visionintparam_pov_focal_blur: int
    visionfloatparam_pov_blur_distance: int
    visionfloatparam_pov_aperture: int
    visionintparam_pov_blur_sampled: int
    visionintparam_render_mode: int
    visionintparam_perspective_operation: int
    visionfarrayparam_viewfrustum: int
    visionintparam_rgbignored: int
    visionintparam_depthignored: int
    jointfloatparam_intrinsic_x: int
    jointfloatparam_intrinsic_y: int
    jointfloatparam_intrinsic_z: int
    jointfloatparam_intrinsic_qx: int
    jointfloatparam_intrinsic_qy: int
    jointfloatparam_intrinsic_qz: int
    jointfloatparam_intrinsic_qw: int
    jointfloatparam_velocity: int
    jointfloatparam_spherical_qx: int
    jointfloatparam_spherical_qy: int
    jointfloatparam_spherical_qz: int
    jointfloatparam_spherical_qw: int
    jointfloatparam_upper_limit: int
    jointfloatparam_kc_k: int
    jointfloatparam_kc_c: int
    jointfloatparam_error_x: int
    jointfloatparam_error_y: int
    jointfloatparam_error_z: int
    jointfloatparam_error_a: int
    jointfloatparam_error_b: int
    jointfloatparam_error_g: int
    jointfloatparam_error_pos: int
    jointfloatparam_error_angle: int
    jointintparam_vortex_dep_handle: int
    jointfloatparam_vortex_dep_multiplication: int
    jointfloatparam_vortex_dep_offset: int
    jointfloatparam_screwlead: int
    jointfloatparam_maxvel: int
    jointfloatparam_maxaccel: int
    jointfloatparam_maxjerk: int
    jointintparam_dynctrlmode: int
    jointintparam_dynvelctrltype: int
    jointintparam_dynposctrltype: int
    shapefloatparam_init_velocity_x: int
    shapefloatparam_init_velocity_y: int
    shapefloatparam_init_velocity_z: int
    shapeintparam_static: int
    shapeintparam_kinematic: int
    shapeintparam_respondable: int
    shapeintparam_respondablesuspendcnt: int
    shapefloatparam_mass: int
    shapefloatparam_texture_x: int
    shapefloatparam_texture_y: int
    shapefloatparam_texture_z: int
    shapefloatparam_texture_a: int
    shapefloatparam_texture_b: int
    shapefloatparam_texture_g: int
    shapefloatparam_texture_scaling_x: int
    shapefloatparam_texture_scaling_y: int
    shapeintparam_culling: int
    shapeintparam_wireframe: int
    shapeintparam_compound: int
    shapeintparam_convex: int
    shapeintparam_convex_check: int
    shapeintparam_respondable_mask: int
    shapefloatparam_init_velocity_a: int
    shapefloatparam_init_velocity_b: int
    shapefloatparam_init_velocity_g: int
    shapestringparam_colorname: int
    shapeintparam_edge_visibility: int
    shapefloatparam_shading_angle: int
    shapefloatparam_edge_angle: int
    shapeintparam_edge_borders_hidden: int
    shapeintparam_component_cnt: int
    shapeintparam_sleepmodestart: int
    proxintparam_ray_invisibility: int
    proxintparam_volume_type: int
    proxintparam_entity_to_detect: int
    forcefloatparam_error_x: int
    forcefloatparam_error_y: int
    forcefloatparam_error_z: int
    forcefloatparam_error_a: int
    forcefloatparam_error_b: int
    forcefloatparam_error_g: int
    forcefloatparam_error_pos: int
    forcefloatparam_error_angle: int
    graphintparam_needs_refresh: int
    lightintparam_pov_casts_shadows: int
    lightfloatparam_spot_exponent: int
    lightfloatparam_spot_cutoff: int
    lightfloatparam_const_attenuation: int
    lightfloatparam_lin_attenuation: int
    lightfloatparam_quad_attenuation: int
    cameraintparam_disabled_light_components: int
    camerafloatparam_perspective_angle: int
    camerafloatparam_ortho_size: int
    cameraintparam_rendering_attributes: int
    cameraintparam_pov_focal_blur: int
    camerafloatparam_pov_blur_distance: int
    camerafloatparam_pov_aperture: int
    cameraintparam_pov_blur_samples: int
    camerafloatparam_near_clipping: int
    camerafloatparam_far_clipping: int
    cameraintparam_perspective_operation: int
    cameraintparam_remotecameramode: int
    camerafarrayparam_viewfrustum: int
    dummyintparam_dummytype: int
    dummyfloatparam_size: int
    dummystringparam_assemblytag: int
    scriptintparam_execorder: int
    scriptintparam_execcount: int
    scriptintparam_type: int
    scriptintparam_enabled: int
    scriptintparam_autorestartonerror: int
    scriptstringparam_description: int
    scriptstringparam_name: int
    scriptstringparam_text: int
    scriptstringparam_namext: int
    scriptstringparam_lang: int

    @classmethod
    def setJointTargetPosition(
        objectHandle: list, targetPosition: list, motionParams: list
    ) -> None:
        """Sets the target linear/angular position of a joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum velocity, acceleration and jerk values. In dynamic and position/custom control mode, the controller is instructed about the desired position
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointTargetPosition.htm
        @param objectHandle:list
        @param targetPosition:list
        @param motionParams:list
        """
        pass

    @classmethod
    def handleDynamics(deltaTime: list) -> list:
        """Handles the dynamics functionality in a scene
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleDynamics.htm
        @param deltaTime:list
        @return result:list"""
        pass

    @classmethod
    def checkDistance(
        entity1Handle: list, entity2Handle: list, threshold: list
    ) -> Union[list, list, list]:
        """Checks the minimum distance between two entities. The measurable flags of the entities are overridden if the entities are objects. If the entities are both the same collection (i.e. with the same collection handle), then same objects will not be checked against themselve
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckDistance.htm
        @param entity1Handle:list
        @param entity2Handle:list
        @param threshold:list
        @return result:list
        @return distanceData:list
        @return objectHandlePair:list"""
        pass

    @classmethod
    def checkCollisionEx(entity1Handle: list, entity2Handle: list) -> Union[list, list]:
        """Checks whether two entities are colliding, and will return all intersections between the two entities. The collidable flags of the entities are overridden if the entities are objects
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckCollisionEx.htm
        @param entity1Handle:list
        @param entity2Handle:list
        @return result:list
        @return intersections:list"""
        pass

    @classmethod
    def checkCollision(entity1Handle: list, entity2Handle: list) -> Union[list, list]:
        """Checks whether two entities are colliding. The collidable flags of the entities are overridden if the entities are objects. If the entities are both the same collection (i.e. with the same collection handle), then same objects will not be checked against themselve
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckCollision.htm
        @param entity1Handle:list
        @param entity2Handle:list
        @return result:list
        @return collidingObjectHandles:list"""
        pass

    @classmethod
    def handleSandboxScript() -> None:
        """Lua only. Calls a specific function in the  sandbox . sim.handleSandboxScript should only be called from the  main script
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleSandboxScript.htm

        """
        pass

    @classmethod
    def handleAddOnScripts() -> None:
        """Lua only. Calls a specific function in  add-ons . Should only be called from the  main script
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleAddOnScripts.htm

        """
        pass

    @classmethod
    def handleEmbeddedScripts() -> None:
        """Lua only. Calls a specific  system callback function  in  simulation scripts  and  customization scripts . Simulation- and customization scripts will be executed in a  precise order . This function should only be called from the  main script
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleEmbeddedScripts.htm

        """
        pass

    @classmethod
    def handleSimulationScripts() -> None:
        """Lua only. Calls a specific  system callback function  in  simulation scripts . Simulation scripts will be executed in a  precise order . This function should only be called from the  main script .
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleSimulationScripts.htm

        """
        pass

    @classmethod
    def getReferencedHandlesTags(objectHandle: list) -> list:
        """Retrieves a list of all referenced handles tags
        @url:https://manual.coppeliarobotics.com/en/sim/simGetReferencedHandlesTags.htm
        @param objectHandle:list
        @return tags:list"""
        pass

    @classmethod
    def getReferencedHandles(objectHandle: list, tag: str) -> list:
        """Retrieves a list of custom handles, linking a given scene object to other scene objects
        @url:https://manual.coppeliarobotics.com/en/sim/simGetReferencedHandles.htm
        @param objectHandle:list
        @param tag:str
        @return referencedHandles:list"""
        pass

    @classmethod
    def setReferencedHandles(
        objectHandle: list, referencedHandles: list, tag: str
    ) -> None:
        """Attaches a list of custom handles to a given scene object. Those custom handles are handles of other scene objects, that are linked to the given scene object (for whatever purpose). The advantage of storing references to other objects with this function is that CoppeliaSim will take care of correctly adjusting the references if needed: For instance, imagine  objectA  storing the handle of  objectB  via this function. If  objectB  is deleted, then the stored handle becomes -1. If  objectA  and  objectB  are duplicated at the same time, then the duplicate of  objectA  stores the handle of the duplicate of  objectB . Optionally, if  sim.handleflag_keeporiginal  is specified, then linking to original objects is guaranteed, e.g. in above example, after a duplication of  objectA , the duplicate of  objectA  will store the handle of the original  objectB  (if  objectB  still exists)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetReferencedHandles.htm
        @param objectHandle:list
        @param referencedHandles:list
        @param tag:str
        """
        pass

    @classmethod
    def getCollectionObjects(collectionHandle: list) -> list:
        """Retrieves the object handles that compose a  collection
        @url:https://manual.coppeliarobotics.com/en/sim/simGetCollectionObjects.htm
        @param collectionHandle:list
        @return objectHandles:list"""
        pass

    @classmethod
    def getObjectsInTree(treeBaseHandle: list, objectType: list, options: list) -> list:
        """Retrieves object handles in a given hierarchy tree
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectsInTree.htm
        @param treeBaseHandle:list
        @param objectType:list
        @param options:list
        @return objects:list"""
        pass

    @classmethod
    def getObjects(index: list, objectType: list) -> list:
        """Retrieves object handles. Use this in a loop where index starts at 0 and is incremented to get all object handles in the scene
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjects.htm
        @param index:list
        @param objectType:list
        @return objectHandle:list"""
        pass

    @classmethod
    def isHandle(objectHandle: list) -> list:
        """Checks whether a general object handle is still valid. When a general object is destroyed (e.g. programmatically or via the user interface), then its related handle is not valid anymore and will trigger an error when used. Use this function to avoid triggering an error
        @url:https://manual.coppeliarobotics.com/en/sim/simIsHandle.htm
        @param objectHandle:list
        @return result:list"""
        pass

    @classmethod
    def cancelScheduledExecution(id: list) -> list:
        """Cancels a scheduled execution of a function
        @url:https://manual.coppeliarobotics.com/en/sim/simCancelScheduledExecution.htm
        @param id:list
        @return canceled:list"""
        pass

    @classmethod
    def scheduleExecution(f: list, args: list, timePoint: list, simTime: list) -> list:
        """Schedules execution of a function
        @url:https://manual.coppeliarobotics.com/en/sim/simScheduleExecution.htm
        @param f:list
        @param args:list
        @param timePoint:list
        @param simTime:list
        @return id:list"""
        pass

    @classmethod
    def moduleEntry(handle: list, label: str, state: list) -> list:
        """Creates, modifies or destroys module menu entries. Those are user selectable items located in [Menu bar > Modules]. When selected, the corresponding script will have its  sysCall_moduleEntry  callback function triggered, or  sim_message_eventcallback_moduleentry  triggered
        @url:https://manual.coppeliarobotics.com/en/sim/simModuleEntry.htm
        @param handle:list
        @param label:str
        @param state:list
        @return handle:list"""
        pass

    @classmethod
    def getUserVariables() -> None:
        """Lua only. Returns all variables, except those set by CoppeliaSim.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetUserVariables.htm

        """
        pass

    @classmethod
    def quitSimulator() -> None:
        """Triggers a quit signal after which the application eventually ends
        @url:https://manual.coppeliarobotics.com/en/sim/simQuitSimulator.htm

        """
        pass

    @classmethod
    def setExplicitHandling(objectHandle: list, explicitFlags: list) -> None:
        """Sets the explicit handling flags for a scene object
        @url:https://manual.coppeliarobotics.com/en/sim/simSetExplicitHandling.htm
        @param objectHandle:list
        @param explicitFlags:list
        """
        pass

    @classmethod
    def getExplicitHandling(objectHandle: list) -> list:
        """Retrieves the explicit handling flags for a scene object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetExplicitHandling.htm
        @param objectHandle:list
        @return explicitHandlingFlags:list"""
        pass

    @classmethod
    def refreshDialogs(refreshDegree: list) -> None:
        """Refreshes CoppeliaSim's internal dialogs. Calling  sim.refreshDialogs  will not trigger a  sim.message_eventcallback_refreshdialogs  message
        @url:https://manual.coppeliarobotics.com/en/sim/simRefreshDialogs.htm
        @param refreshDegree:list
        """
        pass

    @classmethod
    def getSystemTime() -> list:
        """Retrieves the system time.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetSystemTime.htm

        @return systemTime:list"""
        pass

    @classmethod
    def getPluginInfo(pluginName: str, infoType: list) -> list:
        """Returns auxiliary information about a loaded plugin
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPluginInfo.htm
        @param pluginName:str
        @param infoType:list
        @return info:list"""
        pass

    @classmethod
    def getPluginName(index: list) -> str:
        """Retrieves a plugin name based on an index
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPluginName.htm
        @param index:list
        @return pluginName:str"""
        pass

    @classmethod
    def getLastInfo() -> str:
        """Retrieves and clears the information string generated by last API call
        @url:https://manual.coppeliarobotics.com/en/sim/simGetLastInfo.htm

        @return info:str"""
        pass

    @classmethod
    def setPage(index: list) -> None:
        """Switches between pages (main scene views)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetPage.htm
        @param index:list
        """
        pass

    @classmethod
    def getPage() -> list:
        """Retrieves the current page index (view)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPage.htm

        @return pageIndex:list"""
        pass

    @classmethod
    def setNavigationMode(navigationMode: list) -> None:
        """Sets the navigation and selection mode for the mouse
        @url:https://manual.coppeliarobotics.com/en/sim/simSetNavigationMode.htm
        @param navigationMode:list
        """
        pass

    @classmethod
    def getNavigationMode() -> list:
        """Retrieves the navigation and selection mode for the mouse
        @url:https://manual.coppeliarobotics.com/en/sim/simGetNavigationMode.htm

        @return navigationMode:list"""
        pass

    @classmethod
    def announceSceneContentChange() -> list:
        """Announces a change in the scene. This is required for the undo/redo function to operate properly when performing changes via the API. Only call this function directly after a change was made through a dialog element (e.g. a checkbox was checked/unchecked) and that change was reported to the scene. What this call will do is following: the whole scene will be serialized (saved) to memory as a "scene image" and compared to a previously memorized "scene image". If both images are same, then the last image is discarded, otherwise only the changes between the two images are memorized. A call to this function has no effect (and doesn't generate any error) when called during simulation or when in edit mode.
        @url:https://manual.coppeliarobotics.com/en/sim/simAnnounceSceneContentChange.htm

        @return result:list"""
        pass

    @classmethod
    def transformBuffer(
        inBuff: list, inFormat: list, mult: list, off: list, outFormat: list
    ) -> list:
        """Modifies a buffer than contains packed data
        @url:https://manual.coppeliarobotics.com/en/sim/simTransformBuffer.htm
        @param inBuff:list
        @param inFormat:list
        @param mult:list
        @param off:list
        @param outFormat:list
        @return outBuff:list"""
        pass

    @classmethod
    def copyTable() -> None:
        """Lua only. Duplicates a table, i.e. makes a deep copy
        @url:https://manual.coppeliarobotics.com/en/sim/simCopyTable.htm

        """
        pass

    @classmethod
    def unpackDoubleTable(
        data: list,
        startDoubleIndex: list,
        doubleCount: list,
        additionalByteOffset: list,
    ) -> list:
        """Unpacks a string (or part of it) into an array of double floating-point numbers
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackDoubleTable.htm
        @param data:list
        @param startDoubleIndex:list
        @param doubleCount:list
        @param additionalByteOffset:list
        @return doubleNumbers:list"""
        pass

    @classmethod
    def packDoubleTable(
        doubleNumbers: list, startDoubleIndex: list, doubleCount: list
    ) -> list:
        """Packs ab array of double floating-point numbers into a string
        @url:https://manual.coppeliarobotics.com/en/sim/simPackDoubleTable.htm
        @param doubleNumbers:list
        @param startDoubleIndex:list
        @param doubleCount:list
        @return data:list"""
        pass

    @classmethod
    def unpackFloatTable(
        data: list, startFloatIndex: list, floatCount: list, additionalByteOffset: list
    ) -> list:
        """Unpacks a string (or part of it) into an array of floating-point numbers
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackFloatTable.htm
        @param data:list
        @param startFloatIndex:list
        @param floatCount:list
        @param additionalByteOffset:list
        @return floatingNumbers:list"""
        pass

    @classmethod
    def packFloatTable(
        floatingNumbers: list, startFloatIndex: list, floatCount: list
    ) -> list:
        """Packs an array of floating-point numbers into a string
        @url:https://manual.coppeliarobotics.com/en/sim/simPackFloatTable.htm
        @param floatingNumbers:list
        @param startFloatIndex:list
        @param floatCount:list
        @return data:list"""
        pass

    @classmethod
    def unpackInt32Table(
        data: list, startInt32Index: list, int32Count: list, additionalByteOffset: list
    ) -> list:
        """Unpacks a string (or part of it) into an array of int32 numbers
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackInt32Table.htm
        @param data:list
        @param startInt32Index:list
        @param int32Count:list
        @param additionalByteOffset:list
        @return int32Numbers:list"""
        pass

    @classmethod
    def packInt32Table(
        int32Numbers: list, startInt32Index: list, int32Count: list
    ) -> list:
        """Packs an array of int32 numbers into a string
        @url:https://manual.coppeliarobotics.com/en/sim/simPackInt32Table.htm
        @param int32Numbers:list
        @param startInt32Index:list
        @param int32Count:list
        @return data:list"""
        pass

    @classmethod
    def unpackUInt32Table(
        data: list,
        startUint32Index: list,
        uint32Count: list,
        additionalByteOffset: list,
    ) -> list:
        """Unpacks a string (or part of it) into an array of uint32 numbers
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackUInt32Table.htm
        @param data:list
        @param startUint32Index:list
        @param uint32Count:list
        @param additionalByteOffset:list
        @return uint32Numbers:list"""
        pass

    @classmethod
    def packUInt32Table(
        uint32Numbers: list, startUint32Index: list, uint32Count: list
    ) -> list:
        """Packs an array of uint32 numbers into a string
        @url:https://manual.coppeliarobotics.com/en/sim/simPackUInt32Table.htm
        @param uint32Numbers:list
        @param startUint32Index:list
        @param uint32Count:list
        @return data:list"""
        pass

    @classmethod
    def unpackUInt16Table(
        data: list, starUint16Index: list, uint16Count: list, additionalByteOffset: list
    ) -> list:
        """Unpacks a string (or part of it) into an array of uint16 numbers
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackUInt16Table.htm
        @param data:list
        @param starUint16Index:list
        @param uint16Count:list
        @param additionalByteOffset:list
        @return uint16Numbers:list"""
        pass

    @classmethod
    def packUInt16Table(
        uint16Numbers: list, startUint16Index: list, uint16Count: list
    ) -> list:
        """Packs an array of uint16 numbers into a string
        @url:https://manual.coppeliarobotics.com/en/sim/simPackUInt16Table.htm
        @param uint16Numbers:list
        @param startUint16Index:list
        @param uint16Count:list
        @return data:list"""
        pass

    @classmethod
    def unpackUInt8Table(data: list, startUint8Index: list, uint8Count: list) -> list:
        """Unpacks a string (or part of it) into an array of uint8 numbers
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackUInt8Table.htm
        @param data:list
        @param startUint8Index:list
        @param uint8Count:list
        @return uint8Numbers:list"""
        pass

    @classmethod
    def packUInt8Table(
        uint8Numbers: list, startUint8Index: list, uint8count: list
    ) -> list:
        """Packs an array of uint8 numbers into a string
        @url:https://manual.coppeliarobotics.com/en/sim/simPackUInt8Table.htm
        @param uint8Numbers:list
        @param startUint8Index:list
        @param uint8count:list
        @return data:list"""
        pass

    @classmethod
    def unpackTable(buffer: list) -> list:
        """Unpacks a buffer into a table
        @url:https://manual.coppeliarobotics.com/en/sim/simUnpackTable.htm
        @param buffer:list
        @return aTable:list"""
        pass

    @classmethod
    def packTable(aTable: list, packingScheme: list) -> list:
        """Packs a table into a buffer. The table may contain other nested arrays, maps, None/nil, bool, number or string values. All other types (e.g. functions) will be considered as string or None/nil values. You can also use sim.packTable to quickly compare two tables or to perform a deep copy of a table
        @url:https://manual.coppeliarobotics.com/en/sim/simPackTable.htm
        @param aTable:list
        @param packingScheme:list
        @return buffer:list"""
        pass

    @classmethod
    def ruckigRemove(handle: list) -> None:
        """Removes an object previously created via  sim.ruckigPos  or  sim.ruckigVel .
        @url:https://manual.coppeliarobotics.com/en/sim/simRuckigRemove.htm
        @param handle:list
        """
        pass

    @classmethod
    def ruckigVel(
        dofs: list,
        baseCycleTime: list,
        flags: list,
        currentPosVelAccel: list,
        maxAccelJerk: list,
        selection: list,
        targetVel: list,
    ) -> list:
        """Executes a call to the  Ruckig online trajectory generator . The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a velocity-based trajectory generation object, that can then be calculated with  sim.ruckigStep . When this object is not needed anymore, remove it with  sim.ruckigRemove
        @url:https://manual.coppeliarobotics.com/en/sim/simRuckigVel.htm
        @param dofs:list
        @param baseCycleTime:list
        @param flags:list
        @param currentPosVelAccel:list
        @param maxAccelJerk:list
        @param selection:list
        @param targetVel:list
        @return handle:list"""
        pass

    @classmethod
    def ruckigPos(
        dofs: list,
        baseCycleTime: list,
        flags: list,
        currentPosVelAccel: list,
        maxVelAccelJerk: list,
        selection: list,
        targetPosVel: list,
    ) -> list:
        """Executes a call to the  Ruckig online trajectory generator . The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a position-based trajectory generation object, that can then be calculated with  sim.ruckigStep . When this object is not needed anymore, remove it with  sim.ruckigRemove
        @url:https://manual.coppeliarobotics.com/en/sim/simRuckigPos.htm
        @param dofs:list
        @param baseCycleTime:list
        @param flags:list
        @param currentPosVelAccel:list
        @param maxVelAccelJerk:list
        @param selection:list
        @param targetPosVel:list
        @return handle:list"""
        pass

    @classmethod
    def moveToPose_cleanup(motionObject: list) -> None:
        """Destroys a motion object
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose_cleanup.htm
        @param motionObject:list
        """
        pass

    @classmethod
    def moveToPose_step(motionObject: list) -> Union[list, list]:
        """Steps a motion object
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose_step.htm
        @param motionObject:list
        @return res:list
        @return data:list"""
        pass

    @classmethod
    def moveToPose_init(params: list) -> list:
        """Initiates an object motion using the  Ruckig online trajectory generator , by performing interpolations between two poses. The function can operate by handling 4 motion variables (x,y,z and angle between the two poses), or a single movement variable (t, which requires a metric to be specified for distance calculation between the two poses)
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose_init.htm
        @param params:list
        @return motionObject:list"""
        pass

    @classmethod
    def moveToConfig_cleanup(motionObject: list) -> None:
        """Destroys a motion object
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_cleanup.htm
        @param motionObject:list
        """
        pass

    @classmethod
    def moveToConfig_step(motionObject: list) -> Union[list, list]:
        """Steps a motion object
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_step.htm
        @param motionObject:list
        @return res:list
        @return data:list"""
        pass

    @classmethod
    def moveToConfig_init(params: list) -> list:
        """Initiates a n-DoF motion using the  Ruckig online trajectory generator
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_init.htm
        @param params:list
        @return motionObject:list"""
        pass

    @classmethod
    def floatingViewRemove(floatingViewHandle: list) -> list:
        """Removes a floating view previously added with  sim.floatingViewAdd .
        @url:https://manual.coppeliarobotics.com/en/sim/simFloatingViewRemove.htm
        @param floatingViewHandle:list
        @return result:list"""
        pass

    @classmethod
    def floatingViewAdd(
        posX: list, posY: list, sizeX: list, sizeY: list, options: list
    ) -> list:
        """Adds a floating view to current page
        @url:https://manual.coppeliarobotics.com/en/sim/simFloatingViewAdd.htm
        @param posX:list
        @param posY:list
        @param sizeX:list
        @param sizeY:list
        @param options:list
        @return floatingViewHandle:list"""
        pass

    @classmethod
    def textEditorShow(handle: list, showState: list) -> None:
        """Shows or hides a text edition window previously opened with  sim.textEditorOpen
        @url:https://manual.coppeliarobotics.com/en/sim/simTextEditorShow.htm
        @param handle:list
        @param showState:list
        """
        pass

    @classmethod
    def ruckigStep(handle: list, cycleTime: list) -> Union[list, list, list]:
        """Executes a call to the  Ruckig online trajectory generator . The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function steps forward a trajectory generation algorithm previously prepared via  sim.ruckigPos  or  sim.ruckigVel
        @url:https://manual.coppeliarobotics.com/en/sim/simRuckigStep.htm
        @param handle:list
        @param cycleTime:list
        @return result:list
        @return newPosVelAccel:list
        @return synchronizationTime:list"""
        pass

    @classmethod
    def textEditorOpen(initText: str, properties: str) -> list:
        """Opens a text edition window
        @url:https://manual.coppeliarobotics.com/en/sim/simTextEditorOpen.htm
        @param initText:str
        @param properties:str
        @return handle:list"""
        pass

    @classmethod
    def textEditorGetInfo(handle: list) -> Union[str, list, list, list]:
        """Retieves information from a text edition window previously opened with  sim.textEditorOpen
        @url:https://manual.coppeliarobotics.com/en/sim/simTextEditorGetInfo.htm
        @param handle:list
        @return text:str
        @return pos:list
        @return size:list
        @return visible:list"""
        pass

    @classmethod
    def textEditorClose(handle: list) -> Union[str, list, list]:
        """Closes a text edition window previously opened with  sim.textEditorOpen
        @url:https://manual.coppeliarobotics.com/en/sim/simTextEditorClose.htm
        @param handle:list
        @return text:str
        @return pos:list
        @return size:list"""
        pass

    @classmethod
    def auxiliaryConsoleShow(consoleHandle: list, showState: list) -> list:
        """Shows or hides an auxiliary console window
        @url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleShow.htm
        @param consoleHandle:list
        @param showState:list
        @return result:list"""
        pass

    @classmethod
    def moveToPose(params: list) -> list:
        """Executes an object motion using the  Ruckig online trajectory generator , by performing interpolations between two poses. The function can operate by handling 4 motion variables (x,y,z and angle between the two poses), or a single movement variable (t, which requires a metric to be specified for distance calculation between the two poses). This function can only be called from a script running in a thread, since this is a blocking operation
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToPose.htm
        @param params:list
        @return data:list"""
        pass

    @classmethod
    def moveToConfig(params: list) -> list:
        """Executes a n-DoF motion using the  Ruckig online trajectory generator . This function can only be called from scripts running in a thread, since this is a blocking operation
        @url:https://manual.coppeliarobotics.com/en/sim/simMoveToConfig.htm
        @param params:list
        @return data:list"""
        pass

    @classmethod
    def wait(deltaTime: list, simulationTime: list) -> list:
        """Waits for a certain amount of time
        @url:https://manual.coppeliarobotics.com/en/sim/simWait.htm
        @param deltaTime:list
        @param simulationTime:list
        @return deltaTimeLeft:list"""
        pass

    @classmethod
    def writeTexture(
        textureId: list,
        options: list,
        textureData: list,
        posX: list,
        posY: list,
        sizeX: list,
        sizeY: list,
        interpolation: list,
    ) -> None:
        """Overwrites a specific texture (or a portion of it) with RGB data
        @url:https://manual.coppeliarobotics.com/en/sim/simWriteTexture.htm
        @param textureId:list
        @param options:list
        @param textureData:list
        @param posX:list
        @param posY:list
        @param sizeX:list
        @param sizeY:list
        @param interpolation:list
        """
        pass

    @classmethod
    def transformImage(image: list, resolution: list, options: list) -> list:
        """Transforms an image in various ways
        @url:https://manual.coppeliarobotics.com/en/sim/simTransformImage.htm
        @param image:list
        @param resolution:list
        @param options:list
        @return newImage:list"""
        pass

    @classmethod
    def getScaledImage(
        imageIn: list, resolutionIn: list, desiredResolutionOut: list, options: list
    ) -> Union[list, list]:
        """Generates a scaled-up or scaled down version of the input image
        @url:https://manual.coppeliarobotics.com/en/sim/simGetScaledImage.htm
        @param imageIn:list
        @param resolutionIn:list
        @param desiredResolutionOut:list
        @param options:list
        @return imageOut:list
        @return effectiveRolutionOut:list"""
        pass

    @classmethod
    def loadImage(options: list, filenameOrBuffer: list) -> Union[list, list]:
        """Loads an image from file or memory
        @url:https://manual.coppeliarobotics.com/en/sim/simLoadImage.htm
        @param options:list
        @param filenameOrBuffer:list
        @return image:list
        @return resolution:list"""
        pass

    @classmethod
    def saveImage(
        image: list, resolution: list, options: list, filename: str, quality: list
    ) -> list:
        """Saves an image to file or to memory
        @url:https://manual.coppeliarobotics.com/en/sim/simSaveImage.htm
        @param image:list
        @param resolution:list
        @param options:list
        @param filename:str
        @param quality:list
        @return imgBuffer:list"""
        pass

    @classmethod
    def readTexture(
        textureId: list, options: list, posX: list, posY: list, sizeX: list, sizeY: list
    ) -> list:
        """Retrieves the RGB data (or a portion of it) related to a specific texture
        @url:https://manual.coppeliarobotics.com/en/sim/simReadTexture.htm
        @param textureId:list
        @param options:list
        @param posX:list
        @param posY:list
        @param sizeX:list
        @param sizeY:list
        @return textureData:list"""
        pass

    @classmethod
    def getTextureId(textureName: str) -> Union[list, list]:
        """Retrieves the texture ID of a specific texture
        @url:https://manual.coppeliarobotics.com/en/sim/simGetTextureId.htm
        @param textureName:str
        @return textureId:list
        @return resolution:list"""
        pass

    @classmethod
    def systemSemaphore(key: str, acquire: list) -> None:
        """Acquires or releases a system-wide semaphore, i.e. across several CoppeliaSim instances
        @url:https://manual.coppeliarobotics.com/en/sim/simSystemSemaphore.htm
        @param key:str
        @param acquire:list
        """
        pass

    @classmethod
    def pushUserEvent(
        event: str, handle: list, uid: list, eventData: list, options: list
    ) -> None:
        """Pushes a user-triggered event. Messages are received asynchronously via the sysCall_event  callback function  and via the plugin  sim_message_eventcallback_events  message call
        @url:https://manual.coppeliarobotics.com/en/sim/simPushUserEvent.htm
        @param event:str
        @param handle:list
        @param uid:list
        @param eventData:list
        @param options:list
        """
        pass

    @classmethod
    def broadcastMsg(message: list, options: list) -> None:
        """Broadcasts a message to all scripts, except for the emitting script. Messages are received synchronously via the sysCall_msg  callback function
        @url:https://manual.coppeliarobotics.com/en/sim/simBroadcastMsg.htm
        @param message:list
        @param options:list
        """
        pass

    @classmethod
    def auxiliaryConsolePrint(consoleHandle: list, text: str) -> list:
        """Prints to an auxiliary console window
        @url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsolePrint.htm
        @param consoleHandle:list
        @param text:str
        @return result:list"""
        pass

    @classmethod
    def auxiliaryConsoleOpen(
        title: str,
        maxLines: list,
        mode: list,
        position: list,
        size: list,
        textColor: list,
        backgroundColor: list,
    ) -> list:
        """Opens an auxiliary console window for text display. This console window is different from the application main console window. Console window handles are shared across all simulator scenes
        @url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleOpen.htm
        @param title:str
        @param maxLines:list
        @param mode:list
        @param position:list
        @param size:list
        @param textColor:list
        @param backgroundColor:list
        @return consoleHandle:list"""
        pass

    @classmethod
    def auxiliaryConsoleClose(consoleHandle: list) -> list:
        """Closes an auxiliary console window
        @url:https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleClose.htm
        @param consoleHandle:list
        @return result:list"""
        pass

    @classmethod
    def getSimulatorMessage() -> Union[list, list, list]:
        """Retrieves and removes the next message in the C/C++ or Lua message queues. Use this in a while-loop until all messages have been extracted. While the C/C++ interface has one single message queue, each Lua script has its own message queue. The C/C++ version of this function should only be called from the CoppeliaSim client application. A given message queue cannot hold more than 64 messages, unread messages will be discarded.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetSimulatorMessage.htm

        @return message:list
        @return auxiliaryData:list
        @return auxiliaryData2:list"""
        pass

    @classmethod
    def addLog(verbosity: list, message: str) -> None:
        """Adds a log message that will be output in the console or status bar
        @url:https://manual.coppeliarobotics.com/en/sim/simAddLog.htm
        @param verbosity:list
        @param message:str
        """
        pass

    @classmethod
    def yawPitchRollToAlphaBetaGamma(
        yaw: list, pitch: list, roll: list
    ) -> Union[list, list, list]:
        """Converts Yaw-Pitch-Roll angles to CoppeliaSim's alpha-beta-gamma angles
        @url:https://manual.coppeliarobotics.com/en/sim/simYawPitchRollToAlphaBetaGamma.htm
        @param yaw:list
        @param pitch:list
        @param roll:list
        @return alpha:list
        @return beta:list
        @return gamma:list"""
        pass

    @classmethod
    def alphaBetaGammaToYawPitchRoll(
        alpha: list, beta: list, gamma: list
    ) -> Union[list, list, list]:
        """Converts CoppeliaSim's alpha-beta-gamma angles to Yaw-Pitch-Roll angles
        @url:https://manual.coppeliarobotics.com/en/sim/simAlphaBetaGammaToYawPitchRoll.htm
        @param alpha:list
        @param beta:list
        @param gamma:list
        @return yaw:list
        @return pitch:list
        @return roll:list"""
        pass

    @classmethod
    def rotateAroundAxis(poseIn: list, axis: list, axisPos: list, angle: list) -> list:
        """Rotates a pose or transformation matrix around a random axis in space. This function, when used in combination with  sim.getRotationAxis , can be used to build interpolations between poses or transformation matrices
        @url:https://manual.coppeliarobotics.com/en/sim/simRotateAroundAxis.htm
        @param poseIn:list
        @param axis:list
        @param axisPos:list
        @param angle:list
        @return poseOut:list"""
        pass

    @classmethod
    def getRotationAxis(poseStart: list, poseGoal: list) -> Union[list, list]:
        """Retrieves an axis and rotation angle that brings one pose or transformation matrix onto another one. The translation part of the poses/matrices is ignored. This function, when used in combination with  sim.rotateAroundAxis , can be used to build interpolations between transformation matrices
        @url:https://manual.coppeliarobotics.com/en/sim/simGetRotationAxis.htm
        @param poseStart:list
        @param poseGoal:list
        @return axis:list
        @return angle:list"""
        pass

    @classmethod
    def multiplyVector(quaternion: list, vector: list) -> list:
        """Multiplies a vector with a quaternion, a pose, or a matrix (e.g. v = m * v)
        @url:https://manual.coppeliarobotics.com/en/sim/simMultiplyVector.htm
        @param quaternion:list
        @param vector:list
        @return resultVector:list"""
        pass

    @classmethod
    def getPoseInverse(pose: list) -> list:
        """Inverts a pose
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPoseInverse.htm
        @param pose:list
        @return pose:list"""
        pass

    @classmethod
    def getMatrixInverse(matrix: list) -> list:
        """Inverts a transformation matrix
        @url:https://manual.coppeliarobotics.com/en/sim/simGetMatrixInverse.htm
        @param matrix:list
        @return matrix:list"""
        pass

    @classmethod
    def interpolatePoses(poseIn1: list, poseIn2: list, interpolFactor: list) -> list:
        """Computes the interpolated pose between poseIn1 and poseIn2
        @url:https://manual.coppeliarobotics.com/en/sim/simInterpolatePoses.htm
        @param poseIn1:list
        @param poseIn2:list
        @param interpolFactor:list
        @return resultPose:list"""
        pass

    @classmethod
    def interpolateMatrices(
        matrixIn1: list, matrixIn2: list, interpolFactor: list
    ) -> list:
        """Computes the interpolated transformation matrix between matrixIn1 and matrixIn2. Quaternions are used internally
        @url:https://manual.coppeliarobotics.com/en/sim/simInterpolateMatrices.htm
        @param matrixIn1:list
        @param matrixIn2:list
        @param interpolFactor:list
        @return resultMatrix:list"""
        pass

    @classmethod
    def multiplyPoses(poseIn1: list, poseIn2: list) -> list:
        """Multiplies two poses
        @url:https://manual.coppeliarobotics.com/en/sim/simMultiplyPoses.htm
        @param poseIn1:list
        @param poseIn2:list
        @return resultPose:list"""
        pass

    @classmethod
    def multiplyMatrices(matrixIn1: list, matrixIn2: list) -> list:
        """Multiplies two transformation matrices
        @url:https://manual.coppeliarobotics.com/en/sim/simMultiplyMatrices.htm
        @param matrixIn1:list
        @param matrixIn2:list
        @return resultMatrix:list"""
        pass

    @classmethod
    def poseToMatrix(pose: list) -> list:
        """Converts a pose to a transformation matrix
        @url:https://manual.coppeliarobotics.com/en/sim/simPoseToMatrix.htm
        @param pose:list
        @return matrix:list"""
        pass

    @classmethod
    def matrixToPose(matrix: list) -> list:
        """Converts a transformation matrix to a pose
        @url:https://manual.coppeliarobotics.com/en/sim/simMatrixToPose.htm
        @param matrix:list
        @return pose:list"""
        pass

    @classmethod
    def getEulerAnglesFromMatrix(matrix: list) -> list:
        """Retrieves the  Euler angles  from a transformation matrix
        @url:https://manual.coppeliarobotics.com/en/sim/simGetEulerAnglesFromMatrix.htm
        @param matrix:list
        @return eulerAngles:list"""
        pass

    @classmethod
    def buildPose(
        position: list, eulerAnglesOrAxis: list, mode: list, axis2: list
    ) -> list:
        """Builds a pose based on a position vector and  Euler angles  or axes
        @url:https://manual.coppeliarobotics.com/en/sim/simBuildPose.htm
        @param position:list
        @param eulerAnglesOrAxis:list
        @param mode:list
        @param axis2:list
        @return pose:list"""
        pass

    @classmethod
    def buildMatrix(position: list, eulerAngles: list) -> list:
        """Builds a transformation matrix based on a position vector and  Euler angles
        @url:https://manual.coppeliarobotics.com/en/sim/simBuildMatrix.htm
        @param position:list
        @param eulerAngles:list
        @return matrix:list"""
        pass

    @classmethod
    def handleExtCalls() -> None:
        """Handles the message pump for threaded scripts
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleExtCalls.htm

        """
        pass

    @classmethod
    def getSimulationStopping() -> list:
        """Convenience function that returns true when the simulation is about to stop or stopped.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetSimulationStopping.htm

        @return stopping:list"""
        pass

    @classmethod
    def releaseLock() -> None:
        """Counterpart function to  sim.acquireLock . Unlocking is cumulative
        @url:https://manual.coppeliarobotics.com/en/sim/simReleaseLock.htm

        """
        pass

    @classmethod
    def acquireLock() -> None:
        """Allows to have CoppeliaSim wait for a threaded code section to be executed without interruption. Locking is cumulative
        @url:https://manual.coppeliarobotics.com/en/sim/simAcquireLock.htm

        """
        pass

    @classmethod
    def setAutoYieldDelay(dt: list) -> None:
        """Allows specifying a thread interruption or yield delay, that will be automatically enforced by the system (preemptive threading). By default this value is 2 ms
        @url:https://manual.coppeliarobotics.com/en/sim/simSetAutoYieldDelay.htm
        @param dt:list
        """
        pass

    @classmethod
    def step() -> None:
        """Triggers the next simulation step, when in stepping operation mode. When simulation is running, then sim.step only returns once the simulation time has changed
        @url:https://manual.coppeliarobotics.com/en/sim/simStep.htm

        """
        pass

    @classmethod
    def setStepping(enable: list) -> list:
        """Enables or disables the stepping operation mode for a threaded script. If enabled, then the current script has to trigger each simulation step explicitly, via  sim.step . Is applied cumulatively, i.e. if the stepping operation mode is enabled n times, it needs to be disabled n times to return to the initial state                 (Lua specific: in stepping operation mode, automatic thread interruptions, i.e. preemptive threading, is supressed)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetStepping.htm
        @param enable:list
        @return prevStepLevel:list"""
        pass

    @classmethod
    def getRealTimeSimulation() -> list:
        """Indicates whether the simulation is real-time
        @url:https://manual.coppeliarobotics.com/en/sim/simGetRealTimeSimulation.htm

        @return result:list"""
        pass

    @classmethod
    def getSimulationTimeStep() -> list:
        """Retrieves the simulation time step (the simulation time (i.e. not real-time) that passes at each main script simulation pass). This value might not be constant for a given simulation.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetSimulationTimeStep.htm

        @return timeStep:list"""
        pass

    @classmethod
    def getSimulationState() -> list:
        """Retrieves current  simulation state
        @url:https://manual.coppeliarobotics.com/en/sim/simGetSimulationState.htm

        @return simulationState:list"""
        pass

    @classmethod
    def stopSimulation(wait: list) -> None:
        """Requests a stop of the running simulation
        @url:https://manual.coppeliarobotics.com/en/sim/simStopSimulation.htm
        @param wait:list
        """
        pass

    @classmethod
    def pauseSimulation() -> None:
        """Requests a pause of a simulation
        @url:https://manual.coppeliarobotics.com/en/sim/simPauseSimulation.htm

        """
        pass

    @classmethod
    def startSimulation() -> None:
        """Requests a start of a simulation (or a resume of a paused simulation)
        @url:https://manual.coppeliarobotics.com/en/sim/simStartSimulation.htm

        """
        pass

    @classmethod
    def getGenesisEvents() -> list:
        """Retrieves all events that allow to reconstruct a scene's (mostly) visual content remotely
        @url:https://manual.coppeliarobotics.com/en/sim/simGetGenesisEvents.htm

        @return events:list"""
        pass

    @classmethod
    def restoreEntityColor(originalColorData: list) -> None:
        """Restores the color of an  entity , previously modified with  sim.changeEntityColor
        @url:https://manual.coppeliarobotics.com/en/sim/simRestoreEntityColor.htm
        @param originalColorData:list
        """
        pass

    @classmethod
    def changeEntityColor(
        entityHandle: list, newColor: list, colorComponent: list
    ) -> list:
        """Changes the color of an  entity , and returns its original color. Currently only takes into account  collections  and  shapes
        @url:https://manual.coppeliarobotics.com/en/sim/simChangeEntityColor.htm
        @param entityHandle:list
        @param newColor:list
        @param colorComponent:list
        @return originalColorData:list"""
        pass

    @classmethod
    def removeDrawingObject(objectHandle: list) -> None:
        """Removes a previously added drawing object
        @url:https://manual.coppeliarobotics.com/en/sim/simRemoveDrawingObject.htm
        @param objectHandle:list
        """
        pass

    @classmethod
    def addDrawingObjectItem(drawingObjectHandle: list, itemData: list) -> list:
        """Adds an item (or clears all items) to a previously inserted drawing object
        @url:https://manual.coppeliarobotics.com/en/sim/simAddDrawingObjectItem.htm
        @param drawingObjectHandle:list
        @param itemData:list
        @return result:list"""
        pass

    @classmethod
    def addDrawingObject(
        objectType: list,
        size: list,
        duplicateTolerance: list,
        parentObjectHandle: list,
        maxItemCount: list,
        color: list,
    ) -> list:
        """Adds a drawing object that will be displayed in the scene. Drawing objects are containers that hold several items of a given type. This can be used for several different applications (simulation of paint, simulation of welding seam, display of 3D objects, etc.). Drawing objects created in a  simulation script  will be automatically removed at simulation end
        @url:https://manual.coppeliarobotics.com/en/sim/simAddDrawingObject.htm
        @param objectType:list
        @param size:list
        @param duplicateTolerance:list
        @param parentObjectHandle:list
        @param maxItemCount:list
        @param color:list
        @return drawingObjectHandle:list"""
        pass

    @classmethod
    def serialSend() -> None:
        """Writes data to a previously opened serial port (RS-232)
        @url:https://manual.coppeliarobotics.com/en/sim/simSerialSend.htm

        """
        pass

    @classmethod
    def serialRead() -> None:
        """Reads from a previously opened serial port (RS-232). The C version of the function cannot be blocking
        @url:https://manual.coppeliarobotics.com/en/sim/simSerialRead.htm

        """
        pass

    @classmethod
    def serialOpen() -> None:
        """Opens a serial port (RS-232) for communication. When called from a script, the function can only be called when the simulation is running (and in that case the port is automatically closed at simulation stop)
        @url:https://manual.coppeliarobotics.com/en/sim/simSerialOpen.htm

        """
        pass

    @classmethod
    def serialClose() -> None:
        """Closes a serial port (RS-232)
        @url:https://manual.coppeliarobotics.com/en/sim/simSerialClose.htm

        """
        pass

    @classmethod
    def serialCheck() -> None:
        """Reads how many bytes are waiting to be read on a serial port (RS-232)
        @url:https://manual.coppeliarobotics.com/en/sim/simSerialCheck.htm

        """
        pass

    @classmethod
    def addItemToCollection(
        collectionHandle: list, what: list, objectHandle: list, options: list
    ) -> None:
        """Adds an item to a  collection
        @url:https://manual.coppeliarobotics.com/en/sim/simAddItemToCollection.htm
        @param collectionHandle:list
        @param what:list
        @param objectHandle:list
        @param options:list
        """
        pass

    @classmethod
    def destroyCollection(collectionHandle: list) -> None:
        """Removes a  collection
        @url:https://manual.coppeliarobotics.com/en/sim/simDestroyCollection.htm
        @param collectionHandle:list
        """
        pass

    @classmethod
    def createCollection(options: list) -> list:
        """Creates a new  collection . A collection created in a  simulation script , a  customization script  or in the  main script  are automatically destroyed when the script ends
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateCollection.htm
        @param options:list
        @return collectionHandle:list"""
        pass

    @classmethod
    def getPropertiesInfos(target: list, options: list) -> list:
        """Convenience function to fetches all properties infos of a specific target item
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPropertiesInfos.htm
        @param target:list
        @param options:list
        @return propertiesInfo:list"""
        pass

    @classmethod
    def setProperties(target: list, properties: list) -> None:
        """Convenience function to set several properties at once
        @url:https://manual.coppeliarobotics.com/en/sim/simSetProperties.htm
        @param target:list
        @param properties:list
        """
        pass

    @classmethod
    def getProperties(target: list, options: list) -> list:
        """Convenience function to fetches all properties of a specific target item
        @url:https://manual.coppeliarobotics.com/en/sim/simGetProperties.htm
        @param target:list
        @param options:list
        @return properties:list"""
        pass

    @classmethod
    def setProperty(
        target: list, propertyName: str, propertyState: list, propertyType: list
    ) -> None:
        """Convenience function to set a property
        @url:https://manual.coppeliarobotics.com/en/sim/simSetProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param propertyType:list
        """
        pass

    @classmethod
    def getPropertyInfo(
        target: list, propertyName: str, options: list
    ) -> Union[list, list, str]:
        """Fetches information about a specific property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPropertyInfo.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return type:list
        @return flags:list
        @return description:str"""
        pass

    @classmethod
    def getPropertyName(target: list, index: list, options: list) -> str:
        """Fetches the name of a property, based on an index
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPropertyName.htm
        @param target:list
        @param index:list
        @param options:list
        @return propertyName:str"""
        pass

    @classmethod
    def removeProperty(target: list, propertyName: str, options: list) -> None:
        """Removes a removable property
        @url:https://manual.coppeliarobotics.com/en/sim/simRemoveProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        """
        pass

    @classmethod
    def getColorProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a color property (float[3])
        @url:https://manual.coppeliarobotics.com/en/sim/simGetColorProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setColorProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a color property (float[3])
        @url:https://manual.coppeliarobotics.com/en/sim/simSetColorProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getPoseProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a pose property (double[7]: x, y, z, qx, qy, qz, qw)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPoseProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setPoseProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a pose property (double[7]: x, y, z, qx, qy, qz, qw)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetPoseProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getProperty(target: list, propertyName: str, options: list) -> list:
        """Convenience functon to fetch a property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def getQuaternionProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a quaternion property (double[4]: qx, qy, qz, qw)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetQuaternionProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setQuaternionProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a quaternion property (double[4]: qx, qy, qz, qw)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetQuaternionProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getVector3Property(target: list, propertyName: str, options: list) -> list:
        """Fetches a vector3 property (double[3])
        @url:https://manual.coppeliarobotics.com/en/sim/simGetVector3Property.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setVector3Property(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a vector3 property (double[3])
        @url:https://manual.coppeliarobotics.com/en/sim/simSetVector3Property.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getVector2Property(target: list, propertyName: str, options: list) -> list:
        """Fetches a vector2 property (double[2])
        @url:https://manual.coppeliarobotics.com/en/sim/simGetVector2Property.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setVector2Property(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a vector2 property (double[2])
        @url:https://manual.coppeliarobotics.com/en/sim/simSetVector2Property.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getFloatArrayProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a float array property (double[])
        @url:https://manual.coppeliarobotics.com/en/sim/simGetFloatArrayProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setFloatArrayProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a float array property (double[])
        @url:https://manual.coppeliarobotics.com/en/sim/simSetFloatArrayProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getIntArray2Property(target: list, propertyName: str, options: list) -> list:
        """Fetches an int[2] property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetIntArray2Property.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setIntArray2Property(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets an int[2] property
        @url:https://manual.coppeliarobotics.com/en/sim/simSetIntArray2Property.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getIntArrayProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches an int array property (int[])
        @url:https://manual.coppeliarobotics.com/en/sim/simGetIntArrayProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setIntArrayProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets an int array property (int[])
        @url:https://manual.coppeliarobotics.com/en/sim/simSetIntArrayProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getBufferProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a buffer property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetBufferProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setBufferProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a buffer property
        @url:https://manual.coppeliarobotics.com/en/sim/simSetBufferProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getStringProperty(target: list, propertyName: str, options: list) -> str:
        """Fetches a string property (text)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetStringProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:str"""
        pass

    @classmethod
    def setStringProperty(
        target: list, propertyName: str, propertyState: str, options: list
    ) -> None:
        """Sets a string property (text)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetStringProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:str
        @param options:list
        """
        pass

    @classmethod
    def getFloatProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a float property (double)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetFloatProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setFloatProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a float property (double)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetFloatProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getLongProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches an int64 property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetLongProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setLongProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets an int64 property
        @url:https://manual.coppeliarobotics.com/en/sim/simSetLongProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getIntProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches an int32 property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetIntProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setIntProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets an int32 property
        @url:https://manual.coppeliarobotics.com/en/sim/simSetIntProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def getBoolProperty(target: list, propertyName: str, options: list) -> list:
        """Fetches a boolean property
        @url:https://manual.coppeliarobotics.com/en/sim/simGetBoolProperty.htm
        @param target:list
        @param propertyName:str
        @param options:list
        @return propertyState:list"""
        pass

    @classmethod
    def setBoolProperty(
        target: list, propertyName: str, propertyState: list, options: list
    ) -> None:
        """Sets a boolean property
        @url:https://manual.coppeliarobotics.com/en/sim/simSetBoolProperty.htm
        @param target:list
        @param propertyName:str
        @param propertyState:list
        @param options:list
        """
        pass

    @classmethod
    def setObjectColor(
        objectHandle: list, index: list, colorComponent: list, rgbData: list
    ) -> None:
        """Sets the color of a scene object
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectColor.htm
        @param objectHandle:list
        @param index:list
        @param colorComponent:list
        @param rgbData:list
        """
        pass

    @classmethod
    def getObjectColor(objectHandle: list, index: list, colorComponent: list) -> list:
        """Retrieves the color of a scene object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectColor.htm
        @param objectHandle:list
        @param index:list
        @param colorComponent:list
        @return rgbData:list"""
        pass

    @classmethod
    def getObjectVelocity(objectHandle: list) -> Union[list, list]:
        """Retrieves the linear and/or angular velocity of an object, in absolute coordinates. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all objects in the scene
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectVelocity.htm
        @param objectHandle:list
        @return linearVelocity:list
        @return angularVelocity:list"""
        pass

    @classmethod
    def scaleObjects(
        objectHandles: list, scalingFactor: list, scalePositionsToo: list
    ) -> None:
        """Scales specified objects. All related values are automatically scaled appropriately (e.g. masses, forces, etc.)
        @url:https://manual.coppeliarobotics.com/en/sim/simScaleObjects.htm
        @param objectHandles:list
        @param scalingFactor:list
        @param scalePositionsToo:list
        """
        pass

    @classmethod
    def scaleObject(
        objectHandle: list, xScale: list, yScale: list, zScale: list, options: list
    ) -> None:
        """Scales specified objects in a non-isometric fashion, if possible. Only non-compound shapes can be non-isometrically scaled. Some primitive shapes can have some constraints between their axes
        @url:https://manual.coppeliarobotics.com/en/sim/simScaleObject.htm
        @param objectHandle:list
        @param xScale:list
        @param yScale:list
        @param zScale:list
        @param options:list
        """
        pass

    @classmethod
    def copyPasteObjects(objectHandles: list, options: list) -> list:
        """Copies and pastes objects
        @url:https://manual.coppeliarobotics.com/en/sim/simCopyPasteObjects.htm
        @param objectHandles:list
        @param options:list
        @return copiedObjectHandles:list"""
        pass

    @classmethod
    def getObjectSizeFactor(objectHandle: list) -> list:
        """Retrieves the size factor of a scene object. The size factor is different from the real object size. Use this to be able to adapt to scaling operations
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectSizeFactor.htm
        @param objectHandle:list
        @return sizeFactor:list"""
        pass

    @classmethod
    def setObjectSel(objectHandles: list) -> None:
        """Sets the object selection state
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectSel.htm
        @param objectHandles:list
        """
        pass

    @classmethod
    def getObjectSel() -> list:
        """Retrieves the handles of selected objects
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectSel.htm

        @return selectedObjects:list"""
        pass

    @classmethod
    def getObjectType(objectHandle: list) -> list:
        """Retrieves the type of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectType.htm
        @param objectHandle:list
        @return objectType:list"""
        pass

    @classmethod
    def setObjectQuaternion(
        objectHandle: list, quaternion: list, relativeToObjectHandle: list
    ) -> None:
        """Sets the quaternion of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectQuaternion.htm
        @param objectHandle:list
        @param quaternion:list
        @param relativeToObjectHandle:list
        """
        pass

    @classmethod
    def getObjectQuaternion(objectHandle: list, relativeToObjectHandle: list) -> list:
        """Retrieves the quaternion of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectQuaternion.htm
        @param objectHandle:list
        @param relativeToObjectHandle:list
        @return quaternion:list"""
        pass

    @classmethod
    def setObjectOrientation(
        objectHandle: list, eulerAngles: list, relativeToObjectHandle: list
    ) -> None:
        """Sets the orientation ( Euler angles ) of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectOrientation.htm
        @param objectHandle:list
        @param eulerAngles:list
        @param relativeToObjectHandle:list
        """
        pass

    @classmethod
    def getObjectOrientation(objectHandle: list, relativeToObjectHandle: list) -> list:
        """Retrieves the orientation ( Euler angles ) of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectOrientation.htm
        @param objectHandle:list
        @param relativeToObjectHandle:list
        @return eulerAngles:list"""
        pass

    @classmethod
    def setObjectPosition(
        objectHandle: list, position: list, relativeToObjectHandle: list
    ) -> None:
        """Sets the position (x, y and z-coordinates) of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectPosition.htm
        @param objectHandle:list
        @param position:list
        @param relativeToObjectHandle:list
        """
        pass

    @classmethod
    def getObjectPosition(objectHandle: list, relativeToObjectHandle: list) -> list:
        """Retrieves the position of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectPosition.htm
        @param objectHandle:list
        @param relativeToObjectHandle:list
        @return position:list"""
        pass

    @classmethod
    def setObjectPose(
        objectHandle: list, pose: list, relativeToObjectHandle: list
    ) -> None:
        """Sets the pose of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectPose.htm
        @param objectHandle:list
        @param pose:list
        @param relativeToObjectHandle:list
        """
        pass

    @classmethod
    def getObjectPose(objectHandle: list, relativeToObjectHandle: list) -> list:
        """Retrieves the pose of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectPose.htm
        @param objectHandle:list
        @param relativeToObjectHandle:list
        @return pose:list"""
        pass

    @classmethod
    def setObjectMatrix(
        objectHandle: list, matrix: list, relativeToObjectHandle: list
    ) -> None:
        """Sets the transformation matrix of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectMatrix.htm
        @param objectHandle:list
        @param matrix:list
        @param relativeToObjectHandle:list
        """
        pass

    @classmethod
    def getObjectMatrix(objectHandle: list, relativeToObjectHandle: list) -> list:
        """Retrieves the transformation matrix of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectMatrix.htm
        @param objectHandle:list
        @param relativeToObjectHandle:list
        @return matrix:list"""
        pass

    @classmethod
    def getObjectChild(objectHandle: list, index: list) -> list:
        """Retrieves the handle of an object's child object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectChild.htm
        @param objectHandle:list
        @param index:list
        @return childHandle:list"""
        pass

    @classmethod
    def setObjectHierarchyOrder(objectHandle: list, order: list) -> None:
        """Moves an object up or down among its siblings in the scene hierarchy
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectHierarchyOrder.htm
        @param objectHandle:list
        @param order:list
        """
        pass

    @classmethod
    def getObjectHierarchyOrder(objectHandle: list) -> Union[list, list]:
        """Retrieves the zero-based position of an object among its siblings in the scene hierarchy
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectHierarchyOrder.htm
        @param objectHandle:list
        @return order:list
        @return totalSiblingsCount:list"""
        pass

    @classmethod
    def setObjectParent(
        objectHandle: list, parentObjectHandle: list, keepInPlace: list
    ) -> None:
        """Sets an object's parent object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectParent.htm
        @param objectHandle:list
        @param parentObjectHandle:list
        @param keepInPlace:list
        """
        pass

    @classmethod
    def getObjectParent(objectHandle: list) -> list:
        """Retrieves the handle of an object's parent object
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectParent.htm
        @param objectHandle:list
        @return parentHandle:list"""
        pass

    @classmethod
    def setObjectAlias(objectHandle: list, objectAlias: str) -> None:
        """Sets the alias of an object
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectAlias.htm
        @param objectHandle:list
        @param objectAlias:str
        """
        pass

    @classmethod
    def getObjectAlias(objectHandle: list, options: list) -> str:
        """Retrieves the alias or path of an object based on its handle
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectAlias.htm
        @param objectHandle:list
        @param options:list
        @return alias:str"""
        pass

    @classmethod
    def removeModel(objectHandle: list, delayedRemoval: list) -> list:
        """Removes a model from the scene
        @url:https://manual.coppeliarobotics.com/en/sim/simRemoveModel.htm
        @param objectHandle:list
        @param delayedRemoval:list
        @return removedCnt:list"""
        pass

    @classmethod
    def removeObjects(objectHandles: list, delayedRemoval: list) -> None:
        """Removes one or several objects from the scene
        @url:https://manual.coppeliarobotics.com/en/sim/simRemoveObjects.htm
        @param objectHandles:list
        @param delayedRemoval:list
        """
        pass

    @classmethod
    def getObjectUid(objectHandle: list) -> list:
        """Retrieves the unique identifier of an object: throughout a CoppeliaSim session, there won't be two identical unique identifiers. Unique identifiers are however not persistent (i.e. are not saved with the object)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectUid.htm
        @param objectHandle:list
        @return uid:list"""
        pass

    @classmethod
    def getClosestPosOnPath(path: list, pathLengths: list, absPt: list) -> list:
        """Returns the position or distance along a path that is closest to a specified point in space
        @url:https://manual.coppeliarobotics.com/en/sim/simGetClosestPosOnPath.htm
        @param path:list
        @param pathLengths:list
        @param absPt:list
        @return posAlongPath:list"""
        pass

    @classmethod
    def generateTimeOptimalTrajectory(
        path: list,
        pathLengths: list,
        minMaxVel: list,
        minMaxAccel: list,
        trajPtSamples: list,
        boundaryCondition: str,
        timeout: list,
        calculationScriptHandle: list,
    ) -> Union[list, list, list]:
        """Generates a time optimal trajectory, based on the TOPPRA library
        @url:https://manual.coppeliarobotics.com/en/sim/simGenerateTimeOptimalTrajectory.htm
        @param path:list
        @param pathLengths:list
        @param minMaxVel:list
        @param minMaxAccel:list
        @param trajPtSamples:list
        @param boundaryCondition:str
        @param timeout:list
        @param calculationScriptHandle:list
        @return outP:list
        @return times:list
        @return scriptHandle:list"""
        pass

    @classmethod
    def resamplePath(
        path: list, pathLengths: list, finalConfigCnt: list, method: list, types: list
    ) -> list:
        """Returns a resampled path
        @url:https://manual.coppeliarobotics.com/en/sim/simResamplePath.htm
        @param path:list
        @param pathLengths:list
        @param finalConfigCnt:list
        @param method:list
        @param types:list
        @return outputPath:list"""
        pass

    @classmethod
    def getPathInterpolatedConfig(
        path: list, pathLengths: list, t: list, method: list, types: list
    ) -> list:
        """Returns an interpolated configuration from a path
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPathInterpolatedConfig.htm
        @param path:list
        @param pathLengths:list
        @param t:list
        @param method:list
        @param types:list
        @return config:list"""
        pass

    @classmethod
    def getPathLengths(path: list, dof: list, distCallback: str) -> Union[list, list]:
        """Returns the lengths of a path in 1, 2 or 3D Cartesian space, even if more coordinates are provided. Each path point will have a corresponding length value (taken as the distance from the path's first point, along the path)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPathLengths.htm
        @param path:list
        @param dof:list
        @param distCallback:str
        @return pathLengths:list
        @return totalLength:list"""
        pass

    @classmethod
    def getConfigDistance(
        configA: list, configB: list, metric: list, types: list
    ) -> list:
        """Returns the distance between two configurations points
        @url:https://manual.coppeliarobotics.com/en/sim/simGetConfigDistance.htm
        @param configA:list
        @param configB:list
        @param metric:list
        @param types:list
        @return distance:list"""
        pass

    @classmethod
    def createPath(
        ctrlPts: list,
        options: list,
        subdiv: list,
        smoothness: list,
        orientationMode: list,
        upVector: list,
    ) -> list:
        """Creates a  path .
        @url:https://manual.coppeliarobotics.com/en/sim/simCreatePath.htm
        @param ctrlPts:list
        @param options:list
        @param subdiv:list
        @param smoothness:list
        @param orientationMode:list
        @param upVector:list
        @return pathHandle:list"""
        pass

    @classmethod
    def getPointCloudPoints(pointCloudHandle: list) -> list:
        """Retrieves point positions from a  point cloud
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPointCloudPoints.htm
        @param pointCloudHandle:list
        @return points:list"""
        pass

    @classmethod
    def insertObjectIntoPointCloud(
        pointCloudHandle: list,
        objectHandle: list,
        options: list,
        gridSize: list,
        color: list,
        duplicateTolerance: list,
    ) -> list:
        """Inserts an object into a  point cloud , as points
        @url:https://manual.coppeliarobotics.com/en/sim/simInsertObjectIntoPointCloud.htm
        @param pointCloudHandle:list
        @param objectHandle:list
        @param options:list
        @param gridSize:list
        @param color:list
        @param duplicateTolerance:list
        @return totalPointCnt:list"""
        pass

    @classmethod
    def intersectPointsWithPointCloud(
        pcHandle: list, options: list, points: list, tolerance: list
    ) -> list:
        """Removes points from a  point cloud , that do not intersect with the provided points (i.e. the result in the point cloud will be the intersection between the two sets of points). When a point cloud doesn't use an OC tree calculation structure, then this operation cannot be performed
        @url:https://manual.coppeliarobotics.com/en/sim/simIntersectPointsWithPointCloud.htm
        @param pcHandle:list
        @param options:list
        @param points:list
        @param tolerance:list
        @return totalPointCnt:list"""
        pass

    @classmethod
    def subtractObjectFromPointCloud(
        pcHandle: list, objectHandle: list, options: list, tolerance: list
    ) -> list:
        """Removes an object from a  point cloud , as a subtraction
        @url:https://manual.coppeliarobotics.com/en/sim/simSubtractObjectFromPointCloud.htm
        @param pcHandle:list
        @param objectHandle:list
        @param options:list
        @param tolerance:list
        @return totalPointCnt:list"""
        pass

    @classmethod
    def removePointsFromPointCloud(
        pointCloudHandle: list, options: list, points: list, tolerance: list
    ) -> list:
        """Removes points from a  point cloud . When a point cloud doesn't use an OC tree calculation structure, then individual points cannot be removed, only all points can be removed in that case
        @url:https://manual.coppeliarobotics.com/en/sim/simRemovePointsFromPointCloud.htm
        @param pointCloudHandle:list
        @param options:list
        @param points:list
        @param tolerance:list
        @return totalPointCnt:list"""
        pass

    @classmethod
    def insertPointsIntoPointCloud(
        pcHandle: list,
        options: list,
        points: list,
        color: list,
        duplicateTolerance: list,
    ) -> list:
        """Inserts points into a  point cloud
        @url:https://manual.coppeliarobotics.com/en/sim/simInsertPointsIntoPointCloud.htm
        @param pcHandle:list
        @param options:list
        @param points:list
        @param color:list
        @param duplicateTolerance:list
        @return totalPointCnt:list"""
        pass

    @classmethod
    def setPointCloudOptions(
        pcHandle: list,
        maxVoxelSize: list,
        maxPtCntPerVoxel: list,
        options: list,
        pointSize: list,
    ) -> None:
        """Sets various properties of a  point cloud
        @url:https://manual.coppeliarobotics.com/en/sim/simSetPointCloudOptions.htm
        @param pcHandle:list
        @param maxVoxelSize:list
        @param maxPtCntPerVoxel:list
        @param options:list
        @param pointSize:list
        """
        pass

    @classmethod
    def getPointCloudOptions(pcHandle: list) -> Union[list, list, list, list]:
        """Gets various properties of a  point cloud
        @url:https://manual.coppeliarobotics.com/en/sim/simGetPointCloudOptions.htm
        @param pcHandle:list
        @return maxVoxelS:list
        @return maxPtCntPerVoxel:list
        @return opt:list
        @return ps:list"""
        pass

    @classmethod
    def createPointCloud(
        maxVoxelSize: list, maxPtCntPerVoxel: list, options: list, pointSize: list
    ) -> list:
        """Creates an empty  point cloud
        @url:https://manual.coppeliarobotics.com/en/sim/simCreatePointCloud.htm
        @param maxVoxelSize:list
        @param maxPtCntPerVoxel:list
        @param options:list
        @param pointSize:list
        @return handle:list"""
        pass

    @classmethod
    def checkOctreePointOccupancy(
        octreeHandle: list, options: list, points: list
    ) -> Union[list, list, list, list]:
        """Checks whether the provided points collide with the  OC tree  voxels
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckOctreePointOccupancy.htm
        @param octreeHandle:list
        @param options:list
        @param points:list
        @return res:list
        @return tag:list
        @return locLow:list
        @return locHigh:list"""
        pass

    @classmethod
    def getOctreeVoxels(octreeHandle: list) -> list:
        """Retrieves voxel positions from an  OC tree
        @url:https://manual.coppeliarobotics.com/en/sim/simGetOctreeVoxels.htm
        @param octreeHandle:list
        @return voxels:list"""
        pass

    @classmethod
    def subtractObjectFromOctree(
        octreeHandle: list, objectHandle: list, options: list
    ) -> list:
        """Removes an object from an  OC tree , as voxel subtractions
        @url:https://manual.coppeliarobotics.com/en/sim/simSubtractObjectFromOctree.htm
        @param octreeHandle:list
        @param objectHandle:list
        @param options:list
        @return totalVoxelCnt:list"""
        pass

    @classmethod
    def insertObjectIntoOctree(
        octreeHandle: list, objectHandle: list, options: list, color: list, tag: list
    ) -> list:
        """Inserts an object into an  OC tree , as voxels. Each voxel will store a color and a tag value
        @url:https://manual.coppeliarobotics.com/en/sim/simInsertObjectIntoOctree.htm
        @param octreeHandle:list
        @param objectHandle:list
        @param options:list
        @param color:list
        @param tag:list
        @return totalVoxelCnt:list"""
        pass

    @classmethod
    def removeVoxelsFromOctree(octreeHandle: list, options: list, points: list) -> list:
        """Removes voxels from an  OC tree
        @url:https://manual.coppeliarobotics.com/en/sim/simRemoveVoxelsFromOctree.htm
        @param octreeHandle:list
        @param options:list
        @param points:list
        @return totalVoxelCnt:list"""
        pass

    @classmethod
    def insertVoxelsIntoOctree(
        octreeHandle: list, options: list, points: list, color: list, tag: list
    ) -> list:
        """Inserts voxels into an  OC tree . Each voxel will store a color and a tag value
        @url:https://manual.coppeliarobotics.com/en/sim/simInsertVoxelsIntoOctree.htm
        @param octreeHandle:list
        @param options:list
        @param points:list
        @param color:list
        @param tag:list
        @return totalVoxelCnt:list"""
        pass

    @classmethod
    def createOctree(voxelSize: list, options: list, pointSize: list) -> list:
        """Creates an empty  OC tree
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateOctree.htm
        @param voxelSize:list
        @param options:list
        @param pointSize:list
        @return handle:list"""
        pass

    @classmethod
    def cameraFitToView(
        viewHandleOrIndex: list, objectHandles: list, options: list, scaling: list
    ) -> list:
        """Shifts and adjusts a camera associated with a view to fill the view entirely with the specified objects or models
        @url:https://manual.coppeliarobotics.com/en/sim/simCameraFitToView.htm
        @param viewHandleOrIndex:list
        @param objectHandles:list
        @param options:list
        @param scaling:list
        @return result:list"""
        pass

    @classmethod
    def resetGraph(graphHandle: list) -> None:
        """Resets a graph object (i.e. clears all its data streams)
        @url:https://manual.coppeliarobotics.com/en/sim/simResetGraph.htm
        @param graphHandle:list
        """
        pass

    @classmethod
    def handleGraph(graphHandle: list, time: list) -> None:
        """Handles a graph object (i.e. records another value for each curve, given that such value was provided via  sim.setGraphStreamValue
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleGraph.htm
        @param graphHandle:list
        @param time:list
        """
        pass

    @classmethod
    def duplicateGraphCurveToStatic(
        graphHandle: list, curveId: list, staticCurveName: str
    ) -> list:
        """Duplicates a graph stream or curve, and freezes it
        @url:https://manual.coppeliarobotics.com/en/sim/simDuplicateGraphCurveToStatic.htm
        @param graphHandle:list
        @param curveId:list
        @param staticCurveName:str
        @return staticCurveId:list"""
        pass

    @classmethod
    def addGraphCurve(
        graphHandle: list,
        curveName: str,
        dim: list,
        streamIds: list,
        defaultValues: list,
        unitStr: str,
        options: list,
        color: list,
        curveWidth: list,
    ) -> list:
        """Adds or updates a graph curve. A graph curve is persistent, but can be removed with  sim.destroyGraphCurve
        @url:https://manual.coppeliarobotics.com/en/sim/simAddGraphCurve.htm
        @param graphHandle:list
        @param curveName:str
        @param dim:list
        @param streamIds:list
        @param defaultValues:list
        @param unitStr:str
        @param options:list
        @param color:list
        @param curveWidth:list
        @return curveId:list"""
        pass

    @classmethod
    def setGraphStreamValue(graphHandle: list, streamId: list, value: list) -> None:
        """Sets the next value to be recorded for a graph stream
        @url:https://manual.coppeliarobotics.com/en/sim/simSetGraphStreamValue.htm
        @param graphHandle:list
        @param streamId:list
        @param value:list
        """
        pass

    @classmethod
    def setGraphStreamTransformation(
        graphHandle: list,
        streamId: list,
        trType: list,
        mult: list,
        off: list,
        movingAvgPeriod: list,
    ) -> None:
        """Applies a transformation to a graph stream
        @url:https://manual.coppeliarobotics.com/en/sim/simSetGraphStreamTransformation.htm
        @param graphHandle:list
        @param streamId:list
        @param trType:list
        @param mult:list
        @param off:list
        @param movingAvgPeriod:list
        """
        pass

    @classmethod
    def addGraphStream(
        graphHandle: list, streamName: str, unitStr: str, options: list, color: list
    ) -> list:
        """Adds or updates a graph stream. A graph stream is persistent, but can be removed with  sim.destroyGraphCurve
        @url:https://manual.coppeliarobotics.com/en/sim/simAddGraphStream.htm
        @param graphHandle:list
        @param streamName:str
        @param unitStr:str
        @param options:list
        @param color:list
        @return streamId:list"""
        pass

    @classmethod
    def createVisionSensor(options: list, intParams: list, floatParams: list) -> list:
        """Creates a  vision sensor .
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateVisionSensor.htm
        @param options:list
        @param intParams:list
        @param floatParams:list
        @return sensorHandle:list"""
        pass

    @classmethod
    def adjustView(
        viewHandleOrIndex: list, objectHandle: list, options: list, viewLabel: str
    ) -> list:
        """Adjusts parameters of a view
        @url:https://manual.coppeliarobotics.com/en/sim/simAdjustView.htm
        @param viewHandleOrIndex:list
        @param objectHandle:list
        @param options:list
        @param viewLabel:str
        @return res:list"""
        pass

    @classmethod
    def getVisionSensorRes(sensorHandle: list) -> list:
        """Returns the resolution of the vision sensor
        @url:https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorRes.htm
        @param sensorHandle:list
        @return resolution:list"""
        pass

    @classmethod
    def setVisionSensorImg(
        sensorHandle: list, image: list, options: list, pos: list, size: list
    ) -> None:
        """Writes the image of a vision sensor (and applies any image processing via the  vision callback functions ). Make sure the vision sensor is flagged as  external input
        @url:https://manual.coppeliarobotics.com/en/sim/simSetVisionSensorImg.htm
        @param sensorHandle:list
        @param image:list
        @param options:list
        @param pos:list
        @param size:list
        """
        pass

    @classmethod
    def getVisionSensorImg(
        sensorHandle: list, options: list, rgbaCutOff: list, pos: list, size: list
    ) -> Union[list, list]:
        """Reads the image of a vision sensor. The returned data doesn't make sense if  sim.handleVisionSensor  wasn't called previously
        @url:https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorImg.htm
        @param sensorHandle:list
        @param options:list
        @param rgbaCutOff:list
        @param pos:list
        @param size:list
        @return image:list
        @return resolution:list"""
        pass

    @classmethod
    def getVisionSensorDepth(
        sensorHandle: list, options: list, pos: list, size: list
    ) -> list:
        """Reads the depth buffer of a vision sensor. The returned data doesn't make sense if  sim.handleVisionSensor  wasn't called previously
        @url:https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorDepth.htm
        @param sensorHandle:list
        @param options:list
        @param pos:list
        @param size:list
        @return depth:list"""
        pass

    @classmethod
    def checkVisionSensorEx(
        sensorHandle: list, entityHandle: list, returnImage: list
    ) -> list:
        """Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleVisionSensor . The  vision callback functions  will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckVisionSensorEx.htm
        @param sensorHandle:list
        @param entityHandle:list
        @param returnImage:list
        @return buff:list"""
        pass

    @classmethod
    def checkVisionSensor(
        sensorHandle: list, entityHandle: list
    ) -> Union[list, list, list]:
        """Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleVisionSensor . The  vision callback functions  will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckVisionSensor.htm
        @param sensorHandle:list
        @param entityHandle:list
        @return result:list
        @return auxPacket1:list
        @return auxPacket2:list"""
        pass

    @classmethod
    def resetVisionSensor(sensorHandle: list) -> None:
        """Clears the detection state, etc. of a proximity sensor object
        @url:https://manual.coppeliarobotics.com/en/sim/simResetVisionSensor.htm
        @param sensorHandle:list
        """
        pass

    @classmethod
    def readVisionSensor(visionSensorHandle: list) -> Union[list, list, list]:
        """Reads the state of a vision sensor. This function doesn't perform detection, it merely reads the result from a previous call to  sim.handleVisionSensor
        @url:https://manual.coppeliarobotics.com/en/sim/simReadVisionSensor.htm
        @param visionSensorHandle:list
        @return result:list
        @return packet1:list
        @return packet2:list"""
        pass

    @classmethod
    def handleVisionSensor(visionSensorHandle: list) -> Union[list, list, list]:
        """Handles (performs sensing, etc. of) a vision sensor object. It (1) clear previous computed image processing data, (2) reads an image and (3) performs image processing via the  vision callback functions  (if the vision sensor is using an  external input  only (1) is performed)
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleVisionSensor.htm
        @param visionSensorHandle:list
        @return detectionCount:list
        @return packet1:list
        @return packet2:list"""
        pass

    @classmethod
    def createProximitySensor(
        sensorType: list,
        subType: list,
        options: list,
        intParams: list,
        floatParams: list,
    ) -> list:
        """Creates a  proximity sensor
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateProximitySensor.htm
        @param sensorType:list
        @param subType:list
        @param options:list
        @param intParams:list
        @param floatParams:list
        @return sensorHandle:list"""
        pass

    @classmethod
    def checkProximitySensorEx2(
        sensorHandle: list,
        vertices: list,
        itemType: list,
        itemCount: list,
        mode: list,
        threshold: list,
        maxAngle: list,
    ) -> Union[list, list, list, list]:
        """Checks whether the proximity sensor detects the indicated points, segments or triangles. Detection is silent (no visual feedback)
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensorEx2.htm
        @param sensorHandle:list
        @param vertices:list
        @param itemType:list
        @param itemCount:list
        @param mode:list
        @param threshold:list
        @param maxAngle:list
        @return res:list
        @return dist:list
        @return point:list
        @return n:list"""
        pass

    @classmethod
    def checkProximitySensorEx(
        handle: list,
        entityHandle: list,
        detectionMode: list,
        detectionthreshold: list,
        maxAngle: list,
    ) -> Union[list, list, list, list, list]:
        """Checks whether the proximity sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleProximitySensor . Also, the detectable flags of the entity are overridden if the entity is an object
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensorEx.htm
        @param handle:list
        @param entityHandle:list
        @param detectionMode:list
        @param detectionthreshold:list
        @param maxAngle:list
        @return res:list
        @return dist:list
        @return point:list
        @return object:list
        @return n:list"""
        pass

    @classmethod
    def checkProximitySensor(
        sensorHandle: list, entityHandle: list
    ) -> Union[list, list, list, list, list]:
        """Checks whether the proximity sensor detects the indicated entity. Detection is silent (no visual feedback) compared to  sim.handleProximitySensor . Also, the detectable flags of the entity are overridden if the entity is an object
        @url:https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensor.htm
        @param sensorHandle:list
        @param entityHandle:list
        @return res:list
        @return dist:list
        @return point:list
        @return obj:list
        @return n:list"""
        pass

    @classmethod
    def resetProximitySensor(sensorHandle: list) -> None:
        """Clears the detection state, detection color, detection segments, etc. of a proximity sensor object
        @url:https://manual.coppeliarobotics.com/en/sim/simResetProximitySensor.htm
        @param sensorHandle:list
        """
        pass

    @classmethod
    def readProximitySensor(sensorHandle: list) -> Union[list, list, list, list, list]:
        """Reads the state of a proximity sensor. This function doesn't perform detection, it merely reads the result from a previous call to  sim.handleProximitySensor
        @url:https://manual.coppeliarobotics.com/en/sim/simReadProximitySensor.htm
        @param sensorHandle:list
        @return res:list
        @return dist:list
        @return point:list
        @return obj:list
        @return n:list"""
        pass

    @classmethod
    def generateTextShape(
        txt: str, color: list, height: list, centered: list, alphabetLocation: str
    ) -> list:
        """Generates a 3D text model.
        @url:https://manual.coppeliarobotics.com/en/sim/simGenerateTextShape.htm
        @param txt:str
        @param color:list
        @param height:list
        @param centered:list
        @param alphabetLocation:str
        @return modelHandle:list"""
        pass

    @classmethod
    def setShapeBB(shapeHandle: list, size: list) -> None:
        """Sets the size of a shape's bounding box, effectively scaling the shape. Non-isometric scaling is not always possible
        @url:https://manual.coppeliarobotics.com/en/sim/simSetShapeBB.htm
        @param shapeHandle:list
        @param size:list
        """
        pass

    @classmethod
    def getShapeBB(shapeHandle: list) -> Union[list, list]:
        """Returns the size and relative pose of a shape's bounding box
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeBB.htm
        @param shapeHandle:list
        @return size:list
        @return pose:list"""
        pass

    @classmethod
    def relocateShapeFrame(shapeHandle: list, pose: list) -> list:
        """Repositions and reorients the reference frame of a shape, while keeping the mesh in place. The shape's inertia properties are unaffected.
        @url:https://manual.coppeliarobotics.com/en/sim/simRelocateShapeFrame.htm
        @param shapeHandle:list
        @param pose:list
        @return result:list"""
        pass

    @classmethod
    def alignShapeBB(shapeHandle: list, pose: list) -> list:
        """Reorients the bounding box of a shape, while keeping the shape frame in place. The shape's inertia properties are unaffected
        @url:https://manual.coppeliarobotics.com/en/sim/simAlignShapeBB.htm
        @param shapeHandle:list
        @param pose:list
        @return result:list"""
        pass

    @classmethod
    def ungroupShape(shapeHandle: list) -> list:
        """Ungroups a compound shape into several  shapes
        @url:https://manual.coppeliarobotics.com/en/sim/simUngroupShape.htm
        @param shapeHandle:list
        @return shapeHandles:list"""
        pass

    @classmethod
    def groupShapes(shapeHandles: list, merge: list) -> list:
        """Groups (or merges) several shapes into a  compound shape  (or  simple shape )
        @url:https://manual.coppeliarobotics.com/en/sim/simGroupShapes.htm
        @param shapeHandles:list
        @param merge:list
        @return shapeHandle:list"""
        pass

    @classmethod
    def handleProximitySensor(
        sensorHandle: list,
    ) -> Union[list, list, list, list, list]:
        """Handles (performs sensing, etc. of) a registered proximity sensor object
        @url:https://manual.coppeliarobotics.com/en/sim/simHandleProximitySensor.htm
        @param sensorHandle:list
        @return res:list
        @return dist:list
        @return point:list
        @return obj:list
        @return n:list"""
        pass

    @classmethod
    def getExtensionString(objectHandle: list, index: list, key: str) -> str:
        """Retrieves a string that describes additional environment or object properties, mainly used by extension plugins.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetExtensionString.htm
        @param objectHandle:list
        @param index:list
        @param key:str
        @return theString:str"""
        pass

    @classmethod
    def getShapeViz(shapeHandle: list, index: list) -> list:
        """Retrieves a shape's visual information.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeViz.htm
        @param shapeHandle:list
        @param index:list
        @return data:list"""
        pass

    @classmethod
    def getShapeMesh(shapeHandle: list) -> Union[list, list, list]:
        """Retrieves a shape's mesh information
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeMesh.htm
        @param shapeHandle:list
        @return vertices:list
        @return indices:list
        @return normals:list"""
        pass

    @classmethod
    def createHeightfieldShape(
        options: list,
        shadingAngle: list,
        xPointCount: list,
        yPointCount: list,
        xSize: list,
        heights: list,
    ) -> list:
        """Creates a heightfield  shape
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateHeightfieldShape.htm
        @param options:list
        @param shadingAngle:list
        @param xPointCount:list
        @param yPointCount:list
        @param xSize:list
        @param heights:list
        @return objectHandle:list"""
        pass

    @classmethod
    def createPrimitiveShape(primitiveType: list, sizes: list, options: list) -> list:
        """Creates a primitive shape
        @url:https://manual.coppeliarobotics.com/en/sim/simCreatePrimitiveShape.htm
        @param primitiveType:list
        @param sizes:list
        @param options:list
        @return shapeHandle:list"""
        pass

    @classmethod
    def createShape(
        options: list,
        shadingAngle: list,
        vertices: list,
        indices: list,
        normals: list,
        textureCoordinates: list,
        texture: list,
        textureResolution: list,
    ) -> list:
        """Creates a mesh shape
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateShape.htm
        @param options:list
        @param shadingAngle:list
        @param vertices:list
        @param indices:list
        @param normals:list
        @param textureCoordinates:list
        @param texture:list
        @param textureResolution:list
        @return objectHandle:list"""
        pass

    @classmethod
    def setShapeTexture(
        shapeHandle: list,
        textureId: list,
        mappingMode: list,
        options: list,
        uvScaling: list,
        position: list,
        orientation: list,
    ) -> None:
        """Applies/removes a texture to/from a shape
        @url:https://manual.coppeliarobotics.com/en/sim/simSetShapeTexture.htm
        @param shapeHandle:list
        @param textureId:list
        @param mappingMode:list
        @param options:list
        @param uvScaling:list
        @param position:list
        @param orientation:list
        """
        pass

    @classmethod
    def getShapeTextureId(shapeHandle: list) -> list:
        """Retrieves the texture ID of a texture that is applied to a specific shape
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeTextureId.htm
        @param shapeHandle:list
        @return textureId:list"""
        pass

    @classmethod
    def setShapeColor(
        shapeHandle: list, colorName: str, colorComponent: list, rgbData: list
    ) -> None:
        """Sets the color of a shape
        @url:https://manual.coppeliarobotics.com/en/sim/simSetShapeColor.htm
        @param shapeHandle:list
        @param colorName:str
        @param colorComponent:list
        @param rgbData:list
        """
        pass

    @classmethod
    def getShapeColor(
        shapeHandle: list, colorName: str, colorComponent: list
    ) -> Union[list, list]:
        """Retrieves the color of a shape
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeColor.htm
        @param shapeHandle:list
        @param colorName:str
        @param colorComponent:list
        @return result:list
        @return rgbData:list"""
        pass

    @classmethod
    def getJointDependency(jointHandle: list) -> Union[list, list, list]:
        """Retrieves joint dependency information, when the joint is in dependent mode
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointDependency.htm
        @param jointHandle:list
        @return masterJointHandle:list
        @return offset:list
        @return multCoeff:list"""
        pass

    @classmethod
    def setJointDependency(
        jointHandle: list, masterJointHandle: list, offset: list, multCoeff: list
    ) -> None:
        """Sets a joint dependent of another joint. The dependent joint should first be set into dependent mode via  sim.setJointMode
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointDependency.htm
        @param jointHandle:list
        @param masterJointHandle:list
        @param offset:list
        @param multCoeff:list
        """
        pass

    @classmethod
    def getJointMode(jointHandle: list) -> list:
        """Retrieves the operation mode of a joint
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointMode.htm
        @param jointHandle:list
        @return jointMode:list"""
        pass

    @classmethod
    def setJointMode(jointHandle: list, jointMode: list) -> None:
        """Sets the operation mode of a joint
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointMode.htm
        @param jointHandle:list
        @param jointMode:list
        """
        pass

    @classmethod
    def createJoint(
        jointType: list, jointMode: list, options: list, sizes: list
    ) -> list:
        """Creates a  joint
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateJoint.htm
        @param jointType:list
        @param jointMode:list
        @param options:list
        @param sizes:list
        @return jointHandle:list"""
        pass

    @classmethod
    def getJointType(objectHandle: list) -> list:
        """Retrieves the type of a joint
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointType.htm
        @param objectHandle:list
        @return jointType:list"""
        pass

    @classmethod
    def getJointInterval(objectHandle: list) -> Union[list, list]:
        """Retrieves the interval parameters of a joint
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointInterval.htm
        @param objectHandle:list
        @return cyclic:list
        @return interval:list"""
        pass

    @classmethod
    def setJointInterval(objectHandle: list, cyclic: list, interval: list) -> None:
        """Sets the interval parameters of a joint (i.e. range values). The attributes or interval parameters might have no effect, depending on the joint-type
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointInterval.htm
        @param objectHandle:list
        @param cyclic:list
        @param interval:list
        """
        pass

    @classmethod
    def setObjectChildPose(objectHandle: list, pose: list) -> None:
        """Can be used to set a spherical joint's rotational transformation (the translational part is ignored)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetObjectChildPose.htm
        @param objectHandle:list
        @param pose:list
        """
        pass

    @classmethod
    def getObjectChildPose(objectHandle: list) -> list:
        """Retrieves the intrinsic or internal transformation of an object. For a joint, this is the transformation caused by the joint movement, mainly. For joints and force sensors, this will also include a possible error transformation caused by the physics engine (a physics engine can cause joints and force sensors to come apart, when constraints can't be perfectly resolved)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectChildPose.htm
        @param objectHandle:list
        @return pose:list"""
        pass

    @classmethod
    def getJointVelocity(jointHandle: list) -> list:
        """Retrieves the linear or angular velocity of a joint. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all joints in the scene
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointVelocity.htm
        @param jointHandle:list
        @return velocity:list"""
        pass

    @classmethod
    def getJointTargetVelocity(objectHandle: list) -> list:
        """Retrieves the target linear/angular velocity of a non-spherical joint
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointTargetVelocity.htm
        @param objectHandle:list
        @return targetVelocity:list"""
        pass

    @classmethod
    def getJointTargetPosition(objectHandle: list) -> list:
        """Retrieves the target linear/angular position of a joint
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointTargetPosition.htm
        @param objectHandle:list
        @return targetPosition:list"""
        pass

    @classmethod
    def getJointPosition(objectHandle: list) -> list:
        """Retrieves the linear/angular position of a joint. This function cannot be used with spherical joints (use  sim.getObjectChildPose  instead)
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointPosition.htm
        @param objectHandle:list
        @return position:list"""
        pass

    @classmethod
    def setJointPosition(objectHandle: list, position: list) -> None:
        """Sets the linear/angular position of a joint. Cannot be used with spherical joints (use  sim.setObjectChildPose  instead)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointPosition.htm
        @param objectHandle:list
        @param position:list
        """
        pass

    @classmethod
    def setEventFilters(filters: list) -> None:
        """Specifies filters for the sysCall_event callback. Operates on a per script basis
        @url:https://manual.coppeliarobotics.com/en/sim/simSetEventFilters.htm
        @param filters:list
        """
        pass

    @classmethod
    def getStackTraceback() -> None:
        """Lua only. Retrieves and clears the last generated stack traceback for a script
        @url:https://manual.coppeliarobotics.com/en/sim/simGetStackTraceback.htm

        """
        pass

    @classmethod
    def registerScriptFuncHook() -> None:
        """Registers a script function hook for  callback functions , that will be executed before or after the specified function. Calling this function a second time with the same arguments will unregister a previous hook
        @url:https://manual.coppeliarobotics.com/en/sim/simRegisterScriptFuncHook.htm

        """
        pass

    @classmethod
    def getApiInfo(scriptHandle: list, apiWord: str) -> str:
        """Returns the call tip (or info text) for an API function
        @url:https://manual.coppeliarobotics.com/en/sim/simGetApiInfo.htm
        @param scriptHandle:list
        @param apiWord:str
        @return info:str"""
        pass

    @classmethod
    def getApiFunc(scriptHandle: list, apiWord: str) -> list:
        """Retrieves all API functions and variables that match a specific word. Useful for script code auto-completion functionality
        @url:https://manual.coppeliarobotics.com/en/sim/simGetApiFunc.htm
        @param scriptHandle:list
        @param apiWord:str
        @return funcsAndVars:list"""
        pass

    @classmethod
    def executeScriptString(stringToExecute: str, scriptHandle: list) -> list:
        """Executes some code in a specific script (from a  plugin ,  the main client application , or from another script). The target script must be initialized for this call to succeed, e.g. when calling  simulation scripts , then simulation must be running                 From C/C++, data exchange between a plugin and a script happens via a  stack . Reading and writing arguments from/to the stack gives you a maximum of flexibility, and you wil be able to exchange also complex data structures. But it can also be tedious and error prone. Use instead the helper classes located in  programming/include/simStack
        @url:https://manual.coppeliarobotics.com/en/sim/simExecuteScriptString.htm
        @param stringToExecute:str
        @param scriptHandle:list
        @return result:list"""
        pass

    @classmethod
    def getScriptFunctions() -> None:
        """Retrieves a map of another script functions, that can be called
        @url:https://manual.coppeliarobotics.com/en/sim/simGetScriptFunctions.htm

        """
        pass

    @classmethod
    def callScriptFunction(functionName: str, scriptHandle: list) -> None:
        """Calls a script function (from a  plugin ,  the main client application , or from another script). This represents a  user callback  inside of a script. The target script must be initialized for this call to succeed, e.g. when calling  simulation scripts , then simulation must be running
        @url:https://manual.coppeliarobotics.com/en/sim/simCallScriptFunction.htm
        @param functionName:str
        @param scriptHandle:list
        """
        pass

    @classmethod
    def initScript(scriptHandle: list) -> None:
        """Initializes/reinitializes a script. Operates in an asynchronous way, and cannot be called from within the script being reinitialized
        @url:https://manual.coppeliarobotics.com/en/sim/simInitScript.htm
        @param scriptHandle:list
        """
        pass

    @classmethod
    def getScript(scriptType: list, scriptName: str) -> list:
        """Retrieves the handle of a script. For script objects, use sim.getObject instead
        @url:https://manual.coppeliarobotics.com/en/sim/simGetScript.htm
        @param scriptType:list
        @param scriptName:str
        @return scriptHandle:list"""
        pass

    @classmethod
    def getRandom(seed: list) -> list:
        """Generates a random value in the range between 0.0 and 1.0. The value is generated from an individual generator attached to the calling script
        @url:https://manual.coppeliarobotics.com/en/sim/simGetRandom.htm
        @param seed:list
        @return randomValue:list"""
        pass

    @classmethod
    def createScript(scriptType: list, scriptText: str, options: list) -> list:
        """Creates a  script object .
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateScript.htm
        @param scriptType:list
        @param scriptText:str
        @param options:list
        @return scriptHandle:list"""
        pass

    @classmethod
    def createDummy(size: list) -> list:
        """Creates a  dummy .
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateDummy.htm
        @param size:list
        @return dummyHandle:list"""
        pass

    @classmethod
    def isDynamicallyEnabled(objectHandle: list) -> list:
        """Checks whether a scene object is dynamically enabled, i.e. is being handled and simulated by the physics engine. Note that until the physics engine has parsed the scene in the first simulation step (i.e. the first time  sim.handleDynamics  is called), no object will be dynamically enabled
        @url:https://manual.coppeliarobotics.com/en/sim/simIsDynamicallyEnabled.htm
        @param objectHandle:list
        @return dynamicallyEnabled:list"""
        pass

    @classmethod
    def createForceSensor(options: list, intParams: list, floatParams: list) -> list:
        """Creates a  force sensor .
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateForceSensor.htm
        @param options:list
        @param intParams:list
        @param floatParams:list
        @return sensorHandle:list"""
        pass

    @classmethod
    def computeMassAndInertia(shapeHandle: list, density: list) -> list:
        """Computes and applies the mass and inertia matrix for a shape, based on its convex representation. When calling this function while the simulation is running, one should then call  sim.resetDynamicObject , for the changes to take effect
        @url:https://manual.coppeliarobotics.com/en/sim/simComputeMassAndInertia.htm
        @param shapeHandle:list
        @param density:list
        @return result:list"""
        pass

    @classmethod
    def setShapeInertia(
        shapeHandle: list, inertiaMatrix: list, transformationMatrix: list
    ) -> None:
        """Applies a new inertia matrix to a shape. If simulation is running, the shape is dynamically reset (similar to calling  sim.resetDynamicObject  right after)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetShapeInertia.htm
        @param shapeHandle:list
        @param inertiaMatrix:list
        @param transformationMatrix:list
        """
        pass

    @classmethod
    def getShapeInertia(shapeHandle: list) -> Union[list, list]:
        """Retrieves the inertia information from a shape
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeInertia.htm
        @param shapeHandle:list
        @return inertiaMatrix:list
        @return com:list"""
        pass

    @classmethod
    def setShapeMass(shapeHandle: list, mass: list) -> None:
        """Applies a new mass value to a shape. If simulation is running, the shape is dynamically reset (similar to calling  sim.resetDynamicObject  right after)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetShapeMass.htm
        @param shapeHandle:list
        @param mass:list
        """
        pass

    @classmethod
    def getShapeMass(shapeHandle: list) -> list:
        """Retrieves the mass of a shape
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeMass.htm
        @param shapeHandle:list
        @return mass:list"""
        pass

    @classmethod
    def getContactInfo(
        dynamicPass: list, objectHandle: list, index: list
    ) -> Union[list, list, list, list]:
        """Retrieves contact point information of a dynamic simulation pass.
        @url:https://manual.coppeliarobotics.com/en/sim/simGetContactInfo.htm
        @param dynamicPass:list
        @param objectHandle:list
        @param index:list
        @return coll:list
        @return point:list
        @return rForce:list
        @return n:list"""
        pass

    @classmethod
    def removeParticleObject(objectHandle: list) -> None:
        """Removes a previously added particle object
        @url:https://manual.coppeliarobotics.com/en/sim/simRemoveParticleObject.htm
        @param objectHandle:list
        """
        pass

    @classmethod
    def addParticleObjectItem(particleObjectHandle: list, itemData: list) -> None:
        """Adds an item (or clears all items) to a previously inserted particle object
        @url:https://manual.coppeliarobotics.com/en/sim/simAddParticleObjectItem.htm
        @param particleObjectHandle:list
        @param itemData:list
        """
        pass

    @classmethod
    def addParticleObject(
        objectType: list,
        size: list,
        density: list,
        parameters: list,
        lifeTime: list,
        maxItemCount: list,
        color: list,
    ) -> list:
        """Adds a particle object that will be simulated and displayed in the scene. Particle objects are containers that hold several items (particles) of a given type. This can be used for several different applications (e.g. simulation of air/water jets)
        @url:https://manual.coppeliarobotics.com/en/sim/simAddParticleObject.htm
        @param objectType:list
        @param size:list
        @param density:list
        @param parameters:list
        @param lifeTime:list
        @param maxItemCount:list
        @param color:list
        @return particleObjectHandle:list"""
        pass

    @classmethod
    def resetDynamicObject(objectHandle: list) -> None:
        """Dynamically resets an object that is dynamically simulated. This means that the object representation in the dynamics engine is removed, and added again. This can be useful when the set-up of a dynamically simulated chain needs to be modified during simulation (e.g. joint or shape attachement position/orientation changed)
        @url:https://manual.coppeliarobotics.com/en/sim/simResetDynamicObject.htm
        @param objectHandle:list
        """
        pass

    @classmethod
    def setLinkDummy(dummyHandle: list, linkedDummyHandle: list) -> None:
        """Defines (or breaks) a dummy-dummy link pair. Useful to create dynamic loop closure constraints on the fly (among others)
        @url:https://manual.coppeliarobotics.com/en/sim/simSetLinkDummy.htm
        @param dummyHandle:list
        @param linkedDummyHandle:list
        """
        pass

    @classmethod
    def getLinkDummy(dummyHandle: list) -> list:
        """Retrieves the object handle of the dummy linked to this one
        @url:https://manual.coppeliarobotics.com/en/sim/simGetLinkDummy.htm
        @param dummyHandle:list
        @return linkedDummyHandle:list"""
        pass

    @classmethod
    def getVelocity(shapeHandle: list) -> Union[list, list]:
        """Retrieves the linear and/or angular velocity of the center of mass of a non-static shape. Data is provided by the selected physics engine
        @url:https://manual.coppeliarobotics.com/en/sim/simGetVelocity.htm
        @param shapeHandle:list
        @return linearVelocity:list
        @return angularVelocity:list"""
        pass

    @classmethod
    def addForce(shapeHandle: list, position: list, force: list) -> None:
        """Adds a non-central force to a shape object that is dynamically enabled. Added forces are cumulative, applied relative to the center of mass, and are reset to zero after  sim.handleDynamics  was called (or by using the following flag: sim.handleflag_resetforcetorque)
        @url:https://manual.coppeliarobotics.com/en/sim/simAddForce.htm
        @param shapeHandle:list
        @param position:list
        @param force:list
        """
        pass

    @classmethod
    def setJointTargetForce(objectHandle: list, forceOrTorque: list) -> None:
        """Sets the force or torque that a joint can exert
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointTargetForce.htm
        @param objectHandle:list
        @param forceOrTorque:list
        """
        pass

    @classmethod
    def getJointTargetForce(jointHandle: list) -> list:
        """Retrieves the force or torque that a joint can exert
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointTargetForce.htm
        @param jointHandle:list
        @return forceOrTorque:list"""
        pass

    @classmethod
    def getJointForce(jointHandle: list) -> list:
        """Retrieves the force or torque applied to a joint along/about its active axis. This function retrieves meaningful information only if the joint is prismatic or revolute, and is dynamically enabled. With the Bullet, MuJoCo and Newton engine, this function returns the force or torque applied to the joint motor  (torques from joint limits are not taken into account). With the ODE and Vortex engine, this function returns the total force or torque applied to a joint along/about its z-axis
        @url:https://manual.coppeliarobotics.com/en/sim/simGetJointForce.htm
        @param jointHandle:list
        @return forceOrTorque:list"""
        pass

    @classmethod
    def readForceSensor(objectHandle: list) -> Union[list, list, list]:
        """Reads the force and torque applied to a force sensor (filtered values are read)
        @url:https://manual.coppeliarobotics.com/en/sim/simReadForceSensor.htm
        @param objectHandle:list
        @return result:list
        @return forceVector:list
        @return torqueVector:list"""
        pass

    @classmethod
    def setJointTargetVelocity(
        objectHandle: list, targetVelocity: list, motionParams: list
    ) -> None:
        """Sets the target linear/angular velocity of a non-spherical joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum acceleration and jerk values. In dynamic and velocity control mode, the controller is instructed about the desired velocity
        @url:https://manual.coppeliarobotics.com/en/sim/simSetJointTargetVelocity.htm
        @param objectHandle:list
        @param targetVelocity:list
        @param motionParams:list
        """
        pass

    @classmethod
    def getObjectFromUid(objectUid: list, options: list) -> list:
        """Retrieves an object handle based on its unique identifier
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObjectFromUid.htm
        @param objectUid:list
        @param options:list
        @return objectHandle:list"""
        pass

    @classmethod
    def addForceAndTorque(shapeHandle: list, force: list, torque: list) -> None:
        """Adds a force and/or torque to a shape object that is dynamically enabled. Forces are applied at the center of mass. Added forces and torques are cumulative, and are reset to zero after  sim.handleDynamics  was called (or by using the following flags: sim.handleflag_resetforce and/or sim.handleflag_resettorque)
        @url:https://manual.coppeliarobotics.com/en/sim/simAddForceAndTorque.htm
        @param shapeHandle:list
        @param force:list
        @param torque:list
        """
        pass

    @classmethod
    def getObject(objectPath: str, options: list) -> list:
        """Retrieves an object handle based on its path and alias
        @url:https://manual.coppeliarobotics.com/en/sim/simGetObject.htm
        @param objectPath:str
        @param options:list
        @return objectHandle:list"""
        pass

    @classmethod
    def createTexture(
        fileName: str,
        options: list,
        planeSizes: list,
        scalingUV: list,
        xy_g: list,
        fixedResolution: list,
        resolution: list,
    ) -> Union[list, list, list]:
        """Creates a planar shape, that will be textured with a new, or imported texture
        @url:https://manual.coppeliarobotics.com/en/sim/simCreateTexture.htm
        @param fileName:str
        @param options:list
        @param planeSizes:list
        @param scalingUV:list
        @param xy_g:list
        @param fixedResolution:list
        @param resolution:list
        @return shape:list
        @return id:list
        @return res:list"""
        pass

    @classmethod
    def launchExecutable(filename: str, parameters: str, showStatus: list) -> None:
        """Launches an executable. Similar to os.execute or io.popen, but is system independent.
        @url:https://manual.coppeliarobotics.com/en/sim/simLaunchExecutable.htm
        @param filename:str
        @param parameters:str
        @param showStatus:list
        """
        pass

    @classmethod
    def exportMesh(
        fileformat: list,
        pathAndFilename: str,
        options: list,
        scalingFactor: list,
        vertices: list,
        indices: list,
    ) -> None:
        """Exports a mesh to a file
        @url:https://manual.coppeliarobotics.com/en/sim/simExportMesh.htm
        @param fileformat:list
        @param pathAndFilename:str
        @param options:list
        @param scalingFactor:list
        @param vertices:list
        @param indices:list
        """
        pass

    @classmethod
    def importMesh(
        fileformat: list,
        pathAndFilename: str,
        options: list,
        identicalVerticeTolerance: list,
        scalingFactor: list,
    ) -> Union[list, list]:
        """Imports a mesh from a file
        @url:https://manual.coppeliarobotics.com/en/sim/simImportMesh.htm
        @param fileformat:list
        @param pathAndFilename:str
        @param options:list
        @param identicalVerticeTolerance:list
        @param scalingFactor:list
        @return vertices:list
        @return indices:list"""
        pass

    @classmethod
    def importShape(
        fileformat: list,
        pathAndFilename: str,
        options: list,
        identicalVerticeTolerance: list,
        scalingFactor: list,
    ) -> list:
        """Imports a  shape  from a file (first imports meshes, then groups/merges them into a shape)
        @url:https://manual.coppeliarobotics.com/en/sim/simImportShape.htm
        @param fileformat:list
        @param pathAndFilename:str
        @param options:list
        @param identicalVerticeTolerance:list
        @param scalingFactor:list
        @return shapeHandle:list"""
        pass

    @classmethod
    def loadModel(filename: str) -> list:
        """Loads a previously saved model, and selects it
        @url:https://manual.coppeliarobotics.com/en/sim/simLoadModel.htm
        @param filename:str
        @return objectHandle:list"""
        pass

    @classmethod
    def saveModel(baseOfModelHandle: list, filename: str) -> list:
        """Saves a model (an object marked as "Object is model base" and all other objects in its hierarchy tree). Any existing file with same name will be overwritten
        @url:https://manual.coppeliarobotics.com/en/sim/simSaveModel.htm
        @param baseOfModelHandle:list
        @param filename:str
        @return buffer:list"""
        pass

    @classmethod
    def loadScene(filenameOrBuffer: list) -> None:
        """Loads a previously saved scene
        @url:https://manual.coppeliarobotics.com/en/sim/simLoadScene.htm
        @param filenameOrBuffer:list
        """
        pass

    @classmethod
    def saveScene(filename: str) -> list:
        """Saves a scene. Any existing file with same name will be overwritten
        @url:https://manual.coppeliarobotics.com/en/sim/simSaveScene.htm
        @param filename:str
        @return buffer:list"""
        pass

    @classmethod
    def closeScene() -> list:
        """Closes current scene, and switches to another open scene. If there is no other open scene, a new scene is then created. Can only be called from an  add-on , or from the sanbox script, when called from within CoppeliaSim
        @url:https://manual.coppeliarobotics.com/en/sim/simCloseScene.htm

        @return result:list"""
        pass

    @classmethod
    def getShapeGeomInfo(shapeHandle: list) -> Union[list, list, list]:
        """Retrieves geometric information related to a shape
        @url:https://manual.coppeliarobotics.com/en/sim/simGetShapeGeomInfo.htm
        @param shapeHandle:list
        @return result:list
        @return pureType:list
        @return dimensions:list"""
        pass

    @classmethod
    def destroyGraphCurve(graphHandle: list, curveId: list) -> None:
        """Destroys a graph stream or curve
        @url:https://manual.coppeliarobotics.com/en/sim/simDestroyGraphCurve.htm
        @param graphHandle:list
        @param curveId:list
        """
        pass


class SimROS2:
    @classmethod
    def actionClientTreatUInt8ArrayAsString(actionClientHandle: str) -> None:
        """After calling this function, this action client will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionClientTreatUInt8ArrayAsString
        @param actionClientHandle:str
        """
        pass

    @classmethod
    def actionServerActionAbort(
        actionServerHandle: str, goalUUID: str, result: list
    ) -> None:
        """Indicate that a goal could not be reached and has been aborted. Only call this if the goal was executing but cannot be completed. This is a terminal state, no more methods should be called on a goal after this is called.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionAbort
        @param actionServerHandle:str
        @param goalUUID:str
        @param result:list
        """
        pass

    @classmethod
    def actionServerActionCanceled(
        actionServerHandle: str, goalUUID: str, result: list
    ) -> None:
        """Indicate that a goal has been canceled. Only call this if the goal is executing or pending, but has been canceled. This is a terminal state, no more methods should be called on a goal after this is called.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionCanceled
        @param actionServerHandle:str
        @param goalUUID:str
        @param result:list
        """
        pass

    @classmethod
    def actionServerActionExecute(actionServerHandle: str, goalUUID: str) -> None:
        """Indicate that the server is starting to execute a goal. Only call this if the goal is pending.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionExecute
        @param actionServerHandle:str
        @param goalUUID:str
        """
        pass

    @classmethod
    def actionServerActionIsActive(actionServerHandle: str, goalUUID: str) -> list:
        """Check if goal is pending or executing
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionIsActive
        @param actionServerHandle:str
        @param goalUUID:str
        @return result:list"""
        pass

    @classmethod
    def actionServerActionIsCanceling(actionServerHandle: str, goalUUID: str) -> list:
        """Check if there is a cancel request
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionIsCanceling
        @param actionServerHandle:str
        @param goalUUID:str
        @return result:list"""
        pass

    @classmethod
    def actionServerActionIsExecuting(actionServerHandle: str, goalUUID: str) -> list:
        """Check if the goal is executing
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionIsExecuting
        @param actionServerHandle:str
        @param goalUUID:str
        @return result:list"""
        pass

    @classmethod
    def actionServerActionSucceed(
        actionServerHandle: str, goalUUID: str, result: list
    ) -> None:
        """Indicate that a goal has succeeded. Only call this if the goal is executing and has reached the desired final state. This is a terminal state, no more methods should be called on a goal after this is called.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerActionSucceed
        @param actionServerHandle:str
        @param goalUUID:str
        @param result:list
        """
        pass

    @classmethod
    def actionServerPublishFeedback(
        actionServerHandle: str, goalUUID: str, feedback: list
    ) -> None:
        """Send an update about the progress of this goal. This must be only called when the goal is executing. If execution of a goal is deferred then
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerPublishFeedback
        @param actionServerHandle:str
        @param goalUUID:str
        @param feedback:list
        """
        pass

    @classmethod
    def actionServerTreatUInt8ArrayAsString(actionServerHandle: str) -> None:
        """After calling this function, this action server will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionServerTreatUInt8ArrayAsString
        @param actionServerHandle:str
        """
        pass

    @classmethod
    def call(clientHandle: str, request: list) -> list:
        """Call the service associated with this service client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#call
        @param clientHandle:str
        @param request:list
        @return result:list"""
        pass

    @classmethod
    def cancelLastGoal(actionClientHandle: str) -> list:
        """Cancel last submitted goal on the specified action client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#cancelLastGoal
        @param actionClientHandle:str
        @return success:list"""
        pass

    @classmethod
    def clientTreatUInt8ArrayAsString(clientHandle: str) -> None:
        """After calling this function, this service client will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#clientTreatUInt8ArrayAsString
        @param clientHandle:str
        """
        pass

    @classmethod
    def createActionClient(
        actionName: str,
        actionType: str,
        goalResponseCallback: list,
        feedbackCallback: list,
        resultCallback: list,
    ) -> str:
        """Create a action client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createActionClient
        @param actionName:str
        @param actionType:str
        @param goalResponseCallback:list
        @param feedbackCallback:list
        @param resultCallback:list
        @return actionClientHandle:str"""
        pass

    @classmethod
    def createActionServer(
        actionName: str,
        actionType: str,
        handleGoalCallback: list,
        handleCancelCallback: list,
        handleAcceptedCallback: list,
    ) -> str:
        """Create an action server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createActionServer
        @param actionName:str
        @param actionType:str
        @param handleGoalCallback:list
        @param handleCancelCallback:list
        @param handleAcceptedCallback:list
        @return actionServerHandle:str"""
        pass

    @classmethod
    def createClient(serviceName: str, serviceType: str) -> str:
        """Create a service client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createClient
        @param serviceName:str
        @param serviceType:str
        @return clientHandle:str"""
        pass

    @classmethod
    def createInterface(type: str) -> list:
        """Construct an interface of the specified type, initialized with the default values.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createInterface
        @param type:str
        @return result:list"""
        pass

    @classmethod
    def createPublisher(
        topicName: str, topicType: str, unused: list, unused2: list, qos: list
    ) -> str:
        """Create a topic publisher.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createPublisher
        @param topicName:str
        @param topicType:str
        @param unused:list
        @param unused2:list
        @param qos:list
        @return publisherHandle:str"""
        pass

    @classmethod
    def createService(serviceName: str, serviceType: str, serviceCallback: list) -> str:
        """Create a service.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createService
        @param serviceName:str
        @param serviceType:str
        @param serviceCallback:list
        @return serviceHandle:str"""
        pass

    @classmethod
    def createSubscription(
        topicName: str, topicType: str, topicCallback: list, unused: list, qos: list
    ) -> str:
        """Create a subscription to a topic.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#createSubscription
        @param topicName:str
        @param topicType:str
        @param topicCallback:list
        @param unused:list
        @param qos:list
        @return subscriptionHandle:str"""
        pass

    @classmethod
    def deleteParam(name: str) -> None:
        """Delete a parameter in the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#deleteParam
        @param name:str
        """
        pass

    @classmethod
    def getInterfaceConstants(type: str) -> list:
        """Get an object with the constants defined in the specified interface.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getInterfaceConstants
        @param type:str
        @return result:list"""
        pass

    @classmethod
    def getParamBool(name: str, defaultValue: list) -> Union[list, list]:
        """Retrieve a boolean parameter from the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamBool
        @param name:str
        @param defaultValue:list
        @return exists:list
        @return value:list"""
        pass

    @classmethod
    def getParamDouble(name: str, defaultValue: list) -> Union[list, list]:
        """Retrieve a double parameter from the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamDouble
        @param name:str
        @param defaultValue:list
        @return exists:list
        @return value:list"""
        pass

    @classmethod
    def getParamInt(name: str, defaultValue: list) -> Union[list, list]:
        """Retrieve an integer parameter from the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamInt
        @param name:str
        @param defaultValue:list
        @return exists:list
        @return value:list"""
        pass

    @classmethod
    def getParamString(name: str, defaultValue: str) -> Union[list, str]:
        """Retrieve a string parameter from the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getParamString
        @param name:str
        @param defaultValue:str
        @return exists:list
        @return value:str"""
        pass

    @classmethod
    def getSimulationTime() -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getSimulationTime

        """
        pass

    @classmethod
    def getSystemTime() -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getSystemTime

        """
        pass

    @classmethod
    def getTime(clock_type: list) -> list:
        """Return the current time according to the specified clock.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#getTime
        @param clock_type:list
        @return time:list"""
        pass

    @classmethod
    def hasParam(name: str) -> list:
        """Check wether a parameter exists in the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#hasParam
        @param name:str
        @return exists:list"""
        pass

    @classmethod
    def imageTransportCreatePublisher(topicName: str, queueSize: list) -> str:
        """Create a publisher using ImageTransport.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportCreatePublisher
        @param topicName:str
        @param queueSize:list
        @return publisherHandle:str"""
        pass

    @classmethod
    def imageTransportCreateSubscription(
        topicName: str, topicCallback: list, queueSize: list
    ) -> str:
        """Create a subscription using ImageTransport.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportCreateSubscription
        @param topicName:str
        @param topicCallback:list
        @param queueSize:list
        @return subscriptionHandle:str"""
        pass

    @classmethod
    def imageTransportPublish(
        publisherHandle: str, data: list, width: list, height: list, frame_id: str
    ) -> None:
        """Publish a message on the topic associated with this publisher using ImageTransport.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportPublish
        @param publisherHandle:str
        @param data:list
        @param width:list
        @param height:list
        @param frame_id:str
        """
        pass

    @classmethod
    def imageTransportShutdownPublisher(publisherHandle: str) -> None:
        """Shutdown the publisher using ImageTransport.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportShutdownPublisher
        @param publisherHandle:str
        """
        pass

    @classmethod
    def imageTransportShutdownSubscription(subscriptionHandle: str) -> None:
        """Shutdown the subscription using ImageTransport.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportShutdownSubscription
        @param subscriptionHandle:str
        """
        pass

    @classmethod
    def importInterface(name: str) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#importInterface
        @param name:str
        """
        pass

    @classmethod
    def publish(publisherHandle: str, message: list) -> None:
        """Publish a message on the topic associated with this publisher.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#publish
        @param publisherHandle:str
        @param message:list
        """
        pass

    @classmethod
    def publisherTreatUInt8ArrayAsString(publisherHandle: str) -> None:
        """After calling this function, this publisher will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#publisherTreatUInt8ArrayAsString
        @param publisherHandle:str
        """
        pass

    @classmethod
    def sendGoal(actionClientHandle: str, goal: list) -> list:
        """Send a goal using the specified action client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#sendGoal
        @param actionClientHandle:str
        @param goal:list
        @return success:list"""
        pass

    @classmethod
    def sendTransform(transform: list) -> None:
        """Publish a TF transformation between frames.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#sendTransform
        @param transform:list
        """
        pass

    @classmethod
    def sendTransforms(transforms: list) -> None:
        """Publish several TF transformations between frames.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#sendTransforms
        @param transforms:list
        """
        pass

    @classmethod
    def serviceTreatUInt8ArrayAsString(serviceHandle: str) -> None:
        """After calling this function, this service will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#serviceTreatUInt8ArrayAsString
        @param serviceHandle:str
        """
        pass

    @classmethod
    def setParamBool(name: str, value: list) -> None:
        """Set a boolean parameter in the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamBool
        @param name:str
        @param value:list
        """
        pass

    @classmethod
    def setParamDouble(name: str, value: list) -> None:
        """Set a double parameter in the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamDouble
        @param name:str
        @param value:list
        """
        pass

    @classmethod
    def setParamInt(name: str, value: list) -> None:
        """Set a integer parameter in the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamInt
        @param name:str
        @param value:list
        """
        pass

    @classmethod
    def setParamString(name: str, value: str) -> None:
        """Set a string parameter in the ROS Parameter Server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#setParamString
        @param name:str
        @param value:str
        """
        pass

    @classmethod
    def shutdownActionClient(actionClientHandle: str) -> None:
        """Shutdown the action client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownActionClient
        @param actionClientHandle:str
        """
        pass

    @classmethod
    def shutdownActionServer(actionServerHandle: str) -> None:
        """Shutdown the action server.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownActionServer
        @param actionServerHandle:str
        """
        pass

    @classmethod
    def shutdownClient(clientHandle: str) -> None:
        """Shutdown the service client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownClient
        @param clientHandle:str
        """
        pass

    @classmethod
    def shutdownPublisher(publisherHandle: str) -> None:
        """Shutdown the specified publisher.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownPublisher
        @param publisherHandle:str
        """
        pass

    @classmethod
    def shutdownService(serviceHandle: str) -> None:
        """Shutdown the service.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownService
        @param serviceHandle:str
        """
        pass

    @classmethod
    def shutdownSubscription(subscriptionHandle: str) -> None:
        """Shutdown the subscription.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#shutdownSubscription
        @param subscriptionHandle:str
        """
        pass

    @classmethod
    def spinSome() -> None:
        """Calls spin_some(node).
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#spinSome

        """
        pass

    @classmethod
    def subscriptionTreatUInt8ArrayAsString(subscriptionHandle: str) -> None:
        """After calling this function, this subscription will treat uint8 arrays as string. Using strings should be in general much faster that using int arrays in Lua.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#subscriptionTreatUInt8ArrayAsString
        @param subscriptionHandle:str
        """
        pass

    @classmethod
    def supportedInterfaces() -> list:
        """Retrieve a list of supported interfaces.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#supportedInterfaces

        @return result:list"""
        pass

    @classmethod
    def timeFromFloat(t: list) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#timeFromFloat
        @param t:list
        """
        pass

    @classmethod
    def timeToFloat(t: list) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#timeToFloat
        @param t:list
        """
        pass

    @classmethod
    def waitForService(clientHandle: str, timeout: list) -> list:
        """Wait for the service associated with this service client.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#waitForService
        @param clientHandle:str
        @param timeout:list
        @return result:list"""
        pass

    @classmethod
    def subscriptionCallback(message: list) -> None:
        """Callback for ROS subscription.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#subscriptionCallback
        @param message:list
        """
        pass

    @classmethod
    def imageTransportCallback(data: list, width: list, height: list) -> None:
        """Callback for ROS ImageTransport subscription.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#imageTransportCallback
        @param data:list
        @param width:list
        @param height:list
        """
        pass

    @classmethod
    def actionGoalResponseCallback(goalID: str, accepted: list) -> None:
        """Callback for action client goal response.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simROS2.htm?#actionGoalResponseCallback
        @param goalID:str
        @param accepted:list
        """
        pass


class SimUI:
    @classmethod
    def addCurve(
        handle: str,
        id: list,
        type: list,
        name: str,
        color: list,
        style: list,
        options: list,
    ) -> None:
        """Adds a curve to a plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addCurve
        @param handle:str
        @param id:list
        @param type:list
        @param name:str
        @param color:list
        @param style:list
        @param options:list
        """
        pass

    @classmethod
    def addCurveTimePoints(handle: str, id: list, name: str, x: list, y: list) -> None:
        """Adds time points to the specified curve of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addCurveTimePoints
        @param handle:str
        @param id:list
        @param name:str
        @param x:list
        @param y:list
        """
        pass

    @classmethod
    def addCurveXYPoints(
        handle: str, id: list, name: str, t: list, x: list, y: list
    ) -> None:
        """Adds points to the specified curve of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addCurveXYPoints
        @param handle:str
        @param id:list
        @param name:str
        @param t:list
        @param x:list
        @param y:list
        """
        pass

    @classmethod
    def addScene3DNode(
        handle: str, id: list, nodeId: list, parentNodeId: list, type: list
    ) -> None:
        """Add a node in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addScene3DNode
        @param handle:str
        @param id:list
        @param nodeId:list
        @param parentNodeId:list
        @param type:list
        """
        pass

    @classmethod
    def addTreeItem(
        handle: str,
        id: list,
        item_id: list,
        text: list,
        parent_id: list,
        expanded: list,
        suppressEvents: list,
    ) -> None:
        """Add an item to the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#addTreeItem
        @param handle:str
        @param id:list
        @param item_id:list
        @param text:list
        @param parent_id:list
        @param expanded:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def adjustSize(handle: str) -> None:
        """Adjusts the size of the window to fit its contents.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#adjustSize
        @param handle:str
        """
        pass

    @classmethod
    def appendText(handle: str, id: list, text: str, suppressEvents: list) -> None:
        """Append text in a text-browser widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#appendText
        @param handle:str
        @param id:list
        @param text:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def bannerCreate(text: str, btnKeys: list, btnLabels: list, callback: str) -> list:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#bannerCreate
        @param text:str
        @param btnKeys:list
        @param btnLabels:list
        @param callback:str
        @return id:list"""
        pass

    @classmethod
    def bannerDestroy(id: list) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#bannerDestroy
        @param id:list
        """
        pass

    @classmethod
    def clearCurve(handle: str, id: list, name: str) -> None:
        """Clear points of the specified curve of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#clearCurve
        @param handle:str
        @param id:list
        @param name:str
        """
        pass

    @classmethod
    def clearTable(handle: str, id: list, suppressEvents: list) -> None:
        """Clear the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#clearTable
        @param handle:str
        @param id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def clearTree(handle: str, id: list, suppressEvents: list) -> None:
        """Clear the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#clearTree
        @param handle:str
        @param id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def collapseAll(handle: str, id: list, suppressEvents: list) -> None:
        """Collapse all nodes in the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#collapseAll
        @param handle:str
        @param id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def colorDialog(
        initColor: list, title: str, showAlphaChannel: list, native: list
    ) -> list:
        """Display a color dialog.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#colorDialog
        @param initColor:list
        @param title:str
        @param showAlphaChannel:list
        @param native:list
        @return result:list"""
        pass

    @classmethod
    def create(xml: str) -> str:
        """Create a window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#create
        @param xml:str
        @return uiHandle:str"""
        pass

    @classmethod
    def destroy(handle: str) -> None:
        """Destroy a window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#destroy
        @param handle:str
        """
        pass

    @classmethod
    def expandAll(handle: str, id: list, suppressEvents: list) -> None:
        """Expand all nodes in the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#expandAll
        @param handle:str
        @param id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def expandToDepth(handle: str, id: list, depth: list, suppressEvents: list) -> None:
        """Expand nodes up to a certain depth in the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#expandToDepth
        @param handle:str
        @param id:list
        @param depth:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def fileDialog(
        type: list,
        title: str,
        startPath: str,
        initName: str,
        extName: str,
        ext: str,
        native: list,
    ) -> list:
        """Display a file dialog.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#fileDialog
        @param type:list
        @param title:str
        @param startPath:str
        @param initName:str
        @param extName:str
        @param ext:str
        @param native:list
        @return result:list"""
        pass

    @classmethod
    def getCheckboxValue(handle: str, id: list) -> list:
        """Get the value of a checkbox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCheckboxValue
        @param handle:str
        @param id:list
        @return value:list"""
        pass

    @classmethod
    def getColumnCount(handle: str, id: list) -> list:
        """Get the number of columns in the specified table/tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getColumnCount
        @param handle:str
        @param id:list
        @return count:list"""
        pass

    @classmethod
    def getComboboxItemCount(handle: str, id: list) -> list:
        """Get the number of items in the specified combobox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxItemCount
        @param handle:str
        @param id:list
        @return count:list"""
        pass

    @classmethod
    def getComboboxItemText(handle: str, id: list, index: list) -> str:
        """Get the text of an item in a combobox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxItemText
        @param handle:str
        @param id:list
        @param index:list
        @return text:str"""
        pass

    @classmethod
    def getComboboxItems(handle: str, id: list) -> list:
        """Get the content of a combobox.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxItems
        @param handle:str
        @param id:list
        @return items:list"""
        pass

    @classmethod
    def getComboboxSelectedIndex(handle: str, id: list) -> list:
        """Get the selected item index in a combobox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getComboboxSelectedIndex
        @param handle:str
        @param id:list
        @return index:list"""
        pass

    @classmethod
    def getCurrentEditWidget(handle: str) -> list:
        """Get the edit widget with focus and selected text.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCurrentEditWidget
        @param handle:str
        @return id:list"""
        pass

    @classmethod
    def getCurrentTab(handle: str, id: list) -> list:
        """Get the current tab index of a tabs widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCurrentTab
        @param handle:str
        @param id:list
        @return index:list"""
        pass

    @classmethod
    def getCurveData(handle: str, id: list, name: str) -> Union[list, list, list]:
        """Get the data contained in the specified curve.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getCurveData
        @param handle:str
        @param id:list
        @param name:str
        @return t:list
        @return x:list
        @return y:list"""
        pass

    @classmethod
    def getEditValue(handle: str, id: list) -> str:
        """Get the value of a edit widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getEditValue
        @param handle:str
        @param id:list
        @return value:str"""
        pass

    @classmethod
    def getItem(handle: str, id: list, row: list, column: list) -> str:
        """Get the table widget item text.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getItem
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        @return text:str"""
        pass

    @classmethod
    def getKeyboardModifiers() -> list:
        """returns the current state of the modifier keys on the keyboard
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getKeyboardModifiers

        @return m:list"""
        pass

    @classmethod
    def getLabelText(handle: str, id: list) -> str:
        """Get the text of a label widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getLabelText
        @param handle:str
        @param id:list
        @return text:str"""
        pass

    @classmethod
    def getPosition(handle: str) -> Union[list, list]:
        """Get the position of a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getPosition
        @param handle:str
        @return x:list
        @return y:list"""
        pass

    @classmethod
    def getPropertiesState(handle: str, id: list) -> str:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getPropertiesState
        @param handle:str
        @param id:list
        @return state:str"""
        pass

    @classmethod
    def getRadiobuttonValue(handle: str, id: list) -> list:
        """Get the value of a radiobutton widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getRadiobuttonValue
        @param handle:str
        @param id:list
        @return value:list"""
        pass

    @classmethod
    def getRowCount(handle: str, id: list) -> list:
        """Get the table widget number of rows.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getRowCount
        @param handle:str
        @param id:list
        @return count:list"""
        pass

    @classmethod
    def getSize(handle: str) -> Union[list, list]:
        """Get the size of a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getSize
        @param handle:str
        @return w:list
        @return h:list"""
        pass

    @classmethod
    def getSliderValue(handle: str, id: list) -> list:
        """Get the value of a slider widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getSliderValue
        @param handle:str
        @param id:list
        @return value:list"""
        pass

    @classmethod
    def getSpinboxValue(handle: str, id: list) -> list:
        """Get the value of a spinbox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getSpinboxValue
        @param handle:str
        @param id:list
        @return value:list"""
        pass

    @classmethod
    def getTitle(handle: str) -> str:
        """Get the title of a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getTitle
        @param handle:str
        @return title:str"""
        pass

    @classmethod
    def getWidgetVisibility(handle: str, id: list) -> list:
        """Get the visibility status of a widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#getWidgetVisibility
        @param handle:str
        @param id:list
        @return visibility:list"""
        pass

    @classmethod
    def growPlotRanges(
        handle: str, id: list, xmin: list, xmax: list, ymin: list, ymax: list
    ) -> None:
        """Increase the ranges of the plot widget by a fixed amount.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#growPlotRanges
        @param handle:str
        @param id:list
        @param xmin:list
        @param xmax:list
        @param ymin:list
        @param ymax:list
        """
        pass

    @classmethod
    def growPlotXRange(handle: str, id: list, xmin: list, xmax: list) -> None:
        """Increase the X range of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#growPlotXRange
        @param handle:str
        @param id:list
        @param xmin:list
        @param xmax:list
        """
        pass

    @classmethod
    def growPlotYRange(handle: str, id: list, ymin: list, ymax: list) -> None:
        """Increase the Y range of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#growPlotYRange
        @param handle:str
        @param id:list
        @param ymin:list
        @param ymax:list
        """
        pass

    @classmethod
    def hide(handle: str) -> None:
        """Hide the UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#hide
        @param handle:str
        """
        pass

    @classmethod
    def inputDialog(initValue: str, label: str, title: str) -> str:
        """Display an input dialog.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#inputDialog
        @param initValue:str
        @param label:str
        @param title:str
        @return result:str"""
        pass

    @classmethod
    def insertComboboxItem(
        handle: str, id: list, index: list, text: str, suppressEvents: list
    ) -> None:
        """Insert an item in a combobox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#insertComboboxItem
        @param handle:str
        @param id:list
        @param index:list
        @param text:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def insertTableColumn(ui: list, widget: list, index: list) -> None:
        """insert a column in a table widget
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#insertTableColumn
        @param ui:list
        @param widget:list
        @param index:list
        """
        pass

    @classmethod
    def insertTableRow(ui: list, widget: list, index: list) -> None:
        """insert a row in a table widget
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#insertTableRow
        @param ui:list
        @param widget:list
        @param index:list
        """
        pass

    @classmethod
    def isVisible(handle: str) -> list:
        """Check if the window is visible.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#isVisible
        @param handle:str
        @return visibility:list"""
        pass

    @classmethod
    def msgBox(type: list, buttons: list, title: str, message: str) -> list:
        """Display a message box.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#msgBox
        @param type:list
        @param buttons:list
        @param title:str
        @param message:str
        @return result:list"""
        pass

    @classmethod
    def qtVersion() -> list:
        """Returns the version of the Qt library.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#qtVersion

        @return version:list"""
        pass

    @classmethod
    def removeComboboxItem(
        handle: str, id: list, index: list, suppressEvents: list
    ) -> None:
        """Remove an item from a combobox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeComboboxItem
        @param handle:str
        @param id:list
        @param index:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def removeCurve(handle: str, id: list, name: str) -> None:
        """Remove the specified curve from the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeCurve
        @param handle:str
        @param id:list
        @param name:str
        """
        pass

    @classmethod
    def removeScene3DNode(handle: str, id: list, nodeId: list) -> None:
        """Remove a node in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeScene3DNode
        @param handle:str
        @param id:list
        @param nodeId:list
        """
        pass

    @classmethod
    def removeTableColumn(ui: list, widget: list, index: list) -> None:
        """remove a column from a table widget
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeTableColumn
        @param ui:list
        @param widget:list
        @param index:list
        """
        pass

    @classmethod
    def removeTableRow(ui: list, widget: list, index: list) -> None:
        """remove a row from a table widget
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeTableRow
        @param ui:list
        @param widget:list
        @param index:list
        """
        pass

    @classmethod
    def removeTreeItem(
        handle: str, id: list, item_id: list, suppressEvents: list
    ) -> None:
        """Remove an item from the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#removeTreeItem
        @param handle:str
        @param id:list
        @param item_id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def replot(handle: str, id: list) -> None:
        """Refresh all the plots of a plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#replot
        @param handle:str
        @param id:list
        """
        pass

    @classmethod
    def rescaleAxes(
        handle: str, id: list, name: str, onlyEnlargeX: list, onlyEnlargeY: list
    ) -> None:
        """Rescales the axes such that the specified curve in the plot is fully visible.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#rescaleAxes
        @param handle:str
        @param id:list
        @param name:str
        @param onlyEnlargeX:list
        @param onlyEnlargeY:list
        """
        pass

    @classmethod
    def rescaleAxesAll(
        handle: str, id: list, onlyEnlargeX: list, onlyEnlargeY: list
    ) -> None:
        """Rescales the axes such that all curves in the plot are fully visible.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#rescaleAxesAll
        @param handle:str
        @param id:list
        @param onlyEnlargeX:list
        @param onlyEnlargeY:list
        """
        pass

    @classmethod
    def restoreState(handle: str, id: list, state: list) -> None:
        """Restore a previously saved header state of the specified table/tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#restoreState
        @param handle:str
        @param id:list
        @param state:list
        """
        pass

    @classmethod
    def saveState(handle: str, id: list) -> list:
        """Save header state of the specified table/tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#saveState
        @param handle:str
        @param id:list
        @return state:list"""
        pass

    @classmethod
    def setButtonPressed(handle: str, id: list, pressed: list) -> None:
        """Set the state of a button.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setButtonPressed
        @param handle:str
        @param id:list
        @param pressed:list
        """
        pass

    @classmethod
    def setButtonText(handle: str, id: list, text: str) -> None:
        """Set the text of a button.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setButtonText
        @param handle:str
        @param id:list
        @param text:str
        """
        pass

    @classmethod
    def setCheckboxValue(
        handle: str, id: list, value: list, suppressEvents: list
    ) -> None:
        """Set the value of a checkbox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setCheckboxValue
        @param handle:str
        @param id:list
        @param value:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setClipboardText(text: str) -> None:
        """Set the content of the clipboard to the specified text.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setClipboardText
        @param text:str
        """
        pass

    @classmethod
    def setColumnCount(
        handle: str, id: list, count: list, suppressEvents: list
    ) -> None:
        """Resize the specified table/tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setColumnCount
        @param handle:str
        @param id:list
        @param count:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setColumnHeaderText(handle: str, id: list, column: list, text: str) -> None:
        """Set the column header text of the specified table/tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setColumnHeaderText
        @param handle:str
        @param id:list
        @param column:list
        @param text:str
        """
        pass

    @classmethod
    def setColumnWidth(
        handle: str, id: list, column: list, min_size: list, max_size: list
    ) -> None:
        """Resize a column in the specified table/tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setColumnWidth
        @param handle:str
        @param id:list
        @param column:list
        @param min_size:list
        @param max_size:list
        """
        pass

    @classmethod
    def setComboboxItems(
        handle: str, id: list, items: list, index: list, suppressEvents: list
    ) -> None:
        """Populate a combobox widget with the specified items, and set the selected item to the specified index.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setComboboxItems
        @param handle:str
        @param id:list
        @param items:list
        @param index:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setComboboxSelectedIndex(
        handle: str, id: list, index: list, suppressEvents: list
    ) -> None:
        """Change the selected item index in a combobox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setComboboxSelectedIndex
        @param handle:str
        @param id:list
        @param index:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setCurrentEditWidget(handle: str, id: list) -> None:
        """Set the edit widget focus and selected text.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setCurrentEditWidget
        @param handle:str
        @param id:list
        """
        pass

    @classmethod
    def setCurrentTab(handle: str, id: list, index: list, suppressEvents: list) -> None:
        """Set the current tab index in a tabs widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setCurrentTab
        @param handle:str
        @param id:list
        @param index:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setEditValue(handle: str, id: list, value: str, suppressEvents: list) -> None:
        """Set the value of a edit widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setEditValue
        @param handle:str
        @param id:list
        @param value:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setEnabled(handle: str, id: list, enabled: list, suppressEvents: list) -> None:
        """Enable or disable a widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setEnabled
        @param handle:str
        @param id:list
        @param enabled:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setImageData(
        handle: str, id: list, data: list, width: list, height: list
    ) -> None:
        """Set image content using specified bitmap (RGB888) data.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setImageData
        @param handle:str
        @param id:list
        @param data:list
        @param width:list
        @param height:list
        """
        pass

    @classmethod
    def setItem(
        handle: str, id: list, row: list, column: list, text: str, suppressEvents: list
    ) -> None:
        """Change item value in the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItem
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        @param text:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setItemEditable(
        handle: str, id: list, row: list, column: list, editable: list
    ) -> None:
        """Change item editable flag in the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItemEditable
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        @param editable:list
        """
        pass

    @classmethod
    def setItemImage(
        handle: str,
        id: list,
        row: list,
        column: list,
        data: str,
        width: list,
        height: list,
        suppressEvents: list,
    ) -> None:
        """Change item image in the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItemImage
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        @param data:str
        @param width:list
        @param height:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setItems(handle: str, id: list, data: str, suppressEvents: list) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setItems
        @param handle:str
        @param id:list
        @param data:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setLabelText(handle: str, id: list, text: str, suppressEvents: list) -> None:
        """Set the text of a label widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setLabelText
        @param handle:str
        @param id:list
        @param text:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setLegendVisibility(handle: str, id: list, visible: list) -> None:
        """Set visibility of the plot legend (default is hidden).
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setLegendVisibility
        @param handle:str
        @param id:list
        @param visible:list
        """
        pass

    @classmethod
    def setMouseOptions(
        handle: str, id: list, panX: list, panY: list, zoomX: list, zoomY: list
    ) -> None:
        """Set plot widget options for interacting with mouse.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setMouseOptions
        @param handle:str
        @param id:list
        @param panX:list
        @param panY:list
        @param zoomX:list
        @param zoomY:list
        """
        pass

    @classmethod
    def setPlotLabels(handle: str, id: list, x: str, y: str) -> None:
        """Set the labels of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotLabels
        @param handle:str
        @param id:list
        @param x:str
        @param y:str
        """
        pass

    @classmethod
    def setPlotRanges(
        handle: str, id: list, xmin: list, xmax: list, ymin: list, ymax: list
    ) -> None:
        """Set the ranges of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotRanges
        @param handle:str
        @param id:list
        @param xmin:list
        @param xmax:list
        @param ymin:list
        @param ymax:list
        """
        pass

    @classmethod
    def setPlotXLabel(handle: str, id: list, label: str) -> None:
        """Set the X label of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotXLabel
        @param handle:str
        @param id:list
        @param label:str
        """
        pass

    @classmethod
    def setPlotXRange(handle: str, id: list, xmin: list, xmax: list) -> None:
        """Set the X range of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotXRange
        @param handle:str
        @param id:list
        @param xmin:list
        @param xmax:list
        """
        pass

    @classmethod
    def setPlotYLabel(handle: str, id: list, label: str) -> None:
        """Set the Y label of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotYLabel
        @param handle:str
        @param id:list
        @param label:str
        """
        pass

    @classmethod
    def setPlotYRange(handle: str, id: list, ymin: list, ymax: list) -> None:
        """Set the Y range of the plot widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPlotYRange
        @param handle:str
        @param id:list
        @param ymin:list
        @param ymax:list
        """
        pass

    @classmethod
    def setPosition(handle: str, x: list, y: list, suppressEvents: list) -> None:
        """Set the position of a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPosition
        @param handle:str
        @param x:list
        @param y:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setProgress(handle: str, id: list, value: list) -> None:
        """Chnge the value of a progressbar widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setProgress
        @param handle:str
        @param id:list
        @param value:list
        """
        pass

    @classmethod
    def setProperties(
        handle: str,
        id: list,
        pnames: list,
        ptypes: list,
        pvalues: list,
        pflags: list,
        pdisplayk: list,
        pdisplayv: list,
        icons: list,
        suppressEvents: list,
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setProperties
        @param handle:str
        @param id:list
        @param pnames:list
        @param ptypes:list
        @param pvalues:list
        @param pflags:list
        @param pdisplayk:list
        @param pdisplayv:list
        @param icons:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setPropertiesContextMenu(
        handle: str, id: list, keys: list, titles: list
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesContextMenu
        @param handle:str
        @param id:list
        @param keys:list
        @param titles:list
        """
        pass

    @classmethod
    def setPropertiesRows(
        handle: str,
        id: list,
        rows: list,
        pnames: list,
        ptypes: list,
        pvalues: list,
        pflags: list,
        pdisplayk: list,
        pdisplayv: list,
        icons: list,
        suppressEvents: list,
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesRows
        @param handle:str
        @param id:list
        @param rows:list
        @param pnames:list
        @param ptypes:list
        @param pvalues:list
        @param pflags:list
        @param pdisplayk:list
        @param pdisplayv:list
        @param icons:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setPropertiesSelection(
        handle: str, id: list, row: list, suppressEvents: list
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesSelection
        @param handle:str
        @param id:list
        @param row:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setPropertiesState(handle: str, id: list, state: str) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setPropertiesState
        @param handle:str
        @param id:list
        @param state:str
        """
        pass

    @classmethod
    def setRadiobuttonValue(
        handle: str, id: list, value: list, suppressEvents: list
    ) -> None:
        """Set the value of a radiobutton widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRadiobuttonValue
        @param handle:str
        @param id:list
        @param value:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setRowCount(handle: str, id: list, count: list, suppressEvents: list) -> None:
        """Resize the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRowCount
        @param handle:str
        @param id:list
        @param count:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setRowHeaderText(handle: str, id: list, row: list, text: str) -> None:
        """Set the row header text of the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRowHeaderText
        @param handle:str
        @param id:list
        @param row:list
        @param text:str
        """
        pass

    @classmethod
    def setRowHeight(
        handle: str, id: list, row: list, min_size: list, max_size: list
    ) -> None:
        """Resize a row in the specified table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setRowHeight
        @param handle:str
        @param id:list
        @param row:list
        @param min_size:list
        @param max_size:list
        """
        pass

    @classmethod
    def setScene3DNodeEnabled(
        handle: str, id: list, nodeId: list, enabled: list
    ) -> None:
        """Enable or disable a node in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeEnabled
        @param handle:str
        @param id:list
        @param nodeId:list
        @param enabled:list
        """
        pass

    @classmethod
    def setScene3DNodeFloatParam(
        handle: str, id: list, nodeId: list, paramName: str, value: list
    ) -> None:
        """Set node float parameter in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeFloatParam
        @param handle:str
        @param id:list
        @param nodeId:list
        @param paramName:str
        @param value:list
        """
        pass

    @classmethod
    def setScene3DNodeIntParam(
        handle: str, id: list, nodeId: list, paramName: str, value: list
    ) -> None:
        """Set node int parameter in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeIntParam
        @param handle:str
        @param id:list
        @param nodeId:list
        @param paramName:str
        @param value:list
        """
        pass

    @classmethod
    def setScene3DNodeParam(
        ui: list, widget: list, nodeId: list, paramName: str, paramValue: list
    ) -> None:
        """polymorphic version of the onSetScene3DNodeXXXParam() functions
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeParam
        @param ui:list
        @param widget:list
        @param nodeId:list
        @param paramName:str
        @param paramValue:list
        """
        pass

    @classmethod
    def setScene3DNodeStringParam(
        handle: str, id: list, nodeId: list, paramName: str, value: str
    ) -> None:
        """Set node string parameter in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeStringParam
        @param handle:str
        @param id:list
        @param nodeId:list
        @param paramName:str
        @param value:str
        """
        pass

    @classmethod
    def setScene3DNodeVector2Param(
        handle: str, id: list, nodeId: list, paramName: str, x: list, y: list
    ) -> None:
        """Set node vector2 parameter in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeVector2Param
        @param handle:str
        @param id:list
        @param nodeId:list
        @param paramName:str
        @param x:list
        @param y:list
        """
        pass

    @classmethod
    def setScene3DNodeVector3Param(
        handle: str, id: list, nodeId: list, paramName: str, x: list, y: list, z: list
    ) -> None:
        """Set node vector3 parameter in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeVector3Param
        @param handle:str
        @param id:list
        @param nodeId:list
        @param paramName:str
        @param x:list
        @param y:list
        @param z:list
        """
        pass

    @classmethod
    def setScene3DNodeVector4Param(
        handle: str,
        id: list,
        nodeId: list,
        paramName: str,
        x: list,
        y: list,
        z: list,
        w: list,
    ) -> None:
        """Set node vector4 parameter in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setScene3DNodeVector4Param
        @param handle:str
        @param id:list
        @param nodeId:list
        @param paramName:str
        @param x:list
        @param y:list
        @param z:list
        @param w:list
        """
        pass

    @classmethod
    def setSize(handle: str, w: list, h: list, suppressEvents: list) -> None:
        """Set the size of a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setSize
        @param handle:str
        @param w:list
        @param h:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setSliderValue(
        handle: str, id: list, value: list, suppressEvents: list
    ) -> None:
        """Set the value of a slider widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setSliderValue
        @param handle:str
        @param id:list
        @param value:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setSpinboxValue(
        handle: str, id: list, value: list, suppressEvents: list
    ) -> None:
        """Set the value of a spinbox widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setSpinboxValue
        @param handle:str
        @param id:list
        @param value:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setStyleSheet(handle: str, id: list, styleSheet: str) -> None:
        """Set the stylesheet of a widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setStyleSheet
        @param handle:str
        @param id:list
        @param styleSheet:str
        """
        pass

    @classmethod
    def setTableSelection(
        handle: str, id: list, row: list, column: list, suppressEvents: list
    ) -> None:
        """Set selection in a table widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setTableSelection
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setText(handle: str, id: list, text: str, suppressEvents: list) -> None:
        """Set the text in a text-browser widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setText
        @param handle:str
        @param id:list
        @param text:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setTitle(handle: str, title: str, suppressEvents: list) -> None:
        """Set the title of a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setTitle
        @param handle:str
        @param title:str
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setTreeSelection(
        handle: str, id: list, item_id: list, suppressEvents: list
    ) -> None:
        """Set selection in a tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setTreeSelection
        @param handle:str
        @param id:list
        @param item_id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def setUrl(handle: str, id: list, url: str) -> None:
        """Load an url in a text-browser widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setUrl
        @param handle:str
        @param id:list
        @param url:str
        """
        pass

    @classmethod
    def setWidgetVisibility(handle: str, id: list, visibility: list) -> None:
        """Hide or show a widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setWidgetVisibility
        @param handle:str
        @param id:list
        @param visibility:list
        """
        pass

    @classmethod
    def setWindowEnabled(handle: str, enabled: list, suppressEvents: list) -> None:
        """Enable or disable a UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#setWindowEnabled
        @param handle:str
        @param enabled:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def show(handle: str) -> None:
        """Show the UI window.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#show
        @param handle:str
        """
        pass

    @classmethod
    def supportedImageFormats(separator: str) -> Union[list, str]:
        """Return a list of supported image formats
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#supportedImageFormats
        @param separator:str
        @return formatList:list
        @return formatListStr:str"""
        pass

    @classmethod
    def svgLoadData(handle: str, id: list, data: str) -> None:
        """Load a SVG document in a SVG widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#svgLoadData
        @param handle:str
        @param id:list
        @param data:str
        """
        pass

    @classmethod
    def svgLoadFile(handle: str, id: list, file: str) -> None:
        """Load a SVG file in a SVG widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#svgLoadFile
        @param handle:str
        @param id:list
        @param file:str
        """
        pass

    @classmethod
    def updateTreeItemParent(
        handle: str, id: list, item_id: list, parent_id: list, suppressEvents: list
    ) -> None:
        """Modify the parent of an existing item in the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#updateTreeItemParent
        @param handle:str
        @param id:list
        @param item_id:list
        @param parent_id:list
        @param suppressEvents:list
        """
        pass

    @classmethod
    def updateTreeItemText(handle: str, id: list, item_id: list, text: list) -> None:
        """Modify the text of an existing item in the specified tree widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#updateTreeItemText
        @param handle:str
        @param id:list
        @param item_id:list
        @param text:list
        """
        pass

    @classmethod
    def onclickCallback(handle: str, id: list) -> None:
        """Callback for button click event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onclickCallback
        @param handle:str
        @param id:list
        """
        pass

    @classmethod
    def onLinkActivatedCallback(handle: str, id: list, link: str) -> None:
        """Callback for when a link is clicked.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onLinkActivatedCallback
        @param handle:str
        @param id:list
        @param link:str
        """
        pass

    @classmethod
    def onchangeIntCallback(handle: str, id: list, value: list) -> None:
        """Callback for widget change event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onchangeIntCallback
        @param handle:str
        @param id:list
        @param value:list
        """
        pass

    @classmethod
    def onchangeDoubleCallback(handle: str, id: list, value: list) -> None:
        """Callback for widget change event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onchangeDoubleCallback
        @param handle:str
        @param id:list
        @param value:list
        """
        pass

    @classmethod
    def onchangeStringCallback(handle: str, id: list, value: str) -> None:
        """Callback for widget change event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onchangeStringCallback
        @param handle:str
        @param id:list
        @param value:str
        """
        pass

    @classmethod
    def oneditingfinishedCallback(handle: str, id: list, value: str) -> None:
        """Callback for editing finished event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#oneditingfinishedCallback
        @param handle:str
        @param id:list
        @param value:str
        """
        pass

    @classmethod
    def oncloseCallback(handle: str) -> None:
        """Callback for window close event. It will be called when the user clicks the close button of the window. When an onclose callback is specified, the window will not close automatically when the user clicks the window close button.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#oncloseCallback
        @param handle:str
        """
        pass

    @classmethod
    def onPlottableClickCallback(
        handle: str, id: list, curve: str, index: list, x: list, y: list
    ) -> None:
        """Callback for plot widget plottableClick event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPlottableClickCallback
        @param handle:str
        @param id:list
        @param curve:str
        @param index:list
        @param x:list
        @param y:list
        """
        pass

    @classmethod
    def onLegendClickCallback(handle: str, id: list, curve: str) -> None:
        """Callback for plot widget legendClick event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onLegendClickCallback
        @param handle:str
        @param id:list
        @param curve:str
        """
        pass

    @classmethod
    def onCellActivateCallback(
        handle: str, id: list, row: list, column: list, cellValue: str
    ) -> None:
        """Callback for table widget cellActivated event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onCellActivateCallback
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        @param cellValue:str
        """
        pass

    @classmethod
    def onTableSelectionChangeCallback(
        handle: str, id: list, row: list, column: list
    ) -> None:
        """Callback for table widget selectionChanged event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onTableSelectionChangeCallback
        @param handle:str
        @param id:list
        @param row:list
        @param column:list
        """
        pass

    @classmethod
    def onPropertiesSelectionChangeCallback(handle: str, id: list, row: list) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesSelectionChangeCallback
        @param handle:str
        @param id:list
        @param row:list
        """
        pass

    @classmethod
    def onPropertiesDoubleClickCallback(
        handle: str, id: list, row: list, col: list
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesDoubleClickCallback
        @param handle:str
        @param id:list
        @param row:list
        @param col:list
        """
        pass

    @classmethod
    def onPropertiesContextMenuTriggeredCallback(
        handle: str, id: list, key: str
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesContextMenuTriggeredCallback
        @param handle:str
        @param id:list
        @param key:str
        """
        pass

    @classmethod
    def onPropertiesPropertyEditCallback(
        handle: str, id: list, key: str, value: str
    ) -> None:
        """
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onPropertiesPropertyEditCallback
        @param handle:str
        @param id:list
        @param key:str
        @param value:str
        """
        pass

    @classmethod
    def onTreeSelectionChangeCallback(handle: str, id: list, item_id: list) -> None:
        """Callback for tree widget selectionChanged event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onTreeSelectionChangeCallback
        @param handle:str
        @param id:list
        @param item_id:list
        """
        pass

    @classmethod
    def onMouseEventCallback(
        handle: str, id: list, type: list, mods: list, x: list, y: list
    ) -> None:
        """Callback for a mouse event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onMouseEventCallback
        @param handle:str
        @param id:list
        @param type:list
        @param mods:list
        @param x:list
        @param y:list
        """
        pass

    @classmethod
    def onKeyPressCallback(handle: str, id: list, key: list, text: str) -> None:
        """Callback called when a key is pressed in a widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onKeyPressCallback
        @param handle:str
        @param id:list
        @param key:list
        @param text:str
        """
        pass

    @classmethod
    def onScene3DObjectClickCallback(handle: str, id: list, nodeId: list) -> None:
        """Callback called when an object is clicked in a scene3d widget.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onScene3DObjectClickCallback
        @param handle:str
        @param id:list
        @param nodeId:list
        """
        pass

    @classmethod
    def onBannerButtonClickCallback(bannerId: list, btnKey: str) -> None:
        """Callback for banner button click event.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simUI.htm?#onBannerButtonClickCallback
        @param bannerId:list
        @param btnKey:str
        """
        pass


class SimVision:
    @classmethod
    def createVelodyneHDL64E(
        visionSensorHandles: list,
        frequency: list,
        options: list,
        pointSize: list,
        coloring_closeFarDist: list,
        displayScalingFactor: list,
        pointCloudHandle: list,
    ) -> list:
        """Creates a handle for generating data similar to a Velodyne HDL64E. See also
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.createVelodyneHDL64E
        @param visionSensorHandles:list
        @param frequency:list
        @param options:list
        @param pointSize:list
        @param coloring_closeFarDist:list
        @param displayScalingFactor:list
        @param pointCloudHandle:list
        @return handle:list"""
        pass

    @classmethod
    def createVelodyneVPL16(
        visionSensorHandles: list,
        frequency: list,
        options: list,
        pointSize: list,
        coloring_closeFarDist: list,
        displayScalingFactor: list,
        pointCloudHandle: list,
    ) -> list:
        """Creates a handle for generating data similar to a Velodyne VPL16. See also
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.createVelodyneVPL16
        @param visionSensorHandles:list
        @param frequency:list
        @param options:list
        @param pointSize:list
        @param coloring_closeFarDist:list
        @param displayScalingFactor:list
        @param pointCloudHandle:list
        @return handle:list"""
        pass

    @classmethod
    def destroyVelodyneHDL64E(velodyneHandle: list) -> None:
        """Deletes a Velodyne HDL64E handle previously created with
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.destroyVelodyneHDL64E
        @param velodyneHandle:list
        """
        pass

    @classmethod
    def destroyVelodyneVPL16(velodyneHandle: list) -> None:
        """Deletes a Velodyne VPL16 handle previously created with
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.destroyVelodyneVPL16
        @param velodyneHandle:list
        """
        pass

    @classmethod
    def distort(visionSensorHandle: list, pixelMap: list, depthScalings: list) -> None:
        """Transforms (distorts) a vision sensor image via pixel remapping.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.distort
        @param visionSensorHandle:list
        @param pixelMap:list
        @param depthScalings:list
        """
        pass

    @classmethod
    def handleAnaglyphStereo(
        rgbVisionSensorHandle: list,
        handlesOfTwoVisionSensors: list,
        leftAndRightColors: list,
    ) -> None:
        """Allows to generate an anaglyph stereo image from two individual vision sensors (for the left and right eye).
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleAnaglyphStereo
        @param rgbVisionSensorHandle:list
        @param handlesOfTwoVisionSensors:list
        @param leftAndRightColors:list
        """
        pass

    @classmethod
    def handleSpherical(
        rgbVisionSensorHandle: list,
        handlesOfSixVisionSensors: list,
        horizontalAngle: list,
        verticalAngle: list,
        depthVisionSensorHandle: list,
    ) -> None:
        """Allows to generate an RGB and/or depth image that covers all directions, i.e. spherical vision, based on the input of 6 individual vision sensors, each looking into a different and perpendicular direction.
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleSpherical
        @param rgbVisionSensorHandle:list
        @param handlesOfSixVisionSensors:list
        @param horizontalAngle:list
        @param verticalAngle:list
        @param depthVisionSensorHandle:list
        """
        pass

    @classmethod
    def handleVelodyneHDL64E(velodyneHandle: list, dt: list) -> Union[list, list]:
        """Handles a velodyne HDL64E sensor (i.e. generates and displays detection points. See also
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleVelodyneHDL64E
        @param velodyneHandle:list
        @param dt:list
        @return points:list
        @return colors:list"""
        pass

    @classmethod
    def handleVelodyneVPL16(velodyneHandle: list, dt: list) -> Union[list, list]:
        """Handles a velodyne VPL16 sensor (i.e. generates and displays detection points. See also
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.handleVelodyneVPL16
        @param velodyneHandle:list
        @param dt:list
        @return points:list
        @return colors:list"""
        pass

    @classmethod
    def addBuffer1ToWorkImg(handle: list) -> None:
        """Performs a pixel wise addition between the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.addBuffer1ToWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def addWorkImgToBuffer1(handle: list) -> None:
        """Performs a pixel wise addition between the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.addWorkImgToBuffer1
        @param handle:list
        """
        pass

    @classmethod
    def binaryWorkImg(
        handle: list,
        threshold: list,
        oneProportion: list,
        oneTol: list,
        xCenter: list,
        xCenterTol: list,
        yCenter: list,
        yCenterTol: list,
        orient: list,
        orientTol: list,
        roundness: list,
        enableTrigger: list,
        overlayColor: list,
    ) -> Union[list, list]:
        """Transforms the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.binaryWorkImg
        @param handle:list
        @param threshold:list
        @param oneProportion:list
        @param oneTol:list
        @param xCenter:list
        @param xCenterTol:list
        @param yCenter:list
        @param yCenterTol:list
        @param orient:list
        @param orientTol:list
        @param roundness:list
        @param enableTrigger:list
        @param overlayColor:list
        @return trigger:list
        @return packedPacket:list"""
        pass

    @classmethod
    def blobDetectionOnWorkImg(
        handle: list,
        threshold: list,
        minBlobSize: list,
        diffColor: list,
        overlayColor: list,
    ) -> Union[list, list]:
        """Performs blob detection on the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.blobDetectionOnWorkImg
        @param handle:list
        @param threshold:list
        @param minBlobSize:list
        @param diffColor:list
        @param overlayColor:list
        @return trigger:list
        @return packedPacket:list"""
        pass

    @classmethod
    def buffer1ToWorkImg(handle: list) -> None:
        """Copies buffer
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.buffer1ToWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def buffer2ToWorkImg(handle: list) -> None:
        """Copies buffer
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.buffer2ToWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def changedPixelsOnWorkImg(handle: list, threshold: list) -> Union[list, list]:
        """Returns the pixels that changed the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.changedPixelsOnWorkImg
        @param handle:list
        @param threshold:list
        @return trigger:list
        @return packedPacket:list"""
        pass

    @classmethod
    def circularCutWorkImg(handle: list, radius: list, toBuffer1: list) -> None:
        """Performs a circular cut on the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.circularCutWorkImg
        @param handle:list
        @param radius:list
        @param toBuffer1:list
        """
        pass

    @classmethod
    def colorSegmentationOnWorkImg(handle: list, colorDistance: list) -> None:
        """Performs a color segmentation on the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.colorSegmentationOnWorkImg
        @param handle:list
        @param colorDistance:list
        """
        pass

    @classmethod
    def coordinatesFromWorkImg(
        handle: list, pointCount: list, angularSpace: list, returnColorData: list
    ) -> Union[list, list, list]:
        """Extracts coordinates from the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.coordinatesFromWorkImg
        @param handle:list
        @param pointCount:list
        @param angularSpace:list
        @param returnColorData:list
        @return trigger:list
        @return packedPacket:list
        @return colorData:list"""
        pass

    @classmethod
    def edgeDetectionOnWorkImg(handle: list, threshold: list) -> None:
        """Applies an edge detection filter to the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.edgeDetectionOnWorkImg
        @param handle:list
        @param threshold:list
        """
        pass

    @classmethod
    def horizontalFlipWorkImg(handle: list) -> None:
        """Horizontally flips the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.horizontalFlipWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def intensityScaleOnWorkImg(
        handle: list, start: list, end: list, greyscale: list
    ) -> None:
        """Transforms the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.intensityScaleOnWorkImg
        @param handle:list
        @param start:list
        @param end:list
        @param greyscale:list
        """
        pass

    @classmethod
    def matrix3x3OnWorkImg(
        handle: list, passes: list, multiplier: list, matrix: list
    ) -> None:
        """Applies a 3X3 matrix filter to the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.matrix3x3OnWorkImg
        @param handle:list
        @param passes:list
        @param multiplier:list
        @param matrix:list
        """
        pass

    @classmethod
    def matrix5x5OnWorkImg(
        handle: list, passes: list, multiplier: list, matrix: list
    ) -> None:
        """Applies a 5X5 matrix filter to the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.matrix5x5OnWorkImg
        @param handle:list
        @param passes:list
        @param multiplier:list
        @param matrix:list
        """
        pass

    @classmethod
    def multiplyWorkImgWithBuffer1(handle: list) -> None:
        """Multiplies (pixel wise) the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.multiplyWorkImgWithBuffer1
        @param handle:list
        """
        pass

    @classmethod
    def normalizeWorkImg(handle: list) -> None:
        """Normalizes the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.normalizeWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def rectangularCutWorkImg(handle: list, rectangle: list, toBuffer1: list) -> None:
        """Performs a rectangular cut on the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.rectangularCutWorkImg
        @param handle:list
        @param rectangle:list
        @param toBuffer1:list
        """
        pass

    @classmethod
    def resizeWorkImg(handle: list, scaling: list) -> None:
        """Scales the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.resizeWorkImg
        @param handle:list
        @param scaling:list
        """
        pass

    @classmethod
    def rotateWorkImg(handle: list, angle: list) -> None:
        """Performs a rotation of the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.rotateWorkImg
        @param handle:list
        @param angle:list
        """
        pass

    @classmethod
    def scaleAndOffsetWorkImg(
        handle: list,
        colorPreOffset: list,
        colorScaling: list,
        colorPostOffset: list,
        rgbSpace: list,
    ) -> None:
        """Shifts and scales colors of the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.scaleAndOffsetWorkImg
        @param handle:list
        @param colorPreOffset:list
        @param colorScaling:list
        @param colorPostOffset:list
        @param rgbSpace:list
        """
        pass

    @classmethod
    def selectiveColorOnWorkImg(
        handle: list,
        nominalColor: list,
        colorTolerance: list,
        rgbSpace: list,
        keepColor: list,
        toBuffer1: list,
    ) -> None:
        """Selects a specific color in the RGB or HSL space of the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.selectiveColorOnWorkImg
        @param handle:list
        @param nominalColor:list
        @param colorTolerance:list
        @param rgbSpace:list
        @param keepColor:list
        @param toBuffer1:list
        """
        pass

    @classmethod
    def sensorDepthMapToWorkImg(handle: list) -> None:
        """Copies the depth buffer acquired by a vision sensor to the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.sensorDepthMapToWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def sensorImgToWorkImg(handle: list) -> None:
        """Copies the RGB image acquired by a vision sensor to the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.sensorImgToWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def sharpenWorkImg(handle: list) -> None:
        """Sharpens the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.sharpenWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def shiftWorkImg(handle: list, shift: list, wrap: list) -> None:
        """Shifts the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.shiftWorkImg
        @param handle:list
        @param shift:list
        @param wrap:list
        """
        pass

    @classmethod
    def subtractBuffer1FromWorkImg(handle: list) -> None:
        """Subtracts (pixel wise subtraction) buffer
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.subtractBuffer1FromWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def subtractWorkImgFromBuffer1(handle: list) -> None:
        """Subtracts (pixel wise subtraction) the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.subtractWorkImgFromBuffer1
        @param handle:list
        """
        pass

    @classmethod
    def swapBuffers(handle: list) -> None:
        """Swaps buffer
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.swapBuffers
        @param handle:list
        """
        pass

    @classmethod
    def swapWorkImgWithBuffer1(handle: list) -> None:
        """Swaps the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.swapWorkImgWithBuffer1
        @param handle:list
        """
        pass

    @classmethod
    def uniformImgToWorkImg(handle: list, color: list) -> None:
        """Applies a uniform color to the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.uniformImgToWorkImg
        @param handle:list
        @param color:list
        """
        pass

    @classmethod
    def velodyneDataFromWorkImg(
        handle: list, pointCount: list, verticalScanAngle: list, returnColorData: list
    ) -> Union[list, list, list]:
        """Extracts Velodyne coordinates from the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.velodyneDataFromWorkImg
        @param handle:list
        @param pointCount:list
        @param verticalScanAngle:list
        @param returnColorData:list
        @return trigger:list
        @return packedPacket:list
        @return colorData:list"""
        pass

    @classmethod
    def verticalFlipWorkImg(handle: list) -> None:
        """Vertically flips the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.verticalFlipWorkImg
        @param handle:list
        """
        pass

    @classmethod
    def workImgToBuffer1(handle: list) -> None:
        """Copies the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToBuffer1
        @param handle:list
        """
        pass

    @classmethod
    def workImgToBuffer2(handle: list) -> None:
        """Copies the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToBuffer2
        @param handle:list
        """
        pass

    @classmethod
    def workImgToSensorDepthMap(handle: list) -> None:
        """Copies the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToSensorDepthMap
        @param handle:list
        """
        pass

    @classmethod
    def workImgToSensorImg(handle: list) -> None:
        """Copies the
        @url:https://www.coppeliarobotics.com/helpFiles/en/simVision.htm?#simVision.workImgToSensorImg
        @param handle:list
        """
        pass
