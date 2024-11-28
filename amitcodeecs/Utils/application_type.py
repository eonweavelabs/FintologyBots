def get_application_type(user):
    applicationtypes=[]
    if(user.get('preApproval').get('businessFunding')):
        applicationtypes.append("business")
    elif(user.get('preApproval').get('personalFunding')):
        applicationtypes.append("personal")
    return applicationtypes