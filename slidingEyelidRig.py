import maya.cmds as cmds
"""
Slide Over Surface
"""
"""
Select all targets and the surface (should be the last selection)
"""
groupName ="Lfgdfe_Upper_"
list1 = cmds.ls(sl=True)
surface = list1[-1]

follicle_grp = cmds.group( em=True, name = groupName +"_eyelid_Fol_Grp")
joint_grp = cmds.group( em=True, name = groupName + "_eyelid_Jnt_Grp")

for index in range(0,len(list1)-1) :
    loc = list1[index]
    print loc
    follicle_transform = cmds.createNode ('transform', name = loc +'_eyelid' +'_Fol', parent = follicle_grp)
    follicle_shape = cmds.createNode ("follicle", name = loc +"_eyelid" +"_Fol_Shape", parent = follicle_transform);
    closestPoint = cmds.createNode ("closestPointOnSurface", name = loc +"_eyelid_" +"_ClosestPoint")
    divide = cmds.createNode("multiplyDivide", name= loc +"_eyelid" +"_multiplyDivide")
    joint = cmds.joint(p=(0,0,0), name = loc +"_eyelid" +"_Jnt", rad = 0.2)
    cmds.parent( str(joint), str(joint_grp) )
    cmds.pointConstraint (follicle_transform, joint)
    cmds.aimConstraint (loc, joint)
    cmds.setAttr('{0}.operation'.format(divide), 2)
    cmds.connectAttr (str(surface)+'.local', str(follicle_shape)+'.inputSurface')
    cmds.connectAttr (str(follicle_shape)+'.or', str(follicle_transform)+'.r')
    cmds.connectAttr (str(follicle_shape)+'.ot', str(follicle_transform)+'.t')
    cmds.connectAttr (str(surface)+'.worldMatrix[0]', str(follicle_shape)+'.inputWorldMatrix')
    cmds.connectAttr (str(surface)+'.worldSpace[0]', str(closestPoint)+'.inputSurface')
    cmds.connectAttr (str(loc)+'.t', str(closestPoint)+'.inPosition')
    cmds.connectAttr (str(closestPoint)+'.parameterU', str(divide)+'.input1X')
    cmds.connectAttr (str(closestPoint)+'.parameterV', str(divide)+'.input1Y')
    cmds.connectAttr (str(surface)+'.spansU', str(divide)+'.input2X')
    cmds.connectAttr (str(surface)+'.spansV', str(divide)+'.input2Y')
    cmds.connectAttr (str(divide)+'.outputX', str(follicle_shape)+'.parameterU')
    cmds.connectAttr (str(divide)+'.outputY', str(follicle_shape)+'.parameterV')
